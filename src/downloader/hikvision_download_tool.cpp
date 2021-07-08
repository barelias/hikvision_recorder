#include "./hikvision_download_tool.h"
#include "incEn/HCNetSDK.h"
#include <stdio.h>
#include <string>
#include <unistd.h>
#include <iostream>
#include <sstream>
#include <list>
#include <iomanip>

HikvisionDownloader::HikvisionDownloader(
    std::string addr,
    int port,
    std::string user,
    std::string passwd
) {
    this->addr = addr;
    this->port = port;
    this->user = user;
    this->passwd = passwd;
    this->setup();
    this->login(addr, port, user, passwd);
}

std::string NetDVRTime::str() {
    std::ostringstream res;
    res << 
        std::setfill('0') << std::setw(2) << (int) dvr_time.dwYear << "-" << 
        std::setfill('0') << std::setw(2) << (int) dvr_time.dwMonth << "-" << 
        std::setfill('0') << std::setw(2) << (int) dvr_time.dwDay << "T" << 
        std::setfill('0') << std::setw(2) << (int) dvr_time.dwHour << ":" << 
        std::setfill('0') << std::setw(2) << (int) dvr_time.dwMinute << ":" << 
        std::setfill('0') << std::setw(2) << (int) dvr_time.dwSecond;
    return res.str();
}

std::string VideoBlock::str() {
    std::ostringstream res;
    res << dvr_time_initial.str() << "->" << dvr_time_final.str(); 
    return res.str();
}

int HikvisionDownloader::get_error(std::string instance){
    int error = NET_DVR_GetLastError();
    std::cout << instance << " error [" << error << "]\n";
    throw error;
}

void HikvisionDownloader::setup(){
    NET_DVR_Init();
    NET_DVR_SetConnectTime(CON_TIME, 1);
    NET_DVR_SetReconnect(RECON_TIME, true);
}

LONG HikvisionDownloader::login(std::string addr, int port, std::string user, std::string passwd){
    this->lUserID = NET_DVR_Login_V30((char*) addr.c_str(), port, (char*) user.c_str(), (char*) passwd.c_str(), &this->struDeviceInfo);
    if (lUserID < 0) {
        int error = get_error("login");
        return error;
    }
    return this->lUserID;
}

NetDVRTime::NetDVRTime(int year, int month, int day, int hours, int minutes, int seconds) {
    this->dvr_time.dwYear = year;
    this->dvr_time.dwMonth = month;
    this->dvr_time.dwDay = day;
    this->dvr_time.dwHour = hours;
    this->dvr_time.dwMinute = minutes;
    this->dvr_time.dwSecond = seconds;
}

NetDVRTime::NetDVRTime(NET_DVR_TIME tm) {
    this->dvr_time.dwYear = tm.dwYear;
    this->dvr_time.dwMonth = tm.dwMonth;
    this->dvr_time.dwDay = tm.dwDay;
    this->dvr_time.dwHour = tm.dwHour;
    this->dvr_time.dwMinute = tm.dwMinute;
    this->dvr_time.dwSecond = tm.dwSecond;
}

void NetDVRTime::copy(NET_DVR_TIME & tm) {
    tm.dwYear = this->dvr_time.dwYear;
    tm.dwMonth = this->dvr_time.dwMonth;
    tm.dwDay = this->dvr_time.dwDay;
    tm.dwHour = this->dvr_time.dwHour;
    tm.dwMinute = this->dvr_time.dwMinute;
    tm.dwSecond = this->dvr_time.dwSecond;
}

NetDVRTime HikvisionDownloader::get_time_object(int year, int month, int day, int hours, int minutes, int seconds) {
    NetDVRTime retTime(year, month, day, hours, minutes, seconds);
    return retTime;
}

int HikvisionDownloader::setup_playback_by_name(std::string src, std::string dst) {
    int hPlayback = 0;
    if ((hPlayback = NET_DVR_GetFileByName(this->lUserID, (char*) src.c_str(), (char*) dst.c_str())) < 0)
        return this->get_error("setup_playback");
    return hPlayback;
}

bool NetDVRTime::operator==(const NetDVRTime& nt) {
    bool res = nt.dvr_time.dwYear == this->dvr_time.dwYear &&
           nt.dvr_time.dwMonth == this->dvr_time.dwMonth &&
           nt.dvr_time.dwDay == this->dvr_time.dwDay &&
           nt.dvr_time.dwHour == this->dvr_time.dwHour &&
           nt.dvr_time.dwMinute == this->dvr_time.dwMinute &&
           nt.dvr_time.dwSecond == this->dvr_time.dwSecond;
    return res;
}

bool VideoBlock::operator==(const VideoBlock& vb) {
    bool res = this->get_initial() == vb.dvr_time_initial && this->get_final() == vb.dvr_time_final;
    return res;
}

bool NetDVRTime::operator>(const NetDVRTime& vb) {
    long long seconds = vb.dvr_time.dwYear*365*30*24*60*60 + vb.dvr_time.dwMonth*30*24*60*60 + vb.dvr_time.dwDay*24*60*60 + vb.dvr_time.dwHour*60*60 + vb.dvr_time.dwMinute*60 + vb.dvr_time.dwSecond;
    long long another_seconds = this->dvr_time.dwYear*365*30*24*60*60 + this->dvr_time.dwMonth*30*24*60*60 + this->dvr_time.dwDay*24*60*60 + this->dvr_time.dwHour*60*60 + this->dvr_time.dwMinute*60 + this->dvr_time.dwSecond;
    return another_seconds > seconds;
}

int HikvisionDownloader::setup_playback_by_time(NetDVRTime struStartTime, NetDVRTime struStopTime, std::string dst) {
    int hPlayback = 0;
    NET_DVR_TIME sttime = struStartTime.get_struct();
    NET_DVR_TIME stoptime = struStopTime.get_struct();
    VideoBlock block = this->find_named_block(struStartTime, struStopTime);
    VideoBlock block_to_compare = VideoBlock(NetDVRTime(sttime), NetDVRTime(stoptime));

    if (block.str() == block_to_compare.str()) {
        std::cout << "found block and downloading whole named block" << std::endl;
        return this->setup_playback_by_name((char*) block.get_name().c_str(), (char*) dst.c_str());
    }
    if ((hPlayback = NET_DVR_GetFileByTime(lUserID, 1, &sttime, &stoptime, (char*) dst.c_str())) < 0)
        std::cout << "block not found and downloading by time" << std::endl;
        return this->get_error("setup_playback");
    return hPlayback;
}

int HikvisionDownloader::download_block_by_name(std::string name, std::string dstfile){
    int playback = this->setup_playback_by_name((char*) name.c_str(), (char*) dstfile.c_str());
    return this->record_playback(playback);
}

int HikvisionDownloader::download_block_by_time(NetDVRTime struStartTime, NetDVRTime struStopTime, std::string dstfile){
    int playback = this->setup_playback_by_time(struStartTime, struStopTime, (char*) dstfile.c_str());
    return this->record_playback(playback);
}

int HikvisionDownloader::record_playback(int playback){
    if (!NET_DVR_PlayBackControl(playback, NET_DVR_PLAYSTART, 0, NULL))
        return this->get_error("playback_control");

    int nPos = 0;
    for (nPos = 0; nPos < 100 && nPos >= 0; nPos = NET_DVR_GetDownloadPos(playback))
        usleep(5000*1000); //millisecond


    if (!NET_DVR_StopGetFile(playback))
        return this->get_error("stop_get_file");

    if (nPos < 0 || nPos > 100)
        return this->get_error("download");

    return 0;
}

NET_DVR_FILECOND HikvisionDownloader::mount_file_query(NetDVRTime struStartTime, NetDVRTime struStopTime) {
    NET_DVR_FILECOND fileQuery;
    fileQuery.dwFileType = 0xFF;
    fileQuery.lChannel = 1;
    fileQuery.dwIsLocked = 0;
    fileQuery.dwUseCardNo = 0;
    struStartTime.copy(fileQuery.struStartTime);

    struStopTime.copy(fileQuery.struStopTime);
    return fileQuery;
}

int HikvisionDownloader::generate_file_handler(NET_DVR_FILECOND fileQuery) {
    //Search recording files
    NET_DVR_FILECOND fileQueryCopy = fileQuery;
    int lFindHandle = NET_DVR_FindFile_V30(lUserID, &fileQueryCopy);
    if (lFindHandle < 0) return get_error("find file");
    return lFindHandle;
}

void HikvisionDownloader::print_time_structure(NET_DVR_TIME struTime) {
    std::cout << struTime.dwYear << "/" << struTime.dwMonth << "/" << struTime.dwDay << " " << struTime.dwHour << ":" << struTime.dwMinute << ":" << struTime.dwSecond << std::endl;
}

VideoBlock HikvisionDownloader::find_named_block(NetDVRTime struStartTime, NetDVRTime struStopTime) {
    
    NET_DVR_FILECOND fileQuery = this->mount_file_query(struStartTime, struStopTime);
    // std::cout <<  "userId: " << lUserID << "\nchannel: " << fileQuery.lChannel << "\nfileType: " << fileQuery.dwFileType << "\nisLocked: " << fileQuery.dwIsLocked << "\nuseCardNo: " << fileQuery.dwUseCardNo << "\ncardNumber: " << fileQuery.sCardNumber << std::endl;
    // print_time_structure(fileQuery.struStartTime);
    // print_time_structure(fileQuery.struStopTime);

    NET_DVR_FINDDATA_V30 struFileData;
    int fileHandler = this->generate_file_handler(fileQuery);
    while (true)
    {
        int result = NET_DVR_FindNextFile_V30(fileHandler, &struFileData);
        if (result == NET_DVR_ISFINDING) {
            continue;
        }
        else if (result == NET_DVR_FILE_SUCCESS) {   
            char strFileName[256] = {0};
            sprintf(strFileName, "%s", struFileData.sFileName);
            // this->print_time_structure(struFileData.struStartTime);
            // this->print_time_structure(struFileData.struStopTime);
            std::string ret = strFileName;
            NET_DVR_FindClose_V30(fileHandler);
            VideoBlock video_block = VideoBlock(
                NetDVRTime(
                    struFileData.struStartTime), 
                NetDVRTime(
                    struFileData.struStopTime),
                ret
            );
            return video_block;
        }
        else if (result == NET_DVR_FILE_NOFIND || result == NET_DVR_NOMOREFILE)
        {
            this->get_error("no file found");
        }
        else
        {
            this->get_error("find file fail for illegal get file state");
        }
    }
    //Stop searching
    if (fileHandler > 0)
    {
        NET_DVR_FindClose_V30(fileHandler);
    }
}

std::list<VideoBlock> HikvisionDownloader::list_videos(NetDVRTime struStartTime, NetDVRTime struStopTime) {

    NetDVRTime struStopTime_copy = struStopTime;
    NET_DVR_FILECOND fileQuery = this->mount_file_query(struStartTime, struStopTime);
    NET_DVR_FINDDATA_V30 struFileData;
    int fileHandler = this->generate_file_handler(fileQuery);
    std::list<VideoBlock> result_list;
    while (true)
    {
        int result = NET_DVR_FindNextFile_V30(fileHandler, &struFileData);
        if (result == NET_DVR_ISFINDING) {
            continue;
        }
        else if (result == NET_DVR_FILE_SUCCESS) {   
            VideoBlock video_block = VideoBlock(NetDVRTime(struFileData.struStartTime), NetDVRTime(struFileData.struStopTime), std::string(struFileData.sFileName));
            result_list.push_back(video_block);
            
            struStartTime = NetDVRTime(
                    struFileData.struStopTime.dwYear,
                    struFileData.struStopTime.dwMonth,
                    struFileData.struStopTime.dwDay,
                    struFileData.struStopTime.dwHour,
                    struFileData.struStopTime.dwMinute,
                    struFileData.struStopTime.dwSecond + 1
            );

            struStopTime = NetDVRTime(
                    struFileData.struStopTime.dwYear,
                    struFileData.struStopTime.dwMonth,
                    struFileData.struStopTime.dwDay,
                    struFileData.struStopTime.dwHour,
                    struFileData.struStopTime.dwMinute,
                    struFileData.struStopTime.dwSecond + 10
            );

            if (struStopTime > struStopTime_copy) {
                return result_list;
            }

            fileQuery = this->mount_file_query(struStartTime, struStopTime);
            fileHandler = this->generate_file_handler(fileQuery);

        }
        else if (result == NET_DVR_FILE_NOFIND || result == NET_DVR_NOMOREFILE)
        {
            struStartTime = NetDVRTime(struFileData.struStopTime);

            struFileData.struStopTime.dwMinute += 1;
            struStopTime = NetDVRTime(struFileData.struStopTime);

            std::cout<< struStartTime.str() << std::endl; 
            std::cout<< struStopTime.str() << std::endl; 

            if (struStopTime_copy > struStopTime) {
                fileQuery = this->mount_file_query(struStartTime, struStopTime);
                fileHandler = this->generate_file_handler(fileQuery);
                continue;
            }
            return result_list;
        }
        else
        {
            std::cout << "illegal get file state" << std::endl;
            return result_list;
            this->get_error("find file fail for illegal get file state");
        }
    }
    //Stop searching
    std::cout << fileHandler << std::endl;
    if (fileHandler > 0)
    {
        NET_DVR_FindClose_V30(fileHandler);
    }
    return result_list;
}


std::list<VideoBlock> HikvisionDownloader::download_all_videos(NetDVRTime struStartTime, NetDVRTime struStopTime) {

    NetDVRTime struStopTime_copy = struStopTime;
    NET_DVR_FILECOND fileQuery = this->mount_file_query(struStartTime, struStopTime);

    NET_DVR_FINDDATA_V30 struFileData;
    int fileHandler = this->generate_file_handler(fileQuery);
    std::list<VideoBlock> result_list;
    while (true)
    {
        int result = NET_DVR_FindNextFile_V30(fileHandler, &struFileData);
        if (result == NET_DVR_ISFINDING) {
            continue;
        }
        else if (result == NET_DVR_FILE_SUCCESS) {   
            VideoBlock video_block = VideoBlock(NetDVRTime(struFileData.struStartTime), NetDVRTime(struFileData.struStopTime), std::string(struFileData.sFileName));
            result_list.push_back(video_block);
            
            struStartTime = NetDVRTime(
                    struFileData.struStopTime.dwYear,
                    struFileData.struStopTime.dwMonth,
                    struFileData.struStopTime.dwDay,
                    struFileData.struStopTime.dwHour,
                    struFileData.struStopTime.dwMinute,
                    struFileData.struStopTime.dwSecond + 1
            );

            struStopTime = NetDVRTime(
                    struFileData.struStopTime.dwYear,
                    struFileData.struStopTime.dwMonth,
                    struFileData.struStopTime.dwDay,
                    struFileData.struStopTime.dwHour,
                    struFileData.struStopTime.dwMinute,
                    struFileData.struStopTime.dwSecond + 10
            );

            if (struStopTime > struStopTime_copy) {
                return result_list;
            }

            fileQuery = this->mount_file_query(struStartTime, struStopTime);
            fileHandler = this->generate_file_handler(fileQuery);
            this->download_block_by_name(std::string(struFileData.sFileName), std::string(struFileData.sFileName)+".mp4");
        }
        else if (result == NET_DVR_FILE_NOFIND || result == NET_DVR_NOMOREFILE)
        {
            return result_list;
            this->get_error("no file found");
        }
        else
        {
            return result_list;
            this->get_error("find file fail for illegal get file state");
        }
    }
    //Stop searching
    std::cout << fileHandler << std::endl;
    if (fileHandler > 0)
    {
        NET_DVR_FindClose_V30(fileHandler);
    }
    return result_list;
}
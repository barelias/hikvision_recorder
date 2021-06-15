#include "./hikvision_download_tool.h"
#include "incEn/HCNetSDK.h"
#include <stdio.h>
#include <string>
#include <unistd.h>

HikvisionDownloader::HikvisionDownloader(
    char *addr,
    int port,
    char *user,
    char *passwd
) {
    this->setup();
    this->login(addr, port, user, passwd);
}

int HikvisionDownloader::get_error(char *instance){
    int error = NET_DVR_GetLastError();
    printf("%s error [%d]\n", instance, error);
    throw error;
}

void HikvisionDownloader::setup(){
    NET_DVR_Init();
    NET_DVR_SetConnectTime(CON_TIME, 1);
    NET_DVR_SetReconnect(RECON_TIME, true);
}

LONG HikvisionDownloader::login(char *addr, int port, char *user, char *passwd){
    this->lUserID = NET_DVR_Login_V30(addr, port, user, passwd, &this->struDeviceInfo);
    if (lUserID < 0) {
        int error = get_error("login");
        return error;
    }
}

NET_DVR_TIME HikvisionDownloader::get_time_object(int year, int month, int day, int hours, int minutes, int seconds) {
    NET_DVR_TIME struTime;
    struTime.dwYear = year;
    struTime.dwMonth = month;
    struTime.dwDay = day;
    struTime.dwHour = hours;
    struTime.dwMinute = minutes;
    struTime.dwSecond = seconds;
    return struTime;
}

int HikvisionDownloader::setup_playback_by_name(char *src, char *dst) {
    int bRes = 1;
    int hPlayback = 0;
    printf ("%s -> %s\n", src, dst);
    if ((hPlayback = NET_DVR_GetFileByName(this->lUserID, src, dst)) < 0)
        return this->get_error("setup_playback");
    return hPlayback;
}

int HikvisionDownloader::download_block_by_name(char *name, char *dstfile){
    int playback = this->setup_playback_by_name(name, dstfile);
    return this->record_playback(playback);
}

int HikvisionDownloader::record_playback(int playback){
    if (!NET_DVR_PlayBackControl(playback, NET_DVR_PLAYSTART, 0, NULL))
        return this->get_error("playback_control");

    int nPos = 0;
    for (nPos = 0; nPos < 100 && nPos >= 0; nPos = NET_DVR_GetDownloadPos(playback))
        usleep(5000*1000); //millisecond

    printf("have got %d\n", nPos);
    
    if (!NET_DVR_StopGetFile(playback))
        return this->get_error("stop_get_file");

    if (nPos < 0 || nPos > 100)
        return this->get_error("download");

    return 0;
}

NET_DVR_FILECOND HikvisionDownloader::mount_file_query(NET_DVR_TIME struStartTime, NET_DVR_TIME struStopTime) {
    NET_DVR_FILECOND fileQuery;
    fileQuery.dwFileType = 0xFF;
    fileQuery.lChannel = 1;
    fileQuery.dwIsLocked = 0;
    fileQuery.dwUseCardNo = 0;

    fileQuery.struStartTime.dwYear = struStartTime.dwYear;
    fileQuery.struStartTime.dwMonth = struStartTime.dwMonth;
    fileQuery.struStartTime.dwDay = struStartTime.dwDay;
    fileQuery.struStartTime.dwHour = struStartTime.dwHour;
    fileQuery.struStartTime.dwMinute = struStartTime.dwMinute;
    fileQuery.struStartTime.dwSecond = struStartTime.dwSecond;

    fileQuery.struStopTime.dwYear = struStopTime.dwYear;
    fileQuery.struStopTime.dwMonth = struStopTime.dwMonth;
    fileQuery.struStopTime.dwDay = struStopTime.dwDay;
    fileQuery.struStopTime.dwHour = struStopTime.dwHour;
    fileQuery.struStopTime.dwMinute = struStopTime.dwMinute;
    fileQuery.struStopTime.dwSecond = struStopTime.dwSecond;
    return fileQuery;
}

int HikvisionDownloader::generate_file_handler(NET_DVR_FILECOND fileQuery) {
    //Search recording files
    int lFindHandle = NET_DVR_FindFile_V30(this->lUserID, &fileQuery);
    if (lFindHandle < 0) return get_error("find file");
    return lFindHandle;
}

void HikvisionDownloader::print_time_structure(NET_DVR_TIME struTime) {
    printf("%d/%d/%d %d:%d:%d\n", 
    struTime.dwYear, 
    struTime.dwMonth, 
    struTime.dwDay, 
    struTime.dwHour,
    struTime.dwMinute,
    struTime.dwSecond);
}

std::string HikvisionDownloader::find_name_of_block(NET_DVR_TIME struStartTime, NET_DVR_TIME struStopTime) {
    
    NET_DVR_FILECOND fileQuery = this->mount_file_query(struStartTime, struStopTime);
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
            printf ("block found: \n");
            this->print_time_structure(struFileData.struStartTime);
            this->print_time_structure(struFileData.struStopTime);
            std::string ret = strFileName;
            NET_DVR_FindClose_V30(fileHandler);
            return strFileName;
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
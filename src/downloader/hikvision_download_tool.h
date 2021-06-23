#include "incEn/HCNetSDK.h"
#include <string>
#include <list>

#define CON_TIME 20000
#define RECON_TIME 20000

typedef struct tagDownloadOutput {

} DownloadOutput;

class NetDVRTime {
    public:
        NetDVRTime(int year, int month, int day, int hours, int minutes, int seconds);
        NetDVRTime(NET_DVR_TIME dvr_time): dvr_time(dvr_time) {};
        std::string str();
        void copy(NET_DVR_TIME &another);
        NET_DVR_TIME get_struct() { return this->dvr_time; }
        bool operator==(const NetDVRTime& nt);
        bool operator>(const NetDVRTime& nt);
    private:
        NET_DVR_TIME dvr_time;
};

class VideoBlock {
    public:
        VideoBlock(NetDVRTime dvr_time_initial, NetDVRTime dvr_time_final): dvr_time_initial(dvr_time_initial), dvr_time_final(dvr_time_final) { this->name = ""; }
        VideoBlock(NetDVRTime dvr_time_initial, NetDVRTime dvr_time_final, std::string name): dvr_time_initial(dvr_time_initial), dvr_time_final(dvr_time_final), name(name) {}
        NetDVRTime get_initial() { return this->dvr_time_initial; }
        NetDVRTime get_final() { return this->dvr_time_initial; }
        std::string str();
        std::string get_name() { return this->name; }
        bool operator==(const VideoBlock& vb);
    private:
        std::string name;
        NetDVRTime dvr_time_initial;
        NetDVRTime dvr_time_final;  
};

class HikvisionDownloader {
    public:
        int download_block_by_name(std::string name, std::string dstfile);
        VideoBlock find_named_block(NetDVRTime struStartTime, NetDVRTime struStopTime);
        int download_block_by_time(NetDVRTime struStartTime, NetDVRTime struStopTime, std::string dstfile);
        HikvisionDownloader(std::string addr, int port, std::string user, std::string passwd);
        ~HikvisionDownloader() { NET_DVR_Cleanup(); };
        NetDVRTime get_time_object(int year, int month, int day, int hours, int minutes, int seconds);
        std::list<VideoBlock> list_videos(NetDVRTime struStartTime, NetDVRTime struStopTime);
        std::list<VideoBlock> download_all_videos(NetDVRTime struStartTime, NetDVRTime struStopTime);
    private:
        LONG lUserID;
        std::string user;
        std::string addr;
        int port;
        std::string passwd;
        static void print_time_structure(NET_DVR_TIME struTime);
        NET_DVR_DEVICEINFO_V30 struDeviceInfo;
        LONG login(std::string addr, int port, std::string user, std::string passwd);
        void setup();
        LONG get_error(std::string instance);
        int setup_playback_by_name(std::string src, std::string dst);
        int setup_playback_by_time(NetDVRTime struStartTime, NetDVRTime struStopTime, std::string dst);
        NET_DVR_FILECOND mount_file_query(NetDVRTime struStartTime, NetDVRTime struStopTime);
        int generate_file_handler(NET_DVR_FILECOND fileQuery);
        int record_playback(int playback);
};

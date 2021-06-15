#include "incEn/HCNetSDK.h"
#include <string>

#define CON_TIME 2000
#define RECON_TIME 10000

typedef struct tagDownloadOutput {

} DownloadOutput;

class HikvisionDownloader {
    public:
        int download_block_by_name(char *name, char *dstfile);
        std::string find_name_of_block(NET_DVR_TIME struStartTime, NET_DVR_TIME struStopTime);
        int download_block_by_time(NET_DVR_TIME struStartTime, NET_DVR_TIME struStopTime);
        HikvisionDownloader(char *addr, int port, char *user, char *passwd);
        NET_DVR_TIME get_time_object(int year, int month, int day, int hours, int minutes, int seconds);
        static void print_time_structure(NET_DVR_TIME struTime);
    private:
        LONG lUserID;
        NET_DVR_DEVICEINFO_V30 struDeviceInfo;
        LONG login(char *addr, int port, char *user, char *passwd);
        void setup();
        LONG get_error(char *instance);
        int setup_playback_by_name(char *src, char *dst);
        int setup_playback_by_time(char *src, char *dst);
        NET_DVR_FILECOND mount_file_query(NET_DVR_TIME struStartTime, NET_DVR_TIME struStopTime);
        int generate_file_handler(NET_DVR_FILECOND fileQuery);
        int record_playback(int playback);
};
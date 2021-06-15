#include "src/hikvision_download_tool.h"
#include <string>

int main(int argc, char *argv[]){
    HikvisionDownloader hikDownloader = HikvisionDownloader("10.8.0.31", 12556, "visio", "visio123");
    NET_DVR_TIME initTime = hikDownloader.get_time_object(2021, 6, 13, 19, 0, 0);
    NET_DVR_TIME endTime = hikDownloader.get_time_object(2021, 6, 13, 19, 1, 0);
    hikDownloader.print_time_structure(initTime);
    hikDownloader.print_time_structure(endTime);
    std::string file_name = hikDownloader.find_name_of_block(initTime, endTime);
    hikDownloader.download_block_by_name((char *) file_name.c_str(), "./output.mp4");
}
#include "../src/downloader/hikvision_download_tool.h"
#include <string>
#include <cstdio>
#include <cstring>
#include <list>
#include <iostream>

int main(int argc, char *argv[])
{

    // std::cout << argv[2] << ":" << atoi(argv[3]) << ":" << argv[4] << "@" << argv[5] << std::endl;
    HikvisionDownloader hikDownloader = HikvisionDownloader(argv[2], atoi(argv[3]), argv[4], argv[5]);
    if (!strcmp(argv[1], "download")) {
        NetDVRTime initTime = hikDownloader.get_time_object(atoi(argv[7]), atoi(argv[8]), atoi(argv[9]), atoi(argv[10]), atoi(argv[11]), atoi(argv[12]));
        NetDVRTime endTime = hikDownloader.get_time_object(atoi(argv[13]), atoi(argv[14]), atoi(argv[15]), atoi(argv[16]), atoi(argv[17]), atoi(argv[18]));
        return hikDownloader.download_block_by_time(initTime, endTime, argv[6]);
    } else if (!strcmp(argv[1], "list_and_download")) {
        NetDVRTime initTime = hikDownloader.get_time_object(atoi(argv[6]), atoi(argv[7]), atoi(argv[8]), atoi(argv[9]), atoi(argv[10]), atoi(argv[11]));
        NetDVRTime endTime = hikDownloader.get_time_object(atoi(argv[12]), atoi(argv[13]), atoi(argv[14]), atoi(argv[15]), atoi(argv[16]), atoi(argv[17]));
        std::list<VideoBlock> video_blocks = hikDownloader.download_all_videos(initTime, endTime);
        for (auto& x: video_blocks) {
            if (x.str() == (--video_blocks.end())->str()) {
               std::cout << x.str() << std::endl;    
            } else {
               std::cout << x.str() << ",";    
            }
        }
        return 0;
    } else if (!strcmp(argv[1], "list")) {
        NetDVRTime initTime = hikDownloader.get_time_object(atoi(argv[6]), atoi(argv[7]), atoi(argv[8]), atoi(argv[9]), atoi(argv[10]), atoi(argv[11]));
        NetDVRTime endTime = hikDownloader.get_time_object(atoi(argv[12]), atoi(argv[13]), atoi(argv[14]), atoi(argv[15]), atoi(argv[16]), atoi(argv[17]));
        std::list<VideoBlock> video_blocks = hikDownloader.list_videos(initTime, endTime);
        for (auto& x: video_blocks) {
            if (x.str() == (--video_blocks.end())->str()) {
               std::cout << x.str() << std::endl;    
            } else {
               std::cout << x.str() << ",";    
            }
        }
        return 0;
    } else {
        printf ("No function selected");
        return 0;
    }
}
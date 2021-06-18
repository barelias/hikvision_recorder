#define PY_SSIZE_T_CLEAN
#include <python3.8/Python.h>
#include <boost/python.hpp>
#include "hikvision_download_tool.h"
#include <stdio.h>
#include <list>
using namespace boost::python;

list list_videos(HikvisionDownloader* hik, NetDVRTime startTime, NetDVRTime finalTime)
{
    list result;
    std::list<VideoBlock> result_list_cpp = hik->list_videos(startTime, finalTime);

    std::list<VideoBlock>::iterator it;
    for (it = result_list_cpp.begin(); it != result_list_cpp.end(); ++it){
        result.append(*it);    
    }
    return result;
}

list create_object_and_list_videos(NetDVRTime startTime, NetDVRTime finalTime, std::string addr, int port, std::string user, std::string passwd) {
    list result;
    HikvisionDownloader hik = HikvisionDownloader(addr, port, user, passwd);
    NetDVRTime initTime = hik.get_time_object(2021, 6, 16, 14, 0, 0);
    NetDVRTime endTime = hik.get_time_object(2021, 6, 16, 14, 1, 0);
    std::list<VideoBlock> result_list_cpp = hik.list_videos(initTime, endTime);

    std::list<VideoBlock>::iterator it;
    for (it = result_list_cpp.begin(); it != result_list_cpp.end(); ++it){
        result.append(*it);    
    }
    return result;
}

BOOST_PYTHON_MODULE(downloader)
{
    class_<HikvisionDownloader>("HikvisionDownloader", init<std::string, int, std::string, std::string>())
        .def ("download_block_by_name", &HikvisionDownloader::download_block_by_name)
        .def ("find_name_of_block", &HikvisionDownloader::find_named_block)
        .def ("download_block_by_time", &HikvisionDownloader::download_block_by_time) 
        .def ("get_time_object", &HikvisionDownloader::get_time_object)
        .def ("list_videos", &list_videos);

    class_<NetDVRTime>("dvr_datetime", init<int, int, int, int, int, int>())
        .def ("str", &NetDVRTime::str);

    class_<VideoBlock>("video_block", init<NetDVRTime, NetDVRTime>())
        .def ("str", &VideoBlock::str)
        .add_property ("init_time", &VideoBlock::get_initial)
        .add_property ("end_time", &VideoBlock::get_final);

    def ("list_videos", &create_object_and_list_videos);
}
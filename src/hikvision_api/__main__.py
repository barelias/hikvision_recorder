from hikvision_api.downloader import HikvisionDownloader, dvr_datetime
from datetime import date, datetime
import sys

if __name__ == '__main__':

    func, init_date, end_date, host, port, user, password = sys.argv[2:8]
    dt_init = datetime.fromisoformat(init_date)
    dt_end = datetime.fromisoformat(end_date)

    hik = HikvisionDownloader(host, int(port), user, password)
    init_time = dvr_datetime(
        dt_init.year, 
        dt_init.month, 
        dt_init.day,
        dt_init.hour,
        dt_init.minute,
        dt_init.second
    )

    end_time = dvr_datetime(
        dt_end.year, 
        dt_end.month, 
        dt_end.day,
        dt_end.hour,
        dt_end.minute,
        dt_end.second
    )

    if func == 'download':
        output = sys.argv[9]
        hik.download_block_by_time(init_time, end_time, output)
    elif func == 'list':
        file_list = hik.list_videos(init_time, end_time)
        for fl in file_list:
            print (fl.str())
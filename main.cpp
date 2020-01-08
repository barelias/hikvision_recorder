#include <stdio.h>
#include <unistd.h>
#include <stdlib.h>
#include "incEn/HCNetSDK.h"

using namespace std;

int donwload_file(char *addr, 
                  int port, 
                  char *user, 
                  char *passwd, 
                  char *filepath,
                  int begin_year,
                  int begin_month,
                  int begin_day,
                  int begin_hour,
                  int begin_minute,
                  int begin_second,
                  int end_year,
                  int end_month,
                  int end_day,
                  int end_hour,
                  int end_minute,
                  int end_second
                ) {

    NET_DVR_Init();
    NET_DVR_SetConnectTime(2000, 1);
    NET_DVR_SetReconnect(10000, true);

    LONG lUserID;
    NET_DVR_DEVICEINFO_V30 struDeviceInfo;
    
    lUserID = NET_DVR_Login_V30(addr, port, user, passwd, &struDeviceInfo);

    if (lUserID > 0)
    {
        printf("Login error %d\n", NET_DVR_GetLastError());
        NET_DVR_Cleanup();
        return 0;
    }

    NET_DVR_TIME struStartTime, struStopTime;

    struStartTime.dwYear = begin_year;
    struStartTime.dwMonth = begin_month;
    struStartTime.dwDay = begin_day;
    struStartTime.dwHour = begin_hour;
    struStartTime.dwMinute = begin_minute;
    struStartTime.dwSecond = begin_second;

    struStopTime.dwYear = end_year;
    struStopTime.dwMonth = end_month;
    struStopTime.dwDay = end_day;
    struStopTime.dwHour = end_hour;
    struStopTime.dwMinute = end_minute;
    struStopTime.dwSecond = end_second;

    int hPlayback;
    hPlayback = NET_DVR_GetFileByTime(lUserID, 1, &struStartTime, &struStopTime, filepath);
    if (hPlayback < 0)
    {
        printf("NET_DVR_GetFileByTime fail,last error %d\n", NET_DVR_GetLastError());
        NET_DVR_Logout(lUserID);
        NET_DVR_Cleanup();
        return 0;
    }

    if (!NET_DVR_PlayBackControl(hPlayback, NET_DVR_PLAYSTART, 0, NULL))
    {
        printf("play back control failed [%d]\n", NET_DVR_GetLastError());
        NET_DVR_Logout(lUserID);
        NET_DVR_Cleanup();
        return 0;
    }
    int nPos = 0;
    for (nPos = 0; nPos < 100 && nPos >= 0; nPos = NET_DVR_GetDownloadPos(hPlayback))
    {
        sleep(5); //millisecond
    }
    if (!NET_DVR_StopGetFile(hPlayback))
    {
        printf("failed to stop get file [%d]\n", NET_DVR_GetLastError());
        NET_DVR_Logout(lUserID);
        NET_DVR_Cleanup();
        return 0;
    }
    if (nPos < 0 || nPos > 100)
    {
        printf("download err [%d]\n", NET_DVR_GetLastError());
        NET_DVR_Logout(lUserID);
        NET_DVR_Cleanup();
        return 0;
    }
    //Logout
    NET_DVR_Logout(lUserID);
    // Release SDK resource
    NET_DVR_Cleanup();
    return 0;
}

int main(int argc, char *argv[])
{


    for (int i = 0; i < argc; i++) {
        printf ("%s\n", argv[i]);
    }

    return donwload_file(
                argv[0], 
                atoi(argv[1]), 
                argv[2], 
                argv[3], 
                argv[4],
                atoi(argv[5]),
                atoi(argv[6]),
                atoi(argv[7]),
                atoi(argv[8]),
                atoi(argv[9]),
                atoi(argv[10]),
                atoi(argv[11]),
                atoi(argv[12]),
                atoi(argv[13]),
                atoi(argv[14]),
                atoi(argv[15]),
                atoi(argv[16])
                );
}

// ./main.o 10.8.0.2 10556 admin2 iuGyf09213 test.mp4 2020 1 7 21 0 0 2020 1 7 21 20 0
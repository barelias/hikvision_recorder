#include <stdio.h>
#include <unistd.h>
#include <stdlib.h>
#include <cstring>
#include "incEn/HCNetSDK.h"

using namespace std;

long int donwload_file(char *addr, 
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
    printf ("Trying to log in\n");
    if (lUserID < 0)
    {
        int error = NET_DVR_GetLastError();
        printf("Login error %d\n", error);
        NET_DVR_Cleanup();
        return error;
    }
    printf ("Login Succesful\n");
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

    // printf("%d %d %d %d %d %d %d %d %d %d %d %d\n", struStartTime.dwYear, struStartTime.dwMonth, struStartTime.dwDay, struStartTime.dwHour, struStartTime.dwMinute, struStartTime.dwSecond, struStopTime.dwYear, struStopTime.dwMonth, struStopTime.dwDay, struStopTime.dwHour, struStopTime.dwMinute, struStopTime.dwSecond, struStartTime.dwYear, struStartTime.dwMonth, struStartTime.dwDay, struStartTime.dwHour, struStartTime.dwMinute, struStartTime.dwSecond, struStopTime.dwYear, struStopTime.dwMonth, struStopTime.dwDay, struStopTime.dwHour, struStopTime.dwMinute, struStopTime.dwSecond);
    // printf("%d %s\n", lUserID, filepath);
    int hPlayback;
    hPlayback = NET_DVR_GetFileByTime(lUserID, 1, &struStartTime, &struStopTime, filepath);
    if (hPlayback < 0)
    {

        int error = NET_DVR_GetLastError();
        NET_DVR_Logout(lUserID);
        NET_DVR_Cleanup();
        return error;
    }

    if (!NET_DVR_PlayBackControl(hPlayback, NET_DVR_PLAYSTART, 0, NULL))
    {
        int error = NET_DVR_GetLastError();
        NET_DVR_Logout(lUserID);
        NET_DVR_Cleanup();
        return error;
    }
    int nPos = 0;

    for (nPos = 0; nPos < 100 && nPos >= 0; nPos = NET_DVR_GetDownloadPos(hPlayback))
    {
        sleep(5); //millisecond
    }
    if (!NET_DVR_StopGetFile(hPlayback))
    {
        int error = NET_DVR_GetLastError();
        printf("failed to stop get file [%d]\n", error);
        NET_DVR_Logout(lUserID);
        NET_DVR_Cleanup();
        return error;
    }

    return 12334;
    if (nPos < 0 || nPos > 100)
    {
        int error = NET_DVR_GetLastError();
        if (nPos == 200) error=4000;
        printf("download err [%d]\n", error);
        NET_DVR_Logout(lUserID);
        NET_DVR_Cleanup();

        return error;
    }
    //Logout
    NET_DVR_Logout(lUserID);
    // Release SDK resource
    NET_DVR_Cleanup();
    return 0;
}

int test_connection(char *addr, 
                  int port, 
                  char *user, 
                  char *passwd
                ) {

    NET_DVR_Init();
    NET_DVR_SetConnectTime(2000, 1);
    NET_DVR_SetReconnect(10000, true);

    LONG lUserID;
    NET_DVR_DEVICEINFO_V30 struDeviceInfo;
    
    lUserID = NET_DVR_Login_V30(addr, port, user, passwd, &struDeviceInfo);

    if (lUserID > 0) {
        printf("Login error %d\n", NET_DVR_GetLastError());
        NET_DVR_Cleanup();
        return 0;
    } else {
        printf("Connected succesfully\n");
        NET_DVR_Logout(lUserID);
        NET_DVR_Cleanup();
        return 1;
    }

}

int main(int argc, char *argv[])
{

    if (!strcmp(argv[1], "download")) {
        return donwload_file(
                    argv[2], 
                    atoi(argv[3]), 
                    argv[4], 
                    argv[5],
                    argv[6], 
                    atoi(argv[7]),
                    atoi(argv[8]),
                    atoi(argv[9]),
                    atoi(argv[10]),
                    atoi(argv[11]),
                    atoi(argv[12]),
                    atoi(argv[13]),
                    atoi(argv[14]),
                    atoi(argv[15]),
                    atoi(argv[16]),
                    atoi(argv[17]),
                    atoi(argv[18])
                    );
    } else if (!strcmp(argv[1], "verify_login")) {
        return test_connection(
            argv[2], 
            atoi(argv[3]), 
            argv[4], 
            argv[5]
            );
    } else {
        printf ("No function selected");
        return 0;
    }
}

// ./main.o 10.8.0.2 10556 admin2 iuGyf09213 test.mp4 2020 1 7 21 0 0 2020 1 7 21 20 0
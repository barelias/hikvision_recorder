// #include <Python.h>
#include <stdio.h>
#include <iostream>
#include <unistd.h>
#include "incEn/HCNetSDK.h"

using namespace std;

// static PyObject*
// fib(PyObject* self, PyObject* args)
// {
//     int n;

//     if (!PyArg_ParseTuple(args, "i", &n))
//         return NULL;

//     return Py_BuildValue("i", _fib(n));
// }

// static PyMethodDef FibMethods[] = {
//     {"fib", fib, METH_VARARGS, "Calculate the Fibonacci numbers."},
//     {NULL, NULL, 0, NULL}
// };

// PyMODINIT_FUNC
// initfib(void)
// {
//     (void) Py_InitModule("fib", FibMethods);
// }

int main() {

    NET_DVR_Init();
    NET_DVR_SetConnectTime(2000, 1);
    NET_DVR_SetReconnect(10000, true);

    LONG lUserID;
    NET_DVR_DEVICEINFO_V30 struDeviceInfo;
    lUserID = NET_DVR_Login_V30("10.8.0.2", 10556, "admin2", "iuGyf09213", &struDeviceInfo);

    if (lUserID > 0)
    {
        printf("Login error %d\n", NET_DVR_GetLastError());
        NET_DVR_Cleanup();
        return 0;
    }

    NET_DVR_TIME struStartTime, struStopTime;

    struStartTime.dwYear = 2020;
    struStartTime.dwMonth = 1;
    struStartTime.dwDay = 7;
    struStartTime.dwHour = 5;
    struStartTime.dwMinute = 0;
    struStartTime.dwSecond = 0;

    struStopTime.dwYear = 2020;
    struStopTime.dwMonth = 1;
    struStopTime.dwDay = 7;
    struStopTime.dwHour = 5;
    struStopTime.dwMinute = 1;
    struStopTime.dwSecond = 0;

    int hPlayback;
    hPlayback = NET_DVR_GetFileByTime(lUserID, 1, &struStartTime, &struStopTime, "./test.mp4");
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
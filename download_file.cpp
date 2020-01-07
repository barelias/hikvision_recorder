#include <Python.h>
#include <stdio.h>
#include <unistd.h>
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

static PyObject*
download(PyObject* self, PyObject* args)
{

    char *addr;
    int port; 
    char *user; 
    char *passwd; 
    char *filepath;
    int begin_year;
    int begin_month;
    int begin_day;
    int begin_hour;
    int begin_minute;
    int begin_second;
    int end_year;
    int end_month;
    int end_day;
    int end_hour;
    int end_minute;
    int end_second;

    if (!PyArg_ParseTuple(args, "isssiiiiiiiiiiii", 
        &addr,
        &port, 
        &user, 
        &passwd, 
        &filepath,
        &begin_year,
        &begin_month,
        &begin_day,
        &begin_hour,
        &begin_minute,
        &begin_second,
        &end_year,
        &end_month,
        &end_day,
        &end_hour,
        &end_minute,
        &end_second
    ))
        return NULL;

    
    return Py_BuildValue("i", donwload_file(
                addr, 
                port, 
                user, 
                passwd, 
                filepath,
                begin_year,
                begin_month,
                begin_day,
                begin_hour,
                begin_minute,
                begin_second,
                end_year,
                end_month,
                end_day,
                end_hour,
                end_minute,
                end_second
                ));
}

static PyMethodDef ONVIFMethods[] = {
    {"download_file", download, METH_VARARGS, "Retrieve lost files"},
    {NULL, NULL, 0, NULL}
};

static struct PyModuleDef cModPyDem =
{
    PyModuleDef_HEAD_INIT,
    "hikvision_recorder", /* name of module */
    "",          /* module documentation, may be NULL */
    -1,          /* size of per-interpreter state of the module, or -1 if the module keeps state in global variables. */
    ONVIFMethods
};

PyMODINIT_FUNC PyInit_cModPyDem(void)
{
    return PyModule_Create(&cModPyDem);
}
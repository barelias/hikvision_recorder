HCNetSDKFLAGS= -L./lib -L./lib/HCNetSDKCom -lhcnetsdk -lhpr -lHCCore -lHCCoreDevCfg -lStreamTransClient -lSystemTransform -lHCPreview -lHCAlarm -lHCGeneralCfgMgr -lHCIndustry -lHCPlayBack -lHCVoiceTalk -lanalyzedata -lHCDisplay
PYTHONFLAGS= -I/usr/include/python3.8 -Wall -Wextra -fpie $(python3-config --cflags --embed)
BOOSTFLAGS= -L/usr/lib/x86_64-linux-gnu -lboost_filesystem
all: hikvision_tool

hikvision_tool:
	g++ src/downloader/hikvision_download_tool.cpp scripts/main.cpp -o hikvision_tool $(HCNetSDKFLAGS) ${PYTHONFLAGS} ${BOOSTFLAGS}

rm:
	rm hikvision_tool
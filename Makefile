HCNetSDKFLAGS=-L./lib -L./lib/HCNetSDKCom -lhcnetsdk -L./lib -lhpr -lHCCore -lHCCoreDevCfg -lStreamTransClient -lSystemTransform -lHCPreview -lHCAlarm -lHCGeneralCfgMgr -lHCIndustry -lHCPlayBack -lHCVoiceTalk -lanalyzedata -lHCDisplay

all: main
 
main:
	g++ main.cpp -o main.o $(HCNetSDKFLAGS)
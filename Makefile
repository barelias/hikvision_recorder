HCNetSDKFLAGS=-L./lib -L./lib/HCNetSDKCom -lhcnetsdk -L./lib -lhpr -lHCCore -lHCCoreDevCfg -lStreamTransClient -lSystemTransform -lHCPreview -lHCAlarm -lHCGeneralCfgMgr -lHCIndustry -lHCPlayBack -lHCVoiceTalk -lanalyzedata -lHCDisplay

all: hikvision_tool
 
hikvision_tool:
	g++ hikvision_lib.cpp -o hikvision_tool $(HCNetSDKFLAGS)
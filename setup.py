from distutils.core import setup, Extension
import os

os.environ

setup (name = 'Hikvision Recorder',
        version = '1.0',
        description = 'This is a demo package',
        ext_modules = [
            Extension(
                'download_file', 
                sources = ['download_file.cpp'],
                library_dirs = [
                    './lib/HCNetSDKCom',
                    './lib/libz.so.1',
                    './lib/libssl.so',
                    './lib/libcrypto.so',
                    './lib/libz.so',
                    './lib/libSuperRender.so',
                    './lib/libAudioRender.so', 
                    './lib/libHCCore.so',
                    './lib/libcrypto.so.1.0.0',
                    './lib/libPlayCtrl.so',
                    './lib/libNPQos.so',
                    './lib/libssl.so.1.0.0',
                    './lib/libhcnetsdk.so',
                    './lib/libopenal.so.1',
                    './lib/libhpr.so',
                    './lib/HCNetSDKCom/libHCIndustry.so',
                    './lib/HCNetSDKCom/libiconv.so.2',
                    './lib/HCNetSDKCom/libHCPreview.so',
                    './lib/HCNetSDKCom/libHCDisplay.so',
                    './lib/HCNetSDKCom/libHCPlayBack.so',
                    './lib/HCNetSDKCom/libanalyzedata.so',
                    './lib/HCNetSDKCom/libHCVoiceTalk.so',
                    './lib/HCNetSDKCom/libHCCoreDevCfg.so',
                    './lib/HCNetSDKCom/libStreamTransClient.so',
                    './lib/HCNetSDKCom/libHCAlarm.so',
                    './lib/HCNetSDKCom/libiconv2.so',
                    './lib/HCNetSDKCom/libSystemTransform.so', 
                    './lib/HCNetSDKCom/libHCGeneralCfgMgr.so'
                ],  # path to .a or .so file(s)
                extra_compile_args=['-lhcnetsdk', '-lhpr', '-lHCCore', '-lHCCoreDevCfg', '-lStreamTransClient', '-lSystemTransform', '-lHCPreview', '-lHCAlarm', '-lHCGeneralCfgMgr', '-lHCIndustry', '-lHCPlayBack', '-lHCVoiceTalk', '-lanalyzedata', '-lHCDisplay'],
                language='c++11',
                )
            ]
      )
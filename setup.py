from setuptools import setup, Extension
import os
import pathlib

HERE = pathlib.Path(__file__).parent
README = (HERE / "README.md").read_text()

sfc_module = Extension(
    'hikvision_api.downloader', 
    sources = [
        'src/downloader/hikvision_download_tool.cpp',
        'src/downloader/hikvisionmodule.cpp'
    ],
    include_dirs=[
        '/usr/local/include',
        '/usr/include/python3.8'
    ],
    library_dirs=[
        '/usr/local/lib/boost',
        os.path.join(os.path.split(os.path.abspath(__file__))[0], 'lib'),
        os.path.join(os.path.split(os.path.abspath(__file__))[0], 'lib/HCNetSDKCom')
    ],
    runtime_library_dirs=[
        os.path.join(os.path.split(os.path.abspath(__file__))[0], 'lib'),
        os.path.join(os.path.split(os.path.abspath(__file__))[0], 'lib/HCNetSDKCom'),
        '/usr/local/lib/boost'
    ],
    libraries=[
        'boost_python38',
        'boost_filesystem',
        'hcnetsdk',
        'hpr',
        'HCCore',
        'HCCoreDevCfg',
        'StreamTransClient',
        'SystemTransform',
        'HCPreview',
        'HCAlarm',
        'HCGeneralCfgMgr',
        'HCIndustry',
        'HCPlayBack',
        'HCVoiceTalk',
        'analyzedata',
        'HCDisplay'
    ]
)

setup(
    name='hikvision-api',    
    version='1.0.0',
    description='Hikvision Module Package',
    long_description_content_type="text/markdown",
    url="https://github.com/dinthea/hikvision_recorder",
    author="Iago Elias",
    author_email="iago@sflabs.com.br",
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8.7",
    ],
    package_dir={'': 'src'},
    packages=['hikvision_api'],
    ext_modules=[sfc_module]
)
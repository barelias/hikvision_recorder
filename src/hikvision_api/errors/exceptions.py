# No error.
class ExceptionNET_DVR_NOERROR(Exception):
	pass

# User name or password error.
class ExceptionNET_DVR_PASSWORD_ERROR(Exception):
	pass

# Not authorized to do this operation.
class ExceptionNET_DVR_NOENOUGHPRI(Exception):
	pass

# SDK is not initialized.
class ExceptionNET_DVR_NOINIT(Exception):
	pass

# Channel number error. There is no corresponding channel number on the device.
class ExceptionNET_DVR_CHANNEL_ERROR(Exception):
	pass

# The number of connection with the device has exceeded the max limit.
class ExceptionNET_DVR_OVER_MAXLINK(Exception):
	pass

# Version mismatch. SDK version is not matching with the device.
class ExceptionNET_DVR_VERSIONNOMATCH(Exception):
	pass

# Failed to connect to the device. The device is off-line, or connection timeout caused by network.
class ExceptionNET_DVR_NETWORK_FAIL_CONNECT(Exception):
	pass

# Failed to send data to the device.
class ExceptionNET_DVR_NETWORK_SEND_ERROR(Exception):
	pass

# Failed to receive data from the device.
class ExceptionNET_DVR_NETWORK_RECV_ERROR(Exception):
	pass

# Timeout when receiving data from the device.
class ExceptionNET_DVR_NETWORK_RECV_TIMEOUT(Exception):
	pass

# The data sent to the device is illegal, or the data received from the device error. E.g. The input data is not supported by the device for remote configuration.
class ExceptionNET_DVR_NETWORK_ERRORDATA(Exception):
	pass

# API calling order error.
class ExceptionNET_DVR_ORDER_ERROR(Exception):
	pass

# Not authorized for this operation.
class ExceptionNET_DVR_OPERNOPERMIT(Exception):
	pass

# Executing command on the device is timeout.
class ExceptionNET_DVR_COMMANDTIMEOUT(Exception):
	pass

# Serial port number error. The assigned serial port does not exist on the device.
class ExceptionNET_DVR_ERRORSERIALPORT(Exception):
	pass

# Alarm port number error.
class ExceptionNET_DVR_ERRORALARMPORT(Exception):
	pass

# Parameter error. Input or output parameters in the SDK API is NULL, or the value or format of the parameters does not match with the requirement.
class ExceptionNET_DVR_PARAMETER_ERROR(Exception):
	pass

# Device channel is in exception status.
class ExceptionNET_DVR_CHAN_EXCEPTION(Exception):
	pass

# No hard disk on the device, and the operation of recording and hard disk configuration will fail.
class ExceptionNET_DVR_NODISK(Exception):
	pass

# Hard disk number error. The assigned hard disk number does not exist during hard disk management.
class ExceptionNET_DVR_ERRORDISKNUM(Exception):
	pass

# Device hark disk is full.
class ExceptionNET_DVR_DISK_FULL(Exception):
	pass

# Device hard disk error.
class ExceptionNET_DVR_DISK_ERROR(Exception):
	pass

# Device does not support this function.
class ExceptionNET_DVR_NOSUPPORT(Exception):
	pass

# Device is busy.
class ExceptionNET_DVR_BUSY(Exception):
	pass

# Failed to modify device parameters.
class ExceptionNET_DVR_MODIFY_FAIL(Exception):
	pass

# The inputting password format is not correct.
class ExceptionNET_DVR_PASSWORD_FORMAT_ERROR(Exception):
	pass

# Hard disk is formatting, and the operation cannot be done.
class ExceptionNET_DVR_DISK_FORMATING(Exception):
	pass

# Not enough resource on the device.
class ExceptionNET_DVR_DVRNORESOURCE(Exception):
	pass

# Device operation failed.
class ExceptionNET_DVR_DVROPRATEFAILED(Exception):
	pass

# Failed to collect local audio data or to open audio output during voice talk / broadcasting.
class ExceptionNET_DVR_OPENHOSTSOUND_FAIL(Exception):
	pass

# Voice talk channel on the device has been occupied.
class ExceptionNET_DVR_DVRVOICEOPENED(Exception):
	pass

# Time input is not correct.
class ExceptionNET_DVR_TIMEINPUTERROR(Exception):
	pass

# There is no selected file for playback.
class ExceptionNET_DVR_NOSPECFILE(Exception):
	pass

# Failed to create a file, during local recording, saving picture, getting configuration file or downloading record file.
class ExceptionNET_DVR_CREATEFILE_ERROR(Exception):
	pass

# Failed to open a file.
class ExceptionNET_DVR_FILEOPENFAIL(Exception):
	pass

# The last operation has not been completed.
class ExceptionNET_DVR_OPERNOTFINISH(Exception):
	pass

# Failed to get the current played time.
class ExceptionNET_DVR_GETPLAYTIMEFAIL(Exception):
	pass

# Failed to start playback.
class ExceptionNET_DVR_PLAYFAIL(Exception):
	pass

# The file format is not correct.
class ExceptionNET_DVR_FILEFORMAT_ERROR(Exception):
	pass

# File directory error.
class ExceptionNET_DVR_DIR_ERROR(Exception):
	pass

# Resource allocation error.
class ExceptionNET_DVR_ALLOC_RESOURCE_ERROR(Exception):
	pass

# Sound adapter mode error. Currently opened sound playing mode does not match with the set mode.
class ExceptionNET_DVR_AUDIO_MODE_ERROR(Exception):
	pass

# Buffer is not enough.
class ExceptionNET_DVR_NOENOUGH_BUF(Exception):
	pass

# Create SOCKET error.
class ExceptionNET_DVR_CREATESOCKET_ERROR(Exception):
	pass

# Set SOCKET error
class ExceptionNET_DVR_SETSOCKET_ERROR(Exception):
	pass

# The number of login or preview connections has exceeded the SDK limitation.
class ExceptionNET_DVR_MAX_NUM(Exception):
	pass

# User doest not exist. The user ID has been logged out or unavailable.
class ExceptionNET_DVR_USERNOTEXIST(Exception):
	pass

# Writing FLASH error. Failed to write FLASH during device upgrade.
class ExceptionNET_DVR_WRITEFLASHERROR(Exception):
	pass

# Failed to upgrade device. It is caused by network problem or the language mismatch between the device and the upgrade file.
class ExceptionNET_DVR_UPGRADEFAIL(Exception):
	pass

# The decode card has alreadly been initialed.
class ExceptionNET_DVR_CARDHAVEINIT(Exception):
	pass

# Failed to call API of player SDK.
class ExceptionNET_DVR_PLAYERFAILED(Exception):
	pass

# The number of login user has reached the maximum limit.
class ExceptionNET_DVR_MAX_USERNUM(Exception):
	pass

# Failed to get the IP address or physical address of local PC.
class ExceptionNET_DVR_GETLOCALIPANDMACFAIL(Exception):
	pass

# This channel hasn't started encoding.
class ExceptionNET_DVR_NOENCODEING(Exception):
	pass

# IP address not match
class ExceptionNET_DVR_IPMISMATCH(Exception):
	pass

# MAC address not match
class ExceptionNET_DVR_MACMISMATCH(Exception):
	pass

# The language of upgrading file does not match the language of the device.
class ExceptionNET_DVR_UPGRADELANGMISMATCH(Exception):
	pass

# The number of player ports has reached the maximum limit.
class ExceptionNET_DVR_MAX_PLAYERPORT(Exception):
	pass

# No enough space to backup file in backup device.
class ExceptionNET_DVR_NOSPACEBACKUP(Exception):
	pass

# No backup device.
class ExceptionNET_DVR_NODEVICEBACKUP(Exception):
	pass

# The color quality seeting of the picture does not match the requirement, and it should be limited to 24.
class ExceptionNET_DVR_PICTURE_BITS_ERROR(Exception):
	pass

# The dimension is over 128x256.
class ExceptionNET_DVR_PICTURE_DIMENSION_ERROR(Exception):
	pass

# The size of picture is over 100K
class ExceptionNET_DVR_PICTURE_SIZ_ERROR(Exception):
	pass

# Failed to load player SDK.
class ExceptionNET_DVR_LOADPLAYERSDKFAILED(Exception):
	pass

# Can not find the function in player SDK.
class ExceptionNET_DVR_LOADPLAYERSDKPROC_ERROR(Exception):
	pass

# Failed to load the library file-"DsSdk".
class ExceptionNET_DVR_LOADDSSDKFAILED(Exception):
	pass

# Can not find the API in "DsSdk".
class ExceptionNET_DVR_LOADDSSDKPROC_ERROR(Exception):
	pass

# Failed to call the API in "DsSdk".
class ExceptionNET_DVR_DSSDK_ERROR(Exception):
	pass

# Sound adapter has been monopolized.
class ExceptionNET_DVR_VOICEMONOPOLIZE(Exception):
	pass

# Failed to join to multicast group.
class ExceptionNET_DVR_JOINMULTICASTFAILED(Exception):
	pass

# Failed to create log file directory.
class ExceptionNET_DVR_CREATEDIR_ERROR(Exception):
	pass

# Failed to bind socket.
class ExceptionNET_DVR_BINDSOCKET_ERROR(Exception):
	pass

# Socket disconnected. It is caused by network disconnection or destination unreachable.
class ExceptionNET_DVR_SOCKETCLOSE_ERROR(Exception):
	pass

# The user ID is operating when logout.
class ExceptionNET_DVR_USERID_ISUSING(Exception):
	pass

# Failed to listen
class ExceptionNET_DVR_SOCKETLISTEN_ERROR(Exception):
	pass

# Sdk program exception
class ExceptionNET_DVR_PROGRAM_EXCEPTION(Exception):
	pass

# Failed to write file, during local recording, saving picture or downloading record file.
class ExceptionNET_DVR_WRITEFILE_FAILED(Exception):
	pass

# Failed to format read-only HD
class ExceptionNET_DVR_FORMAT_READONLY(Exception):
	pass

# This user name already exists in the user configuration structure.
class ExceptionNET_DVR_WITHSAMEUSERNAME(Exception):
	pass

# Device type does not match when import configuration.
class ExceptionNET_DVR_DEVICETYPE_ERROR(Exception):
	pass

# Language does not match when import configuration.
class ExceptionNET_DVR_LANGUAGE_ERROR(Exception):
	pass

# Software version does not match when import configuration.
class ExceptionNET_DVR_PARAVERSION_ERROR(Exception):
	pass

# IP channel is not on-line when previewing.
class ExceptionNET_DVR_IPCHAN_NOTALIVE(Exception):
	pass

# Load StreamTransClient.dll failed
class ExceptionNET_DVR_RTSP_SDK_ERROR(Exception):
	pass

# Load SystemTransform.dll failed
class ExceptionNET_DVR_CONVERT_SDK_ERROR(Exception):
	pass

# over maximun ipc count
class ExceptionNET_DVR_IPC_COUNT_OVERFLOW(Exception):
	pass

# add label or other operation reach the maximum number
class ExceptionNET_DVR_MAX_ADD_NUM(Exception):
	pass

# Image intensifier, parameter mode error. This error may occur when client sets software or hardware parameters.
class ExceptionNET_DVR_PARAMMODE_ERROR(Exception):
	pass

# Code splitter is offline.
class ExceptionNET_DVR_CODESPITTER_OFFLINE(Exception):
	pass

# Device is backing up.
class ExceptionNET_DVR_BACKUP_COPYING(Exception):
	pass

# Channel not support
class ExceptionNET_DVR_CHAN_NOTSUPPORT(Exception):
	pass

# The height line location is too concentrated, or the length line is not inclined enough.
class ExceptionNET_DVR_CALLINEINVALID(Exception):
	pass

# Cancel calibration conflict, if the rule and overall actual size filter have been set.
class ExceptionNET_DVR_CALCANCELCONFLICT(Exception):
	pass

# Calibration point exceeds the range.
class ExceptionNET_DVR_CALPOINTOUTRANGE(Exception):
	pass

# The size filter does not meet the requirement.
class ExceptionNET_DVR_FILTERRECTINVALID(Exception):
	pass

# Device has not registered to DDNS.
class ExceptionNET_DVR_DDNS_DEVOFFLINE(Exception):
	pass

# DDNS inner error.
class ExceptionNET_DVR_DDNS_INTER_ERROR(Exception):
	pass

# This function don't support this OS.
class ExceptionNET_DVR_FUNCTION_NOT_SUPPORT_OS(Exception):
	pass

# Decode channel can not bind with two display channel.
class ExceptionNET_DVR_DEC_CHAN_REBIND(Exception):
	pass

# Failed to load the audio intercom SDK from current directory.
class ExceptionNET_DVR_INTERCOM_SDK_ERROR(Exception):
	pass

# No current upgrade pack.
class ExceptionNET_DVR_NO_CURRENT_UPDATEFILE(Exception):
	pass

# The user has not logined the device.
class ExceptionNET_DVR_USER_NOT_SUCC_LOGIN(Exception):
	pass

# It is using the log swtich file.
class ExceptionNET_DVR_USE_LOG_SWITCH_FILE(Exception):
	pass

# The ports used to bound in port pool is exhausted.
class ExceptionNET_DVR_POOL_PORT_EXHAUST(Exception):
	pass

# The packet type of stream is error.
class ExceptionNET_DVR_PACKET_TYPE_NOT_SUPPORT(Exception):
	pass

# IPID of IP access configuration is error.
class ExceptionNET_DVR_IPPARA_IPID_ERROR(Exception):
	pass

# Load Preview component Failed.
class ExceptionNET_DVR_LOAD_HCPREVIEW_SDK_ERROR(Exception):
	pass

# Load Voice talk component Failed.
class ExceptionNET_DVR_LOAD_HCVOICETALK_SDK_ERROR(Exception):
	pass

# Load Alarm component Failed.
class ExceptionNET_DVR_LOAD_HCALARM_SDK_ERROR(Exception):
	pass

# Load Playback component Failed.
class ExceptionNET_DVR_LOAD_HCPLAYBACK_SDK_ERROR(Exception):
	pass

# Load Display component Failed.
class ExceptionNET_DVR_LOAD_HCDISPLAY_SDK_ERROR(Exception):
	pass

# Load Industry component Failed.
class ExceptionNET_DVR_LOAD_HCINDUSTRY_SDK_ERROR(Exception):
	pass

# Load general configuration management component failed.
class ExceptionNET_DVR_LOAD_HCGENERALCFGMGR_SDK_ERROR(Exception):
	pass

# Load configuration core component failed.
class ExceptionNET_DVR_LOAD_HCCOREDEVCFG_SDK_ERROR(Exception):
	pass

# There is a mismatch between the component and core version.
class ExceptionNET_DVR_CORE_VER_MISMATCH(Exception):
	pass

# There is a mismatch between Live view component and core version.
class ExceptionNET_DVR_CORE_VER_MISMATCH_HCPREVIEW(Exception):
	pass

# There is a mismatch between voice component and core version.
class ExceptionNET_DVR_CORE_VER_MISMATCH_HCVOICETALK(Exception):
	pass

# There is a mismatch between alarm component and core version.
class ExceptionNET_DVR_CORE_VER_MISMATCH_HCALARM(Exception):
	pass

# There is a mismatch between playback component and core version.
class ExceptionNET_DVR_CORE_VER_MISMATCH_HCPLAYBACK(Exception):
	pass

# There is a mismatch between display component and core version.
class ExceptionNET_DVR_CORE_VER_MISMATCH_HCDISPLAY(Exception):
	pass

# There is a mismatch between industrial application component and core version.
class ExceptionNET_DVR_CORE_VER_MISMATCH_HCINDUSTRY(Exception):
	pass

# There is a mismatch between general configuration management component and the core version.
class ExceptionNET_DVR_CORE_VER_MISMATCH_HCGENERALCFGMGR(Exception):
	pass

# There is a mismatch between Live view component and HCNetSDK version.
class ExceptionNET_DVR_COM_VER_MISMATCH_HCPREVIEW(Exception):
	pass

# There is a mismatch between voice component and HCNetSDK version.
class ExceptionNET_DVR_COM_VER_MISMATCH_HCVOICETALK(Exception):
	pass

# here is a mismatch between alarm component and HCNetSDK version.
class ExceptionNET_DVR_COM_VER_MISMATCH_HCALARM(Exception):
	pass

# There is a mismatch between playback component and HCNetSDK version.
class ExceptionNET_DVR_COM_VER_MISMATCH_HCPLAYBACK(Exception):
	pass

# There is a mismatch between display component and HCNetSDK version.
class ExceptionNET_DVR_COM_VER_MISMATCH_HCDISPLAY(Exception):
	pass

# There is a mismatch between industrial application component and HCNetSDK version.
class ExceptionNET_DVR_COM_VER_MISMATCH_HCINDUSTRY(Exception):
	pass

# There is a mismatch between General configuration management component and the HCNetSDK version.
class ExceptionNET_DVR_COM_VER_MISMATCH_HCGENERALCFGMGR(Exception):
	pass

# Alias is duplicate (for HiDDNS)
class ExceptionNET_DVR_ALIAS_DUPLICATE(Exception):
	pass

# The user name doesn't exist.
class ExceptionNET_DVR_USERNAME_NOT_EXIST(Exception):
	pass

# The user name is locked.
class ExceptionNET_ERR_USERNAME_LOCKED(Exception):
	pass

# Invalid User ID.
class ExceptionNET_DVR_INVALID_USERID(Exception):
	pass

# The login version is too low.
class ExceptionNET_DVR_LOW_LOGIN_VERSION(Exception):
	pass

# Failed to load libeay32.dll.
class ExceptionNET_DVR_LOAD_LIBEAY32_DLL_ERROR(Exception):
	pass

# Failed to load ssleay32.dll.
class ExceptionNET_DVR_LOAD_SSLEAY32_DLL_ERROR(Exception):
	pass

# Failed to load libiconv.dll。
class ExceptionNET_ERR_LOAD_LIBICONV(Exception):
	pass

# Failed to connect to test server.
class ExceptionNET_DVR_TEST_SERVER_FAIL_CONNECT(Exception):
	pass

# Failed to mount to NAS server (No such directory, or user name/password error).
class ExceptionNET_DVR_NAS_SERVER_INVALID_DIR(Exception):
	pass

# Failed to mount to NAS server (not authorized)
class ExceptionNET_DVR_NAS_SERVER_NOENOUGH_PRI(Exception):
	pass

# DNS has not been configured, so domain address may invalid.
class ExceptionNET_DVR_EMAIL_SERVER_NOT_CONFIG_DNS(Exception):
	pass

# GateWay of Email server has not been configured, so it may be failed to send mail.
class ExceptionNET_DVR_EMAIL_SERVER_NOT_CONFIG_GATEWAY(Exception):
	pass

# User name and password tried to login the test server are not matching.
class ExceptionNET_DVR_TEST_SERVER_PASSWORD_ERROR(Exception):
	pass

# The connection between device and SMTP server is abnormal.
class ExceptionNET_DVR_EMAIL_SERVER_CONNECT_EXCEPTION_WITH_SMTP(Exception):
	pass

# Failed to create directory in the FTP server.
class ExceptionNET_DVR_FTP_SERVER_FAIL_CREATE_DIR(Exception):
	pass

# Do not have permission to write in the FTP server.
class ExceptionNET_DVR_FTP_SERVER_NO_WRITE_PIR(Exception):
	pass

# IP conflict.
class ExceptionNET_DVR_IP_CONFLICT(Exception):
	pass

# The storage pool is full.
class ExceptionNET_DVR_INSUFFICIENT_STORAGEPOOL_SPACE(Exception):
	pass

# The storage pool of cloud server is invalid, for not configure the storage pool or the ID of storage pool error.
class ExceptionNET_DVR_STORAGEPOOL_INVALID(Exception):
	pass

# Need reboot the device.
class ExceptionNET_DVR_EFFECTIVENESS_REBOOT(Exception):
	pass

# ANR arming is already established.
class ExceptionNET_ERR_ANR_ARMING_EXIST(Exception):
	pass

# Upload Link is already established.
class ExceptionNET_ERR_UPLOADLINK_EXIST(Exception):
	pass

# Incorrect file format.
class ExceptionNET_ERR_INCORRECT_FILE_FORMAT(Exception):
	pass

# Incorrect file content.
class ExceptionNET_ERR_INCORRECT_FILE_CONTENT(Exception):
	pass

# HRUDP limit the number of connections over equipment.
class ExceptionNET_ERR_MAX_HRUDP_LINK(Exception):
	pass

# Existing name.
class ExceptionNET_DVR_NAME_NOT_ONLY(Exception):
	pass

# Number of arrays has reached its limit.
class ExceptionNET_DVR_OVER_MAX_ARRAY(Exception):
	pass

# Number of virtual disks has reached its limit.
class ExceptionNET_DVR_OVER_MAX_VD(Exception):
	pass

# Virtual disk slot is full.
class ExceptionNET_DVR_VD_SLOT_EXCEED(Exception):
	pass

# Physical disk for rebuilding array is with error status.
class ExceptionNET_DVR_PD_STATUS_INVALID(Exception):
	pass

# Physical disk for rebuilding array is specified as spare drive.
class ExceptionNET_DVR_PD_BE_DEDICATE_SPARE(Exception):
	pass

# Physical disk for rebuilding array is not idle.
class ExceptionNET_DVR_PD_NOT_FREE(Exception):
	pass

# Unable to migrate from the current array type to the new array type.
class ExceptionNET_DVR_CANNOT_MIG2NEWMODE(Exception):
	pass

# The migration operation has been paused.
class ExceptionNET_DVR_MIG_PAUSE(Exception):
	pass

# The migration operation has been cancelled.
class ExceptionNET_DVR_MIG_CANCEL(Exception):
	pass

# Operation failed! Please delete the virtual disk existed in the array first.
class ExceptionNET_DVR_EXIST_VD(Exception):
	pass

# Target physical disk is part of the virtual disk and is functional.
class ExceptionNET_DVR_TARGET_IN_LD_FUNCTIONAL(Exception):
	pass

# Specified physical disk is assigned to a virtual disk
class ExceptionNET_DVR_HD_IS_ASSIGNED_ALREADY(Exception):
	pass

# Number of physical disks doesn't fit the specified RAID level.
class ExceptionNET_DVR_INVALID_HD_COUNT(Exception):
	pass

# Specified virtual disk is functional.
class ExceptionNET_DVR_LD_IS_FUNCTIONAL(Exception):
	pass

# BGA is running.
class ExceptionNET_DVR_BGA_RUNNING(Exception):
	pass

# Can not create virtual disk with ATAPI drive.
class ExceptionNET_DVR_LD_NO_ATAPI(Exception):
	pass

# Migration is not necessary.
class ExceptionNET_DVR_MIGRATION_NOT_NEED(Exception):
	pass

# Physical disks are not of the same type.
class ExceptionNET_DVR_HD_TYPE_MISMATCH(Exception):
	pass

# No virtual disk exist on the specified array.
class ExceptionNET_DVR_NO_LD_IN_DG(Exception):
	pass

# Disk space is too small to be assigned as spare drive.
class ExceptionNET_DVR_NO_ROOM_FOR_SPARE(Exception):
	pass

# Disk is already assigned as a spare drive for an array.
class ExceptionNET_DVR_SPARE_IS_IN_MULTI_DG(Exception):
	pass

# Disk is missing from an array.
class ExceptionNET_DVR_DG_HAS_MISSING_PD(Exception):
	pass

# Name is empty.
class ExceptionNET_DVR_NAME_EMPTY(Exception):
	pass

# The input parameter is error.
class ExceptionNET_DVR_INPUT_PARAM(Exception):
	pass

# The physical disk is not available.
class ExceptionNET_DVR_PD_NOT_AVAILABLE(Exception):
	pass

# The RAID is not available
class ExceptionNET_DVR_ARRAY_NOT_AVAILABLE(Exception):
	pass

# The count of physical disks is not correct.
class ExceptionNET_DVR_PD_COUNT(Exception):
	pass

# Virtual disk is too small.
class ExceptionNET_DVR_VD_SMALL(Exception):
	pass

# Not exist.
class ExceptionNET_DVR_NO_EXIST(Exception):
	pass

# Not support the operation.
class ExceptionNET_DVR_NOT_SUPPORT(Exception):
	pass

# The status of RAID is abnormal.
class ExceptionNET_DVR_NOT_FUNCTIONAL(Exception):
	pass

# The device node of virtual disk does not exist.
class ExceptionNET_DVR_DEV_NODE_NOT_FOUND(Exception):
	pass

# The count of slots reaches the upper limit.
class ExceptionNET_DVR_SLOT_EXCEED(Exception):
	pass

# There is not virtual disk in the RAID.
class ExceptionNET_DVR_NO_VD_IN_ARRAY(Exception):
	pass

# The slot of virtual disk is invalid.
class ExceptionNET_DVR_VD_SLOT_INVALID(Exception):
	pass

# The required space of physical disk is not enough.
class ExceptionNET_DVR_PD_NO_ENOUGH_SPACE(Exception):
	pass

# Only the RAID on normal state supports to be migrated.
class ExceptionNET_DVR_ARRAY_NONFUNCTION(Exception):
	pass

# The space of RAID is not enough.
class ExceptionNET_DVR_ARRAY_NO_ENOUGH_SPACE(Exception):
	pass

# It is pulling the disk out safely or rescanning the disk.
class ExceptionNET_DVR_STOPPING_SCANNING_ARRAY(Exception):
	pass

# Not support create the RAID larger than 16T.
class ExceptionNET_DVR_NOT_SUPPORT_16T(Exception):
	pass

# The device has not been activated.
class ExceptionNET_DVR_ERROR_DEVICE_NOT_ACTIVATED(Exception):
	pass

# There is a risk of the password.
class ExceptionNET_DVR_ERROR_RISK_PASSWORD(Exception):
	pass

# The device has been activated.
class ExceptionNET_DVR_ERROR_DEVICE_HAS_ACTIVATED(Exception):
	pass

# Configuration ID is illegal.
class ExceptionNET_DVR_ID_ERROR(Exception):
	pass

# Polygon does not match requirement.
class ExceptionNET_DVR_POLYGON_ERROR(Exception):
	pass

# Rule parameter is illegal.
class ExceptionNET_DVR_RULE_PARAM_ERROR(Exception):
	pass

# Configuration conflict.
class ExceptionNET_DVR_RULE_CFG_CONFLICT(Exception):
	pass

# Calibration not ready.
class ExceptionNET_DVR_CALIBRATE_NOT_READY(Exception):
	pass

# Camera parameter is illegal.
class ExceptionNET_DVR_CAMERA_DATA_ERROR(Exception):
	pass

# Not tilt enough, not fit to calibrate.
class ExceptionNET_DVR_CALIBRATE_DATA_UNFIT(Exception):
	pass

# Calibration error.
class ExceptionNET_DVR_CALIBRATE_DATA_CONFILICT(Exception):
	pass

# Failed to calculate camera calibration parameter.
class ExceptionNET_DVR_CALIBRATE_CALC_FAIL(Exception):
	pass

# The input calibrating line exceeds the external rectangle sample.
class ExceptionNET_DVR_CALIBRATE_LINE_OUT_RECT(Exception):
	pass

# Enter rule not ready.
class ExceptionNET_DVR_ENTER_RULE_NOT_READY(Exception):
	pass

# It does not include lane in the traffic event rule (especial for traffic jam or driving against the traffic).
class ExceptionNET_DVR_AID_RULE_NO_INCLUDE_LANE(Exception):
	pass

# Lane not ready.
class ExceptionNET_DVR_LANE_NOT_READY(Exception):
	pass

# There are two different directions in event rule.
class ExceptionNET_DVR_RULE_INCLUDE_TWO_WAY(Exception):
	pass

# The lane conflicts with the data rule.
class ExceptionNET_DVR_LANE_TPS_RULE_CONFLICT(Exception):
	pass

# The event type is not supported by the device.
class ExceptionNET_DVR_NOT_SUPPORT_EVENT_TYPE(Exception):
	pass

# The lane has no direction.
class ExceptionNET_DVR_LANE_NO_WAY(Exception):
	pass

# The size of filter is illegal.
class ExceptionNET_DVR_SIZE_FILTER_ERROR(Exception):
	pass

# There is no face when feature point positioning.
class ExceptionNET_DVR_LIB_FFL_NO_FACE(Exception):
	pass

# The input image is too small when feature point positioning.
class ExceptionNET_DVR_LIB_FFL_IMG_TOO_SMALL(Exception):
	pass

# The input image has no face when detecting face in single image.
class ExceptionNET_DVR_LIB_FD_IMG_NO_FACE(Exception):
	pass

# Face is too small when building model.
class ExceptionNET_DVR_LIB_FACE_TOO_SMALL(Exception):
	pass

# Face image is of poor quality when building model.
class ExceptionNET_DVR_LIB_FACE_QUALITY_TOO_BAD(Exception):
	pass

# Advanced parameter setting error.
class ExceptionNET_DVR_KEY_PARAM_ERR(Exception):
	pass

# Calibration sample size error, or data value error, or sample points beyond the horizon
class ExceptionNET_DVR_CALIBRATE_DATA_ERR(Exception):
	pass

# The configured rules do not allow to cancel calibration.
class ExceptionNET_DVR_CALIBRATE_DISABLE_FAIL(Exception):
	pass

# Filter scale is out range.
class ExceptionNET_DVR_VCA_LIB_FD_SCALE_OUTRANGE(Exception):
	pass

# Region is too big.
class ExceptionNET_DVR_LIB_FD_REGION_TOO_LARGE(Exception):
	pass

# Trial overdue.
class ExceptionNET_DVR_TRIAL_OVERDUE(Exception):
	pass

# Config file conflict.
class ExceptionNET_DVR_CONFIG_FILE_CONFLICT(Exception):
	pass

# Feature points location is error in face recognition.
class ExceptionNET_DVR_FR_FPL_FAIL(Exception):
	pass

# Image quality assessment is error in face recognition.
class ExceptionNET_DVR_FR_IQA_FAIL(Exception):
	pass

# Feature extract & match error in face recognition.
class ExceptionNET_DVR_FR_FEM_FAIL(Exception):
	pass

# Detection confidence is too low in feature points location.
class ExceptionNET_DVR_FPL_DT_CONF_TOO_LOW(Exception):
	pass

# Confidence is too low in feature points location.
class ExceptionNET_DVR_FPL_CONF_TOO_LOW(Exception):
	pass

# Size of model data error.
class ExceptionNET_DVR_E_DATA_SIZE(Exception):
	pass

# Model version is error.
class ExceptionNET_DVR_FR_MODEL_VERSION_ERR(Exception):
	pass

# Face detection error in face recognition.
class ExceptionNET_DVR_FR_FD_FAIL(Exception):
	pass

# Face attribute normalize error.
class ExceptionNET_DVR_FA_NORMALIZE_ERR(Exception):
	pass

# Pustream and softdog are mismatched.
class ExceptionNET_DVR_DOG_PUSTREAM_NOT_MATCH(Exception):
	pass

# Pustream device version is error.
class ExceptionNET_DVR_DEV_PUSTREAM_NOT_MATCH(Exception):
	pass

# The pustream has existence.
class ExceptionNET_DVR_PUSTREAM_ALREADY_EXISTS(Exception):
	pass

# Failed to connect face retrieval device.
class ExceptionNET_DVR_SEARCH_CONNECT_FAILED(Exception):
	pass

# Storage space is insufficient.
class ExceptionNET_DVR_INSUFFICIENT_DISK_SPACE(Exception):
	pass

# Failed to connect database.
class ExceptionNET_DVR_DATABASE_CONNECTION_FAILED(Exception):
	pass

# Username or password is error for database.
class ExceptionNET_DVR_DATABASE_ADM_PW_ERROR(Exception):
	pass

# Failed to decode image.
class ExceptionNET_DVR_DECODE_YUV(Exception):
	pass

# Image resolution is unreasonable.
class ExceptionNET_DVR_IMAGE_RESOLUTION_ERROR(Exception):
	pass

# Channel work mode error.
class ExceptionNET_DVR_CHAN_WORKMODE_ERROR(Exception):
	pass

# The scene is in use.
class ExceptionNET_ERROR_SCENE_USING(Exception):
	pass

# The terminal is busy, and the terminal is in one meeting.
class ExceptionNET_ERR_TERMINAL_BUSY(Exception):
	pass

# Network traffic is over device ability limit.
class ExceptionNET_DVR_DEV_NET_OVERFLOW(Exception):
	pass

# The video file is recording and can't be locked.
class ExceptionNET_DVR_STATUS_RECORDFILE_WRITING_NOT_LOCK(Exception):
	pass

# The hard disk capacity is too small and can not be formatted.
class ExceptionNET_DVR_STATUS_CANT_FORMAT_LITTLE_DISK(Exception):
	pass

# Unable to connect to the remote device.
class ExceptionNET_SDK_ERR_REMOTE_DISCONNEC(Exception):
	pass

# It does not support add spare device to a spare device.
class ExceptionNET_SDK_ERR_RD_ADD_RD(Exception):
	pass

# The backup disk is abnormal.
class ExceptionNET_SDK_ERR_BACKUP_DISK_EXCEPT(Exception):
	pass

# The count of spare devices has reached the maximum limit.
class ExceptionNET_SDK_ERR_RD_LIMIT(Exception):
	pass

# The spare device to be added is a working device.
class ExceptionNET_SDK_ERR_ADDED_RD_IS_WD(Exception):
	pass

# The adding order is wrong, such as, to add the working device to the spare device before adding the spare device to the working device.
class ExceptionNET_SDK_ERR_ADD_ORDER_WRONG(Exception):
	pass

# It does not support add working device to a working device.
class ExceptionNET_SDK_ERR_WD_ADD_WD(Exception):
	pass

# The CVR server is abnormal.
class ExceptionNET_SDK_ERR_WD_SERVICE_EXCETP(Exception):
	pass

# The spare device is abnormal.
class ExceptionNET_SDK_ERR_RD_SERVICE_EXCETP(Exception):
	pass

# The working device to be added is a spare device.
class ExceptionNET_SDK_ERR_ADDED_WD_IS_RD(Exception):
	pass

# The performance reaches the upper limit
class ExceptionNET_SDK_ERR_PERFORMANCE_LIMIT(Exception):
	pass

# The devcie to be added has existed.
class ExceptionNET_SDK_ERR_ADDED_DEVICE_EXIST(Exception):
	pass

# Inquest resuming.
class ExceptionNET_SDK_ERR_INQUEST_RESUMING(Exception):
	pass

# Record backuping.
class ExceptionNET_SDK_ERR_RECORD_BACKUPING(Exception):
	pass

# Disk playing.
class ExceptionNET_SDK_ERR_DISK_PLAYING(Exception):
	pass

# Inquest started.
class ExceptionNET_SDK_ERR_INQUEST_STARTED(Exception):
	pass

# Local operating.
class ExceptionNET_SDK_ERR_LOCAL_OPERATING(Exception):
	pass

# Inquest not start.
class ExceptionNET_SDK_ERR_INQUEST_NOT_START(Exception):
	pass

# Chan bind aduio error or no bind.
class ExceptionNET_SDK_ERR_CHAN_AUDIO_BIND(Exception):
	pass

# Not support to set cloud storage mode, for the device is in N+1 mode.
class ExceptionNET_DVR_N_PLUS_ONE_MODE(Exception):
	pass

# The cloud storage mode has been opened.
class ExceptionNET_DVR_CLOUD_STORAGE_OPENED(Exception):
	pass

# Fot the device has been taken over, the operation is not allowed.
class ExceptionNET_DVR_ERR_OPER_NOT_ALLOWED(Exception):
	pass

# Fot the device has been taken over, it requires to get the redirection information and then re-operate.
class ExceptionNET_DVR_ERR_NEED_RELOCATE(Exception):
	pass

# The IR output error.
class ExceptionNET_SDK_ERR_IR_PORT_ERROR(Exception):
	pass

# The command of IR output is not correct.
class ExceptionNET_SDK_ERR_IR_CMD_ERROR(Exception):
	pass

# The device is not inquestiong.
class ExceptionNET_SDK_ERR_NOT_INQUESTING(Exception):
	pass

# The device is not in paused status.
class ExceptionNET_SDK_ERR_INQUEST_NOT_PAUSED(Exception):
	pass

# Check the password mistake.
class ExceptionNET_DVR_CHECK_PASSWORD_MISTAKE_ERROR(Exception):
	pass

# Check the password do not NULL.
class ExceptionNET_DVR_CHECK_PASSWORD_NULL_ERROR(Exception):
	pass

# Unable to calibrate currently.
class ExceptionNET_DVR_UNABLE_CALIB_ERROR(Exception):
	pass

# Please finish the calibration first.
class ExceptionNET_DVR_PLEASE_CALIB_ERROR(Exception):
	pass

# No panorama image for PanoVu camera calibration in flash.
class ExceptionNET_DVR_ERR_PANORAMIC_CAL_EMPTY(Exception):
	pass

# Calibration failed. Please calibrate again.
class ExceptionNET_DVR_ERR_CALIB_FAIL_PLEASEAGAIN(Exception):
	pass

# Please set detection line again. The detection line should be within the red count area.
class ExceptionNET_DVR_ERR_DETECTION_LINE(Exception):
	pass

# Exceed face images error.
class ExceptionNET_DVR_EXCEED_FACE_IMAGES_ERROR(Exception):
	pass

# Analysis face picture error.
class ExceptionNET_DVR_ANALYSIS_FACE_IMAGES_ERROR(Exception):
	pass

# Alarm Input No. A<-1 is used to trigger vehicle capture.
class ExceptionNET_ERR_ALARM_INPUT_OCCUPIED(Exception):
	pass

# Face lib database error.
class ExceptionNET_DVR_FACELIB_DATABASE_ERROR(Exception):
	pass

# Face libary data error.
class ExceptionNET_DVR_FACELIB_DATA_ERROR(Exception):
	pass

# Face data ID error.
class ExceptionNET_DVR_FACE_DATA_ID_ERROR(Exception):
	pass

# Face libary ID error.
class ExceptionNET_DVR_FACELIB_ID_ERROR(Exception):
	pass

# Face exceed face libary error.
class ExceptionNET_DVR_EXCEED_FACE_LIBARY_ERROR(Exception):
	pass

# Picture analysis no target error.
class ExceptionNET_DVR_PIC_ANALYSIS_NO_TARGET_ERROR(Exception):
	pass

# Subpicture analysis modeling error.
class ExceptionNET_DVR_SUBPIC_ANALYSIS_MODELING_ERROR(Exception):
	pass

# Picture Analysis no resource error.
class ExceptionNET_DVR_PIC_ANALYSIS_NO_RESOURCE_ERROR(Exception):
	pass

# Analysis engines no resource error.
class ExceptionNET_DVR_ANALYSIS_ENGINES_NO_RESOURCE_ERROR(Exception):
	pass

# Analysis engines usage exceed error.
class ExceptionNET_DVR_ANALYSIS_ENGINES_USAGE_EXCEED_ERROR(Exception):
	pass

# Exceed human misinfo filter enabled max channel number error.
class ExceptionNET_DVR_EXCEED_HUMANMISINFO_FILTER_ENABLED_ERROR(Exception):
	pass

# Name error.
class ExceptionNET_DVR_NAME_ERROR(Exception):
	pass

# Name exist error.
class ExceptionNET_DVR_NAME_EXIST_ERROR(Exception):
	pass

# Face lib picture importing error.
class ExceptionNET_DVR_FACELIB_PIC_IMPORTING_ERROR(Exception):
	pass

# Picture format error.
class ExceptionNET_DVR_PIC_FORMAT_ERROR(Exception):
	pass

# Picture resolution invalid error.
class ExceptionNET_DVR_PIC_RESOLUTION_INVALID_ERROR(Exception):
	pass

# Picture size exceed.
class ExceptionNET_DVR_PIC_SIZE_EXCEED_ERROR(Exception):
	pass

# Picture target num exceed.
class ExceptionNET_DVR_PIC_ANALYSIS_TARGRT_NUM_EXCEED_ERROR(Exception):
	pass

# Engine loading error.
class ExceptionNET_DVR_ANALYSIS_ENGINES_LOADING_ERROR(Exception):
	pass

# Engine abnorma.
class ExceptionNET_DVR_ANALYSIS_ENGINES_ABNORMA_ERROR(Exception):
	pass

# Analysis engine is import face library.
class ExceptionNET_DVR_ANALYSIS_ENGINES_FACELIB_IMPORTING(Exception):
	pass

# No data for modeling error.
class ExceptionNET_DVR_NO_DATA_FOR_MODELING_ERROR(Exception):
	pass

# face data modeling error.
class ExceptionNET_DVR_FACE_DATA_MODELING_ERROR(Exception):
	pass

# face lib data over limit.
class ExceptionNET_ERR_FACELIBDATA_OVERLIMIT(Exception):
	pass

# Analysis engine has been associated channel.
class ExceptionNET_DVR_ANALYSIS_ENGINES_ASSOCIATED_CHANNEL(Exception):
	pass

# CustomID length error.
class ExceptionNET_DVR_ERR_CUSTOMID_LEN(Exception):
	pass

# CustomFaceLibID repeat.
class ExceptionNET_DVR_ERR_CUSTOMFACELIBID_REPEAT(Exception):
	pass

# CustomHumanID Repeat.
class ExceptionNET_DVR_ERR_CUSTOMHUMANID_REPEAT(Exception):
	pass

# URL download fail.
class ExceptionNET_DVR_ERR_URL_DOWNLOAD_FAIL(Exception):
	pass

# URL not start download.
class ExceptionNET_DVR_ERR_URL_DOWNLOAD_NOTSTART(Exception):
	pass

# Config file secret key error.
class ExceptionNET_DVR_CFG_FILE_SECRETKEY_ERROR(Exception):
	pass

# Window channel index error.
class ExceptionNET_ERR_WINCHAN_IDX(Exception):
	pass

# Window layer number error(the count of window layers on a single screen exceeds the max number).
class ExceptionNET_ERR_WIN_LAYER(Exception):
	pass

# Window block number error(the count of screens that single window overlays exceeds the max number).
class ExceptionNET_ERR_WIN_BLK_NUM(Exception):
	pass

# The output resolution error.
class ExceptionNET_ERR_OUTPUT_RESOLUTION(Exception):
	pass

# Layout index error.
class ExceptionNET_ERR_LAYOUT(Exception):
	pass

# The input resolution is not supported.
class ExceptionNET_ERR_INPUT_RESOLUTION(Exception):
	pass

# The sub-device is off-line.
class ExceptionNET_ERR_SUBDEVICE_OFFLINE(Exception):
	pass

# There is no free decoding channel.
class ExceptionNET_ERR_NO_DECODE_CHAN(Exception):
	pass

# The upper limit of window number.
class ExceptionNET_ERR_MAX_WINDOW_ABILITY(Exception):
	pass

# Calling order error.
class ExceptionNET_ERR_ORDER_ERROR(Exception):
	pass

# Be playing plan.
class ExceptionNET_ERR_PLAYING_PLAN(Exception):
	pass

# Decoder board is in use.
class ExceptionNET_ERR_DECODER_USED(Exception):
	pass

# The data of output board is over the limit.
class ExceptionNET_ERR_OUTPUT_BOARD_DATA_OVERFLOW(Exception):
	pass

# The user name is duplicate.
class ExceptionNET_ERR_SAME_USER_NAME(Exception):
	pass

# Invalid username.
class ExceptionNET_ERR_INVALID_USER_NAME(Exception):
	pass

# The input matrix is in use.
class ExceptionNET_ERR_MATRIX_USING(Exception):
	pass

# The channel type is error (the output channel of matrix is different with the input of controller)
class ExceptionNET_ERR_DIFFERENT_CHAN_TYPE(Exception):
	pass

# The input channel has been bound by other matrix.
class ExceptionNET_ERR_INPUT_CHAN_BINDED(Exception):
	pass

# The number of the matrix output channels in use has exceeded the number of channels bound with controller.
class ExceptionNET_ERR_BINDED_OUTPUT_CHAN_OVERFLOW(Exception):
	pass

# The number of input signal sources is over the limit.
class ExceptionNET_ERR_MAX_SIGNAL_NUM(Exception):
	pass

# The input channel is in use.
class ExceptionNET_ERR_INPUT_CHAN_USING(Exception):
	pass

# The operation failed, for the manager has logged in.
class ExceptionNET_ERR_MANAGER_LOGON(Exception):
	pass

# The operation failed, for the user has logged in.
class ExceptionNET_ERR_USERALREADY_LOGON(Exception):
	pass

# The operation failed, for the layout is being initialized.
class ExceptionNET_ERR_LAYOUT_INIT(Exception):
	pass

# The size of traced drawing not match
class ExceptionNET_ERR_BASEMAP_SIZE_NOT_MATCH(Exception):
	pass

# The operation failed, for the window is performing other operation.
class ExceptionNET_ERR_WINDOW_OPERATING(Exception):
	pass

# The number of windows has reached the maximum limit.
class ExceptionNET_ERR_SIGNAL_UPLIMIT(Exception):
	pass

# The window size exceeds the limit.
class ExceptionNET_ERR_WINDOW_SIZE_OVERLIMIT(Exception):
	pass

# The number of windows overlap has reached the maximum limit.
class ExceptionNET_ERR_MAX_WIN_OVERLAP(Exception):
	pass

# stream ID and channel number are both valid.
class ExceptionNET_ERR_STREAMID_CHAN_BOTH_VALID(Exception):
	pass

# The device has no zero channel.
class ExceptionNET_ERR_NO_ZERO_CHAN(Exception):
	pass

# Need redirection (for transcoding system)
class ExceptionNEED_RECONNECT(Exception):
	pass

# The stream ID does not exist.
class ExceptionNET_ERR_NO_STREAM_ID(Exception):
	pass

# The transcoding has not been started.
class ExceptionNET_DVR_TRANS_NOT_START(Exception):
	pass

# The number of stream ID has reached the maximum limit.
class ExceptionNET_ERR_MAXNUM_STREAM_ID(Exception):
	pass

# The work mode does not match with the requirement.
class ExceptionNET_ERR_WORKMODE_MISMATCH(Exception):
	pass

# It Has been working in current mode.
class ExceptionNET_ERR_MODE_IS_USING(Exception):
	pass

# The device is in processing
class ExceptionNET_ERR_DEV_PROGRESSING(Exception):
	pass

# It is in transcoding.
class ExceptionNET_ERR_PASSIVE_TRANSCODING(Exception):
	pass

# Wrong window position.
class ExceptionNET_DVR_ERR_WINDOW_SIZE_PLACE(Exception):
	pass

# Screen distance exceeds the limit.
class ExceptionNET_DVR_ERR_RGIONAL_RESTRICTIONS(Exception):
	pass

# Operation failed. Close the window first.
class ExceptionNET_DVR_ERR_CLOSE_WINDOWS(Exception):
	pass

# Beyond the cycle decoding capacity.
class ExceptionNET_DVR_ERR_MATRIX_LOOP_ABILITY(Exception):
	pass

# Invalid cycle decoding time.
class ExceptionNET_DVR_ERR_MATRIX_LOOP_TIME(Exception):
	pass

# No more linked camera can be added.
class ExceptionNET_DVR_ERR_LINKED_OUT_ABILITY(Exception):
	pass

# Not support to get this node of the capability set.
class ExceptionXML_ABILITY_NOTSUPPORT(Exception):
	pass

# The output buffer is not enough
class ExceptionXML_ANALYZE_NOENOUGH_BUF(Exception):
	pass

# Can not find the corresponding xml file.
class ExceptionXML_ANALYZE_FIND_LOCALXML_ERROR(Exception):
	pass

# Failed to load the local xml file.
class ExceptionXML_ANALYZE_LOAD_LOCALXML_ERROR(Exception):
	pass

# Data format of the capability is wrong.
class ExceptionXML_NANLYZE_DVR_DATA_FORMAT_ERROR(Exception):
	pass

# The type of capability set is wrong.
class ExceptionXML_ANALYZE_TYPE_ERROR(Exception):
	pass

# Format of XML capability node is wrong.
class ExceptionXML_ANALYZE_XML_NODE_ERROR(Exception):
	pass

# The input value of XML capability node is wrong.
class ExceptionXML_INPUT_PARAM_ERROR(Exception):
	pass

# XML version not match
class ExceptionXML_VERSION_MISMATCH(Exception):
	pass

# The operation is failed, for transparent channel has been opened.
class ExceptionNET_ERR_TRANS_CHAN_START(Exception):
	pass

# The device is upgrading.
class ExceptionNET_ERR_DEV_UPGRADING(Exception):
	pass

# The type of upgrade package not match.
class ExceptionNET_ERR_MISMATCH_UPGRADE_PACK_TYPE(Exception):
	pass

# The device is being formatted.
class ExceptionNET_ERR_DEV_FORMATTING(Exception):
	pass

# The version of upgrade package not match.
class ExceptionNET_ERR_MISMATCH_UPGRADE_PACK_VERSION(Exception):
	pass

# The device PT has been locked.
class ExceptionNET_ERR_PT_LOCKED(Exception):
	pass

# Verification Code illegal.
class ExceptionNET_DVR_ERR_ILLEGAL_VERIFICATION_CODE(Exception):
	pass

# Verification Code missing.
class ExceptionNET_DVR_ERR_LACK_VERIFICATION_CODE(Exception):
	pass

# This IP address has been banned, do not allow the configuration.
class ExceptionNET_DVR_ERR_FORBIDDEN_IP(Exception):
	pass

# The device is searching for the external module.
class ExceptionNET_ERR_SEARCHING_MODULE(Exception):
	pass

# The device is registering to the external module.
class ExceptionNET_ERR_REGISTERING_MODULE(Exception):
	pass

# The device is getting defense zone parameters.
class ExceptionNET_ERR_GETTING_ZONES(Exception):
	pass

# The device is getting triggers.
class ExceptionNET_ERR_GETTING_TRIGGERS(Exception):
	pass

# The system is armed.
class ExceptionNET_ERR_ARMED_STATUS(Exception):
	pass

# The system is in programming mode.
class ExceptionNET_ERR_PROGRAM_MODE_STATUS(Exception):
	pass

# The system is in pacing mode.
class ExceptionNET_ERR_WALK_TEST_MODE_STATUS(Exception):
	pass

# Bypass state
class ExceptionNET_ERR_BYPASS_STATUS(Exception):
	pass

# The function is disabled.
class ExceptionNET_ERR_DISABLED_MODULE_STATUS(Exception):
	pass

# The defense zone does not support the operation.
class ExceptionNET_ERR_NOT_SUPPORT_OPERATE_ZONE(Exception):
	pass

# The module address can not be modified.
class ExceptionNET_ERR_NOT_SUPPORT_MOD_MODULE_ADDR(Exception):
	pass

# The module is unregistered.
class ExceptionNET_ERR_UNREGISTERED_MODULE(Exception):
	pass

# The public subsystem is set to associate with itself.
class ExceptionNET_ERR_PUBLIC_SUBSYSTEM_ASSOCIATE_SELF(Exception):
	pass

# The number of subsystems associated with the public subsystem exceeds the max limit.
class ExceptionNET_ERR_EXCEEDS_ASSOCIATE_SUBSYSTEM_NUM(Exception):
	pass

# The subsystem has been associated with the other public subsystem.
class ExceptionNET_ERR_BE_ASSOCIATED_BY_PUBLIC_SUBSYSTEM(Exception):
	pass

# The defense zone is in the fault state.
class ExceptionNET_ERR_ZONE_FAULT_STATUS(Exception):
	pass

# The opening and close of alarm output triggered by event have associated with same event type.
class ExceptionNET_ERR_SAME_EVENT_TYPE(Exception):
	pass

# The defense zone is in the alarm state.
class ExceptionNET_ERR_ZONE_ALARM_STATUS(Exception):
	pass

# Short circuit of expansion bus.
class ExceptionNET_ERR_EXPANSION_BUS_SHORT_CIRCUIT(Exception):
	pass

# Password conflict.
class ExceptionNET_ERR_PWD_CONFLICT(Exception):
	pass

# Detector gistered by other zone.
class ExceptionNET_ERR_DETECTOR_GISTERED_BY_OTHER_ZONE(Exception):
	pass

# Detector gistered by other PU.
class ExceptionNET_ERR_DETECTOR_GISTERED_BY_OTHER_PU(Exception):
	pass

# Detector disconnect.
class ExceptionNET_ERR_DETECTOR_DISCONNECT(Exception):
	pass

# Call busy.
class ExceptionNET_ERR_CALL_BUSY(Exception):
	pass

# File name error, null or illegal.
class ExceptionNET_ERR_FILE_NAME(Exception):
	pass

# Broadcast busy.
class ExceptionNET_ERR_BROADCAST_BUSY(Exception):
	pass

# The number of lanes exceeds the limit.
class ExceptionNET_DVR_ERR_LANENUM_EXCEED(Exception):
	pass

# License plate recognition region is too large.
class ExceptionNET_DVR_ERR_PRAREA_EXCEED(Exception):
	pass

# The access parameters of traffic light is error.
class ExceptionNET_DVR_ERR_LIGHT_PARAM(Exception):
	pass

# The configuration of lane line is invalid.
class ExceptionNET_DVR_ERR_LANE_LINE_INVALID(Exception):
	pass

# The configuration of stop line is invalid.
class ExceptionNET_DVR_ERR_STOP_LINE_INVALID(Exception):
	pass

# The boundary line configuration of left-turn or right-turn lane is invalid.
class ExceptionNET_DVR_ERR_LEFTORRIGHT_LINE_INVALID(Exception):
	pass

# The overlaid lane number is repeated.
class ExceptionNET_DVR_ERR_LANE_NO_REPEAT(Exception):
	pass

# The polygon region of license plate recognition does not meet the requirement.
class ExceptionNET_DVR_ERR_PRAREA_INVALID(Exception):
	pass

# The number of traffic lights of the video detection exceeds the max limit.
class ExceptionNET_DVR_ERR_LIGHT_NUM_EXCEED(Exception):
	pass

# The number of the sub traffic lights of video detection is illegal.
class ExceptionNET_DVR_ERR_SUBLIGHT_NUM_INVALID(Exception):
	pass

# The input area size of the video detection traffic light is illegal.
class ExceptionNET_DVR_ERR_LIGHT_AREASIZE_INVALID(Exception):
	pass

# The color of the video detection traffic light is illegal.
class ExceptionNET_DVR_ERR_LIGHT_COLOR_INVALID(Exception):
	pass

# The direction of the video detection traffic light is illegal.
class ExceptionNET_DVR_ERR_LIGHT_DIRECTION_INVALID(Exception):
	pass

# Lack of IO ablity.
class ExceptionNET_DVR_ERR_LACK_IOABLITY(Exception):
	pass

# FTP port error.
class ExceptionNET_DVR_ERR_FTP_PORT(Exception):
	pass

# FTP catalogue error.
class ExceptionNET_DVR_ERR_FTP_CATALOGUE(Exception):
	pass

# FTP upload type error.
class ExceptionNET_DVR_ERR_FTP_UPLOAD_TYPE(Exception):
	pass

# Setting param flash write error.
class ExceptionNET_DVR_ERR_FLASH_PARAM_WRITE(Exception):
	pass

# Getting param flash read error.
class ExceptionNET_DVR_ERR_FLASH_PARAM_READ(Exception):
	pass

# Pic name delimiter error.
class ExceptionNET_DVR_ERR_PICNAME_DELIMITER(Exception):
	pass

# Pic name item error.
class ExceptionNET_DVR_ERR_PICNAME_ITEM(Exception):
	pass

# Plate recognize type error.
class ExceptionNET_DVR_ERR_PLATE_RECOGNIZE_TYPE(Exception):
	pass

# Capture times error.
class ExceptionNET_DVR_ERR_CAPTURE_TIMES(Exception):
	pass

# Loop distance error.
class ExceptionNET_DVR_ERR_LOOP_DISTANCE(Exception):
	pass

# Loop input status error.
class ExceptionNET_DVR_ERR_LOOP_INPUT_STATUS(Exception):
	pass

# Related IO conflict.
class ExceptionNET_DVR_ERR_RELATE_IO_CONFLICT(Exception):
	pass

# Interval time error.
class ExceptionNET_DVR_ERR_INTERVAL_TIME(Exception):
	pass

# Sign speed error.
class ExceptionNET_DVR_ERR_SIGN_SPEED(Exception):
	pass

# Flip is used.
class ExceptionNET_DVR_ERR_PIC_FLIP(Exception):
	pass

# Related lane number error.
class ExceptionNET_DVR_ERR_RELATE_LANE_NUMBER(Exception):
	pass

# Trigger mode error.
class ExceptionNET_DVR_ERR_TRIGGER_MODE(Exception):
	pass

# Delay time error.
class ExceptionNET_DVR_ERR_DELAY_TIME(Exception):
	pass

# Exceed RS485 count.
class ExceptionNET_DVR_ERR_EXCEED_RS485_COUNT(Exception):
	pass

# Radar type error.
class ExceptionNET_DVR_ERR_RADAR_TYPE(Exception):
	pass

# Radar angle error.
class ExceptionNET_DVR_ERR_RADAR_ANGLE(Exception):
	pass

# Radar speed valid time error.
class ExceptionNET_DVR_ERR_RADAR_SPEED_VALID_TIME(Exception):
	pass

# Radar line correct error.
class ExceptionNET_DVR_ERR_RADAR_LINE_CORRECT(Exception):
	pass

# Radar const correct error.
class ExceptionNET_DVR_ERR_RADAR_CONST_CORRECT(Exception):
	pass

# Record param error.
class ExceptionNET_DVR_ERR_RECORD_PARAM(Exception):
	pass

# Light number and other param error.
class ExceptionNET_DVR_ERR_LIGHT_WITHOUT_COLOR_AND_DIRECTION(Exception):
	pass

# Light number and detection region error.
class ExceptionNET_DVR_ERR_LIGHT_WITHOUT_DETECTION_REGION(Exception):
	pass

# Plate recognize Province param error.
class ExceptionNET_DVR_ERR_RECOGNIZE_PROVINCE_PARAM(Exception):
	pass

# IO Speed TimeOut Param error.
class ExceptionNET_DVR_ERR_SPEED_TIMEOUT(Exception):
	pass

# NTP TimeZone Param error.
class ExceptionNET_DVR_ERR_NTP_TIMEZONE(Exception):
	pass

# NTP Interval Time error.
class ExceptionNET_DVR_ERR_NTP_INTERVAL_TIME(Exception):
	pass

# Network Card Num error.
class ExceptionNET_DVR_ERR_NETWORK_CARD_NUM(Exception):
	pass

# Default Route error.
class ExceptionNET_DVR_ERR_DEFAULT_ROUTE(Exception):
	pass

# Banding Work Mode error.
class ExceptionNET_DVR_ERR_BONDING_WORK_MODE(Exception):
	pass

# Slave Card error.
class ExceptionNET_DVR_ERR_SLAVE_CARD(Exception):
	pass

# Primary Card error.
class ExceptionNET_DVR_ERR_PRIMARY_CARD(Exception):
	pass

# DHCP and PPOE not Meanwhile start.
class ExceptionNET_DVR_ERR_DHCP_PPOE_WORK(Exception):
	pass

# Net Interface invalid.
class ExceptionNET_DVR_ERR_NET_INTERFACE(Exception):
	pass

# MTU Param invalid.
class ExceptionNET_DVR_ERR_MTU(Exception):
	pass

# Netmask address invalid.
class ExceptionNET_DVR_ERR_NETMASK(Exception):
	pass

# IP address invalid.
class ExceptionNET_DVR_ERR_IP_INVALID(Exception):
	pass

# Multicast IP address invalid.
class ExceptionNET_DVR_ERR_MULTICAST_IP_INVALID(Exception):
	pass

# Gateway address invalid.
class ExceptionNET_DVR_ERR_GATEWAY_INVALID(Exception):
	pass

# DNS Param invalid.
class ExceptionNET_DVR_ERR_DNS_INVALID(Exception):
	pass

# AlarmHost IP invalid.
class ExceptionNET_DVR_ERR_ALARMHOST_IP_INVALID(Exception):
	pass

# IP address Conflict.
class ExceptionNET_DVR_ERR_IP_CONFLICT(Exception):
	pass

# IP not support Multi Network segment.
class ExceptionNET_DVR_ERR_NETWORK_SEGMENT(Exception):
	pass

# NetPort param error.
class ExceptionNET_DVR_ERR_NETPORT(Exception):
	pass

# Unsupport PPPOE.
class ExceptionNET_DVR_ERR_PPPOE_NOSUPPORT(Exception):
	pass

# Not Support Domain Name.
class ExceptionNET_DVR_ERR_DOMAINNAME_NOSUPPORT(Exception):
	pass

# Speed Not Enabled.
class ExceptionNET_DVR_ERR_NO_SPEED(Exception):
	pass

# IO Status invalid.
class ExceptionNET_DVR_ERR_IOSTATUS_INVALID(Exception):
	pass

# Burst Interval invalid.
class ExceptionNET_DVR_ERR_BURST_INTERVAL_INVALID(Exception):
	pass

# Reserve Mode invalid.
class ExceptionNET_DVR_ERR_RESERVE_MODE(Exception):
	pass

# Lane No error.
class ExceptionNET_DVR_ERR_LANE_NO(Exception):
	pass

# Coil Area Type error.
class ExceptionNET_DVR_ERR_COIL_AREA_TYPE(Exception):
	pass

# Trigger Area Param error.
class ExceptionNET_DVR_ERR_TRIGGER_AREA_PARAM(Exception):
	pass

# Speed Limit Param error.
class ExceptionNET_DVR_ERR_SPEED_LIMIT_PARAM(Exception):
	pass

# Lane Protocol Type error.
class ExceptionNET_DVR_ERR_LANE_PROTOCOL_TYPE(Exception):
	pass

# Capture Interval Type error.
class ExceptionNET_DVR_ERR_INTERVAL_TYPE(Exception):
	pass

# Capture Interval Distance error.
class ExceptionNET_DVR_ERR_INTERVAL_DISTANCE(Exception):
	pass

# Rs485 Associate DevType error.
class ExceptionNET_DVR_ERR_RS485_ASSOCIATE_DEVTYPE(Exception):
	pass

# Rs485 Associate LaneNo error.
class ExceptionNET_DVR_ERR_RS485_ASSOCIATE_LANENO(Exception):
	pass

# LaneNo Associate MulitRs485 error.
class ExceptionNET_DVR_ERR_LANENO_ASSOCIATE_MULTIRS485(Exception):
	pass

# Light Detection Region error.
class ExceptionNET_DVR_ERR_LIGHT_DETECTION_REGION(Exception):
	pass

# UnSupport Capture Frame 2D Noise Reduction.
class ExceptionNET_DVR_ERR_DN2D_NOSUPPORT(Exception):
	pass

# UnSupport scene Mode.
class ExceptionNET_DVR_ERR_IRISMODE_NOSUPPORT(Exception):
	pass

# UnSupport White Balance Mode.
class ExceptionNET_DVR_ERR_WB_NOSUPPORT(Exception):
	pass

# IO Effectiveness invalid.
class ExceptionNET_DVR_ERR_IO_EFFECTIVENESS(Exception):
	pass

# Access Detector Lights Red / Yellow Overrun.
class ExceptionNET_DVR_ERR_LIGHTNO_MAX(Exception):
	pass

# Access Detector Lights Red / Yellow Conflict.
class ExceptionNET_DVR_ERR_LIGHTNO_CONFLICT(Exception):
	pass

# Trigger straight line error.
class ExceptionNET_DVR_ERR_CANCEL_LINE(Exception):
	pass

# Subject line area stop line error.
class ExceptionNET_DVR_ERR_STOP_LINE(Exception):
	pass

# Red light trigger lines error.
class ExceptionNET_DVR_ERR_RUSH_REDLIGHT_LINE(Exception):
	pass

# IO out port error.
class ExceptionNET_DVR_ERR_IOOUTNO_MAX(Exception):
	pass

# IO out ahead time error.
class ExceptionNET_DVR_ERR_IOOUTNO_AHEADTIME_MAX(Exception):
	pass

# IO out inwork time error.
class ExceptionNET_DVR_ERR_IOOUTNO_IOWORKTIME(Exception):
	pass

# IO out frequency multiplication error.
class ExceptionNET_DVR_ERR_IOOUTNO_FREQMULTI(Exception):
	pass

# IO out duty rate error.
class ExceptionNET_DVR_ERR_IOOUTNO_DUTYRATE(Exception):
	pass

# IO out work mode error.
class ExceptionNET_DVR_ERR_VIDEO_WITH_EXPOSURE(Exception):
	pass

# Plate enable in plate compensate mode on.
class ExceptionNET_DVR_ERR_PLATE_BRIGHTNESS_WITHOUT_FLASHDET(Exception):
	pass

# Recognize Type error.
class ExceptionNET_DVR_ERR_RECOGNIZE_TYPE_PARAM(Exception):
	pass

# Plate Recognize Area Param error.
class ExceptionNET_DVR_ERR_PALTE_RECOGNIZE_AREA_PARAM(Exception):
	pass

# Port Conflict.
class ExceptionNET_DVR_ERR_PORT_CONFLICT(Exception):
	pass

# IP cannot be the loopback address.
class ExceptionNET_DVR_ERR_LOOP_IP(Exception):
	pass

# Driveline sensitivity error.
class ExceptionNET_DVR_ERR_DRIVELINE_SENSITIVE(Exception):
	pass

# The time period conflict.
class ExceptionNET_ERR_VQD_TIME_CONFLICT(Exception):
	pass

# The diagnostic plan of VQD dese not exist.
class ExceptionNET_ERR_VQD_PLAN_NO_EXIST(Exception):
	pass

# The channel dese not exist.
class ExceptionNET_ERR_VQD_CHAN_NO_EXIST(Exception):
	pass

# The total number of VQD plans exceeds the max limit.
class ExceptionNET_ERR_VQD_CHAN_MAX(Exception):
	pass

# The total number of VQD tasks exceeds the max limit.
class ExceptionNET_ERR_VQD_TASK_MAX(Exception):
	pass

class ExceptionNET_DVR_ERR_EXCEED_MAX_CAPTURE_TIMES(Exception):
	pass

# Radar type conflict.
class ExceptionNET_DVR_ERR_REDAR_TYPE_CONFLICT(Exception):
	pass

# The license plate is null.
class ExceptionNET_DVR_ERR_LICENSE_PLATE_NULL(Exception):
	pass

# Failed to write data into the database.
class ExceptionNET_DVR_ERR_WRITE_DATABASE(Exception):
	pass

# The effective time of licence plate error.
class ExceptionNET_DVR_ERR_LICENSE_EFFECTIVE_TIME(Exception):
	pass

# The pre recorded start time is greater than the number of illegal capture.
class ExceptionNET_DVR_ERR_PRERECORDED_STARTTIME_LONG(Exception):
	pass

# Trigger rule line error.
class ExceptionNET_DVR_ERR_TRIGGER_RULE_LINE(Exception):
	pass

# Left and right trigger line is not vertical.
class ExceptionNET_DVR_ERR_LEFTRIGHT_TRIGGERLINE_NOTVERTICAL(Exception):
	pass

# Flash lamp mode error.
class ExceptionNET_DVR_ERR_FLASH_LAMP_MODE(Exception):
	pass

# Illegal capture number error.
class ExceptionNET_DVR_ERR_ILLEGAL_SNAPSHOT_NUM(Exception):
	pass

# Illegal detection type error.
class ExceptionNET_DVR_ERR_ILLEGAL_DETECTION_TYPE(Exception):
	pass

# Positive back to trigger line height error.
class ExceptionNET_DVR_ERR_POSITIVEBACK_TRIGGERLINE_HIGH(Exception):
	pass

# Mixed mode only supports capture type all targets.
class ExceptionNET_DVR_ERR_MIXEDMODE_CAPTYPE_ALLTARGETS(Exception):
	pass

# Car sign speed greater than speed limit value.
class ExceptionNET_DVR_ERR_CARSIGNSPEED_GREATERTHAN_LIMITSPEED(Exception):
	pass

# Big car sign speed limit greater than speed limit value.
class ExceptionNET_DVR_ERR_BIGCARSIGNSPEED_GREATERTHAN_LIMITSPEED(Exception):
	pass

# Big car sign speed limit is greater than the car sign speed limit value.
class ExceptionNET_DVR_ERR_BIGCARSIGNSPEED_GREATERTHAN_CARSIGNSPEED(Exception):
	pass

# Big car speed limit value is greater than the car speed limit value.
class ExceptionNET_DVR_ERR_BIGCARLIMITSPEED_GREATERTHAN_CARLIMITSPEED(Exception):
	pass

# Big car low speed limit value is greater than the car low speed limit value.
class ExceptionNET_DVR_ERR_BIGCARLOWSPEEDLIMIT_GREATERTHAN_CARLOWSPEEDLIMIT(Exception):
	pass

# Car speed limit greater than exception high speed value.
class ExceptionNET_DVR_ERR_CARLIMITSPEED_GREATERTHAN_EXCEPHIGHSPEED(Exception):
	pass

# Big car speed limit greater than exception high speed value.
class ExceptionNET_DVR_ERR_BIGCARLIMITSPEED_GREATERTHAN_EXCEPHIGHSPEED(Exception):
	pass

# Stopping more than straight lines trigger lines.
class ExceptionNET_DVR_ERR_STOPLINE_MORETHAN_TRIGGERLINE(Exception):
	pass

# The time period is overlapped.
class ExceptionNET_ERR_TIME_OVERLAP(Exception):
	pass

# The holiday plan is overlapped.
class ExceptionNET_ERR_HOLIDAY_PLAN_OVERLAP(Exception):
	pass

# The card number is not sorted.
class ExceptionNET_ERR_CARDNO_NOT_SORT(Exception):
	pass

# The card number is not existed.
class ExceptionNET_ERR_CARDNO_NOT_EXIST(Exception):
	pass

# The card number is false.
class ExceptionNET_ERR_ILLEGAL_CARDNO(Exception):
	pass

# The zone is armed(the modification of parameters is not allowed)
class ExceptionNET_ERR_ZONE_ALARM(Exception):
	pass

# The zone does not support the operation.
class ExceptionNET_ERR_ZONE_OPERATION_NOT_SUPPORT(Exception):
	pass

# Both the multi-door interlocking and anti-sneak configuration are false.
class ExceptionNET_ERR_INTERLOCK_ANTI_CONFLICT(Exception):
	pass

# The card is full(return when up to 10W).
class ExceptionNET_ERR_DEVICE_CARD_FULL(Exception):
	pass

# Holiday group download error.
class ExceptionNET_ERR_HOLIDAY_GROUP_DOWNLOAD(Exception):
	pass

# Local control off.
class ExceptionNET_ERR_LOCAL_CONTROL_OFF(Exception):
	pass

# Local control disadd.
class ExceptionNET_ERR_LOCAL_CONTROL_DISADD(Exception):
	pass

# Local control hasadd.
class ExceptionNET_ERR_LOCAL_CONTROL_HASADD(Exception):
	pass

# Local control doorNO conflict.
class ExceptionNET_ERR_LOCAL_CONTROL_DOORNO_CONFLICT(Exception):
	pass

# Local control communication fail.
class ExceptionNET_ERR_LOCAL_CONTROL_COMMUNICATION_FAIL(Exception):
	pass

# Operand inexistence.
class ExceptionNET_ERR_OPERAND_INEXISTENCE(Exception):
	pass

# Local control over limit.
class ExceptionNET_ERR_LOCAL_CONTROL_OVER_LIMIT(Exception):
	pass

# Door over limit.
class ExceptionNET_ERR_DOOR_OVER_LIMIT(Exception):
	pass

# Alarm over limit.
class ExceptionNET_ERR_ALARM_OVER_LIMIT(Exception):
	pass

# Local control address inconformity type.
class ExceptionNET_ERR_LOCAL_CONTROL_ADDRESS_INCONFORMITY_TYPE(Exception):
	pass

# Device not support one more card.
class ExceptionNET_ERR_NOT_SUPPORT_ONE_MORE_CARD(Exception):
	pass

# NET_ERR_DELETE_NO_EXISTENCE_FACE*/"Delete no existence face.
class ExceptionNET_ERR_DELETE_NO_EXISTENCE_FACE(Exception):
	pass

# Communication the door machine abnormality.
class ExceptionNET_DVR_ERR_OUTDOOR_COMMUNICATION(Exception):
	pass

# Not configured room no.
class ExceptionNET_DVR_ERR_ROOMNO_UNDEFINED(Exception):
	pass

# No call.
class ExceptionNET_DVR_ERR_NO_CALLING(Exception):
	pass

# Ring the bell.
class ExceptionNET_DVR_ERR_RINGING(Exception):
	pass

# Is calling now.
class ExceptionNET_DVR_ERR_IS_CALLING_NOW(Exception):
	pass

# Intelligent lock password mistake.
class ExceptionNET_DVR_ERR_LOCK_PASSWORD_WRONG(Exception):
	pass

# Switch lock failure.
class ExceptionNET_DVR_ERR_CONTROL_LOCK_FAILURE(Exception):
	pass

# Switch lock timeout.
class ExceptionNET_DVR_ERR_CONTROL_LOCK_OVERTIME(Exception):
	pass

# Intelligent lock device is busy.
class ExceptionNET_DVR_ERR_LOCK_DEVICE_BUSY(Exception):
	pass

# Remote lock function is not open.
class ExceptionNET_DVR_ERR_UNOPEN_REMOTE_LOCK_FUNCTION(Exception):
	pass

# The downloaded file is incomplete.
class ExceptionNET_DVR_ERR_FILE_NOT_COMPLETE(Exception):
	pass

# The IPC has been existed.
class ExceptionNET_DVR_ERR_IPC_EXIST(Exception):
	pass

# The channel has added one IPC.
class ExceptionNET_DVR_ERR_ADD_IPC(Exception):
	pass

# Out of network bandwidth capacity.
class ExceptionNET_DVR_ERR_OUT_OF_RES(Exception):
	pass

# IP conflict between IPC and DVR.
class ExceptionNET_DVR_ERR_CONFLICT_TO_LOCALIP(Exception):
	pass

# Illegal IP.
class ExceptionNET_DVR_ERR_IP_SET(Exception):
	pass

# Illegal port.
class ExceptionNET_DVR_ERR_PORT_SET(Exception):
	pass

# Not in the same WLAN, not support security question config or export GUID.
class ExceptionNET_ERR_WAN_NOTSUPPORT(Exception):
	pass

# Mutual exclusion function error.
class ExceptionNET_ERR_MUTEX_FUNCTION(Exception):
	pass

# Security question config amount error.
class ExceptionNET_ERR_QUESTION_CONFIGNUM(Exception):
	pass

# Face intelligent channel resource has run out.
class ExceptionNET_ERR_FACECHAN_NORESOURCE(Exception):
	pass

# Data is Callbacking.
class ExceptionNET_ERR_DATA_CALLBACK(Exception):
	pass

# SMD insufficient encoding resources.
class ExceptionNET_DVR_SMD_ENCODING_NORESOURSE(Exception):
	pass

# SMD insufficient decoding resources.
class ExceptionNET_DVR_SMD_DECODING_NORESOURSE(Exception):
	pass

# Facelib data is being processed.
class ExceptionNET_DVR_FACELIB_DATA_PROCESSING(Exception):
	pass

# Too large time difference between device and server.
class ExceptionNET_DVR_ERR_LARGE_TIME_DIFFRENCE(Exception):
	pass

# Open the playback,this function is not supported.
class ExceptionNET_DVR_NO_SUPPORT_WITH_PLAYBACK(Exception):
	pass

# The channel has opened SMD,this function is not supported.
class ExceptionNET_DVR_CHANNEL_NO_SUPPORT_WITH_SMD(Exception):
	pass

# The channel has opened Face snap,this function is not supported.
class ExceptionNET_DVR_CHANNEL_NO_SUPPORT_WITH_FD(Exception):
	pass

# The phone number is illegal.
class ExceptionNET_DVR_ILLEGAL_PHONE_NUMBER(Exception):
	pass

# The certificate number is illegal.
class ExceptionNET_DVR_ILLEGAL_CERITIFICATE_NUMBER(Exception):
	pass

# The resolving power of this chanel is not supported.
class ExceptionNET_DVR_ERR_CHANNEL_RESOLUTION_NO_SUPPORT(Exception):
	pass

# The encoding format of this chanel is not supported.
class ExceptionNET_DVR_ERR_CHANNEL_COMPRESSION_NO_SUPPORT(Exception):
	pass

# Deep learning resources exceed limits.
class ExceptionNET_DVR_INSUFFICIENT_DEEP_LEARNING_RESOURCES(Exception):
	pass

# The panel mode is not configured.
class ExceptionNET_DVR_PANEL_MODE_NOT_CONFIG(Exception):
	pass

# Not support Deicing.
class ExceptionNET_DVR_ERR_NOTSUPPORT_DEICING(Exception):
	pass

# Thermometry is not enabled.
class ExceptionNET_DVR_ERR_THERMENABLE_CLOSE(Exception):
	pass

# Panoramic view and position limit can not be operated at the same time.
class ExceptionNET_DVR_ERR_PANORAMIC_LIMIT_OPERATED(Exception):
	pass

# SmartH264 and ROI can not be operated at the same time.
class ExceptionNET_DVR_ERR_SMARTH264_ROI_OPERATED(Exception):
	pass

# Upper limit of rule number.
class ExceptionNET_DVR_ERR_RULENUM_LIMIT(Exception):
	pass

# Laser and deicing cannot be operated at the same time.
class ExceptionNET_DVR_ERR_LASER_DEICING_OPERATED(Exception):
	pass

# Turn off the digital zoom function or set the zoom limit to the minimum.
class ExceptionNET_DVR_ERR_OFFDIGITALZOOM_OR_MINZOOMLIMIT(Exception):
	pass

class ExceptionNET_DVR_FILE_NOT_AVAILABLE(Exception):
    pass
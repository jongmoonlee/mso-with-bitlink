from ctypes import *
import platform
import os

lib_ext = ""
if os.name == 'nt':
    lib_ext = "dll"
elif platform.system() == "Linux":
    lib_ext = "so"
else:
    exit("OS not supported.")

cdll.LoadLibrary("libBitLink." + lib_ext)
bslink = CDLL("libBitLink." + lib_ext)

BS_Broadcast  = bslink.BS_Broadcast
BS_Close      = bslink.BS_Close
BS_Count      = bslink.BS_Count
BS_Demo       = bslink.BS_Demo
BS_Error      = bslink.BS_Error
BS_File       = bslink.BS_File
BS_ID         = bslink.BS_ID
BS_Init       = bslink.BS_Init
# BS_Intro      = bslink.BS_Intro
BS_Name       = bslink.BS_Name
BS_Open       = bslink.BS_Open
BS_OpenLink   = bslink.BS_OpenLink
BS_Receive    = bslink.BS_Receive
BS_Reset      = bslink.BS_Reset
BS_Send       = bslink.BS_Send
BS_SendRaw    = bslink.BS_SendRaw
BS_Speed      = bslink.BS_Speed
BS_StartTimer = bslink.BS_StartTimer
BS_StopTimer  = bslink.BS_StopTimer
BS_Version    = bslink.BS_Version


BS_Broadcast.argtypes  = [c_int, c_char_p]
BS_Count.argtypes      = [c_int]
BS_Demo.argtypes       = [c_int]
BS_Error.argtypes      = [c_int]
BS_File.argtypes       = [c_char_p]
BS_ID.argtypes         = [c_char_p]
# BS_Intro.argtypes      = [c_float]
BS_Name.argtypes       = [c_int, c_char_p]
BS_Open.argtypes       = [c_int]
BS_OpenLink.argtypes   = [c_char_p]
BS_Receive.argtypes    = [c_int, POINTER(c_ubyte), c_int, c_int]
BS_Reset.argtypes      = [c_int]
BS_Send.argtypes       = [c_int, c_char_p, c_int]
BS_SendRaw.argtypes    = [c_int, c_char_p, c_int]
BS_Speed.argtypes      = [c_int]
BS_StartTimer.argtypes = [c_int]
BS_StopTimer.argtypes  = [c_int]
BS_Version.argtypes    = [c_int]


BS_Count.restype      = c_int
BS_Demo.restype       = c_bool
BS_Error.restype      = c_int
BS_File.restype       = c_bool
BS_ID.restype         = c_char_p
# BS_Intro.restype      = c_float
BS_Name.restype       = c_char_p
BS_Open.restype       = c_int
BS_OpenLink.restype   = c_int
BS_Receive.restype    = c_bool
BS_Speed.restype      = c_int
BS_Version.restype    = c_char_p
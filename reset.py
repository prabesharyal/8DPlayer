from ctypes import cast, POINTER
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume
import sys
import os

# Get default audio device using PyCAW
def fix_audio():
    devices = AudioUtilities.GetSpeakers()
    interface = devices.Activate(
        IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
    volume = cast(interface, POINTER(IAudioEndpointVolume))


    currentVolumeDb = volume.GetMasterVolumeLevel()
    print("Master Volume Level is :{} \n".format(str(currentVolumeDb)))

    volumeL = volume.GetChannelVolumeLevel(0)
    volumeR = volume.GetChannelVolumeLevel(1)
    print("Volume of different channels:  Left = {} and Right ={} \n".format(str(volumeL),str(volumeR)))

    volume.SetChannelVolumeLevel(0, -6, None) # Left
    volume.SetChannelVolumeLevel(1, -6, None) # Right
    # Get & print new volume
    volumeL = volume.GetChannelVolumeLevel(0)
    volumeR = volume.GetChannelVolumeLevel(1)
    print("New Volume of different channels:  Left = {} and Right ={}\n".format(str(volumeL),str(volumeR)))


    volume.SetMasterVolumeLevel(0, None)
    print("New Volume Level is :{} \n".format(str(currentVolumeDb)))


    #Exit
    sys.exit(0)
    os.exit(0)

fix_audio()
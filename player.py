import math
import sys
import time
import os
from ctypes import cast, POINTER
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume
import multiprocessing

vol = 70
amp = 30
tp = 3

def audiocontroller():
    try:
        global vol,amp,tp
        # Get default audio device using PyCAW
        devices = AudioUtilities.GetSpeakers()
        interface = devices.Activate(
            IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
        volume = cast(interface, POINTER(IAudioEndpointVolume))



        def setBalance(left,right):
            fmap2 = lambda y: (y/100 - 1)*45
            left = ( fmap2(left) )
            right = ( fmap2(right) )
            try:
                volume.SetChannelVolumeLevel(0, left, None) # Left
                volume.SetChannelVolumeLevel(1, right, None) # Right
            except BaseException:
                volume.SetChannelVolumeLevel(0, -6, None) # Left
                volume.SetChannelVolumeLevel(1, -6, None) # Right


        def_balance = (vol,vol)
        l = def_balance[0]
        r = def_balance[1]

        sleep_int = 50

        t = 0
        dt = 0.1
        freq = 1/tp

        while True:
            t+= dt
            # print(f"setting balance lr({l,r})")
            l = def_balance[0]+ amp*math.sin(t*freq)/2
            r = def_balance[1]+ amp*math.sin(t*freq + math.pi/2)/2
            setBalance(l,r)
            time.sleep((1/1000)*sleep_int)
    except KeyboardInterrupt:
        print('Interrupted')
        print("%50s"%"")
        print("%50s"%"")
        print('\033[1m' + '%50s' % "Audio Made Normal" +'\033[0m')
        fix_audio()

def animation():
    try:
        #animations
        vals="▁▂▃▄▅▆▇█▇▆▅▄▃▁"
        dval = list(vals)
        k = -1
        l = len(vals)
        dk = 1
        print("%50s"%"")
        print("%50s"%"")
        print("%50s"%"")
        print("%50s"%"")
        print("%50s"%"")
        print("%50s"%"")
        print('\033[1m' + '%50s' % "Plying in 8D" +'\033[0m'''+"\n")
        while True:
            k+= dk
            for x in range(l):
                n = (x+k)%l
                dval[x] = vals[n]
            sys.stdout.flush()
            sys.stdout.write('\r    '+' '.join(dval*3))
            sys.stdout.flush()
            time.sleep(0.1)
        print("%50s"%"")
        print("%50s"%"")
        print("%50s"%"")
        print("%50s"%"")
        print("%50s"%"")
        print("%50s"%"")
    except KeyboardInterrupt:
        print('Interrupted')
        print("%50s"%"")
        print("%50s"%"")
        print('\033[1m' + '%50s' % "Audio Made Normal" +'\033[0m')
        fix_audio()

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
        

    print("%50s"%"")
    print("%50s"%"")
    print("%50s"%"")
    print("%50s"%"")
    print("%50s"%"")
    print("%50s"%"")        
    print("%50s"%"")
    print("%50s"%"")
    print('\033[1m' + '%50s' % "Audio Made Normal" +'\033[0m')
    print("%50s"%"")
    print("%50s"%"")
    print("%50s"%"")
    print("%50s"%"")
    print("%50s"%"")
    print("%50s"%"")
    print("%50s"%"")
    print("%50s"%"")


    #Exit
    try:
        sys.exit(0)
    except SystemExit:
            os._exit(0)

def main():
    def inputs():
        global vol, amp, tp
        try:
            vol = int(input("Input volume you want : "))
        except ValueError:
            vol = vol
        try:
            amp = int(input("Enter amplitude required : "))
        except ValueError:
            amp = amp
        try:
            tp = int(input("Enter Time period of revolution :"))
        except ValueError:
            tp = tp

    inputs()
    animate = multiprocessing.Process(name='animate', target=animation)
    play = multiprocessing.Process(name='play', target=audiocontroller)
    animate.start()
    play.start()

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print('Interrupted')
        print("%50s"%"")
        print("%50s"%"")
        print('\033[1m' + '%50s' % "Audio Made Normal" +'\033[0m')
        fix_audio()
        try:
            sys.exit(0)
        except SystemExit:
            os._exit(0)
    except EOFError:
        print("EOF")
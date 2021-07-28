import os
import subprocess


adb_ops={
        "tap":".\\adb\\nox_adb shell input tap {args}",
        "swipe":".\\adb\\nox_adb shell input swipe {args}",
        "scrcap":".\\adb\\nox_adb shell screencap {args}",
        "pull":".\\adb\\nox_adb pull {args}"
    }

def tap(c):
    return os.popen(adb_ops['tap'].replace('{args}',str(c[0])+' '+str(c[1])))
def swipe(x1,y1,x2,y2):
    pass
def scrcap(filename):
    return os.popen(adb_ops['scrcap'].replace('{args}',filename))
def pull(filename):
    return os.popen(adb_ops['pull'].replace('{args}',filename))
    
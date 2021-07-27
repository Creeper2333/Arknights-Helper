import os
import subprocess

class phone:
    adb_ops={
        "tap":"adb shell input tap {args}",
        "swipe":"adb shell input swipe {args}",
        "scrcap":"adb shell screencap {args}",
        "pull":"adb pull {args}"
    }
    def __init__(self):
        pass
    def tap(self,x,y):
        return os.popen(self.adb_ops['tap'].replace('{args}',x+' '+y))
    def swipe(self,x1,y1,x2,y2):
        pass
    def scrcap(self,filename):
        return os.popen(self.adb_ops['scrcap'].replace('{args}',filename))
    def pull(self,filename):
        return os.popen(self.adb_ops['pull'].replace('{args}',filename))
    
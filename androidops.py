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
    
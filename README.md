# Arknights-Helper
### 介绍
一个适用于明日方舟自动刷关的脚本，比如钱本什么的
### 使用说明
其实这玩意不需要安装，直接运行就可以了
```
python akhelper.py
```
值得说明的是，这个脚本是给屏幕宽高16:9(1600x900)的做的

可以在模拟器设置里调

还有那个自动选择关卡的坐标填的是钱本-4和碳本-4的坐标，可以自己改（akhelper.py>coordinates>'select_op'）

为了节约资源我在作战的时候设置了一个时间，我默认50secs，你自己调，比如剿灭就调个600sec

如果发现换成别的副本以后开始作战按钮点不上可以考虑把阈值调高（akhelper.py>dosth() 或 akhelper.py>THRESHOLD_VALUE）

adb过期了记得提醒我，或者换夜神模拟器

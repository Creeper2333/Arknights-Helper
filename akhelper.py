from operator import truediv
import imgcompare
from androidops import *
from PIL import Image
import sys
import time

TIME_ELAPSE_SCRSHOT=3#检测间隔时间，太长则很迟钝，太短会频繁写入文件
TIME_ELAPSE_BATTLE=50#战斗时间，减少无用截屏次数

coordinates={
    'select_op':(1065,370),#在这里填上要选择的关卡的屏幕坐标
    'start_op':(1428,848),
    'op_begin':(1375,644),
    'start_op_btn_1':(1300,830),
    'start_op_btn_2':(1555,865),
    'op_begin_btn_1':(1295,460),
    'op_begin_btn_2':(1464,828),
    'sanity_1':(1010,323),
    'sanity_2':(1343,606),
}
boxes={
    'start_op_btn':(1300,780,1555,865),
    'op_begin_btn':(1295,460,1464,808),
    'sanity':(1010,323,1343,606)
}
flag_isinbattle=False

def screenshot():
    scrcap('/sdcard/capture.png')
    time.sleep(1)#防止未截屏完而导出文件导致文件损坏
    pull('/sdcard/capture.png')

def start_btn_cpr(img):
    region=img.crop(boxes['start_op_btn'])
    start_btn_def=Image.open('ak_ui/start_op_btn.png')
    tmp=start_btn_def
    #region.save('start_op_btn.png')
    return imgcompare.image_contrast(region,tmp)

def begin_btn_cpr(img):
    region=img.crop(boxes['op_begin_btn'])
    begin_btn_def=Image.open('ak_ui/op_begin_btn.png')
    tmp=begin_btn_def
    #region.save('op_begin_btn.png')
    return imgcompare.image_contrast(region,tmp)
def sanity(img):
    region=img.crop(boxes['sanity'])
    sanity=Image.open('ak_ui/sanity.png')
    tmp=sanity
    #region.save('op_begin_btn.png')
    return imgcompare.image_contrast(region,tmp)
def dosth():
    if(start_btn_cpr(img_origin)<10):
            tap(coordinates['start_op'])
            return True
    if(begin_btn_cpr(img_origin)<10):
        tap(coordinates['op_begin'])
        flag_isinbattle=True
        return True
    if(sanity(img_origin)<10):
        input('没有理智了')
        sys.exit(0)
    return False
if(__name__=='__main__'):
    flag=True
    while(flag):
        try:
            screenshot()
        except:
            print('截屏失败，可能是模拟器未正常启动')
            #sys.exit(0)
        #img=Image.open('ak_ui/op_select.png')
        time.sleep(1)#防止文件没有导出完
        img_origin=Image.open('capture.png')
        if(not dosth()):
            tap(coordinates['select_op'])
        if(flag_isinbattle):
            time.sleep(TIME_ELAPSE_BATTLE)
        img_origin.close()
        time.sleep(TIME_ELAPSE_SCRSHOT)
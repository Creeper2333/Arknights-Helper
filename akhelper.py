from operator import truediv
import imgcompare
from androidops import *
from PIL import Image
import sys
import time

coordinates={
    'select_op':(1065,370),
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

def screenshot():
    scrcap('/sdcard/capture.png')
    time.sleep(1)
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
        time.sleep(1)
        img_origin=Image.open('capture.png')
        if(not dosth()):
            tap(coordinates['select_op'])
        
        img_origin.close()
        time.sleep(5)
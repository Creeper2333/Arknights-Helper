import imgcompare
from androidops import *
from PIL import Image
import sys

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
    phone.scrcap('/sdcard/capture.png')
    phone.pull('/sdcard/capture.png')

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

if(__name__=='__main__'):
    try:
        screenshot()
        img_origin=Image.open('capture.png')
        
    except:
        print('截屏失败，可能是模拟器未正常启动')
        #sys.exit(0)
    img=Image.open('ak_ui/op_select.png')
    print(start_btn_cpr(img))
    
    img_origin.close()
#!/usr/bin/python
#coding:utf-8
from skimage import io, transform
import numpy as np
import matplotlib.pyplot as plt
import tensorflow as tf
from pylab import mpl

mpl.rcParams['font.sans-serif']=['SimHei'] # 正常显示中文标签
mpl.rcParams['axes.unicode_minus']=False # 正常显示正负号

#去中间的区域（正方形），再进行缩放。中间的区域选择：选取行列小的值，
def load_image(path):
    fig = plt.figure("Centre and Resize")
    img = io.imread(path) 
    img = img / 255.0
    
    ax0 = fig.add_subplot(131)  
    ax0.set_xlabel(u'Original Picture') 
    ax0.imshow(img) 
    print("3 shape",img.shape)
    print('shape:',img.shape[:2])
    short_edge = min(img.shape[:2]) 
    print("short_edge",short_edge)
    y = (img.shape[0] - short_edge) / 2
    x = (img.shape[1] - short_edge) / 2
    print("x,y",x,y)
    crop_img = img[int(y):int(y+short_edge), int(x):int(x+short_edge)]
    
    ax1 = fig.add_subplot(132) 
    ax1.set_xlabel(u"Centre Picture") 
    ax1.imshow(crop_img)
    
    re_img = transform.resize(crop_img, (224, 224)) 
    
    ax2 = fig.add_subplot(133) 
    ax2.set_xlabel(u"Resize Picture") 
    ax2.imshow(re_img)
	
    img_ready = re_img.reshape((1, 224, 224, 3))

    return img_ready

def percent(value):
    return '%.2f%%' % (value * 100)


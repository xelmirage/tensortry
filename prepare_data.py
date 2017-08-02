# -*- coding: utf-8 -*-
# Author:
# FileName:
# Function: 整理源数据图像，剪切至正方形并缩放到统一尺寸
__author__ = 'xelmirage'
import sys
import os
import glob
from PIL import Image as image

path = './data'
list = os.listdir(path)
serial_num = 0
for i in list:

    l1 = os.path.splitext(i)
    len_l1 = len(l1)

    newfname = str('%04d' % serial_num) + '.jpg'
    newfpath = "./prepared/%s" % (newfname)
    oldfpath = "%s/%s" % (path, i)
    im = image.open(oldfpath)
    if im.height > im.width:
        x_upperleft = 0
        y_upperleft = (im.height - im.width) / 2
        x_lowerright = im.width
        y_lowerright = y_upperleft + im.width
    else:
        x_upperleft = (im.width - im.height) / 2
        y_upperleft = 0
        x_lowerright = x_upperleft + im.height
        y_lowerright = im.height
    box = (x_upperleft, y_upperleft, x_lowerright, y_lowerright)
    im = im.crop(box)
    im = im.convert('L')
    im = im.resize((256, 256), image.ANTIALIAS)

    im.save(newfpath)

    serial_num += 1

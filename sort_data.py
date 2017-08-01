# -*- coding: utf-8 -*-
# Author:
# FileName:
# Function: 批量命名某一文件夹下的文件名
__author__ = 'xelmirage'
import sys
import os
import glob

path = './data'
list = os.listdir(path)
serial_num = 0
for i in list:

    l1 = os.path.splitext(i)
    len_l1 = len(l1)
    if (l1[len_l1 - 1] == '.jpg') or (l1[len_l1 - 1] == '.jpeg'):
        newfname = str('%04d' % serial_num) + '.jpg'
        newfpath = "%s/%s" % (path, newfname)
        oldfpath = "%s/%s" % (path, i)
        os.rename(oldfpath, newfpath)
    elif (l1[len_l1 - 1] == '.png'):
        newfname = str('%04d' % serial_num) + '.png'
        newfpath = "%s/%s" % (path, newfname)
        oldfpath = "%s/%s" % (path, i)
        os.rename(oldfpath, newfpath)
    print(l1, l1[len_l1 - 1])
    serial_num += 1

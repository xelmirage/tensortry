# -*- coding: utf-8 -*-
# 导入TensorFlow
import tensorflow as tf
from PIL import Image
import os


def _int64_feature(value):
    return tf.train.Feature(int64_list=tf.train.Int64List(value=[value]))


def _bytes_feature(value):
    return tf.train.Feature(bytes_list=tf.train.BytesList(value=[value]))


writer = tf.python_io.TFRecordWriter("try_to_write")

# filename = ['data/0005.jpg', 'data/0006.jpg', 'data/0007.jpg']
path = './prepared'
filename = os.listdir(path)
num_examples = len(filename)

for i in range(num_examples):
    file_path = "%s/%s" % (path, filename[i])
    img = Image.open(file_path)
    image_raw = img.tobytes()
    example = tf.train.Example(features=tf.train.Features(feature={
        'name': _bytes_feature(bytes(filename[i], encoding="utf8")),
        'image_raw': _bytes_feature(image_raw)
    }))  #
    writer.write(example.SerializeToString())

writer.close()


# 新建一个Session

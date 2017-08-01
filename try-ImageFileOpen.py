# -*- coding: utf-8 -*-
# 导入TensorFlow
import tensorflow as tf

# 新建一个Session
with tf.Session() as sess:
    # 我们要读三幅图片A.jpg, B.jpg, C.jpg
    filename = ['data/0005.jpg', 'data/0006.jpg', 'data/0007.jpg']
    # string_input_producer会产生一个文件名队列
    filename_queue = tf.train.string_input_producer(filename, shuffle=True, num_epochs=5)
    # reader从文件名队列中读数据。对应的方法是reader.read
    reader = tf.WholeFileReader()
    key, value = reader.read(filename_queue)
    # tf.train.string_input_producer定义了一个epoch变量，要对它进行初始化
    tf.local_variables_initializer().run()
    # 使用start_queue_runners之后，才会开始填充队列
    threads = tf.train.start_queue_runners(sess=sess)

    i = 0
    for i in range(0,15):

        # 获取图片数据并保存
        image_data = sess.run(value)
        with open('out/test_%d.jpg' % i, 'wb') as f:
            f.write(image_data)
    
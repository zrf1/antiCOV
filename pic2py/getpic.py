# -*- coding: utf-8 -*-
# @Time    : 2018/6/6 18:29
# @Author  : Octan3
# @Email   : Octan3@stu.ouc.edu.cn
# @File    : Pic2py.py
# @Software: PyCharm
from memory_pic import *
import base64

def get_pic(pic_code, pic_name):
    image = open(pic_name, 'wb')
    image.write(base64.b64decode(pic_code))
    image.close()

get_pic(background_gif, 'background.gif')
# 在这里使用图片
bgpic("background.gif")

os.remove('background.gif')

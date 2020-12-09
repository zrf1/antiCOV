from turtle import *
from Helper import TurtleHelper
from Doctor import Doctor
from Nurse import Nurse

t = Turtle()
setup(800 ,600)
th = TurtleHelper()
docter = Doctor(t, th, 150, -30)
nurse = Nurse(t, th, -150, -90)
docter.draw()
nurse.draw()

# 方法1：使用sys._MEIPASS获取打包后路径（成功）。注意需分区脚本模式和打包模式
'''
import sys, os
if getattr(sys, 'frozen', False):   #打包模式
    path = sys._MEIPASS
else:
    path = os.path.abspath(".")
bgpic(os.path.join(path, "img","background.gif"))
'''

# 方法2：使用pic2py以base64方式把图片写入py文件，在新建和使用图片
from memory_pic import *
import os, base64

def get_pic(pic_code, pic_name):
    image = open(pic_name, 'wb')
    image.write(base64.b64decode(pic_code))
    image.close()

get_pic(background_gif, 'background.gif')
# 在这里使用图片
bgpic("background.gif")

os.remove('background.gif')

th.Run()
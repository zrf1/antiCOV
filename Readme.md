# 抗疫主题创意作品

http://work.wotojo.com/python/antiCOV

![效果图](antiCOV.png)

# 项目思路

1. 查找和学习同类cartoon代码
1. 查找并确定图片资源
1. 写代码，测试
1. 建立辅助工具与绘制模式
1. 打包程序与提交作品

# 代码说明

* Doctor.py  医生类
* Nurse.py  护士类
* Helper.py  辅助类
* memory    用py存储的背景图片（否则打包后，目录不易确定）
* main.py   主程序入口

## Doctor.py 医生类

### 成员变量

(x, y)为中心点位置，使用相对值，便于后期移动

self.th  helper实例

### 成员函数

_get_color()  各种颜色值

draw()      依次调用绘制各部分

其他函数     绘制各部分

## Nurse.py 护士类

### 成员变量

(x, y)为中心点位置，使用相对值，便于后期移动

self.th  helper实例

### 成员函数

_get_color()  各种颜色值

draw()      依次调用绘制各部分

其他函数     绘制各部分

### 几点注意

* 不断利用直线、弧线、圆形、曲线、椭圆、多边形等做图（代码复用度低）
* 最好分部分画，否则很难修改（每部分起点最好是独立的）
* 遮盖的问题：从底层往上画（因此有时画的顺序比较怪）
* 画轮廓时要兼顾颜色填充，防止线条和图形不一致（最好是一遍过）
* 注意绘制速度，画时间长的复杂动作可用tracer(False)过滤掉
* 提取可复用的方法，如_goto()、_goto_up()、DrawCurve()、DrawEllipse() 
* 操作繁琐：如何取得坐标值，测试需反复运行


```python
def _goto_up(self, x, y):
    'goto相对位置，不画图'
    self.t.up()
    self.t.goto(self.x + x, self.y + y)
    self.t.down()

def _goto(self, x, y):
    'goto，相对位置'
    self.t.goto(self.x + x, self.y + y)
```

## Helper.py  辅助类

### 成员变量

_debug  是否调试（调试状态下，画笔为红色；否则为黑色）

_sleep  循环绘制时的时间间隔

### 成员函数

#### Run()  运行模式

* 默认   发布时，正常绘制
* getpost 获取坐标值，便于编程时写坐标值
* repeat  重复画，便于检测代码变化情况

>用importlib.reload重新加载画图过程，减少人工调试，调用`python helper.py`


#### DrawCurve()  绘制曲线
#### DrawEllipse()  绘制椭圆

## memory_pic.py 用py存储的背景图片

background_gif = "xxxxxxxxxx"

用 base64.b64encode 和 b64str.decode 将图片内容转换为base64编码，并生成的py文件

## main.py  主函数

1. 初始化
1. 实例化Doctor和Nurse类，并绘制
1. 加载背景并绘制

# 文件打包

打包为exe程序

`pyinstaller -F -i img\favicon.ico main.py`

（注：修改`.spec`文件的方法测试未成功）

截图，录屏，制作gif，发布到网页

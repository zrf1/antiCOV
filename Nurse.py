# coding:utf-8
'''
turtle画护士
'''
class Nurse(object):
    '护士（女）'

    def __init__(self, _t, _th, _x, _y):
        '初始化，(x, y)为中心点位置，使用相对值，便于后期移动'
        self.x, self.y = _x, _y
        self.t = _t
        self.th = _th
        self.penset()
    
    def penset(self):
        '设置画笔'
        self.t.st()
        self.t.speed(10)
        self.t.pensize(3)
        self.t.pencolor(self._get_color('pen'))
    
    def _get_color(self, sname):
        '获取颜色值'
        if sname == 'pen':
            return 'black' if not self.th.Debug() else 'red'
        elif sname == 'skin':       #皮肤
            return '#f7ceba'
        elif sname == 'eyes':       #眼睛
            return '#030303'
        elif sname == 'hair':       #头发
            return '#613616'
        elif sname == 'kouzhao':    #口罩
            return '#9bebf4'
        elif sname == 'cross':      #红十字
            return '#e64732'
        elif sname == 'linzi':      #衣领
            return '#96d4ed'
        else:
            return 'white'

    def draw(self):
        self.penset()
        
        self._hair_above()
        self._hair_below()
        self._ears()
        self._face()
        self._eyes()
        self._kouzhao()
        self._hat()
        self._neck()
        self._linzi()
        self._yifu()
        
        #完成
        self.t.ht()
    
    def _hair_above(self):
        '头发-上部分'
        self._goto_up(-72, 24)
        self.t.seth(112)
        self.t.fillcolor(self._get_color('hair'))
        self.t.begin_fill()
        self.t.circle(-60,80)
        self.t.rt(12)
        self.t.circle(-200,15)
        self.t.rt(8)
        self.t.circle(-200,15)
        self.t.rt(21)
        self.t.circle(-68,54)
        self._goto(72, 38)
        self.t.rt(86)
        self.t.circle(-76,68)
        self.t.lt(146)
        self.t.circle(-76,75)
        self._goto(-72, 24)
        self.t.end_fill()
        self._goto_up(-29, 94)
        self.t.seth(212)
        self.t.circle(76,50)
        self._goto_up(25, 94)
        self.t.seth(-22)
        self.t.circle(-76,40)

    def _face(self):
        '画脸'
        self._goto_up(-72, 24)
        self.t.seth(-80)
        self.t.fillcolor(self._get_color('skin'))
        self.t.begin_fill()
        self.t.circle(60,60)
        self.t.circle(100,55)
        self.t.lt(10)
        self.t.circle(50,55)

        self.t.penup()
        self._goto(68, 38)
        self.t.seth(176)
        self.t.circle(-76,64)
        self.t.lt(148)
        self.t.circle(-76,77)
        self.t.end_fill()
        self.t.pendown()

    def _ears(self):
        '耳朵'
        #右耳
        self._goto_up(72, 33)
        self.t.fillcolor(self._get_color('skin'))
        self.t.begin_fill()
        self._goto(82, 40)
        self.t.seth(0)
        self.th.DrawCurve(self.t, 0.1, 32, 0.1, 5.1)
        self.t.pu()
        self._goto(72, 33)
        self.t.end_fill()
        self.t.pd()
        #左耳
        self._goto_up(-74, 22)
        self.t.fillcolor(self._get_color('skin'))
        self.t.begin_fill()
        self.t.seth(150)
        self.th.DrawCurve(self.t, 0.1, 30, 0.1, -7)
        self.t.pu()
        self._goto(-74, 22)
        self.t.end_fill()
        self.t.pd()

    def _eyes(self):
        '眼睛'
        #眼眉
        self._goto_up(-15, 41)
        self._goto(-23, 43)
        self._goto_up(21, 42)
        self.t.seth(0)
        self.t.circle(-100, 10)
        #眼睛
        self._goto_up(-29, 32)
        self.t.seth(0)
        self.t.fillcolor(self._get_color('eyes'))
        self.t.begin_fill()
        self.t.circle(-10)
        self.t.end_fill()
        self._goto_up(-31, 22)
        self.t.dot(5, 'white')

        self._goto_up(30, 33)
        self.t.seth(0)
        self.t.fillcolor(self._get_color('eyes'))
        self.t.begin_fill()
        self.t.circle(-10)
        self.t.end_fill()
        self._goto_up(27, 27)
        self.t.dot(5, 'white')

    def _kouzhao(self):
        '口罩'
        self._goto_up(-65, 18)
        self._goto(-45, 8)
        self.t.fillcolor(self._get_color('kouzhao'))
        self.t.begin_fill()
        #self._goto(51, 11)
        self.t.seth(-10)
        self.t.circle(220,25)
        self._goto(48, -12)
        self.t.seth(210)
        self.t.pu()
        self.t.circle(-100,54)
        self.t.pd()
        self._goto(-45, 8)
        self.t.end_fill()

        self._goto_up(51, 12)
        self._goto(68, 31)

    def _hat(self):
        '帽子'
        self._goto_up(-75, 63)
        self._goto(-93, 79)
        self._goto(-53, 142)
        self._goto(15, 154)
        self._goto(49, 148)
        self._goto(83, 102)
        self._goto(72, 80)
        #红十字
        self.t.pensize(7)
        self.t.pencolor(self._get_color('cross'))
        self._goto_up(-23, 125)
        self._goto(23, 130)
        self._goto_up(0, 143)
        self._goto(1, 116)
        self.t.pensize(4)
        self.t.pencolor(self._get_color('pen'))

    def _hair_below(self):
        '头发-下部分'
        #左
        self._goto_up(-71, -8)
        self.t.seth(-100)
        self.t.fillcolor(self._get_color('hair'))
        self.t.begin_fill()
        self.t.circle(200,20)
        self.t.lt(11)
        self.t.circle(18,100)
        self.t.seth(60)
        self.t.pu()
        self.t.circle(-200,13)
        self._goto(-7, -53)
        self._goto(-5, -31)
        self._goto(-40, -18)
        self._goto(-62, -7)
        self._goto(-72, -8)
        self.t.end_fill()
        self.t.pd()

        #右
        self._goto_up(60, -87)
        self.t.seth(-30)
        self.t.begin_fill()
        self.t.circle(13,100)
        self.t.lt(8)
        self.t.circle(200,24)
        self.t.pu()
        self._goto(64, -4)
        self._goto(50, -15)
        self._goto(33, -21)
        self._goto(27, -25)
        self._goto(21, -38)
        self._goto(22, -48)
        self._goto(35, -51)
        self._goto(38, -57)
        self._goto(39, -64)
        self._goto(62, -87)
        self.t.end_fill()
        self.t.pd()
        #线条
        self._goto_up(-57, -16)
        self.t.seth(-100)
        self.t.circle(100,42)
        self._goto_up(-26, -29)
        self.t.seth(-95)
        self.t.circle(100,16)
        self._goto_up(36, -23)
        self.t.seth(-80)
        self.t.circle(-100,15)
        self._goto_up(64, -7)
        self.t.seth(-74)
        self.t.circle(-100,42)

    def _neck(self):
        '脖子'
        self._goto_up(-9, -31)
        self.t.seth(-60)
        self.t.fillcolor(self._get_color('skin'))
        self.t.begin_fill()
        self.t.circle(-30, 40)
        self.t.seth(-50)
        self.t.circle(-100,18)
        self._goto(19, -49)
        self._goto(26, -27)
        self.t.end_fill()

    def _linzi(self):
        '领子'
        self._goto_up(-8, -51)
        self.t.seth(160)
        self.t.fillcolor(self._get_color('linzi'))
        self.t.begin_fill()
        self.t.circle(10,150)
        self._goto(11, -81)
        self.t.end_fill()

        self._goto_up(20, -54)
        self.t.seth(50)
        self.t.begin_fill()
        self.t.circle(-10,145)
        self._goto(14, -88)
        self.t.end_fill()

    def _yifu(self):
        '衣服'
        self._goto_up(-24, -57)
        self.t.seth(-130)
        self.t.circle(200,16)
        self._goto_up(-34, -101)
        self._goto(-32, -110)
        self._goto_up(11, -82)
        self._goto(18, -111)
        self._goto_up(50, -102)
        self._goto(53, -110)
        self._goto_up(39, -65)
        self.t.seth(-40)
        self.t.circle(-110,30)

    def _goto_up(self, x, y):
        'goto，不画图'
        self.t.up()
        self.t.goto(self.x + x, self.y + y)
        self.t.down()

    def _goto(self, x, y):
        'goto，计算中心点'
        self.t.goto(self.x + x, self.y + y)

if __name__ == "__main__":
    from turtle import *
    from Helper import TurtleHelper
    th = TurtleHelper()
    bgpic('img/nurse.gif')
    d = Nurse(Turtle(), th, 0, 0)
    d.draw()
    update()
    th.Run('GetPos')

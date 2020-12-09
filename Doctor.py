# coding:utf-8
'''
turtle画医生
'''
class Doctor(object):
    '医生（男，拿注射器）'

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
        self.t.pensize(4)
        self.t.pencolor(self._get_color('pen'))
    
    def _get_color(self, sname):
        '获取颜色值'
        if sname == 'pen':
            return 'black' if not self.th.Debug() else 'red'
        elif sname == 'skin':       #皮肤
            return '#f4dcc4'
        elif sname == 'eyes':       #眼睛
            return 'black'
        elif sname == 'hair':       #头发
            return '#846444'
        elif sname == 'kouzhao':    #口罩
            return '#84d4fc'
        elif sname == 'zhentou':    #针头
            return '#bbbbbb'
        elif sname == 'zhenguan':   #针管
            return '#bce4fc'
        elif sname == 'kdx':        #刻度线
            return '#0493df'
        elif sname == 'tuizi':      #推子
            return '#7ec8f5'
        else:
            return 'white'

    def draw(self):
        self.penset()
        # 面部
        self.t.fillcolor(self._get_color('skin'))
        self.t.begin_fill()
        self._right_face()
        self._neck()
        self._left_face()
        self._hair_below_sp()
        self.t.end_fill()
        # 五官、头发、口罩
        self._left_ear()
        self._right_ear()
        self._left_eye()
        self._right_eye()
        self._hair()
        self._kouzhao()
        # 注射器、手、衣服
        self._zhusheqi()
        self._hand_left()
        self._hand_right()
        self._yifu_left()
        self._yifu_linzi()
        self._yifu_right()
        self._yifu_kd_kz()
        #完成
        self.t.ht()

    def _right_face(self):
        '右脸'
        self._goto_up(71, 39)     # (71, 39)
        self.t.seth(60)
        self.th.DrawCurve(self.t, 1.5, 20, -0.012, 5)
        self.t.rt(30)
        self.th.DrawCurve(self.t, 2.3, 20, 0.04, 6)
        self.t.seth(-118)
        self.t.circle(-70, 42)  # (31, -22)
        self.t.seth(-96)
        self.t.fd(12)           # (29, -32)

    def _neck(self):
        '脖子，不画出'
        self.t.up()
        self._goto(18, -51)
        self._goto(8, -63)
        self._goto(9, -45)
        self._goto(3, -36)

    def _left_face(self):
        '左脸'
        self._goto(2, -37)        # (2, -37)
        self.t.down()
        self.t.seth(75)
        self.t.fd(9)              # (2, -28)
        self.t.seth(172)
        self.t.circle(-90,10)
        self.t.circle(-50,90)       # (-44, 42)
        self.t.seth(96)
        self.t.circle(-180, 18)      # (-42, 93)

    def _hair_below_sp(self):
        '头发下沿，轮廓'
        self.t.up()
        self._goto(-33, 115)
        self._goto(12, 128)
        self._goto(48, 128)
        self._goto(65, 121)
        self._goto(75, 87)
        self._goto(77, 62)
        self._goto(71, 39)

    def _left_ear(self):
        '左耳'
        #左耳
        self._goto_up(-43, 41)    # (-43, 41)
        self.t.seth(160)
        self.t.fillcolor(self._get_color('skin'))
        self.t.begin_fill()
        self.th.DrawCurve(self.t, 0.5, 36, 0.02, -5)
        self._goto(-43, 41)
        self.t.end_fill()

    def _right_ear(self):
        '右耳'
        self._goto_up(83, 38)     # (83, 38)
        self.t.seth(190)
        self.th.DrawCurve(self.t, 3, 10, -0.015, -10)
        self.t.lt(60)
        self.th.DrawCurve(self.t, 1.5, 16, -0.05, -15)

    def _left_eye(self):
        #左眼
        self._goto_up(-23, 82)    # (-23, 82)
        self.t.seth(150)
        self.t.circle(10,92)    # (-36, 75)

        self._goto_up(-18, 49)    # (-18, 49)
        self.t.seth(124)
        self.th.DrawCurve(self.t, 2.4, 20, -0.1, -8)
        #眼珠
        self._goto_up(-32, 44)    # (-32, 44)
        self.t.seth(-85)
        self.t.fillcolor(self._get_color('eyes'))
        self.t.begin_fill()
        self.th.DrawEllipse(self.t, 0.5, 0.01, 3)
        self.t.end_fill()
        self._goto_up(-25, 43)    # (-25, 43)
        self.t.dot(6, "white")

    def _right_eye(self):
        '右眼'
        self._goto_up(15, 89)      # (15, 89)
        self.t.seth(18)
        self.t.circle(-20,80)    # (35, 84)
        self._goto_up(14, 55)      # (14, 55)
        self.t.seth(75)
        self.t.circle(-14,140)   # (43, 53)
        self._goto_up(23, 48)      # (23, 48)
        self.t.dot(20, "black")
        self.t.dot(5, "white")

    def _hair(self):
        '头发'
        '右上'
        self._goto_up(67, 135)     # (67, 135)
        self.t.seth(5)
        self.t.fillcolor(self._get_color('hair'))
        self.t.begin_fill()
        self.t.circle(-30,60)    # (94, 125)
        self._goto(88, 119)
        self._goto(88, 119)
        self._goto(95, 114)
        self._goto(92, 112)
        self._goto(97, 105)
        self._goto(92, 100)
        self._goto(99, 91)
        self._goto(95, 89)
        self._goto(94, 72)
        self._goto(88, 51)
        '左上'
        self._goto_up(67, 135)     # (67, 135)
        self.t.seth(110)
        self.t.circle(35,60)    # (33, 159)
        self._goto(32, 159)
        self._goto(34, 154)
        self._goto(21, 159)
        self._goto(15, 159)
        self._goto(14, 154)
        self._goto(1, 155)
        self._goto(-10, 152)
        self._goto(-5, 151)
        self._goto(-15, 149)
        self._goto(-28, 142)
        self._goto(-22, 140)
        self._goto(-32, 136)
        self._goto(-40, 133)
        self._goto(-45, 129)
        self._goto(-40, 128)
        self._goto(-46, 121)
        self._goto(-53, 111)
        self._goto(-50, 111)
        self._goto(-54, 99)
        self._goto(-46, 97)
        '头发下沿'
        self._goto(-44, 96)
        self._goto(-38, 99)
        self._goto(-29, 103)
        self._goto(-28, 100)
        self._goto(-15, 110)
        self._goto(-11, 105)
        self._goto(9, 118)
        self._goto(13, 115)
        self._goto(24, 118)
        self._goto(29, 114)
        self._goto(40, 117)
        self._goto(41, 112)
        self._goto(54, 118)
        self._goto(56, 107)
        self._goto(59, 108)
        self._goto(61, 94)
        self._goto(66, 94)
        self._goto(64, 77)
        self._goto(67, 78)
        self._goto(66, 64)
        self._goto(67, 60)
        self._goto(70, 63)
        self._goto(69, 52)
        self._goto(71, 39)     # (71, 39)
        self.t.seth(60)
        self.th.DrawCurve(self.t, 1.5, 13, -0.012, 5)
        self._goto(88, 51)
        self.t.end_fill()

    def _kouzhao(self):
        '口罩'
        self._goto_up(47, 32)   # (47, 32)
        self.t.seth(172)
        self.t.fillcolor(self._get_color('kouzhao'))
        self.t.begin_fill()
        self.t.circle(300,18)   # (-46, 31)
        self.t.seth(-92)
        self.t.circle(90,20)
        self.t.lt(30)
        self.t.circle(80,30)
        self.t.lt(11)
        self.t.circle(120,26)   # (45, -6)
        self.t.seth(90)
        self.t.fd(39)           # (46, 33)
        self.t.end_fill()
        self.t.seth(22)
        self.t.fd(28)           # (74, 45)
        self._goto_up(47, -5)   # (47, -5)
        self.t.seth(24)
        self.t.fd(19)           # (64, 6)

    def _yifu_linzi(self):
        '领子'
        #领子1
        self._goto_up(31, -28)
        self._goto(53, -37)
        self._goto(31, -53)
        self._goto(40, -59)
        self._goto(8, -112)
        self._goto(6, -81)
        self._goto(11, -61)
        self._goto(30, -34)
        self._goto(30, -27)
        #领子2
        self._goto_up(9, -62)
        self._goto(8, -64)
        self._goto(7, -47)
        self._goto(1, -36)
        self._goto(1, -29)
        self._goto(-17, -35)
        self._goto(-6, -47)
        self._goto(-13, -56)
        self._goto(-1, -84)
        self._goto(7, -113)
        self._goto(4, -134)

    def _zhusheqi(self):
        '注射器'
        #针头
        self._goto_up(-120, 90)
        self.t.fillcolor(self._get_color('zhentou'))
        self.t.begin_fill()
        self._goto(-102, 34)
        self._goto(-93, 39)
        self._goto(-112, 85)
        self._goto(-120, 90)
        self.t.end_fill()
        #针管
        self._goto_up(-119, 18)
        self.t.fillcolor(self._get_color('zhenguan'))
        self.t.begin_fill()
        self._goto(-70, -106)
        self._goto(-22, -87)
        self._goto(-69, 39)
        self.t.seth(175)
        self.t.circle(60,52)
        self.t.end_fill()
        #刻度线
        self.t.pencolor(self._get_color('kdx'))
        self._goto_up(-112, 9)
        self._goto(-105, 12)
        self._goto_up(-108, -3)
        self._goto(-101, 0)
        self._goto_up(-104, -14)
        self._goto(-97, -10)
        self._goto_up(-101, -26)
        self._goto(-94, -24)
        self._goto_up(-95, -39)
        self._goto(-88, -36)
        self._goto_up(-91, -51)
        self._goto(-83, -49)
        self._goto_up(-88, -59)
        self._goto(-80, -56)
        self._goto_up(-83, -67)
        self._goto(-78, -66)
        self._goto_up(-78, -83)
        self._goto(-69, -80)
        self._goto_up(-73, -91)
        self._goto(-68, -89)
        self._goto_up(-70, -99)
        self._goto(-65, -99)
        self.t.pencolor(self._get_color('pen'))
        #推子
        self._goto_up(-50, -101)
        self.t.fillcolor(self._get_color('tuizi'))
        self.t.begin_fill()
        self._goto(-45, -117)
        self._goto(-62, -129)
        self._goto(-53, -140)
        self._goto(-12, -119)
        self._goto(-17, -107)
        self._goto(-33, -113)
        self._goto(-40, -97)
        self._goto(-49, -102)
        self.t.end_fill()

    def _hand_left(self):
        '左手'
        self._goto_up(-99, -67)
        self.t.seth(110)
        self.t.fillcolor(self._get_color('skin'))
        self.t.begin_fill()
        self.t.circle(-60,10)
        self.t.rt(20)
        self.t.circle(-50,20)
        self._goto(-89, -37)
        self._goto(-84, -42)
        self._goto(-94, -53)
        self._goto(-84, -46)
        self._goto(-79, -50)
        self._goto(-87, -61)
        self._goto(-80, -56)
        self._goto(-75, -59)
        self._goto(-83, -68)
        self._goto(-77, -65)
        self._goto(-74, -71)
        self._goto(-82, -80)
        self._goto(-89, -80)
        self._goto(-99, -67)
        self.t.end_fill()

        self.t.seth(-72)
        self.t.circle(60,36)

        self._goto_up(-60, -106)
        self.t.seth(-30)
        self.t.circle(60,15)

    def _hand_right(self):
        '右手'
        self._goto_up(-14, -146)
        self.t.fillcolor(self._get_color('skin'))
        self.t.begin_fill()
        self._goto(-14, -147)
        self._goto(-19, -150)
        self._goto(-24, -149)
        self._goto(-33, -156)
        self._goto(-45, -151)
        self._goto(-50, -139)
        self._goto(-49, -135)
        self._goto(-41, -142)
        self._goto(-44, -132)
        self._goto(-41, -126)
        self._goto(-37, -128)
        self._goto(-32, -138)
        self._goto(-36, -126)
        self._goto(-33, -119)
        self._goto(-30, -120)
        self._goto(-24, -137)
        self._goto(-29, -121)
        self._goto(-28, -118)
        self._goto(-22, -118)
        self._goto(-16, -124)
        self._goto(-8, -139)
        self._goto(0, -146)
        self._goto(-8, -165)
        self._goto(-26, -174)
        self._goto(-27, -168)
        self._goto(-25, -163)
        self._goto(-30, -157)
        self._goto(-17, -165)
        self.t.end_fill()

    def _yifu_left(self):
        '衣服-左边'
        self._goto_up(-15, -42)
        self._goto(-31, -61)
        self._goto_up(-26, -92)
        self._goto(-30, -108)
        self._goto_up(-36, -157)
        self._goto(-37, -210)

    def _yifu_right(self):
        '衣服'
        self._goto_up(53, -39)
        self.t.seth(-35)
        self.t.circle(-100, 60)
        self.t.rt(4)
        self.t.circle(-90, 75)
        self.t.rt(10)
        self.t.circle(-45, 60)
        #右下一笔
        self._goto_up(88, -157)
        self._goto(88, -217)
        #袖口
        self._goto_up(-25, -174)
        self._goto(-17, -182)
        self.t.seth(-8)
        self.t.circle(24,160)
        self.t.seth(6)
        self.t.circle(-50,60)
        self._goto_up(48, -103)
        self._goto(34, -144)

    def _yifu_kd_kz(self):
        '口袋'
        self._goto_up(20, -101)
        self._goto(41, -103)
        self._goto(37, -128)
        self._goto(30, -130)
        self._goto(21, -129)
        self._goto(20, -103)
        self._goto(20, -106)
        self._goto(29, -113)
        self._goto(40, -106)
        #扣子
        self._goto_up(9, -123)
        self.t.seth(-90)
        self.th.DrawEllipse(self.t, 0.36, 0.01, 3)

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
    # bgpic('img/doctor.gif')
    d = Doctor(Turtle(), th, 0, 0)
    d.draw()
    update()
    th.Run('GetPos')
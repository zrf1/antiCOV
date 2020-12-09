# coding:utf-8
from turtle import *
from time import sleep
from importlib import reload

class TurtleHelper(object):
    '辅助类，放置公共变量和函数'

    def __init__(self, _debug=False, _sleep=1):
        '初始化'
        self._debug = _debug
        self._sleep = _sleep
        screensize(800, 600, "#f0f0f0")
        if(self._debug):
            setup(startx=-1, starty=0)
            tracer(False)
            # bgpic('img/doctor.gif')
            # bgpic('img/nurse.gif')

    def Debug(self, *debug_tuple):
        '设置是否调试'
        if(len(debug_tuple) == 1):
            self._debug = debug_tuple[0]
        return self._debug

    def Run(self, mode=''):
        '运行'
        if(mode.lower() == 'getpos'):
            # 调试用，从背景找坐标点
            onscreenclick(lambda x, y: print("(%d, %d)" % (x,y)))
            title('GetPos')
            mainloop()
        elif(mode.lower() == 'repeat'):
            '重复画'
            title('Repeat')
            sleep(self._sleep)
        else:
            mainloop()

    def DrawCurve(self, t, distance, count, step_distance, step_angle_right):
        '''
        画曲线（画笔/海龟，数量，每步变化，变化角度）
        步长可正负，角度可正负
        '''
        tracer(False)
        d = distance
        for i in range(1, count):
            d += step_distance
            t.rt(step_angle_right)
            t.fd(d)
        tracer(not self._debug)

    def DrawEllipse(self, t, distance, det_distance, angle):
        '''
        画椭圆（画笔/海龟，距离，变长，角度）
        '''
        tracer(False)
        d = distance
        for i in range(120):
            if 0 <= i < 30 or 60 <= i < 90:
                d -= det_distance
                t.lt(angle)
                t.fd(d)
            else:
                d += det_distance
                t.lt(angle)
                t.fd(d)
        tracer(not self._debug)

if __name__ == "__main__":
    t = Turtle()
    th = TurtleHelper(_debug=True)

    # import Doctor
    import Nurse
    while True:
        #print('draw %d times.' % i)
        # reload(Doctor)
        reload(Nurse)
        n = Nurse.Nurse(t, th, 0, 0)
        t.reset()
        n.draw()
        update()
        th.Run('Repeat')
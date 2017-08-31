#!/usr/bin/env python
from Point import Point
from BaseSpline import BaseSpline


class QuadraticBezier(BaseSpline):
    def __init__(self, controlPoints=None):
        super(QuadraticBezier, self).__init__(controlPoints)
        self.p0 = 0
        self.p1 = 0
        self.p2 = 0

    def __str__(self):
        return 'p0 = %s, p1= %s, p2= %s' %(self.p0, self.p1, self.p2)

    def compute(self, p0, p1 , p2):
        '''from bernstein definition on The Morgan Kaufmann Series in Computer Graphics Curves and Surfaces ch5 '''
        self.controlPoints = []
        self.points = []
        self.p0 = p0
        self.p1 = p1
        self.p2 = p2
        self.controlPoints.append(self.p0)
        self.controlPoints.append(self.p1)
        self.controlPoints.append(self.p2)
        t = 0.0
        while t <= 1:
            t2 = t * t
            oneMinusT = (1.0 - t)
            ptx = oneMinusT * oneMinusT * p0.x + 2 * oneMinusT * t * p1.x + t2 * p2.x
            pty = oneMinusT * oneMinusT * p0.y + 2 * oneMinusT * t * p1.y + t2 * p2.y
            ptz = oneMinusT * oneMinusT * p0.z + 2 * oneMinusT * t * p1.z + t2 * p2.z
            point = Point(ptx, pty, ptz)
            self.points.append(point)
            t += 0.1

from PyQt5.QtGui import QVector3D, QVector4D, QMatrix4x4


class QuadraticBezierSpline(BaseSpline):
    def __init__(self, controlPoints=None):
        super(QuadraticBezierSpline, self).__init__(controlPoints)

    def __str__(self):
        return 'p0 = %s, p1= %s, p2= %s' %(self.p0, self.p1, self.p2)

    def compute(self):
        '''from bernstein definition on The Morgan Kaufmann Series in Computer Graphics Curves and Surfaces ch5 '''
        t = 0.0
        while t <= 1:
            point = QuadraticBezierSpline.computePoint(p0=self.controlPoints[0], p1=self.controlPoints[1], p2=self.controlPoints[2], t=t)
            self.points.append(point)
            t += 0.1

    @staticmethod
    def computePoint(p0, p1, p2, t):
        M = QMatrix4x4( 1,  0, 0, 0,
                       -2,  2, 0, 0,
                        1, -2, 1, 0,
                        0,  0, 0, 0)
        P = QMatrix4x4(p0.x(), p0.y(), p0.z(), 0,
                       p1.x(), p1.y(), p1.z(), 0,
                       p2.x(), p2.y(), p2.z(), 0,
                       0, 0, 0, 0)
        vecT = QVector4D(1.0, t, t*t, 0)
        point = vecT * M * P
        return QVector3D(point.x(), point.y(), point.z())


if __name__ == '__main__':
    quadraticBezier = QuadraticBezier()
    quadraticBezier.compute(Point(0, 0, 0), Point(2.5, 5, 0), Point(5, 0, 0))
    for vec in quadraticBezier.controlPoints:
        print(vec.x, ',', vec.y, )
    print("points")
    for vec in quadraticBezier.points:
        print(vec.x, ',', vec.y, )

    print("Using Matrices")
    quadraticBezierSpline = QuadraticBezierSpline([QVector3D(0, 0, 0), QVector3D(2.5, 5, 0), QVector3D(5, 0, 0)])
    quadraticBezierSpline.compute()
    for vec in quadraticBezierSpline.controlPoints:
        print(vec.x(), ',', vec.y(), )
    print("points")
    for vec in quadraticBezierSpline.points:
        print(vec.x(), ',', vec.y(), )


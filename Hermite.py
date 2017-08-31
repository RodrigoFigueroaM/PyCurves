#!/usr/bin/env python
from Point import Point
from BaseSpline import BaseSpline


class HermiteCurve(BaseSpline):
    def __init__(self, *argv):
        '''
        HermiteCurve needs 2 points(p0, p1) and 2 tangents(m0, m1) in order to be plotted.
        '''
        super(HermiteCurve, self).__init__()
        if len(argv) == 4:
            self.p0, self.m0, self.p1, self.m1 = argv
        else:
            self.p0 = 0
            self.m0 = 0
            self.p1 = 0
            self.m1 = 0
        self.points = []

    def __str__(self):
        return 'p0 = %s,m0 = %s, p1 = %s, m1 = %s' %(self.p0 ,self.m0, self.p1, self.m1)

    def compute(self):
        '''
        Curve is always computed fron the origin
        p(t) = (2t^3 - 3t^2 + 1)p0 + (t^3 - 2t^2 + t)m0 + ( -2t^3 + 3t^2)p1 + (t^3 - t^2)m1
        '''
        # m0, m1 tangents at p0 and p1 respectively
        print(self.p0.y)
        self.points = []
        t = 0.0
        while t < 1.0:
            t3 = t * t * t
            t2 = t * t
            pty = (2 * t3 - 3 * t2 + 1) * self.p0.y + (t3 - 2 * t2 + t) * self.m0 + (-2 * t3 + 3 * t2) * self.p1.y + (t3 - t2) * self.m1
            point = Point(t, pty, 1)
            self.points.append(point.data())
            t += 0.1

from PyQt5.QtGui import QVector4D, QMatrix4x4, QVector3D
from BaseSpline import BaseSpline

class HermiteSpline(BaseSpline):
    def __init__(self, p0, m0, p1, m1):
        """Given : Points P0, P1 Tangent vectors m0, m1 """
        super(HermiteSpline, self).__init__()
        self.points = []
        self.p0 = p0
        self.m0 = m0
        self.p1 = p1
        self.m1 = m1

    def compute(self):
        """
        Compute spline  using control points and tangents.
        """
        t = 0.0
        while t <= 1:
            point = HermiteSpline.computePoint(self.p0, self.m0, self.p1, self.m1, t)
            self.points.append(point)
            t += 0.1

    @staticmethod
    def computePoint(p0, m0, p1, m1, t):
        """
           Given four Points P0, P1 Tangent vectors m0, m1, calculate a point on spline at time t.
           :param p0: QVector3D
           :param m0: QVector3D
           :param p1: QVector3D
           :param m1: QVector3D
           :param t: float
           :return: QVector3D; p(t) a point at time t
        """

        M = QMatrix4x4(  2, -3,  0,  1,
                        -2,  3,  0,  0,
                         1, -2,  1,  0,
                         1, -1,  0,  0)
        P = QMatrix4x4(p0.x(), p0.y(), p0.z(), 0,
                       p1.x(), p1.y(), p1.z(), 0,
                       m0.x(), m0.y(), m0.z(), 0,
                       m1.x(), m1.y(), m1.z(), 0)
        vecT = QVector4D( t*t*t, t*t, t, 0)
        point = M * P * vecT
        return QVector3D(point.x(), point.y(), point.z())


if __name__ == "__main__":
    points = [Point(0, 0, 0), 2, Point(1, 1, 0), 3]
    hermite = HermiteCurve(points[0], points[1], points[2], points[3])
    hermite.compute()
    for point in hermite.points:
        print(point)

    print("Using Matrices")
    hermiteSpline = HermiteSpline(QVector3D(0, 0, 0), QVector3D(0, 1, 0), QVector3D(1, 1, 0), QVector3D(1, 0, 0))
    hermiteSpline.compute()
    for point in hermiteSpline.points:
        print(point)
#!/usr/bin/env python

from Point import Point
class CatmullRom:
    def __init__(self):
        super(CatmullRom,self).__init__()
        self.points = []
        self.userDefinedPoints=[]

    def compute(self, userDefinedPoints):
        self.points = [] #make sure our points to be ploted is empty
        self.userDefinedPoints = userDefinedPoints
        #we need at least 4 points to define a Catmull-Rom Spline
        if len(userDefinedPoints) >= 4:
            i = 0
            while  i < len(userDefinedPoints) - 3 :
                self.__computeCurve(userDefinedPoints[i], userDefinedPoints[i+1], userDefinedPoints[i+2],userDefinedPoints[i+3])
                i += 1
        else:
            print('at least 4 points need to be provided ')

    def __computeCurve(self, p0, p1, p2, p3):
        '''q(t) = 0.5 *( (2 * P1) + (-P0 + P2) * t + (2*P0 - 5*P1 + 4*P2 - P3) * t2 +(-P0 + 3*P1- 3*P2 + P3) * t3)'''
        # HermiteCurve function where: mn = (pn+1 - pn-1)/(tn+1 - tn-1))
        t = 0.0
        while t <= 1:
            t3 = t * t * t
            t2 = t * t
            ptx = 0.5 * ( (2 * p1.x) + (-1 * p0.x + p2.x) * t + (2 * p0.x - 5 * p1.x + 4 * p2.x - p3.x) * t2 + ( -1 * p0.x + 3 * p1.x - 3 * p2.x + p3.x )* t3 )
            pty = 0.5 * ( (2 * p1.y) + (-1 * p0.y + p2.y) * t + (2 * p0.y - 5 * p1.y + 4 * p2.y - p3.y) * t2 + ( -1 * p0.y + 3 * p1.y - 3 * p2.y + p3.y )* t3 )
            ptz = 0.5 * ( (2 * p1.z) + (-1 * p0.z + p2.z) * t + (2 * p0.z - 5 * p1.z + 4 * p2.z - p3.z) * t2 + ( -1 * p0.z + 3 * p1.z - 3 * p2.z + p3.z )* t3 )
            point = Point(ptx, pty, ptz)
            self.points.append( point)
            t += 0.1

from PyQt5.QtGui import QVector3D, QVector4D, QMatrix4x4


class CatmullRomSpline:
    """
    A CatmullRom spline implementation dependant on PyQt's
    QVector3D, QVector4D, QMatrix4x4
    """
    def __init__(self, controlPoints=None):
        """
        A curve is a collection of points.
        A curve can be computed with given control points
        :param controlPoints: if specified, control points is a list of QVector3D
        """
        self.controlPoints = []
        if controlPoints:
            self.controlPoints = controlPoints[:]
        self.points = []

    def compute(self, controlPoints=None):
        """
        Used to compute spline.
        If controlPoints are given they will take over the spline control points
        otherwise, use the old specified control points
        :param controlPoints: if specified, control points is a list of QVector3D
        """
        self.points = []
        if controlPoints:
            self.controlPoints = controlPoints[:]
        if len(self.controlPoints) >= 4:
            for i in range(0, len(self.controlPoints) - 3):
                self._computeSpline(self.controlPoints[i], self.controlPoints[i+1], self.controlPoints[i+2], self.controlPoints[i+3])
        else:
            print('at least 4 points need to be provided ')

    def _computeSpline(self, p0, p1, p2, p3):
        """
        Compute spline values given 4 control points.
        Store the computed points on spline points for later access
        :param p0: QVector3D
        :param p1: QVector3D
        :param p2: QVector3D
        :param p3: QVector3D
        """
        t = 0.0
        while t <= 1:
            point = CatmullRomSpline.computePoint(p0, p1, p2, p3, t)
            self.points.append(point)
            t += 0.1

    @staticmethod
    def computePoint(p0, p1, p2, p3, t):
        """
        Given four control points, calculate a point on spline at time t.
        :param p0: QVector3D
        :param p1: QVector3D
        :param p2: QVector3D
        :param p3: QVector3D
        :param t: float
        :return: QVector3D; p(t) a point at time t
        """
        M = QMatrix4x4( 0,  2,  0,  0,
                       -1,  0,  1,  0,
                        2, -5,  4, -1,
                       -1,  3, -3,  1)
        P = QMatrix4x4(p0.x(), p0.y(), p0.z(), 0,
                       p1.x(), p1.y(), p1.z(), 0,
                       p2.x(), p2.y(), p2.z(), 0,
                       p3.x(), p3.y(), p3.z(), 0)
        point = 0.5 * QVector4D(1.0, t, t*t, t*t*t) * M * P
        return QVector3D(point.x(), point.y(), point.z())


if __name__ == "__main__":
    print("---------------------- OLD CATMULL ----------------------")
    spline = CatmullRom()
    spline.compute([Point(0, 0, 0), Point(0, 1, 0), Point(1, 1, 0), Point(1, 0, 0)])
    for point in spline.points:
        print(point)

    print("---------------------- NEW CATMULL ----------------------")
    vectorSpline = CatmullRomSpline([QVector3D(0, 0, 0), QVector3D(0, 1, 0), QVector3D(1, 1, 0), QVector3D(1, 0, 0)])
    vectorSpline.compute()
    for point in vectorSpline.points:
        print(point)


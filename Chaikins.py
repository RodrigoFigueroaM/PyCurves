#!/usr/bin/env python
from PyQt5.QtGui import QVector3D


class Chaikins:
    def __init__(self, controlPoints= None, dept=1):
        """
        A curve is a collection of points.
        A curve can be computed with given control points
        :param controlPoints: if specified, control points is a list of QVector3D
        """
        self.controlPoints = []
        if controlPoints:
            self.controlPoints = controlPoints[:]
        self.dept = dept
        self._points = []

    def compute(self, controlPoints=None, dept=None):
        """
        Used to compute spline.
        If controlPoints are given they will take over the spline control points
        otherwise, use the old specified control points
        :param controlPoints: if specified, control points is a list of QVector3D
        """
        self._points = []
        if controlPoints:
            self.controlPoints = controlPoints[:]
        if dept:
            self.dept = dept
        tempContolPoints = self.controlPoints[:]
        for n in range(0, self.dept):
            self._points = []
            for i in range(0, len(tempContolPoints) - 1):
                q , r = Chaikins.chaikinsAlg(tempContolPoints[i], tempContolPoints[i + 1])
                self._points.append(q)
                self._points.append(r)
            tempContolPoints = self._points[:]

    @staticmethod
    def chaikinsAlg(p0, p1):
        """ Chainkin's Algorithm to compute subdivision on a given line defined by p0, p1
            using 1/4, 3/4 method
        :param p0: QVector3D initial point in line
        :param p1: QVector3D finlan point in line
        :return: QVector3D q, r point in line at 1/4, 3/4 respectively
        """
        q = 3 / 4 * p0 + 1 / 4 * p1
        r = 1 / 4 * p0 + 3 / 4 * p1
        return q, r

    @property
    def points(self):
        return self._points


if __name__ == "__main__":
    spline = Chaikins([QVector3D(0,0,0), QVector3D(0,2,0), QVector3D(2,2,0), QVector3D(3,-1,0),QVector3D(6,3,0)],4)
    spline.compute()
    print("controlPoints")
    for vec in spline.controlPoints:
        print(vec.x(), ',', vec.y(), )
    print("points")
    for vec in spline.points:
        print( vec.x(), ',', vec.y(), )






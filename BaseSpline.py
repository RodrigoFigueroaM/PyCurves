#!/usr/bin/env python
import abc

class BaseSpline(abc.ABC):
    """
    A spline base class for implementation of other splines dependant on PyQt's
    QVector3D, QVector4D, QMatrix4x4
    """

    def __init__(self, controlPoints=None):
        self.controlPoints = []
        if controlPoints:
            self.controlPoints = controlPoints[:]
        self.points = []

    @abc.abstractmethod
    def compute(self):
        """
        Used to compute spline.
        """
        pass


class Test:
    def __init__(self):
        pass

"""Module to define the geometric object to approximate the shape."""

import numpy
from shapely.geometry import LineString
from shapely.geometry import Polygon


class GeometryObject:
    """Abstract geometry object class."""

    def __init__(self, status):
        self.status = status 
        self.name = status["name"]

    def Distance(self, other):
        pass


class Circle(GeometryObject):
    """Implement the circle object."""

    def __init__(self, status):
        GeometryObject.__init__(self, status)
        self.center = numpy.array(self.status["center"], dtype='float')
        self.radius = abs(self.status["radius"])
        
    def Distance(self, circle_other):
        diff_dist = numpy.linalg.norm(self.center - circle_other.center)
        if diff_dist < (self.radius + circle_other.radius):
            return 0
        return diff_dist - (self.radius + circle_other.radius)


class Rectangular(GeometryObject):
    """Implement the Rectangular object."""

    def __init__(self, status):
        GeometryObject.__init__(self, status)
        self.center = numpy.array(self.status["center"], dtype='float')
        self.axis_one = self.status["axis_one"]
        self.axis_two = self.status["axis_two"]
        self.angle = self.status["angle"]
        self._BuildCorners()
        self._BuildPolygon()


    def _BuildCorners(self):
        """Calculate the corner points for rectangular."""

        self.corners = []
        theta = (self.angle * numpy.pi / 180)
        rotation_matrix = numpy.array([[numpy.cos(theta), -1*numpy.sin(theta)], 
                                       [numpy.sin(theta), numpy.cos(theta)]])

        for shift_one, shift_two in [(1, 1), (1, -1), (-1, -1), (-1, 1)]:
            diff_one = 0.5 * shift_one * rotation_matrix.dot(numpy.array([self.axis_one, 0]))
            diff_two = 0.5 * shift_two * rotation_matrix.dot(numpy.array([0, self.axis_two]))
            pt = self.center + diff_one + diff_two
            self.corners.append(pt)


    def _BuildPolygon(self):
        """Defines the shapely.Polygon by corners."""
        tmp_pts = list(self.corners)
        tmp_pts.append(self.corners[0])
        self.polygon = Polygon(tmp_pts)

    def Distance(self, other_rect):
        return self.polygon.distance(other_rect.polygon)



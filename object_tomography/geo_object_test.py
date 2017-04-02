import geo_object
import unittest
import numpy


class TestCircle(unittest.TestCase):

    def testDistance(self):
        circle_a = geo_object.Circle({"center": (0, 0), "radius": 2, "name": "circ_1"})
        circle_b = geo_object.Circle({"center": (5, 0), "radius": 1, "name": "circ_2"})

        self.assertAlmostEqual(circle_a.Distance(circle_b), 2.0)


class TestRectangle(unittest.TestCase):
    def testDistance(self):
        rect_a = geo_object.Rectangular({"center": (0, 0), "axis_one": 2, "axis_two": 2,
                                        "angle": 45, "name": "rect_1"})
        rect_b = geo_object.Rectangular({"center": (5, 5), "axis_one": 3, "axis_two": 3,
                                        "angle": 0, "name": "rect_2"})

        self.assertAlmostEqual(rect_b.Distance(rect_a), numpy.sqrt(2) * (3.5 - numpy.sqrt(2)/2))


if __name__ == '__main__':
    unittest.main()
import unittest
from Project1 import *

class TestArea(unittest.TestCase):
    def test_calcArea(self):
        self.assertEqual(calcArea(-2, -2), 4)
        self.assertEqual(calcArea(-2, 2), -4)
        self.assertEqual(calcArea(2, -2), -4)

        self.assertEqual(calcArea(0, 0), 0)
        self.assertEqual(calcArea(0, 2), 0)
        self.assertEqual(calcArea(2, 0), 0)

        self.assertAlmostEqual(calcArea(2.0, 2.0), 4.0, delta=0.001)
        self.assertAlmostEqual(calcArea(2.0, 2), 4.0, delta=0.001)
        self.assertAlmostEqual(calcArea(2, 2.0), 4.0, delta=0.001)
        self.assertEqual(calcArea(2, 2), 4.0)

    def test_calcPerimeter(self):
        self.assertEqual(calcPerimeter(-2, -2), -8)
        self.assertEqual(calcPerimeter(-2, 2), 0)
        self.assertEqual(calcPerimeter(2, -2), 0)

        self.assertEqual(calcPerimeter(0, 0), 0)
        self.assertEqual(calcPerimeter(0, 2), 4)
        self.assertEqual(calcPerimeter(2, 0), 4)

        self.assertAlmostEqual(calcPerimeter(2.0, 2.0), 8.0, delta=0.001)
        self.assertAlmostEqual(calcPerimeter(2.0, 2), 8.0, delta=0.001)
        self.assertAlmostEqual(calcPerimeter(2, 2.0), 8.0, delta=0.001)
        self.assertEqual(calcPerimeter(2, 2), 8.0)

    def test_calcRadius(self):
        self.assertEqual(calcRadius(1), '3.14')
        self.assertEqual(calcRadius(-1), '3.14')
        self.assertEqual(calcRadius(1), '3.14')
        self.assertEqual(calcRadius(2), '12.57')
        self.assertEqual(calcRadius(0), '0.00')

    def test_calcTriangle(self):
        self.assertEqual(calcTriangle(-2, -2), 2.0)
        self.assertEqual(calcTriangle(-2, 2), -2.0)
        self.assertEqual(calcTriangle(2, -2), -2.0)

        self.assertEqual(calcTriangle(0, 0), 0.0)
        self.assertEqual(calcTriangle(0, 2), 0.0)
        self.assertEqual(calcTriangle(2, 0), 0.0)

        self.assertAlmostEqual(calcTriangle(2.0, 2.0), 2.0, delta=0.001)
        self.assertAlmostEqual(calcTriangle(2.0, 2), 2.0, delta=0.001)
        self.assertAlmostEqual(calcTriangle(2, 2.0), 2.0, delta=0.001)
        self.assertEqual(calcTriangle(2, 2), 2.0)

    def test_calcCircleP(self):
        self.assertEqual(calcCircleP(1), '6.28')
        self.assertEqual(calcCircleP(-1), '-6.28')
        self.assertEqual(calcCircleP(2), '12.57')
        self.assertEqual(calcCircleP(0), '0.00')

    def test_calcTriangleP(self):
        self.assertEqual(calcTriangleP(-2, -2, -2), -6)
        self.assertEqual(calcTriangleP(-2, 2, 2), 2)
        self.assertEqual(calcTriangleP(2, -2, 2), 2)
        self.assertEqual(calcTriangleP(2, 2, -2), 2)

        self.assertEqual(calcTriangleP(0, 0, 0), 0)
        self.assertEqual(calcTriangleP(0, 2, 0), 2)
        self.assertEqual(calcTriangleP(2, 0, 0), 2)
        self.assertEqual(calcTriangleP(2, 0, 2), 4)

        self.assertAlmostEqual(calcTriangleP(2.0, 2.0, 2.0), 6.0, delta=0.001)
        self.assertAlmostEqual(calcTriangleP(2.0, 2, 2), 6.0, delta=0.001)
        self.assertAlmostEqual(calcTriangleP(2, 2.0, 2), 6.0, delta=0.001)
        self.assertAlmostEqual(calcTriangleP(2, 2, 2.0), 6.0, delta=0.001)
        self.assertEqual(calcTriangleP(2, 2, 2), 6.0)

if __name__ == '__main__':
    unittest.main()
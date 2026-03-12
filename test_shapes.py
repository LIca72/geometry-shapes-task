import unittest
from task1 import square, rectangle, circle

class TestShapes(unittest.TestCase):
    def test_square(self):
        parts = ["Square", "TopRight", "1", "1", "Side", "1"]
        name, perimeter, area = square(parts)

        self.assertEqual(perimeter, 4)
        self.assertEqual(area, 1)

    def test_rectangle(self):
        parts = ["Rectangle","TopRight","2","2","BottomLeft","1","1"]
        name, perimeter, area = rectangle(parts)

        self.assertEqual(perimeter, 4)
        self.assertEqual(area, 1)

    def test_circle(self):
        parts = ["Circle","Center","1","1","Radius","2"]
        name, perimeter, area = circle(parts)

        self.assertAlmostEqual(perimeter, 12.566370614359172)
        self.assertAlmostEqual(area, 12.566370614359172)

if __name__ == "__main__":
    unittest.main()

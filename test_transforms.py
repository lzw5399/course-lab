#!/usr/bin/python3

import unittest

from transforms import change_colors, mirror, grayscale


image_black = [[(0, 0, 0), (0, 0, 0), (0, 0, 0)],
               [(0, 0, 0), (0, 0, 0), (0, 0, 0)],
               [(0, 0, 0), (0, 0, 0), (0, 0, 0)]]

image_white = [[(255, 255, 255), (255, 255, 255), (255, 255, 255)],
               [(255, 255, 255), (255, 255, 255), (255, 255, 255)],
               [(255, 255, 255), (255, 255, 255), (255, 255, 255)]]

image_redblue = [[(255, 0, 0), (255, 0, 0), (255, 0, 0)],
                 [(0, 0, 255), (255, 0, 0), (255, 0, 0)],
                 [(0, 0, 255), (0, 0, 255), (255, 0, 0)]]

image_greenblue = [[(0, 255, 0), (0, 255, 0), (0, 255, 0)],
                   [(0, 0, 255), (0, 255, 0), (0, 255, 0)],
                   [(0, 0, 255), (0, 0, 255), (0, 255, 0)]]

image_greenblue_mirror = [[(0, 0, 255), (0, 0, 255), (0, 255, 0)],
                          [(0, 0, 255), (0, 255, 0), (0, 255, 0)],
                          [(0, 255, 0), (0, 255, 0), (0, 255, 0)]]

image_greenblue_gray = [[(85, 85, 85), (85, 85, 85), (85, 85, 85)],
                        [(85, 85, 85), (85, 85, 85), (85, 85, 85)],
                        [(85, 85, 85), (85, 85, 85), (85, 85, 85)]]


class TestChangeColors(unittest.TestCase):

    def test_red_green(self):
        result = change_colors(image_redblue, to_change=(255, 0, 0), to_change_to=(0, 255, 0))
        self.assertEqual(result, image_greenblue)

    def test_black_white(self):
        result = change_colors(image_black, to_change=(0, 0, 0), to_change_to=(255, 255, 255))
        self.assertEqual(result, image_white)


class TestMirror(unittest.TestCase):

    def test_greenblue(self):
        result = mirror(image_greenblue)
        self.assertEqual(result, image_greenblue_mirror)

class TestGray(unittest.TestCase):

    def test_greenblue(self):
        result = grayscale(image_greenblue)
        self.assertEqual(result, image_greenblue_gray)


if __name__ == '__main__':
    unittest.main()


#!/usr/bin/python3
import filecmp
import sys
import unittest

import transform_simple

class TestGrayscale(unittest.TestCase):

    def test_simple(self):

        sys.argv = ['program.py', '../cafe.jpg', 'grayscale']
        transform_simple.main()
        self.assertTrue(filecmp.cmp('cafe_gray.jpg', '../cafe_trans.jpg'),
                        msg="Files are different")

class TestMirror(unittest.TestCase):

    def test_simple(self):

        sys.argv = ['program.py', '../cafe.jpg', 'mirror']
        transform_simple.main()
        self.assertTrue(filecmp.cmp('cafe_mirror.jpg', '../cafe_trans.jpg'),
                        msg="Files are different")


if __name__ == '__main__':
    unittest.main()

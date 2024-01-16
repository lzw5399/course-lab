#!/usr/bin/python3
import filecmp
import sys
import unittest

import transform_args

class TestChangeColors(unittest.TestCase):

    def test_change_colors(self):

        sys.argv = ['program.py', '../captura.jpg', 'change_colors',
                    '255', '255', '255', '0', '255', '0']
        transform_args.main()
        self.assertTrue(filecmp.cmp('captura_change_colors.jpg', '../captura_trans.jpg'),
                        msg="Files are different")

class TestGrayscale(unittest.TestCase):

    def test_simple(self):

        sys.argv = ['program.py', '../cafe.jpg', 'grayscale']
        transform_args.main()
        self.assertTrue(filecmp.cmp('cafe_gray.jpg', '../cafe_trans.jpg'),
                        msg="Files are different")

class TestMirror(unittest.TestCase):

    def test_simple(self):

        sys.argv = ['program.py', '../cafe.jpg', 'mirror']
        transform_args.main()
        self.assertTrue(filecmp.cmp('cafe_mirror.jpg', '../cafe_trans.jpg'),
                        msg="Files are different")


if __name__ == '__main__':
    unittest.main()

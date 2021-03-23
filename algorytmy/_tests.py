from bi import bsearch, bisect
from czynniki_pierwsze import czynniki_pierwsze

import unittest


class TestAlgorithms(unittest.TestCase):

    def test_bsearch(self):
        arr = [0, 2, 4, 6, 9, 69]
        self.assertEqual(bsearch(0, arr), 0)
        self.assertEqual(bsearch(2, arr), 1)
        self.assertEqual(bsearch(6, arr), 3)
        self.assertEqual(bsearch(9, arr), 4)
        self.assertEqual(bsearch(69, arr), 5)

    def test_czynniki_pierwsze(self):
        self.assertEqual(czynniki_pierwsze(8), [2, 2, 2])
        self.assertEqual(czynniki_pierwsze(81), [3, 3, 3, 3])
        self.assertEqual(czynniki_pierwsze(13), [13])

from bi import bsearch, bisect
from czynniki_pierwsze import czynniki_pierwsze
from sito_eratostenesa import sito
from nwd import nwd_i, nwd_r
from sortowanie import bubble_sort

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

    def test_sito_eratostenesa(self):
        target = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
        self.assertEqual(sito(1), [])
        self.assertEqual(sito(30), target)

    def test_nwd(self):
        self.assertEqual(nwd_i(150, 120), 30)
        self.assertEqual(nwd_r(198, 231), 33)

        self.assertEqual(nwd_i(100, 100), 100)
        self.assertEqual(nwd_r(100, 100), 100)

    def test_sort(self):
        arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        arr_sorted = sorted(arr)
        self.assertEqual(bubble_sort(arr), arr_sorted)

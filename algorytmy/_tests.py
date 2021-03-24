from bi import bsearch, bisect
from czynniki_pierwsze import czynniki_pierwsze
from sito_eratostenesa import sito
from nwd import nwd_i, nwd_r
from sortowanie import bubble_sort, merge_sort, insertion_sort, quick_sort, bucket_sort, selection_sort
from trojkaty import czy_trojkat, czy_prostokatny, czy_rownoboczny, czy_ostrokatny, czy_rozwartokatny
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
        arr = [1, 3, 7, 4, 6, 9, 2, 8, 5]
        arr_sorted = sorted(arr)
        self.assertEqual(bubble_sort(arr, debug=False), arr_sorted)
        self.assertEqual(selection_sort(arr, debug=False), arr_sorted)
        self.assertEqual(insertion_sort(arr, debug=False), arr_sorted)
        self.assertEqual(quick_sort(arr), arr_sorted)
        # self.assertEqual(merge_sort(arr), arr_sorted)
        # self.assertEqual(bucket_sort(arr), arr_sorted)

    def test_trojkat(self):
        nie = [1, 2, 69]
        normalny = [3, 4, 6]
        prostokatny = [3, 4, 5]
        ostrokatny = [2, 3, 3]
        rozwartokatny = [10, 10, 16]

        self.assertEqual(czy_trojkat(*nie), False)
        self.assertEqual(czy_trojkat(*normalny), True)
        self.assertEqual(czy_prostokatny(*normalny), False)
        self.assertEqual(czy_prostokatny(*prostokatny), True)
        self.assertEqual(czy_ostrokatny(*prostokatny), False)
        self.assertEqual(czy_ostrokatny(*ostrokatny), True)
        self.assertEqual(czy_rozwartokatny(*ostrokatny), False)
        self.assertEqual(czy_rozwartokatny(*rozwartokatny), True)

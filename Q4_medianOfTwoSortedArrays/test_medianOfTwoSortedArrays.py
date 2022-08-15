from medianOfTwoSortedArraysQ4 import Solution
import unittest

class MedianOfTwoSortedArraysTestCase(unittest.TestCase):
    def test_even_arrays(self):
        list1 = [1,2]
        list2 = [3,4]

        expectedMedian = 2.5
        actualMedian = Solution.findMedianSortedArrays(list1, list2)

        self.assertEqual(expectedMedian, actualMedian, "Expected median doesn't match output")

    def test_odd_array_lengths(self):
        list1 = [1,3]
        list2 = [2]

        expectedMedian = 2
        actualMedian = Solution.findMedianSortedArrays(list1, list2)

        self.assertEqual(expectedMedian, actualMedian, "Expected median doesn't match output")

    def test_array_with_negative_numbers(self):
        list1 = [-2,-1]
        list2 = [1,3]

        expectedMedian = 0
        actualMedian = Solution.findMedianSortedArrays(list1, list2)

        self.assertEqual(expectedMedian, actualMedian, "Expected median doesn't match output")

    def test_empty_arrays(self):
        list1 = []
        list2 = []

        expectedMedian = 0
        actualMedian = Solution.findMedianSortedArrays(list1, list2)

        self.assertEqual(expectedMedian, actualMedian, "Expected median doesn't match output")

    def test_single_full_array(self):
        list1 = []
        list2 = [1,2]

        expectedMedian = 1.5
        actualMedian = Solution.findMedianSortedArrays(list1, list2)

        self.assertEqual(expectedMedian, actualMedian, "Expected median doesn't match output")

if __name__ == '__main__':
    unittest.main()
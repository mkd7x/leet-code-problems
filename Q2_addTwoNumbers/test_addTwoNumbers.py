from linkedList import ListNode
from AddTwoNumbers import Solution
import unittest

class AddTwoNumbersTestCase(unittest.TestCase):

    def test_two_even_lists(self):
        list1 = [2,4,3]
        list2 = [5,6,4]

        list1Head = ListNode.createLinkedList(list1)
        list2Head = ListNode.createLinkedList(list2)

        expectedOutputSum = [7,0,8]
        actualOutput = Solution.addTwoNumbers(list1Head, list2Head)
        actualOutputSum = ListNode.getLinkedListValues(actualOutput)

        self.assertEqual(expectedOutputSum, actualOutputSum, "Expected sum does not match output sum")

    def test_two_ueven_lists(self):
        list1 = [9,9,9,9,9,9,9]
        list2 = [9,9,9,9]

        list1Head = ListNode.createLinkedList(list1)
        list2Head = ListNode.createLinkedList(list2)

        expectedOutputSum = [8,9,9,9,0,0,0,1]
        actualOutput = Solution.addTwoNumbers(list1Head, list2Head)
        actualOutputSum = ListNode.getLinkedListValues(actualOutput)

        self.assertEqual(expectedOutputSum, actualOutputSum, "Expected sum does not match output sum")

    def test_sum_with_ending_zero(self):
        list1 = [0,1]
        list2 = [0,1]

        list1Head = ListNode.createLinkedList(list1)
        list2Head = ListNode.createLinkedList(list2)

        expectedOutputSum = [0,2]
        actualOutput = Solution.addTwoNumbers(list1Head, list2Head)
        actualOutputSum = ListNode.getLinkedListValues(actualOutput)

        self.assertEqual(expectedOutputSum, actualOutputSum, "Expected sum does not match output sum")

    def test_adding_zero_lists(self):
        list1Head = ListNode(0)
        list2Head = ListNode(0)

        expectedOutputSum = [0]
        actualOutput = Solution.addTwoNumbers(list1Head, list2Head)
        actualOutputSum = ListNode.getLinkedListValues(actualOutput)

        self.assertEqual(expectedOutputSum, actualOutputSum, "Expected sum does not match output sum")

    def test_add_one_zero_list(self):
        list1 = [0,1]

        list1Head = ListNode.createLinkedList(list1)
        list2Head = ListNode(0)

        expectedOutputSum = [0,1]
        actualOutput = Solution.addTwoNumbers(list1Head, list2Head)
        actualOutputSum = ListNode.getLinkedListValues(actualOutput)

        self.assertEqual(expectedOutputSum, actualOutputSum, "Expected sum does not match output sum")

if __name__ == '__main__':
    unittest.main()
import unittest
from linkedList import ListNode
from mergeTwoSortedLists import Solution

class mergeTwoSortedListsTestCase(unittest.TestCase):
    
    def test_even_list(self):
        list1 = [1,2,4]
        list2 = [1,3,4]

        expectedList = [1,1,2,3,4,4]

        list1head = ListNode.createLinkedList(list1)
        list2head = ListNode.createLinkedList(list2)

        actualOutput = Solution.mergeTwoLists(list1head, list2head)
        actualOutputArray = ListNode.getLinkedListValues(actualOutput)

        self.assertEqual(expectedList, actualOutputArray, "Unexpected output")
    
    def test_uneven_list(self):
        list1 = [1,2,4]
        list2 = [1,3,4,5,6]

        expectedList = [1,1,2,3,4,4,5,6]

        list1head = ListNode.createLinkedList(list1)
        list2head = ListNode.createLinkedList(list2)

        actualOutput = Solution.mergeTwoLists(list1head, list2head)
        actualOutputArray = ListNode.getLinkedListValues(actualOutput)

        self.assertEqual(expectedList, actualOutputArray, "Unexpected output")


    def test_two_empty_lists(self):

        expectedList = []

        actualOutput = Solution.mergeTwoLists(None, None)

        self.assertEqual(None, None, "Unexpected output")
    

    def test_one_empty_list(self):
        list1 = [1,2,4]

        expectedList = [1,2,4]

        list1head = ListNode.createLinkedList(list1)
        list2head = None

        actualOutput = Solution.mergeTwoLists(list1head, list2head)
        actualOutputArray = ListNode.getLinkedListValues(actualOutput)

        self.assertEqual(expectedList, actualOutputArray, "Unexpected output")


if __name__ == '__main__':
    unittest.main()
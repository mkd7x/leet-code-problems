import unittest
from longestCommonPrefix import Solution

class longestCommonPrefixTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.LCPfinder = Solution()
    
    def test_two_prefix(self):
        testInput = ["flower","flow","flight"]
        expectedOutput = "fl"
        
        actualOuput = self.LCPfinder.longestCommonPrefix(testInput)

        self.assertEqual(actualOuput, expectedOutput, "Input %s, expected: %s, got: %s" % (testInput, expectedOutput, actualOuput))


    def test_no_common_prefix(self):
        testInput = ["dog","racecar","car"]
        expectedOutput = ""

        actualOuput = self.LCPfinder.longestCommonPrefix(testInput)

        self.assertEqual(actualOuput, expectedOutput, "Input %s, expected: %s, got: %s" % (testInput, expectedOutput, actualOuput))
    
    def test_whole_word_prefix(self):
        testInput = ["racecar", "racecar", "racecar"]
        expectedOutput = "racecar"

        actualOuput = self.LCPfinder.longestCommonPrefix(testInput)

        self.assertEqual(actualOuput, expectedOutput, "Input %s, expected: %s, got: %s" % (testInput, expectedOutput, actualOuput))


    def test_mixed_length_words(self):
        testInput = ["race", "racecar", "racecardriver"]
        expectedOutput = "race"

        actualOuput = self.LCPfinder.longestCommonPrefix(testInput)

        self.assertEqual(actualOuput, expectedOutput, "Input %s, expected: %s, got: %s" % (testInput, expectedOutput, actualOuput))


    def test_empty_words(self):
        testInput = ["race", "racecar", ""]
        expectedOutput = ""

        actualOuput = self.LCPfinder.longestCommonPrefix(testInput)

        self.assertEqual(actualOuput, expectedOutput, "Input %s, expected: %s, got: %s" % (testInput, expectedOutput, actualOuput))




if __name__ == '__main__':
    unittest.main()
from Q32_LVP import Solution
import unittest

class LVPTestCase(unittest.TestCase):
    def test_single_valid_parentheses(self):
        inputString = "(()"
        expectedOuput = 2

        actualOutput = Solution.longestValidParentheses(inputString)

        self.assertEqual(expectedOuput, actualOutput, "Expected output does not match actual output")

    def test_empty_string(self):
        inputString = ""
        expectedOuput = 0

        actualOutput = Solution.longestValidParentheses(inputString)

        self.assertEqual(expectedOuput, actualOutput, "Expected output does not match actual output")
    
    def test_no_matching_parentheses(self):
        inputString = "(((((((("
        expectedOuput = 0

        actualOutput = Solution.longestValidParentheses(inputString)

        self.assertEqual(expectedOuput, actualOutput, "Expected output does not match actual output")
    
    def test_24_matching_parentheses(self):
        inputString = ")()(()()(())()()))())())((((())"
        expectedOuput = 16

        actualOutput = Solution.longestValidParentheses(inputString)

        self.assertEqual(expectedOuput, actualOutput, "Expected output does not match actual output")
    
    def test_10_matching(self):
        inputString = "(()()(()))))"
        expectedOuput = 10

        actualOutput = Solution.longestValidParentheses(inputString)

        self.assertEqual(expectedOuput, actualOutput, "Expected output does not match actual output")
    
    def test_14_matching(self):
        inputString = "((()()((())))))"
        expectedOuput = 14

        actualOutput = Solution.longestValidParentheses(inputString)

        self.assertEqual(expectedOuput, actualOutput, "Expected output does not match actual output")

    def test_6_matching(self):
        inputString = "()()))()()())))((()()"
        expectedOuput = 6

        actualOutput = Solution.longestValidParentheses(inputString)

        self.assertEqual(expectedOuput, actualOutput, "Expected output does not match actual output")

    def test_2_matching_edge(self):
        inputString = "()(()"
        expectedOuput = 2

        actualOutput = Solution.longestValidParentheses(inputString)

        self.assertEqual(expectedOuput, actualOutput, "Expected output does not match actual output")

    def test_6_match_3_left_open(self):
        inputString = "()(()()(()()()"
        expectedOuput = 6

        actualOutput = Solution.longestValidParentheses(inputString)

        self.assertEqual(expectedOuput, actualOutput, "Expected output does not match actual output")


if __name__ == '__main__':
    unittest.main()
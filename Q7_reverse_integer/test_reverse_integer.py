from Q7_reverseInteger import Solution
import unittest

class ReverseIntegerTestCase(unittest.TestCase):

    def test_123_numbers(self):
        inputNumber = 123
        expectedOutput = 321

        actualOutput = Solution.reverse(inputNumber)

        self.assertEqual(expectedOutput, actualOutput, "Output number doesn't match expected")

    def test_negative_123_numbers(self):
        inputNumber = -123
        expectedOutput = -321

        actualOutput = Solution.reverse(inputNumber)

        self.assertEqual(expectedOutput, actualOutput, "Output number doesn't match expected")

    def test_numbers_with_leading_zero(self):
        inputNumber = 120
        expectedOutput = 21

        actualOutput = Solution.reverse(inputNumber)

        self.assertEqual(expectedOutput, actualOutput, "Output number doesn't match expected")

    def test_number_larger_than_32_bit(self):
        inputNumber = 2147483647
        expectedOutput = 0

        actualOutput = Solution.reverse(inputNumber)

        self.assertEqual(expectedOutput, actualOutput, "Output number doesn't match expected")
    
    def test_number_almost_larger_than_32_bit(self):
        inputNumber = 2147447412
        expectedOutput = 2147447412

        actualOutput = Solution.reverse(inputNumber)

        self.assertEqual(expectedOutput, actualOutput, "Output number doesn't match expected")
    
    def test_number_almost_smaller_than_32_bit(self):
        inputNumber = -2147447412
        expectedOutput = -2147447412

        actualOutput = Solution.reverse(inputNumber)

        self.assertEqual(expectedOutput, actualOutput, "Output number doesn't match expected")

    def test_number_reverse_larger_than_32_bit(self):
        inputNumber = 1534236469
        expectedOutput = 0

        actualOutput = Solution.reverse(inputNumber)

        self.assertEqual(expectedOutput, actualOutput, "Output number doesn't match expected")

    def test_negative_number_reverse_smaller_than_32_bit(self):
        inputNumber = -2147483412
        expectedOutput = -2143847412

        actualOutput = Solution.reverse(inputNumber)

        self.assertEqual(expectedOutput, actualOutput, "Output number doesn't match expected")

    def test_input_1563847412_case(self):
        inputNumber = 1563847412
        expectedOutput = 0

        actualOutput = Solution.reverse(inputNumber)

        self.assertEqual(expectedOutput, actualOutput, "Output number doesn't match expected")


if __name__ == '__main__':
    unittest.main()
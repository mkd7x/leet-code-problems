import logging
import unittest
import sys
from romanToInt import Solution

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

class romanToIntTestCase(unittest.TestCase):
    
    def setUp(self) -> None:
        self.stream_handler = logging.StreamHandler(sys.stdout)
        logger.addHandler(self.stream_handler)
        self.romanConverter = Solution()
        #logger.info("Running test setup")
    
    def test_single_numeral(self):
        inputString = "I"
        expectedOutput = 1
        #logger.info("Testing input: %s, expected output: %d" % (inputString, expectedOutput))

        result = self.romanConverter.romanToInt(inputString)
        self.assertEqual(result, expectedOutput, "Inputted '%s' expected: %d, got %d" % (inputString, expectedOutput, result))
    
    def test_second_numeral(self):
        inputString = "II"
        expectedOutput = 2
        #logger.info("Testing input: %s, expected output: %d" % (inputString, expectedOutput))

        result = self.romanConverter.romanToInt(inputString)
        self.assertEqual(result, expectedOutput, "Inputted '%s' expected: %d, got %d" % (inputString, expectedOutput, result))

    def test_four_numeral(self):
        inputString = "IV"
        expectedOutput = 4
        #logger.info("Testing input: %s, expected output: %d" % (inputString, expectedOutput))

        result = self.romanConverter.romanToInt(inputString)
        self.assertEqual(result, expectedOutput, "Inputted '%s' expected: %d, got %d" % (inputString, expectedOutput, result))
    
    def test_1994_numeral(self):
        inputString = "MCMXCIV"
        expectedOutput = 1994
        #logger.info("Testing input: %s, expected output: %d" % (inputString, expectedOutput))

        result = self.romanConverter.romanToInt(inputString)
        self.assertEqual(result, expectedOutput, "Inputted '%s' expected: %d, got %d" % (inputString, expectedOutput, result))
    
    def test_1695_numeral(self):
        inputString = "MDCXCV"
        expectedOutput = 1695
        #logger.info("Testing input: %s, expected output: %d" % (inputString, expectedOutput))

        result = self.romanConverter.romanToInt(inputString)
        self.assertEqual(result, expectedOutput, "Inputted '%s' expected: %d, got %d" % (inputString, expectedOutput, result))

    def tearDown(self) -> None:
        #logger.info("Running test teardown")
        logger.removeHandler(self.stream_handler)

def suite():
    suite = unittest.TestSuite()
    suite.addTest(romanToIntTestCase('test_single_numeral'))
    suite.addTest(romanToIntTestCase('test_second_numeral'))
    suite.addTest(romanToIntTestCase('test_four_numeral'))
    suite.addTest(romanToIntTestCase('test_1994_numeral'))
    suite.addTest(romanToIntTestCase('test_1695_numeral'))
    return suite

if __name__ == '__main__':
    # unittest.main()

    testRunner = unittest.TextTestRunner()
    testRunner.run(suite())
        
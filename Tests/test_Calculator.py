import unittest

from Calculator.Calculator import Calculator
from CsvReader.CsvReader import CsvReader


class MyTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.calculator = Calculator()

    def test_instantiate_calculator(self):
        self.assertIsInstance(self.calculator, Calculator)

    def test_add_method_calculator(self):  # tests that addition works in calculator
        test_data = CsvReader("Tests/Data/UT_Addition").data
        for row in test_data:
            result = float(row['Result'])
            self.assertEqual(self.calculator.add(row['Value 1'], row['Value 2'], result))
            self.assertEqual(self.calculator.result, result)

    def test_subtract_method_calculator(self):  # tests that subtraction works in calculator
        test_data = CsvReader("Tests/Data/UT_Subtraction").data
        for row in test_data:
            result = float(row['Result'])
            self.assertEqual(self.calculator.subtract(row['Value 1'], row['Value 2'], result))
            self.assertEqual(self.calculator.result, result)

    def test_multiply_method_calculator(self): # tests that multiplication works
        test_data = CsvReader("Tests/Data/UT_Multiply").data
        for row in test_data:
            result = float(row['Result'])
            self.assertEqual(self.calculator.multiply(row['Value 1'], row['Value 2'], result))
            self.assertEqual(self.calculator.result, result)

    def test_divide_method_calculator(self):
        test_data = CsvReader("Tests/Data/UT_Division").data
        for row in test_data:
            result = float(row['Result'])
            self.assertEqual(self.calculator.divide(row['Value 1'], row['Value 2'], result))
            self.assertEqual(self.calculator.result, result)

    def test_results_property(self):
        self.assertEqual(self.calculator.result, 0)

if __name__ == '__main__':
    unittest.main()

import unittest
from BMI import calculate_bmi
from BMI import bmi_check
class MyTestCase(unittest.TestCase):
    def test_bmi(self):
        #stub
        stub1_weight = "50"
        stub1_height = "167"

        stub2_weight = "50"
        stub2_height = "0"

        stub3_weight = "50"
        stub3_height = "a"

        stub4_weight = "50"
        stub4_height = "-5"

        # assume
        expected1 = (50/(1.67*1.67))
        expected2 = None
        expected3 = None
        expected4 = None

        # action
        result1 = calculate_bmi(stub1_height,stub1_weight)
        result2 = calculate_bmi(stub2_height,stub2_weight)
        result3 = calculate_bmi(stub3_height,stub3_weight)
        result4 = calculate_bmi(stub4_height, stub4_weight)

        # expect/assert
        self.assertEqual(result1, expected1)
        self.assertEqual(result2, expected2)
        self.assertEqual(result3, expected3)
        self.assertEqual(result4, expected4)

    def test_bmiCheck(self):
        # stub
        stub1 =16
        stub2=19
        stub3=None
        stub4=26
        stub5=32
        stub6=37

        # assume
        expected1='Underweight'
        expected2='OK'
        expected3='wrong input'
        expected4='overweight'
        expected5='obesity'
        expected6='Severe obesity'

        # action
        result1 = bmi_check(stub1)
        result2 = bmi_check(stub2)
        result3 = bmi_check(stub3)
        result4 = bmi_check(stub4)
        result5 = bmi_check(stub5)
        result6 = bmi_check(stub6)

        # expect/assert
        self.assertEqual(result1, expected1)
        self.assertEqual(result2, expected2)
        self.assertEqual(result3, expected3)
        self.assertEqual(result4, expected4)
        self.assertEqual(result5, expected5)
        self.assertEqual(result6, expected6)




if __name__ == '__main__':
    unittest.main()

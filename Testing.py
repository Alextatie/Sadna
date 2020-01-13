import unittest
from bubbleSort import *
from BMI import *


class Testing(unittest.TestCase):
    def test_is_empty(self):
        arr= [5,3,8,6,1,3]
        self.assertTrue(bubbleSort(arr)),"bubble is empty"
    def test_not_lost(self):
        arr= [5,3,8,6,1,3]
        temp=arr.copy()
        self.assertCountEqual(bubbleSort(arr), temp),"something was lost"
    def test_is_sorted(self):
        arr= [5,3,8,6,1,3]
        sorted = [1,3,3,5,6,8]
        self.assertListEqual(bubbleSort(arr),sorted),"not sorted"
    def test_BMI_returned(self):
        weight = 45
        height = 1.8
        self.assertTrue(bmiCalc(weight,height)),"nothing returned"





if __name__ == '__main__':
    unittest.main()
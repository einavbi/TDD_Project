import unittest
from bubble_sort import bubblesort
from bubble_sort import check
class MyTestCase(unittest.TestCase):

    def test_sort(self):
        # stub
        stub1 = [3,6,9,1]
        stub2 = [0,7,2,3,4]
        stub3 = []

        # assume
        expected1 = [1,3,6,9]
        expected2 = [0,2,3,4,7]
        expected3 = "no input"

        # action
        result1 = bubblesort(stub1)
        result2 = bubblesort(stub2)
        result3 = bubblesort(stub3)

        # expect/assert
        self.assertEqual(result1, expected1)
        self.assertEqual(result2, expected2)
        self.assertEqual(result3, expected3)


    def test_check(self):
        # stub
        stub1 = [2,5,8,1]
        stub2 = [1,2,3,4,]


        # assume
        expected1 = False
        expected2 = True


        # action
        result1 = check(stub1)
        result2 =check(stub2)


        # expect/assert
        self.assertEqual(result1, expected1)
        self.assertEqual(result2, expected2)





if __name__ == '__main__':
    unittest.main()

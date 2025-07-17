"""Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].

The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

You must write an algorithm that runs in O(n) time and without using the division operation.



Example 1:

Input: nums = [1,2,3,4]
Output: [24,12,8,6]
Example 2:

Input: nums = [-1,1,0,-3,3]
Output: [0,0,9,0,0]


Constraints:

2 <= nums.length <= 105
-30 <= nums[i] <= 30
The input is generated such that answer[i] is guaranteed to fit in a 32-bit integer.
"""
"""
Core insight output[i] = product of all elements to the left of i × product of all elements to the right of i
we will do one pass to create product of prefixes and anoter pass to create product of suffixes
"""
import unittest

class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        # create and initialize output array with filled value 1
        arraySize = len(nums)
        output = [1 for _ in range(arraySize)]
        # go one round from start to calculate prefixes and save it in output
        prefix =1 
        for i in range(arraySize):
            output[i] = prefix 
            prefix = prefix * nums[i]
        
        # go one round from end to calculate suffixes and save it in output
        suffix = 1 
        for i in range(arraySize -1 , -1 , -1):
            output[i] = suffix * output[i]
            suffix = suffix * nums[i]
        
        return output
    

class TestProductExceptSelf(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_empty(self):
        self.assertEqual(self.sol.productExceptSelf([]), [])

    def test_single_element(self):
        self.assertEqual(self.sol.productExceptSelf([5]), [1])

    def test_two_elements(self):
        self.assertEqual(self.sol.productExceptSelf([2, 3]), [3, 2])

    def test_no_zeros(self):
        self.assertEqual(self.sol.productExceptSelf([1, 2, 3, 4]),
                         [24, 12, 8, 6])

    def test_one_zero(self):
        # only the position of zero should get product of others
        self.assertEqual(self.sol.productExceptSelf([0, 3, 4, 5]),
                         [60, 0, 0, 0])

    def test_two_zeros(self):
        # with two zeros, all products except self are zero
        self.assertEqual(self.sol.productExceptSelf([0, 2, 0, 4]),
                         [0, 0, 0, 0])

    def test_negatives(self):
        self.assertEqual(self.sol.productExceptSelf([-1, 1, 0, -3, 3]),
                         [0, 0, 9, 0, 0])

    def test_large_numbers(self):
        arr = [10, 20, 30]
        # products: [20*30, 10*30, 10*20]
        self.assertEqual(self.sol.productExceptSelf(arr),
                         [600, 300, 200])

if __name__ == '__main__':
    unittest.main()
"""
Write a function that returns the second largest distinct element in an unsorted integer array.
Constraints:
Do not use sorting.

Do it in a single pass (ideal).

Return None if a second max doesn't exist.
"""
import unittest

class Solution(object):
    # this solution works in O(n) time and O(n) space
    def second_max(self, nums):
        if not nums or len(nums) < 2:
            return None
        
        second_largest = None
        largest = None


        for num in nums :
            if  largest is None or num > largest:
                second_largest = largest
                largest = num
            elif num < largest and (second_largest is None or second_largest < num):
                second_largest = num
        return second_largest
    # this is alternate more optimal for Fang
    def second_max_fang(self, nums):
        if not nums or len(nums) < 2:
            return None
        
        largest = second_largest = float('-inf')
        
        for num in nums:
            if num > largest:
                second_largest = largest
                largest = num
            elif num > second_largest and num < largest:
                second_largest = num
        
        return second_largest if second_largest != float('-inf') else None
    
    
class TestSecondMax(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()
        
    def test_normal_case(self):
        self.assertEqual(self.sol.second_max([10, 5, 20, 8, 20]), 10)
        self.assertEqual(self.sol.second_max_fang([10, 5, 20, 8, 20]), 10)

    def test_descending(self):
        self.assertEqual(self.sol.second_max([100, 90, 80, 70]), 90)
        self.assertEqual(self.sol.second_max_fang([100, 90, 80, 70]), 90)

    def test_ascending(self):
        self.assertEqual(self.sol.second_max([1, 2, 3, 4]), 3)
        self.assertEqual(self.sol.second_max_fang([1, 2, 3, 4]), 3)

    def test_all_duplicates(self):
        self.assertIsNone(self.sol.second_max([5, 5, 5, 5]))
        self.assertIsNone(self.sol.second_max_fang([5, 5, 5, 5]))

    def test_single_element(self):
        self.assertIsNone(self.sol.second_max([42]))
        self.assertIsNone(self.sol.second_max_fang([42]))

    def test_empty_array(self):
        self.assertIsNone(self.sol.second_max([]))
        self.assertIsNone(self.sol.second_max_fang([]))

    def test_negative_numbers(self):
        self.assertEqual(self.sol.second_max([-10, -20, -30]), -20)
        self.assertEqual(self.sol.second_max_fang([-10, -20, -30]), -20)

    def test_mixed_signs(self):
        self.assertEqual(self.sol.second_max([-5, 0, 5, 10]), 5)
        self.assertEqual(self.sol.second_max_fang([-5, 0, 5, 10]), 5)

    def test_second_max_at_end(self):
        self.assertEqual(self.sol.second_max([10, 20, 30, 40, 30]), 30)
        self.assertEqual(self.sol.second_max_fang([10, 20, 30, 40, 30]), 30)

    def test_multiple_second_max(self):
        self.assertEqual(self.sol.second_max([1, 2, 3, 3, 2]), 2)
        self.assertEqual(self.sol.second_max_fang([1, 2, 3, 3, 2]), 2)

if __name__ == '__main__':
    unittest.main()
                
        
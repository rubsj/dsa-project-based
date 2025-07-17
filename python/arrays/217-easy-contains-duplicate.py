"""
    Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.

 

Example 1:

Input: nums = [1,2,3,1]

Output: true

Explanation:

The element 1 occurs at the indices 0 and 3.

Example 2:

Input: nums = [1,2,3,4]

Output: false

Explanation:

All elements are distinct.

Example 3:

Input: nums = [1,1,1,3,3,4,3,2,4,2]

Output: true

 

Constraints:

1 <= nums.length <= 105
-109 <= nums[i] <= 109
"""

import unittest

"""
🔷 Problem 1: Inventory Check (Easy)
ID-style: LeetCode #217
🛠️ You manage a warehouse and want to check if any product ID is scanned more than once during intake.

Input: arr = [1001, 1002, 1003, 1001]
Output: True
"""

class Solution(object):
    def containsDuplicate(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        seen = set()
        for num in arr:
            if num in seen:
                return True
            seen.add(num)
        return False
    
class TestContainsDuplicate(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_empty(self):
        self.assertFalse(self.sol.containsDuplicate([]))

    def test_no_duplicates(self):
        self.assertFalse(self.sol.containsDuplicate([1, 2, 3, 4, 5]))

    def test_with_duplicates(self):
        self.assertTrue(self.sol.containsDuplicate([1, 2, 3, 2]))

    def test_all_same(self):
        self.assertTrue(self.sol.containsDuplicate([7, 7, 7, 7]))

    def test_single_element(self):
        self.assertFalse(self.sol.containsDuplicate([42]))


if __name__ == '__main__':
    unittest.main()
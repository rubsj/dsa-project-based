"""
    Find all valid combinations of k numbers that sum up to n such that the following conditions are true:

Only numbers 1 through 9 are used.
Each number is used at most once.
Return a list of all possible valid combinations. The list must not contain the same combination twice, and the combinations may be returned in any order.

 

Example 1:

Input: k = 3, n = 7
Output: [[1,2,4]]
Explanation:
1 + 2 + 4 = 7
There are no other valid combinations.
Example 2:

Input: k = 3, n = 9
Output: [[1,2,6],[1,3,5],[2,3,4]]
Explanation:
1 + 2 + 6 = 9
1 + 3 + 5 = 9
2 + 3 + 4 = 9
There are no other valid combinations.
Example 3:

Input: k = 4, n = 1
Output: []
Explanation: There are no valid combinations.
Using 4 different numbers in the range [1,9], the smallest sum we can get is 1+2+3+4 = 10 and since 10 > 1, there are no valid combination.
 

Constraints:

2 <= k <= 9
1 <= n <= 60
"""

from typing import List


class Solution(object):
    def combinationSum3(self, k, n):
        """
        :type k: int
        :type n: int
        :rtype: List[List[int]]
        """
        res = []
        numbers = [1,2,3,4,5,6,7,8,9]
        def dfs(pos , target, current):            
            if target == 0 and len(current) == k :
                res.append(current[:])
                return
            if target < 0  or pos == len(numbers) or len(current) > k:
                return
            for i in range(pos , len(numbers)):
                current.append(numbers[i])
                dfs(i + 1, target - numbers[i], current)
                current.pop()
        dfs(0, n , [])
        return res
    
solution = Solution()
result = solution.combinationSum3(3, 7)
print(result)

# more optimized solution is
class Solution2(object):
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        res = []

        def dfs(pos , target, current):       
            if target == 0 and len(current) == k :
                res.append(current[:])
                return
            if target < 0 or len(current) > k:
                return
            for i in range(pos , 10):
                current.append(i)
                dfs(i+1, target - i, current)
                current.pop()
        dfs(1, n , [])
        return res
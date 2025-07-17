class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        elements = {}
        maxCount = 0
        maxElement = None
        for num in nums :
            count = elements.get(num, 0) + 1
            elements[num] = count
            if count > maxCount:
                maxCount = count
                maxElement = num
        return maxElement
           
validateClass = Solution()
result =  validateClass.majorityElement([3,2,3]) 
print(result)
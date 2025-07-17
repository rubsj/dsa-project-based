🔁 Problem Statement:
Given an array nums of n integers, return an array output such that:

output[i] = product of all elements in nums except nums[i]

✋ You cannot use division
✅ Solution must be in O(n) time
✅ Extra space usage must be O(1) (excluding the result array)

E🧪 Example
Input:  [2, 3, 4]
Output: [12, 8, 6]

Why?
Output[0] = 3 × 4 = 12

Output[1] = 2 × 4 = 8

Output[2] = 2 × 3 = 6

✅ FAANG-Optimal Solution: Prefix × Suffix Products

🔍 Core Insight:
For index i:
output[i] = product of all elements to the left of i × product of all elements to the right of i

✏️ Step-by-Step Breakdown:
```
def product_except_self(nums):
    n = len(nums)
    output = [1] * n

    # Step 1: Prefix product
    prefix = 1
    for i in range(n):
        output[i] = prefix
        prefix *= nums[i]

    # Step 2: Suffix product
    suffix = 1
    for i in range(n - 1, -1, -1):
        output[i] *= suffix
        suffix *= nums[i]

    return output
```
🔄 Dry Run (Annotated)
nums = [2, 3, 4]
n = 3
output = [1, 1, 1]

# Pass 1: prefix
prefix = 1
i = 0 → output[0] = 1, prefix = 1 × 2 = 2  
i = 1 → output[1] = 2, prefix = 2 × 3 = 6  
i = 2 → output[2] = 6, prefix = 6 × 4 = 24

→ output after prefix pass = [1, 2, 6]

# Pass 2: suffix
suffix = 1
i = 2 → output[2] = 6 × 1 = 6, suffix = 1 × 4 = 4  
i = 1 → output[1] = 2 × 4 = 8, suffix = 4 × 3 = 12  
i = 0 → output[0] = 1 × 12 = 12, suffix = 12 × 2 = 24

→ Final output = [12, 8, 6]

⏱ Time and Space Complexity
Resource	Complexity
Time	O(n)
Space	O(1) (excluding output) ✅

💡 We only use constant extra space: prefix, suffix, and the output array (which doesn't count toward space complexity in interviews).

❓ What If There Are Zeros?
What happens if nums = [2, 3, 0, 4]?

With exactly one 0, the result will be:

All positions except the zero’s index → 0

Zero’s index → product of all non-zero values

With more than one 0, the entire result is [0, 0, 0, 0]

✅ This solution handles zeros correctly.

🧠 Interviewer Signals
You recognize this is a variation of the famous “product of array except self”

You avoid brute force and division

You optimize space by reusing the output array

You give clear reasoning and dry run
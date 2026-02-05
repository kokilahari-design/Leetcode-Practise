# Question 1: Single Number - every element appears twice except for one element. Find that single one. ( Input: nums = [4,1,2,1,2] Output: 4)

# Using Counter: Time - O(n)   Space - O(n)
from typing import List
from collections import Counter
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        result = Counter(nums)
        for k,v in result.items():
            if v == 1:
                return k

# Optimal Solution: Time: O(n) Space: O(1) -> XOR - [(a ^ a = 0) Same number cancels itself, (a ^ 0 = a) Zero is identity]
# All duplicates vanish, leaving the single unique element
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        result = 0
        for i in nums:
            result ^= i
        return result
    
Obj = Solution()
print(Obj.singleNumber(nums = [4, 1, 2, 1, 2]))


    

    


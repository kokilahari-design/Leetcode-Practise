# 217. Contains Duplicate      Time Complexity: O(n) Space Complexity: O(n)
# Create empty set as s, Iterate elements through the list, check if element already in list, if element present -> return True then exit loop
# else add that element in set. After Iterating all elements, all elements in list are unique -> return False atlast

class Solution(object):
    def containsDuplicate(self, nums):
        s = set()
        for i in nums:
            if i in s:
                return True
            else:
                s.add(i)
        return False

o = Solution()
r = o.containsDuplicate([22,2,14,18,22])
print(r)

# Alternative Solution: Check len(input_list) != len(set(input_list)) return True else return False
# Time Complexity: O(n) Space Complexity: O(n)

class Solution(object):
    def containsDuplicate(self, nums):
       return len(nums) != len(set(nums))

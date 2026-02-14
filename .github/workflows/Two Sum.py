# 1. Two Sum
# Input: nums = [2,7,11,15], target = 9, Output: [0,1]
# Explanation:  nums[0] + nums[1] == 9, we return [0, 1].

# Iterate element through the list with range concept to fetch the element position, Iterate and store the element in curr_element variable
# Check the difference = target - current_element then check if current_element not in dictionary, if not, then store the difference value as key and current_element index position as value
# If current_element in dictionary, then store the current_element position in current_index variable then fetch the value of current_elemnt present in dictionary and store in previous_index variable.


class Solution(object):
    def twoSum(self, nums, target):
        d = {}                            # Create dictionary to store the differnece value and element index value
        for i in range(0,len(nums)):
            curr_element = nums[i]
            diff = target - curr_element      # differnece = target - current_element_value
            if curr_element not in d:
                d[diff] = i
            else:
                previous_index = d[curr_element]
                current_index = i
                return [previous_index,current_index]
            
obj = Solution()
result = obj.twoSum([2,7,11,15], 9)
print(result)

# 55. Jump Game  -> Explanation: Jump 1 step from index 0 to 1, then 3 steps to the last index.
# Input: nums = [2,3,1,1,4]  Output: true
# Greedy Algorithm: solves a problem by repeatedly choosing the locally optimal option at each step in hopes of reaching a globally optimal solution.
# Initially Consider last position of input as jump_index, then iterate from second last position to 0 index, 
# if the sum of current index and its value is greater than or equal to jump_index, then update jump_index with current index. 
# Finally if jump_index is 0, then return true else false.  


nums = [2,3,1,1,4]
jump_index = len(nums) -1
for current_index in range(len(nums)-2, -1, -1):
    res = nums[current_index] + current_index
    if res >= jump_index:
        jump_index = current_index
if jump_index == 0:
    print("true")
else:
    print("false")

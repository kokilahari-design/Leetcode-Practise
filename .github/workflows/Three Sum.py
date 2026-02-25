# 15. 3Sum
# input = [0,1,1] or [0,0,0] or [-1,0,1,2,-1,-4]  Output =  [], [[0,0,0]], [[-1,-1,2],[-1,0,1]]
# Time Complexity = O(n²) -> O(n log n) sort + O(n × n) for + while loop
# Space Complexity = O(k) -> O(k) list output + O(log n) sort stack   (k = number of valid triplets)

# Sort the list, Check if length of given list is greater than 3 to find the triplets sum
# Iterate elements in list, check if current left_pt value equal to previous left_pt value and intially we'll not have previous left_pt value, so check this condition when index value is greater than 0 and reaches index to 1, it compares the value and skips if value is same (skips checking two pointer loop).  when index = 0, condition fails. 
# store element in out_ele variable, set left_pt as next index and right_pt as last index in list
# while loop to check left_pt is less than right_pt, add 3 elements to find the triplet sum
# If adding_3_value == 0, return the triplet value. After return, increase left pointer and decrease right pointer by 1
# If adding_3_value < 0,then increase left pointer by 1 and in while loop, check If current left_pt value is same as previous left_pt value, skip and increment left_pt by 1.
# If adding_3_value > 0,then decrease right pointer by 1 and in while loop, check If current right_pt value is same as upcoming next right_pt value, skip and decrement right_pt by one
# when left_pt is greater than right_pt, exit the while loop


nums = [-1,0,1,2,-1,-4]     
nums.sort()   
result = []   # Create empty list to store the result values
if len(nums) < 3:
    print([])

for i in range(0, len(nums)-2):
    if nums[i] == nums[i-1] and i > 0 :
        continue 
    out_ele = nums[i]
    left_pt = i+1
    right_pt = len(nums)-1
    while left_pt < right_pt:
        adding_3_value = nums[i] + nums[left_pt] + nums[right_pt]
        if adding_3_value == 0:
            result.append([nums[i],nums[left_pt],nums[right_pt]])
            left_pt = left_pt+1
            right_pt = right_pt-1
            while left_pt < right_pt and nums[left_pt] == nums[left_pt-1]:           # to skip checking the same value, If current left_pt value is same as previous left_pt value, skip and increment
                left_pt = left_pt+1
            while left_pt < right_pt and nums[right_pt] == nums[right_pt+1]:           # to skip checking the same value, If current right_pt value is same as upcoming next right_pt value, skip and decrement
                right_pt = right_pt-1
        elif adding_3_value < 0:
            left_pt=left_pt+1
            while nums[left_pt] == nums[left_pt-1] and left_pt < right_pt:           # to skip checking the same value, If current left_pt value is same as previous left_pt value, skip and increment
                left_pt = left_pt+1
        elif adding_3_value > 0:
            right_pt= right_pt-1
            while nums[right_pt] == nums[right_pt+1] and left_pt < right_pt:           # to skip checking the same value, If current right_pt value is same as upcoming next right_pt value, skip and decrement
                right_pt = right_pt-1
print(result)









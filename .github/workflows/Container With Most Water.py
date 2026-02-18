# 11. Container With Most Water -> Time Complexity → O(n) Space Complexity → O(1)
# Input: height = [1,8,6,2,5,4,8,3,7], Output: 49
# Two pointer approach: Set left pointer at 0 and right pointer at len(height)-1
# while loop until pointers meet, Calculate distance of container (rt_pt - lf_pt) and find minimum height of the two pointers,
# Calculate area (length * breadth) and update result_max variable by comparing with current area value and previous result_max value.
# Move the pointer which has smaller height value, if left pointer element is smaller than right pointer element → move left pointer, else move right pointer. 
# Finally return result_max value which is the maximum area of container.


height = [1,8,6,2,5,4,8,3,7]
lf_pt = 0
rt_pt = len(height)-1
breadth = 0
result_max = 0
while lf_pt < rt_pt:
    breadth = rt_pt - lf_pt
    min_ele = min(height[lf_pt], height[rt_pt])
    area = min_ele * breadth
    result_max = max(result_max, area)
    if height[lf_pt] < height[rt_pt]:
        lf_pt+=1
    else:
        rt_pt-=1
print(result_max)

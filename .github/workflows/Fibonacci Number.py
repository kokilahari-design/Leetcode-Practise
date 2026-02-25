
# 509. Fibonacci Number :  
# F(0) = 0, F(1) = 1, F(n) = F(n - 1) + F(n - 2), for n > 1.
# Input: n = 4, Output: 3 (return last index value), Explanation: F(4) = F(3) + F(2) = 2 + 1 = 3.

# Using Dynamic Programming approach: In Python, list data structure is a dynamic 1D array . It automatically resizes as you add or remove elements.  
# Use Dynamic approach when want to avoid redundant calculations by storing previously computed results. Final result depends on the previous values and initial value
# check if n is 0 or 1, return n, if not specified, shows index out of range error, as loop starts from 2.
# create a dp array of size n+1 by initializing all values to 0, this array will store the Fibonacci numbers up to n.
# initialize dp[0] = 0 and dp[1] = 1, Iterate from 2 to n index 
# Fill the dp array using the relation dp[i] = dp[i-1] + dp[i-2], finally return the last element of the dp array which is the nth Fibonacci number. 

# Dynamic Approach: Time complexity -> O(n), Space complexity -> O(n) as it stores all the (n+1) values in the dp array.

class Solution(object):
    def fib(self, n):
        if n==0:
            return 0
        if n==1:
            return 1
        dp = [0]*(n+1)    # create dynamic array with initial values as 0 till n+1 to store up to n using repetition. As dp array automatically resizes
        dp[0] = 0
        dp[1] = 1
        for i in range(2,len(dp)):
            dp[i] = dp[i-1] + dp[i-2]
        return dp[-1]

n=4
obj = Solution()
print(obj.fib(n))


# Fibonacci Number : Time complexity -> O(n), Space complexity -> O(1) Instead of storing whole array, store only two variables. 
# Because Fibonacci only needs the last 2 values, not entire array.

n = 4
if n == 0:
    print(0)
elif n == 1:
    print(1)
else:
    prev2 = 0
    prev1 = 1

    for i in range(2, n + 1):
        curr = prev1 + prev2
        prev1 = curr
        prev2 = prev1
        

    print(prev1)

# Recursion Approach:  Time complexity -> O(2^n), Space complexity -> O(n) 
def fib(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fib(n-1) + fib(n-2)
print(fib(4))

fib(4)
 ├── fib(3)
 │    ├── fib(2)
 │    │    ├── fib(1) → 1
 │    │    └── fib(0) → 0
 │    └── fib(1) → 1
 └── fib(2)
      ├── fib(1) → 1
      └── fib(0) → 0

fib(2) is calculated twice
fib(1) is calculated multiple times
It's Slow, Because of overlapping subproblems, Same Fibonacci values are recomputed again and again.

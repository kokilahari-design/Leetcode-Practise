# 9. Palindrome Number
# Input: x = 121 Output: true Explanation: 121 reads as 121 from left to right and from right to left.

# Reverse the Number approach: Time Complexity = O(log x) or O(n) Space Complexity = O(1)

def isPalindrome(x):
    copy_x = x
    total = 0
    while x > 0:
        rem = x % 10
        total=total*10+rem
        x = x//10
    if total == copy_x:
        return True
    else:
        return False

  print(isPalindrome(121))

# Two pointer method:  Time complexity is O(n) Space Complexity = O(n) due to string conversion

def isPalindrome(x):
    s = str(x)
    lf_pt =0
    rt_pt = len(s)-1
    while lf_pt < rt_pt:
        if s[lf_pt] == s[rt_pt]:
            lf_pt +=1
            rt_pt -=1
        else:
            return False
    return True

print(isPalindrome(121))



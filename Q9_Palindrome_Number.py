# Ian Macdonald 
# 2024/02/09

# Description:

# Given an integer x, return true if x is a 
# palindrome, and false otherwise.


# Example 1:

# Input: x = 121
# Output: true
# Explanation: 121 reads as 121 from left to right and from right to left.
# Example 2:

# Input: x = -121
# Output: false
# Explanation: From left to right, it reads -121. From right to left, it becomes 121-.
# Therefore it is not a palindrome.
# Example 3:

# Input: x = 10
# Output: false
# Explanation: Reads 01 from right to left. Therefore it is not a palindrome.
 

# Constraints:

# -2^31 <= x <= 2^31 - 1

# Intial thoughts:
# Since a Palindrome is a mirror, we only need to loop through the first half of the list.
# Then compare it to the object in the mirrored index. 
# Abandon the search immediately if a bad value is found. 



class Solution:
    def isPalindrome(self, x: int) -> bool:
        x_str = str(x)
        x_len = len(x_str)
        for i in range(0, (x_len//2)):
            if not (x_str[i] == x_str[-(i+1)]):
                return False
        return True

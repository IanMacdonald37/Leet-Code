# Ian Macdonald
# 2024/02/10

# Description:

# Write a function to find the longest common prefix string amongst an array of strings.

# If there is no common prefix, return an empty string "".
 

# Example 1:

# Input: strs = ["flower","flow","flight"]
# Output: "fl"
# Example 2:

# Input: strs = ["dog","racecar","car"]
# Output: ""
# Explanation: There is no common prefix among the input strings.
 

# Constraints:

# 1 <= strs.length <= 200
# 0 <= strs[i].length <= 200
# strs[i] consists of only lowercase English letters.


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        running_prefix = strs[0]
        for i in range (1, len(strs)):
            a = 0
            current_word = strs[i]
            matching_letters = ''
            while a < len(current_word) and a < len(running_prefix):
                if current_word[a] == running_prefix[a]:
                    matching_letters += running_prefix[a]
                else:
                    break

                a += 1

            running_prefix = matching_letters
# Ian Macdonald 
# 2024/02/09

# Description:

# Given an array of integers nums and an integer target, 
# return indices of the two numbers such that they add up to target.
# You may assume that each input would have exactly one solution, 
# and you may not use the same element twice.
# You can return the answer in any order.


# Example 1:

# Input: nums = [2,7,11,15], target = 9
# Output: [0,1]
# Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
# Example 2:

# Input: nums = [3,2,4], target = 6
# Output: [1,2]
# Example 3:

# Input: nums = [3,3], target = 6
# Output: [0,1]
 

# Constraints:

# 2 <= nums.length <= 10^4
# -10^9 <= nums[i] <= 10^9
# -10^9 <= target <= 10^9
# Only one valid answer exists.


# Intial thoughts:

# Loop throught the list twice to observe every possible combination of the passed numbers
# return their indexs if they equal the target

# Issues:
# the time complexity on this is O(n^2) since we go through the list twice

# Solution:
# Make a hashmap as we loop through the list the first time,
# reducing our time complexity to O(n) as the hash map has a linear time complexity.



class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        '''a = 0
        l = len(nums)

        while a < l:
            b = a + 1

            while b < l:
                if nums[a] + nums[b] == target:
                    return [a,b]
                b += 1

            a += 1
        '''
        number_map = {}
        n = len(nums)
        for i in range(0, n):
            difference = target - nums[i]
            if difference in number_map.keys():
                return [number_map[difference],i]
            number_map[nums[i]] = i
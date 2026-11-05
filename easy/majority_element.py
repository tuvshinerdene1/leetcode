# 169. Majority Element

# Given an array nums of size n, return the majority element.

# The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element always exists in the array.

 

# Example 1:

# Input: nums = [3,2,3]
# Output: 3

# Example 2:

# Input: nums = [2,2,1,1,1,2,2]
# Output: 2

 

# Constraints:

#     n == nums.length
#     1 <= n <= 5 * 104
#     -109 <= nums[i] <= 109
#     The input is generated such that a majority element will exist in the array.

class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        counts = {}
        threshold = len(nums) // 2

        for num in nums : 
            counts[num] = counts.get(num, 0) + 1
            if counts[num] > threshold:
                return num

    def boyerMooreVotingAlgorithm(self, nums:list[int]) -> int:
        candidate = None
        count = 0

        for num in nums:
            if count == 0:
                candidate = num

            count += 1 if num == candidate else -1
        return candidate
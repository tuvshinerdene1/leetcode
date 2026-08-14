# 3090. Maximum Length Substring With Two Occurrences
# Given a string s, return the maximum length of a substring
#  such that 
# it contains at most two occurrences of each character.

# Example 1:
# Input: s = "bcbbbcba"
# Output: 4

# Explanation:
# The following substring has a length of 4 and contains at most two occurrences of each character: "bcbbbcba".

# Example 2:
# Input: s = "aaaa"
# Output: 2

# Explanation:
# The following substring has a length of 2 and contains at most two occurrences of each character: "aaaa".

class Solution:
    def maximumLengthSubstring(self, s: str) -> int:
        if not s:
            return 0

        char_count = {}
        left = 0
        max_len = 0

        for right in range(len(s)):
            # add the curret character to the window
            char = s[right]
            char_count[char] = char_count.get(char, 0) + 1

            # if any character exceeds 2 occurrences, shrink the window from the left
            while char_count[char] > 2:
                left_char = s[left]
                char_count[left_char] -= 1
                left += 1

            # update the maximum lengt found so far
            max_len = max ( max_len, right - left + 1)
        
        return max_len
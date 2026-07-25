# 5. Longest Palindromic Substring
# Given a string s, return the longest in s.


# Example 1:
# Input: s = "babad"
# Output: "bab"
# Explanation: "aba" is also a valid answer.

# Example 2:
# Input: s = "cbbd"
# Output: "bb"

# def longestPalindrome( s:str) -> str:
#     if s == "":
#         return ""

#     result = s[0]
#     left = 0
#     length = len(s)

#     while left < length:
#         for right in range(left,length):
#             current = s[left:right]
#             if is_palindrome(current):
#                 if len(result) < len(current):
#                     result = current
#         left += 1
#     return result


# def is_palindrome(s:str)-> bool:
#     length = len(s)
#     for i in range(length//2):
#         if s[i] != s[length - 1 -i]:
#             return False
#     return True

def longestPalindrome(s:str) -> str:
    if not s:
        return ""

    start = 0
    max_len = 0

    def expand_around_center(left:int, right:int) -> int:
        while left>= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        return right - left - 1

    for i in range(len(s)):
        len1 = expand_around_center(i, i)
        len2 = expand_around_center(i, i + 1)

        current_max = max(len1, len2)

        if current_max > max_len:
            max_len = current_max
            start = i - (current_max - 1) // 2
            
    return s[start:start + max_len]


def main():
    print(longestPalindrome("babad"))
    print(longestPalindrome("cbbd"))
    print(longestPalindrome("hahaaaah"))

if __name__ == "__main__":
    main()
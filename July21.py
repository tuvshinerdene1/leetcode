# Given two strings needle and haystack, return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.

 

# Example 1:
# Input: haystack = "sadbutsad", needle = "sad"
# Output: 0
# Explanation: "sad" occurs at index 0 and 6.
# The first occurrence is at index 0, so we return 0.

# Example 2:
# Input: haystack = "leetcode", needle = "leeto"
# Output: -1
# Explanation: "leeto" did not occur in "leetcode", so we return -1.

# Solution #1

# def strStr( haystack: str, needle: str) -> int:
#         for right in range(len(haystack)):
#              if haystack[right] == needle[0]:
#                   print(haystack[right:right+len(needle)])
#                   if haystack[right:right+len(needle)] == needle:
#                        return right
#         return -1

def strStr( haystack: str, needle: str) -> int:
    if not needle:
        return 0
    
    h_len, n_len = len(haystack), len(needle)

    for i in range(h_len - n_len + 1):
        if haystack[i: i+n_len] == needle:
            return i
    
    return -1
             


def main():
    print("Leetcode july 21st problem")
    print(strStr("sadbutsad", "sad"))
    print(strStr("leetcode", "leeto"))


if __name__ == "__main__":
    main()
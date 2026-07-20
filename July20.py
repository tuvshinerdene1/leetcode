#  Given a string s, find the length of the longest without duplicate characters
#  Example 1:
#  Input: s = "abcabcbb"
#  Output: 3
#  Explanation: The answer is "abc", with the length of 3. Note that "bca" and "cab" are also correct answers
#  Example 2:
#  Input: s = "bbbbb"
#  Output: 1
#  Explanation: The answer is "b", with the length of 1
#  Example 3:
#  Input: s = "pwwkew"
#  Output: 3
#  Explanation: The answer is "wke", with the length of 3.
#  Notice that the answer must be a substring, "pwke" is a subsequence and not a substring
#  Constraints:
#      0 <= s.length <= 5 * 104
#      s consists of English letters, digits, symbols and spaces.


def lengthOfLongestSubstring(s):
    # track characters currently inside window
    seen_chars = set()

    left = 0
    max_len = 0

    # loop through the stirng with the right pointer
    for right in range(len(s)):
        # if hit a duplicate, shrink the window from the left
        while s[right] in seen_chars:
            seen_chars.remove(s[left])
            left += 1
        
        # add the current character to the window
        seen_chars.add(s[right])

        # calculate the current window size and update max_len if it's larger
        current_window_size = right - left + 1
        max_len = max(max_len, current_window_size)
    
    return max_len

def main():
    print("Leetcode july 20th problem")
    print(lengthOfLongestSubstring("abcabcbb"))
    print(lengthOfLongestSubstring("bbbbb"))
    print(lengthOfLongestSubstring("pwwkew"))

if __name__ == "__main__":
    main()
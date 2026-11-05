# Given a string s consisting of words and spaces, return the length of the last word in the string.
# A word is a maximal consisting of non-space characters only.

# Example 1:
# Input: s = "Hello World"
# Output: 5
# Explanation: The last word is "World" with length 5.

# Example 2:
# Input: s = "   fly me   to   the moon  "
# Output: 4
# Explanation: The last word is "moon" with length 4.

# Example 3:
# Input: s = "luffy is still joyboy"
# Output: 6
# Explanation: The last word is "joyboy" with length 6.

def lengthOfLastWord( s: str) -> int:
    s_list  = s.split()
    # return len(s_list[len(s_list) - 1])
    return len(s_list[-1])

def lengthOfLastWord_space_optimized(s: str) -> int:
    length = 0
    i = len(s) - 1

    # Step 1: skip trailing spaces 
    while i>=0 and s[i] == ' ':
        i -= 1
    
    # step 2: count the length of the last word 
    while i >= 0 and s[i] != ' ':
        length += 1
        i -= 1
    
    return length
    
def main():
    print(lengthOfLastWord("Hello World"))
    print(lengthOfLastWord("   fly me   to   the moon  "))
    print(lengthOfLastWord("luffy is still joyboy"))

    print(lengthOfLastWord_space_optimized("Hello World"))
    print(lengthOfLastWord_space_optimized("   fly me   to   the moon  "))
    print(lengthOfLastWord_space_optimized("luffy is still joyboy"))

if __name__ == "__main__":
    main()
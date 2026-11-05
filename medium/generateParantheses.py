# 22. Generate Parentheses

# Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

# Example 1:

# Input: n = 3
# Output: ["((()))","(()())","(())()","()(())","()()()"]

# Example 2:

# Input: n = 1
# Output: ["()"]


class Solution:
    def generateParenthesis(self, n: int) -> list[str]:
        result = []

        def backtrack(current_string, open_count, close_count):
            # base case: if the string length is 2 * n, all n pairs have been used
            if len(current_string) == 2*n:
                result.append(current_string)
                return

            # choice 1: add an opening paranthesis if we haven't reached n yet
            if open_count < n:
                backtrack(current_string + "(", open_count + 1, close_count)

            # choice 2: add a closing parenthesis if it won't exceed the opening count
            if close_count < open_count:
                backtrack(current_string + ")", open_count, close_count + 1)

        backtrack("", 0, 0)
        return result
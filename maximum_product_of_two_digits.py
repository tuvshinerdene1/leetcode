# You are given a positive integer n.

# Return the maximum product of any two digits in n.

# Note: You may use the same digit twice if it appears more than once in n.

# Example 1:
# Input: n = 31
# Output: 3
# Explanation:
#     The digits of n are [3, 1].
#     The possible products of any two digits are: 3 * 1 = 3.
#     The maximum product is 3.

# Example 2:
# Input: n = 22
# Output: 4
# Explanation:
#     The digits of n are [2, 2].
#     The possible products of any two digits are: 2 * 2 = 4.
#     The maximum product is 4.

# Example 3:
# Input: n = 124
# Output: 8
# Explanation:
#     The digits of n are [1, 2, 4].
#     The possible products of any two digits are: 1 * 2 = 2, 1 * 4 = 4, 2 * 4 = 8.
#     The maximum product is 8.

def maxProduct(n:int) -> int:
    array = []
    number = n
    while number > 0:
        array.append(number % 10)
        number = number // 10
    max1 = max(array)
    array.remove(max1)
    max2 = max(array)

    return max1 * max2
    

def main():
    print(maxProduct(31))
    print(maxProduct(22))
    print(maxProduct(124))

if __name__ == "__main__":
    main()
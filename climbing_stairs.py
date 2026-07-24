# You are climbing a staircase. It takes n steps to reach the top.

# Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

# Example 1:

# Input: n = 2
# Output: 2
# Explanation: There are two ways to climb to the top.
# 1. 1 step + 1 step
# 2. 2 steps

# Example 2:

# Input: n = 3
# Output: 3
# Explanation: There are three ways to climb to the top.
# 1. 1 step + 1 step + 1 step
# 2. 1 step + 2 steps
# 3. 2 steps + 1 step
import math

def climbStairs(n: int) -> int:
    if n <= 2:
        return n

    prev, curr = 1, 2
    for _ in range (3, n + 1):
        prev, curr = curr, prev + curr
    
    return curr

def climbStairs_combanitorics(n: int) -> int:
    total_ways = 0
    for k in range (n // 2 + 1):
        total_moves = n- k
        total_ways += math.comb(total_moves, k)
    return total_ways

def main():
    print(climbStairs(2))
    print(climbStairs(3))
    print(climbStairs_combanitorics(2))
    print(climbStairs_combanitorics(3))
    

if __name__ == "__main__":
    main()
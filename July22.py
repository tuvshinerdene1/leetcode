# Given a sorted array of distinct integers and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

# You must write an algorithm with O(log n) runtime complexity.

 
# Example 1:
# Input: nums = [1,3,5,6], target = 5
# Output: 2

# Example 2:
# Input: nums = [1,3,5,6], target = 2
# Output: 1

# Example 3:
# Input: nums = [1,3,5,6], target = 7
# Output: 4

def searchInsert(nums, target):
    """
        :type nums: List[int]
        :type target: int
        :rtype: int
    """
    length = len(nums)
    for index in range(length):
        if nums[index] == target or nums[index] > target:
            return index
        elif index == length - 1:
            return index + 1
        
def searchInsert_binary(nums, target):
    left , right = 0, len(nums) - 1

    while left <= right:
        mid = (left + right) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            left = mid + 1
        else: 
            right = mid - 1
    # if target is not found, 'left' will be standing at the correct insertion index 
    return left 
        
def main():
    print("leetcode july 22nd problem")
    print(searchInsert([1,3,5,6], 5))
    print(searchInsert([1,3,5,6], 2))
    print(searchInsert([1,3,5,6], 7))

    print(searchInsert_binary([1,3,5,6], 5))
    print(searchInsert_binary([1,3,5,6], 2))
    print(searchInsert_binary([1,3,5,6], 7))
    

if __name__ == "__main__":
    main()
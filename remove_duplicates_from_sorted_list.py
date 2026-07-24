from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        current = head
        
        while current and current.next:
            if current.val == current.next.val:
                # Bypass the duplicate node
                current.next = current.next.next
            else:
                # Move to the next unique node
                current = current.next
                
        return head

# Helper functions for testing
def create_linked_list(arr):
    if not arr:
        return None
    head = ListNode(arr[0])
    current = head
    for val in arr[1:]:
        current.next = ListNode(val)
        current = current.next
    return head

def print_linked_list(head):
    vals = []
    current = head
    while current:
        vals.append(current.val)
        current = current.next
    print(vals)

def main():
    sol = Solution()
    
    # Test Case 1: [1, 1, 2]
    head1 = create_linked_list([1, 1, 2])
    result1 = sol.deleteDuplicates(head1)
    print_linked_list(result1)  # Output: [1, 2]

    # Test Case 2: [1, 1, 2, 3, 3]
    head2 = create_linked_list([1, 1, 2, 3, 3])
    result2 = sol.deleteDuplicates(head2)
    print_linked_list(result2)  # Output: [1, 2, 3]

if __name__ == "__main__":
    main()
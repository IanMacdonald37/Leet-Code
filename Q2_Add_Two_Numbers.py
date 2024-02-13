# Ian Macdonald
# 2024/02/12

# Description:

# You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

# You may assume the two numbers do not contain any leading zero, except the number 0 itself.


# Example 1:

# Input: l1 = [2,4,3], l2 = [5,6,4]
# Output: [7,0,8]
# Explanation: 342 + 465 = 807.
# Example 2:

# Input: l1 = [0], l2 = [0]
# Output: [0]
# Example 3:

# Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
# Output: [8,9,9,9,0,0,0,1]
 

# Constraints:

# The number of nodes in each linked list is in the range [1, 100].
# 0 <= Node.val <= 9
# It is guaranteed that the list represents a number that does not have leading zeros.

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        current_el_1 = l1
        current_el_2 = l2

        l3 = ListNode()
        current_el_3 = l3

        while True:
            sum = current_el_1.val + current_el_2.val + current_el_3.val

            current_el_3.next = ListNode()
            if sum > 9:
                sum -= 10
                current_el_3.next.val += 1
            
            current_el_3.val = sum

            if current_el_1.next == None or current_el_2.next == None:

                if current_el_1.next == None and current_el_2.next is not None:

                    current_el_2 = current_el_2.next
                    current_el_3 = current_el_3.next

                    while True:

                        sum = current_el_2.val + current_el_3.val

                        current_el_3.next = ListNode()
                        if sum > 9:
                            sum -= 10
                            current_el_3.next.val += 1
                        
                        current_el_3.val = sum

                        if current_el_2.next == None:
                            break
                        
                        current_el_2 = current_el_2.next
                        current_el_3 = current_el_3.next

                elif  current_el_1.next is not None and current_el_2.next == None:

                    current_el_1 = current_el_1.next
                    current_el_3 = current_el_3.next

                    while True:

                        print(current_el_3.val)
                        sum = current_el_1.val + current_el_3.val

                        current_el_3.next = ListNode()
                        if sum > 9:
                            sum -= 10
                            current_el_3.next.val += 1
                        
                        current_el_3.val = sum

                        if current_el_1.next is None:
                            break
                        
                        current_el_1 = current_el_1.next
                        current_el_3 = current_el_3.next

                break
            
            current_el_1 = current_el_1.next
            current_el_2 = current_el_2.next
            current_el_3 = current_el_3.next

        if current_el_3.next.val == 0:
            current_el_3.next = None
        return l3
        
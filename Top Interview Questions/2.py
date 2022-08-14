"""
2. Add Two Numbers
Medium

20526

4066

Add to List

Share
You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

 

Example 1:


Input: l1 = [2,4,3], l2 = [5,6,4]
Output: [7,0,8]
Explanation: 342 + 465 = 807.
Example 2:

Input: l1 = [0], l2 = [0]
Output: [0]
Example 3:

Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
Output: [8,9,9,9,0,0,0,1]
 

Constraints:

The number of nodes in each linked list is in the range [1, 100].
0 <= Node.val <= 9
It is guaranteed that the list represents a number that does not have leading zeros.
"""

from audioop import reverse


def main(l1, l2):
    def iterator(ll):
        temp = ""
        head = ll
        while head:
            temp += str(head.val)
            head = head.next
        return int(temp[::-1])

    def convert_to_ll(num):
        num.reverse()
        head = ListNode(int(num[0]), None)
        cur = head
        try:
            for i in num[1:]:
                temp = ListNode(int(i), None)
                cur.next = temp
                cur = cur.next
        except:
            pass
        return head

    num = list(str(iterator(l1) + iterator(l2)))
    return convert_to_ll(num)
"""21. Merge Two Sorted Lists
Easy

Merge two sorted linked lists and return it as a new sorted list. The new list should be made by splicing together the nodes of the first two lists.

Example:

Input: 1->2->4, 1->3->4
Output: 1->1->2->3->4->4

"""
"""def mergeTwoLists(l1, l2):
    if (l1 == None and l2 == None):
            return None
        l = []
        while l1 != None:
            l.append(l1.val)
            l1 = l1.next
        while l2 != None:
            l.append(l2.val)
            l2 = l2.next
        l.sort()
        head = ListNode(l[0])
        cur = head
        for i in range(1, len(l)):
            cur.next = ListNode(l[i])
            cur = cur.next
        return head"""
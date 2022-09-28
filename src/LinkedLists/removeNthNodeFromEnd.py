# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def removeNthFromEnd(self, head, n):
        
        # make a dummy node in case need to modify first node
        dummy = ListNode(0, head)
        slow = dummy
        fast = head
        
        # traverse the list with just the fast node, n times
        while n > 0 and fast:
            fast = fast.next
            n -= 1
        
        # now that fast is ahead of slow by n nodes, traverse the list increasing both until the end
        while fast:
            fast = fast.next
            slow = slow.next
        
        # since slow started at the dummy, the node to be deleted is slow.next
        slow.next = slow.next.next
        # return the head
        return dummy.next
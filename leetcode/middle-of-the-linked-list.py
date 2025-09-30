# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def middleNode(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        nodes = 0
        temp = head
        while temp is not None:
            nodes += 1
            temp = temp.next
        for i in range(1, ((nodes + 1) / 2)):
            head = head.next
        if nodes % 2 == 0:
            head = head.next
        return head
# Problem: Remove Linked List Elements - https://leetcode.com/problems/remove-linked-list-elements/

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeElements(self, head, val):
        
        curNode = head
        prevNode = ListNode(None)

        while curNode:
            if curNode.val == val:
                prevNode.next = curNode.next
                if prevNode.val == None:
                    head = head.next
            else:
                prevNode = curNode

            curNode = curNode.next

        return head
            

        
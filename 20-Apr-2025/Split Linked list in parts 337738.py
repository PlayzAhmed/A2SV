# Problem: Split Linked list in parts - https://leetcode.com/problems/split-linked-list-in-parts/

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def splitListToParts(self, head, k):
        n = 0
        cur = head
        i = 0
        res = []
        
        while cur:
            n += 1
            cur = cur.next

        if n <= k:
            cur = head
            while cur:
                temp = cur
                cur = cur.next
                temp.next = None
                res.append(temp)
                i += 1

            res.extend([None]*(k-i))
        else:
            h = n % k
            n //= k
            seg = 0

            cur = head
            new_head = head
            
            while cur and cur.next and seg < k - 1:
                if n == i and h:
                    temp = cur.next
                    cur.next = None
                    res.append(new_head)
                    cur = new_head = temp
                    i = 0
                    h -= 1
                    seg += 1
                    continue
                elif n-1 == i and not h:
                    temp = cur.next
                    cur.next = None
                    res.append(new_head)
                    cur = new_head = temp
                    i = 0
                    seg += 1
                    continue

                cur = cur.next
                i += 1

            res.append(new_head)

        return res
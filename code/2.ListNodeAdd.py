# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        rest = ListNode(0)
        res = rest
        jinwei = 0
        while ((l1 is not None) or (l2 is not None)):

            if (l1.next is not None or l2.next is not None):  #有任意一边没结束则补全另一边
                if (l1.next is None):
                    l1.next = ListNode(0)
                if (l2.next is None):
                    l2.next = ListNode(0)

            val = l1.val + l2.val + jinwei

            if (val >= 10):
                jinwei = 1
                val -= 10
                if(l1.next is None and l2.next is None):
                    l1.next = ListNode(0)
                    l2.next = ListNode(0)
            else:
                jinwei = 0

            res.next = ListNode(val)
            l1 = l1.next
            l2 = l2.next
            res = res.next

        return rest.next

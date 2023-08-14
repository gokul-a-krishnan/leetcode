# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __str__(self):
        return f"List <{self.val}>"


class Solution:
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        temp = head
        while temp is not None:
            if temp.next is not None:
                g = ListNode(self.gcd(temp.val, temp.next.val), temp.next)
                temp.next = g
                temp = g
            temp = temp.next
        return head

    # Euclidian Algorithm
    def gcd(self, a, b):
        while b:
            a, b = b, a % b
        return abs(a)


if __name__ == '__main__':
    x = ListNode(3)
    x = ListNode(10, x)
    x = ListNode(6, x)
    head = ListNode(18, x)
    input1 = [18, 6, 10, 3]
    output1 = [18, 6, 6, 2, 10, 1, 3]
    sol = Solution()
    h = sol.insertGreatestCommonDivisors(head)
    t = h
    while t is not None:
        print(t.val)
        t = t.next

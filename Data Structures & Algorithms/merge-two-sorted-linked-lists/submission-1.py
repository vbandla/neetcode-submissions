# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        cur1 = list1;
        cur2 = list2;
        orig = head = None;
        
        if cur1 and cur2:
            if cur1.val <= cur2.val :
                head = cur1;
                cur1 = cur1.next;
            else :
                head = cur2;
                cur2 = cur2.next;
            orig = head;
        while cur1 and cur2 :
            if cur1.val <= cur2.val :
                head.next = cur1;
                head = cur1;
                cur1 = cur1.next;
            else :
                head.next = cur2;
                head = cur2;
                cur2 = cur2.next;
        if head :
            print(head.val)
            head.next = cur1 or cur2;
        else:
            print("blank")
            orig = cur1 or cur2;
        
        return orig;
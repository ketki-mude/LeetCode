# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getDecimalValue(self, head: ListNode | None) -> int:

        str_of_values= ""

        while head:
            str_of_values = str_of_values + str(head.val)
            head= head.next

        result= int(f"{str_of_values}", 2)

        return result
            

        

        



        
        
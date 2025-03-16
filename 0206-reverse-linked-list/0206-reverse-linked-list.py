# Definition for singly-linked list.
class ListNode(object):
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next
class Solution(object):
    def reverseList(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        #Brute Force
        '''temp=head
        stack=[]

        while temp is not None:
            stack.append(temp.val)
            temp=temp.next
        temp=head
        while temp is not None:
            temp.val=stack.pop()
            temp=temp.next
        return head'''

        #Optimal
        #initialize temp to head
        temp=head
        #initialize prev to NULL / None
        prev=None
        #Traverse the linked list
        while temp is not None:
            #initialize the front to the next node i.e temp pointing
            #to preserve the refernece
            front=temp.next
            # reverse the arrows by 
            #initializing temp.next to prev
            temp.next=prev
            #now prev is temp
            prev=temp
            #temp is front
            temp=front

        return prev


            
        
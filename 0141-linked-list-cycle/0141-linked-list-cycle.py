# Definition for singly-linked list.
class ListNode(object):
     def __init__(self, x):
         self.val = x
         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """

        #Brute Force
        '''#initialized temp as head
        temp=head
        #hash map
        node_set=set()

        #traversing the linked list
        while temp is not None:
            if temp in node_set:
                return True
            node_set.add(temp)
            temp=temp.next
        return False'''

        #Optimal Solution
        slow=head
        fast=head

        while fast is not None and fast.next is not None:
            slow=slow.next
            fast=fast.next.next

            if slow==fast:
                return True

        return False

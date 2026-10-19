# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: ListNode | None) -> ListNode | None:
        # convert the list to arr of nodes 
        nodes = []
        while head : 
            nodes.append(head)
            head = head.next

        # divide the array pairs 
        def solve(nodes):
            if len(nodes) <= 1:
                return nodes 

            
            mid = len(nodes) // 2
            left = solve(nodes[:mid])
            right = solve(nodes[mid:])               

            l , r = 0 , 0
            merged = []

            while l < len(left) and r < len(right):
                if left[l].val <= right[r].val:
                    merged.append(left[l])
                    l += 1
                else:
                    merged.append(right[r])
                    r += 1

            merged.extend(left[l:])
            merged.extend(right[r:])
            
            return merged

        
        # merge each pair   
        sorted_nodes = solve(nodes)
        
        if not sorted_nodes:
            return None

        for i in range(len(sorted_nodes) - 1):
            sorted_nodes[i].next = sorted_nodes[i + 1]

        sorted_nodes[-1].next = None

        return sorted_nodes[0]

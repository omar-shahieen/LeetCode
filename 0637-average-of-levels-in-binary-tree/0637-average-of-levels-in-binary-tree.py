# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        
        res = [ ]
        q = deque()
        q.append(root)

        while q : 
            lvl_size = len(q)
            lvl_sum = 0

            for _ in range(lvl_size):

                node = q.popleft()
                lvl_sum += node.val

                if node.left:
                    q.append(node.left)
                
                if node.right :
                    q.append(node.right)

            res.append( lvl_sum / lvl_size)

        return res 
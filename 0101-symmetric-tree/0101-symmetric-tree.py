# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        """
        i need queue to apply bfs 
        """

        q = deque()
        q.append(root)

        while q : 
            size = len(q)
            lvl = []
            for _ in range(size):
                node = q.popleft()
                lvl.append(node.left)
                lvl.append(node.right)
                if node.left:
                    q.append(node.left)
                
                if node.right:
                    q.append(node.right)

            l , r = 0 , len(lvl)-1

            while l < r : 
                if not lvl[r] and not lvl[l]:
                    l += 1
                    r -= 1
                    continue
                if not lvl[l] or not lvl[r] :
                    return False

                if  lvl[r].val != lvl[l].val :
                    return False
                r -= 1
                l += 1
            
        return True
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        queue = deque([root])
        res = []
        levelSize = 0

        while queue:
            levelSize = len(queue)
            if not root:
                return []
            pointer = 1
            for _ in range(levelSize):
                node = queue.popleft()
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)   
                pointer += 1  
                if pointer > levelSize:
                    res.append(node.val)        
        return res   
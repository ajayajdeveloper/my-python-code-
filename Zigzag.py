class TreeNode:
     def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
from collections import deque
class Zigzag:

    
    def zigzagLevelOrder(self, root):
        if not root:
            return []
        res = []
        q = collections.deque()

        zigzag = False
        q.append(root)

        while q:
            level = []
            for _ in range(len(q)):
                if zigzag:
                    node = q.pop()
                    level.append(node.val)
                    if node.right:
                        q.appendleft(node.right)
                    if node.left:
                        q.appendleft(node.left)

                else:
                    node = q.popleft()
                    level.append(node.val)
                    if node.left:
                        q.append(node.left)
                    if node.right:
                        q.append(node.right)
            res.append(level)
            zigzag = not zigzag

        return res
root=[3,9,20,None,None,15,7]
z=Zigzag()
a=z.zigzagLevelOrder(root)
print(a)

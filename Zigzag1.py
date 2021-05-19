class TreeNode:

     def __init__(self, val=0, left=None, right=None):

        self.val = val

        self.left = left

        self.right = right



from collections import deque



class Zigzag1:

    def zigzagLevelOrder(self, root):

        if not root:

            return []

        res = []

        q = deque()



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

#create the nodes
three_node = TreeNode(3)
nine_node = TreeNode(9)
fifteen_node = TreeNode(15)
seven_node = TreeNode(7)
twenty_node = TreeNode(20)

#connect the nodes togather to form a tree structure
three_node.left = nine_node
three_node.right = twenty_node

twenty_node.left = fifteen_node
twenty_node.right = seven_node

#instance of the Zigzag class
z=Zigzag1()

a=z.zigzagLevelOrder(three_node)

print(a) 


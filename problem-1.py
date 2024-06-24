# Time Complexity : O(n)

# space complexity : O(n)

# Approach :

# use bfs
# append root left and right
# run a loop, and in every iteration record the size of the queue
# once the size of the queue is exceeded, terminate the list and make a new one

# Breadth first search

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque


class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:

        if not root:
            return []

        self.q = deque()
        self.result = []

        self.result.append([root.val])
        self.bfs(root.left, root.right)

        return self.result

    def bfs(self, rootLeft, rootRight):

        self.q.append(rootLeft)
        self.q.append(rootRight)

        while self.q:

            r = []
            sizeQueue = len(self.q)
            rangeQueue = range(sizeQueue)
            for i in rangeQueue:

                poppedVal = self.q.popleft()

                if poppedVal:
                    r.append(poppedVal.val)
                    if poppedVal.left:
                        self.q.append(poppedVal.left)
                    if poppedVal.right:
                        self.q.append(poppedVal.right)

            if len(r) > 0:
                self.result.append(r)


# Depth first search


# Time Complexity : O(n)

# space complexity : O(h)

# Approach :

# use dfs
#  keep track of level and size of stack
# if size of stack and level are same, create a new list
# and append a element at position arr[level]
# else just keep appending at the current level

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:

        self.final = []
        self.dfs(root, 0)
        return self.final

    def dfs(self, root, level):

        if root is None:
            return None

        if len(self.final) == level:
            r = []
            self.final.append(r)

        self.final[level].append(root.val)
        self.dfs(root.left, level+1)
        self.dfs(root.right, level+1)

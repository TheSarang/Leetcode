# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        if root == None:
            return []
        stack1 = []
        stack2 = []
        output = []
        temp = []
        stack1.append(root)
        output.append([root.val])
        flag = True
        while stack1 != []:
            cur = stack1.pop(-1)
            if flag:
                if cur.right:
                    stack2.append(cur.right)
                    temp.append(cur.right.val)
                if cur.left:
                    stack2.append(cur.left)
                    temp.append(cur.left.val)
            else:
                if cur.left:
                    stack2.append(cur.left)
                    temp.append(cur.left.val)
                if cur.right:
                    stack2.append(cur.right)
                    temp.append(cur.right.val)
            if stack1 == []:
                stack1 = stack2
                stack2 = []
                if temp!=[]:
                    output.append(temp)
                temp = []
                flag = not flag 
        return output
            
    def helper(self, node):
        return [node.right, node.left]

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def _helper(self, node):
        return [node.left, node.right]
    
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        q1 = []
        if not root:
            return []
        num = 0
        list1 = []
        q1.append(root)
        while q1 != []:
            size = len(q1)
            temp = []
            while size>0:
                curr = q1.pop(0)
                temp.append(curr.val)
                if curr.left:
                    q1.append(curr.left)
                if curr.right:
                    q1.append(curr.right)
                size -= 1
            
            if num%2 == 0:
                list1.append(temp)
            else:
                list1.append(temp[::-1])
            num +=1
            
        return list1
   
#------------------------------------------------------------------------------------------------------------

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

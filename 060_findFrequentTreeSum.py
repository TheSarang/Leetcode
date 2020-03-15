# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def findFrequentTreeSum(self, root: TreeNode) -> List[int]:
        array = []
        hashMap = dict()
        maxNum = 0
        returnArray = []
        def _helper(root):
            if root == None:
                return None
            
            left = _helper(root.left)
            right = _helper(root.right)
            
            if left == None and right == None:
                array.append(root.val)
                return root
            elif left == None:
                array.append(root.val + right.val)
                return TreeNode(root.val + right.val)
            elif right == None:
                array.append(root.val + left.val)
                return TreeNode(root.val + left.val)
            else:
                array.append(left.val + right.val + root.val)
                return TreeNode(left.val + right.val + root.val)
        _helper(root)
        for i in range(len(array)):
            if array[i] not in hashMap:
                hashMap[array[i]] = 1
            else:
                hashMap[array[i]] += 1
        for vals in hashMap:
            if hashMap[vals] > maxNum:
                maxNum = hashMap[vals]
        print(hashMap)
        print(array)
        print(maxNum)
        for vals in hashMap:
            if hashMap[vals] == maxNum:
                returnArray.append(vals)
        return returnArray
                

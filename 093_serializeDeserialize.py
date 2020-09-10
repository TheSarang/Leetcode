class Codec:
    def serialize(self, root):
        def _helper(root, string):
            if root == None:
                string += 'None,'
                return string
            string += str(root.val) + ','
            string = _helper(root.left, string)
            string = _helper(root.right, string)
            return string
        # print(_helper(root, ''))
        return _helper(root, '')
        

    def deserialize(self, data):
        def _helper(value):
            if value[0] == 'None':
                value.pop(0)
                return None
            root = TreeNode(value[0])
            value.pop(0)
            root.left = _helper(value)
            root.right = _helper(value)
            return root
        data_list = data.split(',')
        return _helper(data_list)
        

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))

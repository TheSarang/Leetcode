class TrieNode():
    def __init__(self):
        self.children = {}
        self.content = ''
        
class FileSystem:

    def __init__(self):
        self.root = TrieNode()
        
    def find(self, path):
        node = self.root
        if len(path) == 1:
            return node
        for n in path.split('/')[1:]:
            if n not in node.children:
                node.children[n] = TrieNode()
            node = node.children[n]
        return node

    def ls(self, path: str) -> List[str]:
        node = self.find(path)
        if node.content:
            return [path.split('/')[-1]]
        return sorted(node.children.keys())

    def mkdir(self, path: str) -> None:
        self.find(path)

    def addContentToFile(self, filePath: str, content: str) -> None:
        node = self.find(filePath)
        node.content += content

    def readContentFromFile(self, filePath: str) -> str:
        node = self.find(filePath)
        return node.content


# Your FileSystem object will be instantiated and called as such:
# obj = FileSystem()
# param_1 = obj.ls(path)
# obj.mkdir(path)
# obj.addContentToFile(filePath,content)
# param_4 = obj.readContentFromFile(filePath)

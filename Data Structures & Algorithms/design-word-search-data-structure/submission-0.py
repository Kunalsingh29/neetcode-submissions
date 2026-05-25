class TrieNode():
    def __init__(self):
        self.children = [None]*27
        self.is_end = False
class WordDictionary:

    def __init__(self):
        self.root = TrieNode()
        

    def addWord(self, word: str) -> None:
        curr = self.root
        for ch in word:
            idx = ord(ch) - ord('a')
            if curr.children[idx] is None: 
                curr.children[idx] = TrieNode()
            curr = curr.children[idx]
            
        curr.is_end = True
        

    def search(self, word: str) -> bool:
        curr = self.root
        def dfs(node, index):
            if(index == len(word)):
                return node.is_end
            ch = word[index]
            if ch == '.':
                for child in node.children:
                    if child is not None and dfs(child, index+1):
                        return True
                    
                return False

            idx = ord(ch) - ord('a')
            if node.children[idx] is None:
                return False
            return dfs(node.children[idx], index+1)

        return dfs(curr, 0)
            






        


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)
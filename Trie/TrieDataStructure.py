class TrieNode:
    def __init__(self):
        self.children = [None] * 30
        self.countEndOfTuple = 0
        self.countDiffChild = 0
        self.countTotChild = 0

class Trie:
    def __init__(self):
        self.root = self.getNode()
    
    def vocabulary_count(self):
        return self.root.countDiffChild
    
    def total_word_count(self):
        return self.root.countTotChild
    
    def getNode(self):
        return TrieNode()
    
    def _charToIndex(self, ch):
        if ch == '<':
            return 26
        if ch == '>':
            return 27
        if ch == '/':
            return 28
        
        return ord(ch) - ord('a')

    def insert(self, key):
    
        currentNode = self.root
        length = len(key)
    
        parentNodes = []

        for i in range(length):
            parentNodes.append(currentNode)
            currentNode.countTotChild = currentNode.countTotChild + 1
            c = self._charToIndex(key[i])
            if currentNode.children[c] is None:
                currentNode.children[c] = self.getNode()
            currentNode = currentNode.children[c]
        
        if currentNode.countEndOfTuple == 0:
            for parent in parentNodes:
                parent.countDiffChild = parent.countDiffChild + 1
        currentNode.countEndOfTuple = currentNode.countEndOfTuple + 1
    
    def search(self, key):
        currentNode = self.root
        length = len(key)
        for i in range(length):
            c = self._charToIndex(key[i])
            if currentNode.children[c] is None:
                return 0
            currentNode = currentNode.children[c]
        return currentNode.countEndOfTuple
    
    def searchTotChild(self, key):
        currentNode = self.root
        length = len(key)
        for i in range(length):
            c = self._charToIndex(key[i])
            if currentNode.children[c] is None:
                return 0
            currentNode = currentNode.children[c]
        return currentNode.countTotChild
    
    def searchDiffChild(self, key):
        currentNode = self.root
        length = len(key)
        for i in range(length):
            c = self._charToIndex(key[i])
            if currentNode.children[c] is None:
                return 0
            currentNode = currentNode.children[c]
        return currentNode.countDiffChild
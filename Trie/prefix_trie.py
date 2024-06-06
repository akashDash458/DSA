# Implement Trie (Prefix Tree)
########################################################################### 
# Method 1
###########################################################################
class TrieNode:
    def __init__(self):
        self.children = dict()
        self.end_node = False


class Trie:
    def __init__(self):
        self.trie = TrieNode()

    def insert(self, word: str) -> None:
        trie = self.trie
        for c in word:
            if c not in trie.children:
                trie.children[c] = TrieNode()
            trie = trie.children[c]

        trie.end_node = True

    def search(self, word: str) -> bool:
        trie = self.trie
        for c in word:
            if c not in trie.children:
                return False
            trie = trie.children[c]

        return trie.end_node == True

    def startsWith(self, prefix: str) -> bool:
        trie = self.trie
        for c in prefix:
            if c not in trie.children:
                return False
            trie = trie.children[c]

        return True

########################################################################### 
# Method 2
###########################################################################
class SimpleTrie:
    def __init__(self):
        self.trie = dict()

    def insert(self, word):
        t = self.trie
        for w in word:
            if w not in t:
                t[w] = dict()
            t = t[w]
            
        t['#'] = '#' # Signifies End
    
    def startsWith(self, prefix):
        t = self.trie
        for w in prefix:
            if w not in t:
                return False
            t = t[w]
        return True

    def search(self, word):
        return self.startsWith(word + '#')

###########################################################################


def testTrie(obj):
    words = ["apple", "app", "appolo"]
    assert obj.startsWith("apple") == False
    for word in words:
        obj.insert(word)

    assert obj.startsWith("ap")
    assert obj.startsWith("app")
    assert obj.startsWith("apps") == False
    assert obj.search("app")
    assert obj.search("apps") == False
    

def main():
    testTrie(Trie())
    testTrie(SimpleTrie())
    
    print("All Tests Passed !")


if __name__ == "__main__":
    main()

class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end = False
        self.count = 0  

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
            node.count += 1
        node.is_end = True

    def find_kth(self, k):
        return self._find_kth_helper(self.root, k)

    def _find_kth_helper(self, node, k):
        if k <= 0 or not node:
            return ""
        
        for char in sorted(node.children.keys()):
            child = node.children[char]
            if k <= child.count:
                if child.is_end and k == 1:
                    return char
                return char + self._find_kth_helper(child, k - (1 if child.is_end else 0))
            k -= child.count

        return ""  

def main():
    n = int(input())
    trie = Trie()
    
    for _ in range(n):
        command = input().strip()
        if command.isdigit():
            k = int(command)
            print(trie.find_kth(k))
        else:
            trie.insert(command)

if __name__ == "__main__":
    main()
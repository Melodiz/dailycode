class Deque:
    def __init__(self):
        self.items = []

    def append(self, item):
        self.items.append(item)

    def popleft(self):
        if not self.items:
            raise IndexError()
        return self.items.pop(0)

    def __bool__(self):
        return bool(self.items)

class TrieNode:
    def __init__(self):
        self.children = {}
        self.fail = None
        self.output = []
        self.word_end = False

def build_trie(words):
    root = TrieNode()
    for i, word in enumerate(words):
        node = root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.word_end = True
        node.output.append(i)
    return root

def build_automaton(root):
    queue = Deque()
    queue.append(root)
    while queue:
        current = queue.popleft()
        for char, child in current.children.items():
            queue.append(child)
            failure = current.fail
            while failure and char not in failure.children:
                failure = failure.fail
            child.fail = failure.children[char] if failure else root
            child.output += child.fail.output

def search(text, root):
    current = root
    results = [False] * len(words)
    for char in text:
        while current and char not in current.children:
            current = current.fail
        if not current:
            current = root
            continue
        current = current.children[char]
        for index in current.output:
            results[index] = True
    return results

text = input().strip()
m = int(input())
words = [input().strip() for _ in range(m)]

root = build_trie(words)
build_automaton(root)

results = search(text, root)

for result in results:
    print("Yes" if result else "No")
class WordDictionary:

    def __init__(self):
        self.children = {}
        self.isEnd = False

    def addWord(self, word: str) -> None:
        curr = self

        for ch in word:
            if ch not in curr.children:
                curr.children[ch] = WordDictionary()

            curr = curr.children[ch]

        curr.isEnd = True

    def search(self, word: str) -> bool:
        def dfs(index, node):
            if index == len(word):
                return node.isEnd

            ch = word[index]

            if ch == '.':
                for child in node.children.values():
                    if dfs(index + 1, child):
                        return True
                return False

            else:
                if ch not in node.children:
                    return False
                
                return dfs(index + 1, node.children[ch])

        return dfs(0, self)

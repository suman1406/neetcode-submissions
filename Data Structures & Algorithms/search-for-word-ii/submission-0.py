class TrieNode:
    def __init__(self):
        self.children = {}
        self.word = None

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        root = TrieNode()

        for word in words:
            curr = root

            for ch in word:
                if ch not in curr.children:
                    curr.children[ch] = TrieNode()
                curr = curr.children[ch]

            curr.word = word

        rows = len(board)
        cols = len(board[0])

        res = []

        def dfs(r, c, node):
            if (
                r < 0 or r >= rows or
                c < 0 or c >= cols or
                board[r][c] not in node.children
            ):
                return
            
            ch = board[r][c]
            next_node = node.children[ch]

            if next_node.word:
                res.append(next_node.word)
                next_node.word = None

            board[r][c] = '#'

            dfs(r + 1, c, next_node)
            dfs(r - 1, c, next_node)
            dfs(r, c + 1, next_node)
            dfs(r, c - 1, next_node)

            board[r][c] = ch
        for r in range(rows):
            for c in range(cols):
                dfs(r, c, root)

        return res
        
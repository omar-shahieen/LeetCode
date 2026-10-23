class TrieNode:
    def __init__(self):
        self.children = {}
        self.word = None


class Solution:
    def findWords(
        self, board: list[list[str]], words: list[str]
    ) -> list[str]:

        if not board or not board[0] or not words:
            return []

        root = TrieNode()

        # Build Trie
        for word in words:
            node = root
            for char in word:
                if char not in node.children:
                    node.children[char] = TrieNode()
                node = node.children[char]

            node.word = word

        m, n = len(board), len(board[0])
        res = []

        def dfs(i, j, parent):
            char = board[i][j]

            # Follow the Trie directly
            if char not in parent.children:
                return

            node = parent.children[char]

            # Found a complete word
            if node.word is not None:
                res.append(node.word)
                node.word = None  # Avoid duplicates

            # Mark visited
            board[i][j] = "#"

            # Explore neighbors
            if i > 0:
                dfs(i - 1, j, node)
            if i + 1 < m:
                dfs(i + 1, j, node)
            if j > 0:
                dfs(i, j - 1, node)
            if j + 1 < n:
                dfs(i, j + 1, node)

            # Restore the board
            board[i][j] = char

            # Prune exhausted Trie branches
            if not node.children and node.word is None:
                del parent.children[char]

        for i in range(m):
            for j in range(n):
                dfs(i, j, root)

                # All words have been found
                if not root.children:
                    return res

        return res
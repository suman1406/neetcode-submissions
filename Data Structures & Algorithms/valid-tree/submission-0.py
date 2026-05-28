class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:

        if len(edges) != n - 1:
            return False

        edgeLog = {i: [] for i in range(n)}

        for key, value in edges:
            edgeLog[key].append(value)
            edgeLog[value].append(key)

        visit = set()

        def dfs(node, parent):
            if node in visit:
                return False

            visit.add(node)

            for leaf in edgeLog[node]:
                if leaf == parent:
                    continue

                if not dfs(leaf, node):
                    return False

            return True

        if not dfs(0, -1):
            return False

        return len(visit) == n
class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        graph = {ch: set() for word in words for ch in word}
        indegree = {ch: 0 for ch in graph}

        for i in range(len(words) - 1):
            w1 = words[i]
            w2 = words[i + 1]

            if len(w1) > len(w2) and w1[:len(w2)] == w2:
                return ""

            for j in range(min(len(w1), len(w2))):
                if w1[j] != w2[j]:
                    parent = w1[j]
                    child = w2[j]

                    if child not in graph[parent]:
                        graph[parent].add(child)
                        indegree[child] += 1

                    break

        q = deque()
        for ch in indegree:
            if indegree[ch] == 0:
                q.append(ch)

        res = []

        while q:
            ch = q.popleft()

            res.append(ch)

            for nei in graph[ch]:
                indegree[nei] -= 1

                if indegree[nei] == 0:
                    q.append(nei)

        if len(res) != len(indegree):
            return ""

        return "".join(res)
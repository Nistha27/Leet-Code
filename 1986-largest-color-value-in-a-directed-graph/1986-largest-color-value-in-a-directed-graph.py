from collections import deque, defaultdict
class Solution(object):
    def largestPathValue(self, colors, edges):
        n = len(colors)
        graph = defaultdict(list)
        indegree = [0] * n

        for u, v in edges:
            graph[u].append(v)
            indegree[v] += 1

        # Topological sort with color count tracking
        queue = deque()
        color_count = [[0] * 26 for _ in range(n)]
        
        # Initialize queue with nodes having 0 indegree
        for i in range(n):
            if indegree[i] == 0:
                queue.append(i)
        
        visited = 0
        max_color_value = 0

        while queue:
            node = queue.popleft()
            visited += 1
            color_index = ord(colors[node]) - ord('a')
            color_count[node][color_index] += 1
            max_color_value = max(max_color_value, color_count[node][color_index])

            for neighbor in graph[node]:
                for c in range(26):
                    color_count[neighbor][c] = max(color_count[neighbor][c], color_count[node][c])
                indegree[neighbor] -= 1
                if indegree[neighbor] == 0:
                    queue.append(neighbor)

        # If not all nodes were visited, there's a cycle
        return max_color_value if visited == n else -1

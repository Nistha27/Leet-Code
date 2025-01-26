from collections import defaultdict, deque

class Solution(object):
    def maximumInvitations(self, favorite):
        """
        :type favorite: List[int]
        :rtype: int
        """
        N = len(favorite)
        visited = [False] * N
        longest_cycle = 0
        length_2_cycles = []

        # Detect cycles and their lengths
        for i in range(N):
            if visited[i]:
                continue
            path = []
            cur = i
            while not visited[cur]:
                visited[cur] = True
                path.append(cur)
                cur = favorite[cur]
            if cur in path:
                cycle_start = path.index(cur)
                cycle_length = len(path) - cycle_start
                if cycle_length == 2:
                    length_2_cycles.append((path[cycle_start], path[cycle_start + 1]))
                longest_cycle = max(longest_cycle, cycle_length)

        # Reverse graph for BFS
        reverse_graph = defaultdict(list)
        for src, dst in enumerate(favorite):
            reverse_graph[dst].append(src)

        # BFS to calculate chain length
        def bfs(node, exclude):
            queue = deque([(node, 0)])
            max_length = 0
            while queue:
                cur, length = queue.popleft()
                max_length = max(max_length, length)
                for neighbor in reverse_graph[cur]:
                    if neighbor != exclude:
                        queue.append((neighbor, length + 1))
            return max_length

        # Calculate the sum of chains for 2-cycles
        chain_sum = 0
        for n1, n2 in length_2_cycles:
            chain_sum += bfs(n1, n2) + bfs(n2, n1) + 2

        return max(chain_sum, longest_cycle)

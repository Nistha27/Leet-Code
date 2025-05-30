class Solution(object):
    def closestMeetingNode(self, edges, node1, node2):
        def get_distances(start):
            dist = [-1] * len(edges)
            curr = start
            distance = 0
            while curr != -1 and dist[curr] == -1:
                dist[curr] = distance
                curr = edges[curr]
                distance += 1
            return dist

        dist1 = get_distances(node1)
        dist2 = get_distances(node2)

        min_dist = float('inf')
        result = -1

        for i in range(len(edges)):
            if dist1[i] != -1 and dist2[i] != -1:
                max_dist = max(dist1[i], dist2[i])
                if max_dist < min_dist:
                    min_dist = max_dist
                    result = i
                elif max_dist == min_dist and i < result:
                    result = i

        return result

        
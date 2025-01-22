class Solution(object):
    def highestPeak(self, isWater):
        """
        :type isWater: List[List[int]]
        :rtype: List[List[int]]
        """
        ROWS,COLS=len(isWater),len(isWater[0])
        q=deque()
        res=[[-1]* COLS for _ in range(ROWS)]

        for r in range(ROWS):
            for c in range(COLS):
                if isWater[r][c]:
                    q.append((r,c))
                    res[r][c]=0
        while q:
            r,c = q.popleft()
            h=res[r][c]
            neigh=[[r+1,c],[r,c+1],[r-1,c],[r,c-1]]
            for nr,nc in neigh:
                if(nr<0 or nc<0 or
                nr==ROWS or nc==COLS or
                res[nr][nc]!=-1
                ):
                    continue
                q.append((nr,nc))
                res[nr][nc]=h+1
        return res

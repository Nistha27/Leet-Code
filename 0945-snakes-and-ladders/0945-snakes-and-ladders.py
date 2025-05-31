from collections import deque
class Solution(object):
    def snakesAndLadders(self, board):
        n = len(board)

        def get_board_position(s):
            """Convert a square number to board coordinates."""
            quot, rem = divmod(s - 1, n)
            row = n - 1 - quot
            col = rem if quot % 2 == 0 else n - 1 - rem
            return row, col

        visited = [False] * (n * n + 1)
        queue = deque()
        queue.append((1, 0))  # (current square, steps)
        visited[1] = True

        while queue:
            curr, steps = queue.popleft()
            for move in range(1, 7):
                next_square = curr + move
                if next_square > n * n:
                    continue
                r, c = get_board_position(next_square)
                if board[r][c] != -1:
                    next_square = board[r][c]
                if next_square == n * n:
                    return steps + 1
                if not visited[next_square]:
                    visited[next_square] = True
                    queue.append((next_square, steps + 1))
        
        return -1

        
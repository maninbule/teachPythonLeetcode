'''
面试题
https://leetcode.cn/problems/game-of-life/description/
'''


class Solution:
    def gameOfLife(self, board: list[list[int]]) -> None:
        if len(board) == 0:
            return
        n, m = len(board), len(board[0])
        ans = [[0] * m for i in range(n)]
        for i in range(n):
            for j in range(m):
                live = 0
                for dx in [-1, 0, 1]:
                    for dy in [-1, 0, 1]:
                        if dx == 0 and dy == 0:
                            continue
                        x = i + dx
                        y = j + dy
                        if x < 0 or x >= n or y < 0 or y >= m:
                            continue
                        if board[x][y] == 1:
                            live += 1
                if board[i][j] == 1:
                    if live < 2:
                        ans[i][j] = 0
                    elif live == 2 or live == 3:
                        ans[i][j] = 1
                    elif live > 3:
                        ans[i][j] = 0
                else:
                    if live == 3:
                        ans[i][j] = 1
        board = ans
        for i in range(n):
            for j in range(m):
                board[i][j] = ans[i][j]

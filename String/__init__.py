class Solution:
    def dfs(self, grid, x, y):  # 深度优先搜索
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        sum = 1
        n = len(grid)
        m = len(grid[0])

        grid[x][y] = 0
        dir = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        for i in dir:
            x += i[0]
            y += i[1]
            if 0 <= x < n and 0 <= y < m and grid[x][y] == 1:
                sum += self.dfs(grid, x, y)
        return sum


    def maxAreaOfIsland(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        mx = 0
        n = len(grid)
        m = len(grid[0])
        for i in range(n):
           for j in range(m):
               if grid[i][j]:
                   mx = max(self.dfs(grid, i, j), mx);
        return mx

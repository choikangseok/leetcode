class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        count = 0
        self.m=len(grid[0])
        self.n=len(grid)
        self.grid = grid
        

        
        for i in range(self.n):
            for j in range(self.m):
                if grid[i][j] =="1" :
                    count = count + 1
                    self.solve(i, j)
                        
                else:
                    pass
        return count
#     self.solve(m,n)
#     def solve(self, i, j):
#         print(self.grid)
        
    def solve(self, i, j):
        
        #동
        if j+1 < self.m:
            if self.grid[i][j+1] == "1":
                self.grid[i][j+1]="0"
                self.solve(i, j+1)
        #서
        if j-1 >= 0:
            if self.grid[i][j-1] == "1":
                self.grid[i][j-1]="0"
                self.solve(i, j-1)
        #남
        if i+1 < self.n:
            if self.grid[i+1][j] == "1":
                self.grid[i+1][j]="0"
                self.solve(i+1, j)
        #북
        if i-1 >= 0:
            if self.grid[i-1][j] == "1":
                self.grid[i-1][j]="0"
                self.solve(i-1, j)
        
        
        
        
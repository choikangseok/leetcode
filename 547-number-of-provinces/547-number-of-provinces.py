class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        self.n = len(isConnected)
        
        self.isConnected = isConnected
        count=0
        
        for i in range(self.n):
            for j in range(self.n):
                if isConnected[i][j] == 1 :
                    self.isConnected[i][j]=0
                    if i == j :
                        # print("main", i,j, self.isConnected)
                        count= count+1
                    else:
                        self.solve(j)
                    
        return count
                    
    def solve(self,j):
        for k in range(self.n):
            if self.isConnected[j][k] == 1 :
                self.isConnected[j][k]=0
                self.solve(k)
                    
        
        
    
            
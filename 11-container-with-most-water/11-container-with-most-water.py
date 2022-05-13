class Solution:
    def maxArea(self, height: List[int]) -> int:
        
        width = len(height)-1
        
        maxV = 0
        i=0
        j=0
        
        while True:
            
            square = min(height[i], height[width-j]) * (width-j-i)
            if square > maxV:
                maxV = square
                
            if height[i] < height[width-j]:
                i+=1
            else:
                j+=1
                
            if i == (width-j) :
                break
                
        
        
        
        return maxV
                
                
            
            
            
        
        
        
class Solution:
    def jump(self, nums: List[int]) -> int:
        
        res = 0 
        l = r = 0
        
        while r < len(nums) - 1:
            far = 0
            for i in range(l, r+1):
                far = max(nums[i]+i, far)
            res= res+1
            l= r+1
            r= far
        
        
        
        return res
    
        
                    
            
                
            
                
            
        
        
    
        
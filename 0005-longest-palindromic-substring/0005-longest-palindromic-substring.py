class Solution:
    def longestPalindrome(self, s: str) -> str:
        
        initlen=len(s) #변하지 않는값
        leng=len(s)
        answer = 0
        
        if leng == 1:
            return s
            
        
        while True:
            i=0
            while True:
                if s[i:i+leng] == s[i:i+leng][::-1]:
                    return s[i:i+leng]
                if leng+i == initlen:
                    leng=leng-1
                    break
                i=i+1
        
                
                    
                    
                    
            
            
            
            
        
        
        
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l=0
        r=0
        answer=0
        
        if len(s) <=1:
            return len(s)
            
        
        while l != len(s)-1:
            
            # if len(s)-l < answer:
            #     break
            
            if len(set(s[l:r])) == r-l:
                answer=max(answer, r-l)
                r=r+1
            
            else:
                l=l+1
                
        return answer
                
            
            
            
            
            
        
        
        
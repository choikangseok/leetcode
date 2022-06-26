class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        
        leftsum = 0
        rightsum = 0
        
        # start 
        
        value = sum(cardPoints[:k])
        max_v = value
        
        for i in range(k):
            value = value - cardPoints[k-1-i] + cardPoints[-(1+i)]
            max_v = max(value, max_v)
        return max_v
            
            
            
        
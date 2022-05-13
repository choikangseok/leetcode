class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        # fL = firstList[-1][-1]
        # sL = secondList[-1][-1]
        
        ans =[]
        for first_item in firstList:
            for second_item in secondList:
                if first_item[1] < second_item[0]:
                    break
                
                left = max(first_item[0], second_item[0])
                right = min(first_item[1], second_item[1])
                if left <=right:
                    ans.append([left,right])    
                
                
                    
                    
                    
                
            
        
                
                
        return ans
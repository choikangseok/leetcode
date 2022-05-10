from collections import deque
class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        
        Ds = ""
        Dt = ""
        
        for item in s:
            if item == "#":
                Ds = Ds[:-1]
            else:
                Ds = Ds+item
        
        for item in t:
            if item == "#":
                Dt = Dt[:-1]
            else:
                Dt = Dt+item
                
        if Ds == Dt:
            return True
        else:
            return False
            
            
        
        
        
        
       
        
        
        
        
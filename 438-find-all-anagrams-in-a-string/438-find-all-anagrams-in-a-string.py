from collections import Counter

class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        
        
        dict_s=Counter("abcdefghijklmnopqrstuvwxyz")
        dict_p=Counter(p)
        ans = []
        for k,v in dict_p.items():
            dict_s[k]=0
        
            
        for item in s[0:len(p)]:
            dict_s[item]+=1
            for k,v in dict_p.items():
                if dict_s[k] >= v:
                    pass
                else:
                    break
            else:
                ans.append(0)
                     
        for i in range(1, len(s)-len(p)+1):
            #빼고
            dict_s[s[i-1]]-=1
            
            #더하고
            dict_s[s[i-1+len(p)]]+=1
            
            for k,v in dict_p.items():
                if dict_s[k] >= v:
                    pass
                else:
                    break
            else:
                ans.append(i)
            
                
                
                
            
                
                
        return ans
                
            
        
        
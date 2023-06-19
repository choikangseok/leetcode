class Solution:
    def myAtoi(self, s: str) -> int:
        
        if s =='':
            return 0
        
        while True:
            if s[0] == ' ':
                s=s[1:]
                if s=='':
                    return 0
            else:
                break

        sign ='+'
        if (s[0] == '-') or (s[0] == '+'):
            sign=s[0]
            s=s[1:]
        
        if s =='':
            return 0
        while True:
            if s[0] == '0':
                s=s[1:]
                if s=='':
                    return 0
                
            else:
                break
                
        
        back=''
        i=0
        
        while True:
            if (i < len(s)) and (s[i] in '0123456789'):
                back=back+s[i]    
            else:
                break
            i=i+1
        
        if back =='':
            return 0
        
        value = int(sign+'1')* int(back)
        value = min(value, 2 ** 31 - 1)
        value = max(-(2 ** 31), value)
            
        return value
                            
                
            
            
                
                
        
        
        
        
class Solution:
    def convert(self, s: str, numRows: int) -> str:
        
        #example1
        # [P]AYP[A]LIS[H]IRI[N]G.. 3칸씩 뜨워서
        # [P][A]Y[P][A][L]I[S][H][I]R[I][N][G].. 2칸씩 띄워서
        # PAYPALISHIRING
        
        
        #example2
        # [P](A){Y}P{A}(L)[I](S){H}I{R}(I)[N](G)
        
        # numrows - 처음 점프
        # 1 - 1개씩 점프
        # 2 - 2개씩 점프
        # 3 - 4개씩 점프
        # 4 - 6개씩 점프
        # 5 - 8개씩 점프
        # 6 - 10개
        # 2*(numrows-1)
        
        
        
        listN = [[0, c] for c in s]
        strlen=len(s)
        answer=""
        
        if strlen == 1 or numRows ==1:
            return s
        
        
        #첫판에는 0으로 선정함.
        fjump=2*(numRows-1)
        
        i=0
        
        while True:
            
            if i >= len(s):
                i-len(s)
                listN = listN + [[0, "*"] for _ in range(i+1-len(s))]
                listN[-1][0]=1
                answer = answer + "*"*(i+1-len(s) > 0)
                s=s+"*"*(i+1-len(s))
                break
            
            answer = answer + s[i]
            listN[i][0]=1
            i=i+fjump
        
        strlen=len(s)
        
        # print(answer)
        # print(s)
        
        
        #1. 첫판에는 0으로 선정함.
        #2. 양쪽에 0 이 있으면 해당 값을 1로 바꾸고 그 값을 스트링에 넣어줌.
        
         
        while True:
            addindex=[]
            for j in range(strlen):
                # print(listN)
                if listN[j][0] == 0:
                    
                    #왼쪽, 오른쪽
                    if (j-1>=0 and listN[j-1][0]==1) or (j+1<strlen and listN[j+1][0]==1):
                        # listN[j][0]=1
                        addindex.append(j)
                        answer=answer + listN[j][1]
                        # print(answer, listN)
                    
                            
                                
                if len(answer) == strlen:
                    return answer.replace("*","")
            else:
                for item in addindex:
                    listN[item][0]=1
            # print(listN)
            
                

                        
            

            
            
        
        
        
        
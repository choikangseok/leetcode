class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        
        start=0
        end=0
        total=nums[start]
        answer= 1000000000
        
        while True:
            if total >=target:
                if answer > end-start+1:
                    answer = end-start+1
                total=total-nums[start]
                
                if start + 1 > len(nums)-1:
                    return answer
                start=start+1
                if start > end:
                    end = start
                    total = nums[start]
                    
            else:
                # print("k")
                if end+1 > len(nums)-1:
                    if answer == 1000000000:
                        return 0
                    else:
                        return answer
                end=end+1
                total=total+nums[end]
                
                
            
            
        
#         for i in range(1, len(nums)+1):
#             #시작
#             sumv = sum(nums[0:i])
#             j=0
            
#             while True:
#                 # print(sumv)

#                 if sumv >= target:
#                     return i
#                 else:
#                     if i+j == len(nums):
#                         break
#                     # print(nums[j], nums[i+j])
#                     sumv = sumv - nums[j] + nums[i+j]
#                     j=j+1
                    
        return 0
                
                

                
            
        
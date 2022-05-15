class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        
        if k == 0:
            return 0
        start, prod, cnt = 0, 1, 0
        for end in range(len(nums)):
            while start <= end and prod*nums[end] >= k:
                prod = prod/nums[start]
                start += 1
            prod = 1 if start > end else prod*nums[end]
            cnt = cnt if start > end else cnt+(end-start+1)
        return cnt
        
#         count=0
#         for i in range(1, len(nums)+1):
#             for j in range(len(nums)-i+1):
#                 result=1
#                 # print(nums[j:j+i])
#                 for item in nums[j:j+i]:
#                     result*=item
#                 else:
#                     if result < k:
#                         count+=1
#         return count
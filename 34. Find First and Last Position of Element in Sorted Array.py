class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        start = -1
        end = -1

        for i in range(len(nums)):
            if nums[i] == target:
                start = i
                end = i
                for j in range(i+1, len(nums)):
                    if nums[j]== target:
                        end = j
                    else:
                        return [start, end]
                else:
                    return [start, end]
        else:
            return [start, end]

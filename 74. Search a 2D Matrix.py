class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        start = len(matrix)-1
        for i in range(len(matrix)):
            if target < matrix[i][0]:
                start = i - 1
                break
        for item in matrix[start] :
            if item == target :
                return True
            if item > target:
                return False

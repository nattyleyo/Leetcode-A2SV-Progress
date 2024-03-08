class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)
        n = len(matrix[0])
        low = 0
        high = m*n -1
        while low <= high:
            mid = (low + high)//2
            row = mid//n
            col = mid % n
            if matrix[row][col] > target:
                high = mid -1
            elif matrix[row][col] < target:
                low = mid + 1
            else:
                return True
        
        return False  

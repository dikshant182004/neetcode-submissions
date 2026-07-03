class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if len(matrix)==0:
            return False
        for i in matrix:
            for j in i:
                if j==target:
                    return True
        return False


        
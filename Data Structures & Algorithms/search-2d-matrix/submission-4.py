class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        top,bottom=0,len(matrix)-1
        row=self.row_search(top, bottom, target, matrix)
        if row ==-1:
            return False
        p1, p2 = 0, len(matrix[row])-1
        while(p1<=p2):
            mid=(p1+p2)//2
            if matrix[row][mid]==target:
                return True 
            elif matrix[row][mid]<target:
                p1=mid+1
            else:
                p2 = mid-1 
        return False

    def row_search(self, i,j, target, arr):
        if len(arr) == 0:
            return -1 
        while(i<=j):
            mid = (i+j)//2 
            if arr[mid][0] <= target <= arr[mid][-1]:
                return mid
            elif arr[mid][-1]< target:
                i= mid+1
            elif arr[mid][0] > target:
                j= mid-1
        return -1
            


        
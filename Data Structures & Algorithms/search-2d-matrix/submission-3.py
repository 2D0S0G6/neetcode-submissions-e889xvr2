class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        comb_list = []
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                comb_list.append(matrix[i][j])
        left = 0
        right = len(comb_list)-1
        while left <= right :
            mid = (left+right)//2

            if target == comb_list[mid]:
                return True
            elif target > comb_list[mid]:
                left = mid+1
            elif target < comb_list[mid]:
                right = mid-1
        return False

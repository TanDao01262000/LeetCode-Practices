
class Solution:
    # Solution 1: iterate all rows and execute the binary search - O(n*m*log(m)) if matrix is nxm
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        def binary_search(arr, left, right, target):
            if right >= left:
                mid = (right+left)//2
                if arr[mid] == target:
                    return True
                elif arr[mid] <  target:
                    return binary_search(arr, mid+1, right, target)
                else:
                    return binary_search(arr, left, mid-1, target)
            return False 

        for i in range(len(matrix)):
            if binary_search(matrix[i], 0, len(matrix[0])-1, target):
                return True
        return False   


    # Solution 2: finding the place row that the target may belong to and use binary search
    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:
        list = [matrix[i][len(matrix[0]) - 1] for i in range(len(matrix))]
        def binary_search(arr, left, right, target):
            if right >= left:
                mid = (right + left) // 2
                if arr[mid] == target:
                    return True
                elif arr[mid] < target:
                    return binary_search(arr, mid + 1, right, target)
                else:
                    return binary_search(arr, left, mid - 1, target)
            return False
        def find_row(arr, target):
            left = 0
            right = len(arr) - 1
            while right >= left:
                mid = (left + right) // 2
                if arr[mid] > target:
                    right = mid - 1
                else:
                    left = mid + 1
            return max(left, right)
        if binary_search(list, 0, len(list)-1, target):
            return True
        else:
            target_row = find_row(list, target)
            """
            since the target_row is the possible place, so there are two possible scenerio,
            One: the target is bigger than the largest number in the matrix
            ->  the target_row will be the greater than the limit range 1 unit
                Thus it needs to be reduce once
            """
            if target_row >= len(matrix):   
                target_row == 1
            if binary_search(matrix[target_row], 0, len(matrix[0])-1, target):
                return True

        return False







    

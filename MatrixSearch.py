"""
Author: Vinh Truong
Implementation of searching a 2D matrix.

Input Properties: 
Each inner array is sorted, and the last element of 
the nth array is less than the first element of the
n+1 array
The target is the number being searched

Returns a bool; True if in the matrix, else False
"""

def searchMatrix(matrix, target):
    """
    :type matrix: List[List[int]]
    :type target: int
    :rtype: bool
    """
    if len(matrix) == 0 or len(matrix[0]) == 0:
        return False
    left = 0
    right = len(matrix)-1
    while right > left:
        mid = (right-left)//2 + left +1
        if (matrix[mid][0] > target):
            right = mid-1
        else:
            left = mid

    index = left
    left = 0
    right = len(matrix[index])-1
    while right > left:
        mid = (right-left)//2 + left +1
        if (matrix[index][mid] > target):
            right = mid-1
        else:
            left = mid
    return matrix[index][left] == target



matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,50]]
target = 13

print(searchMatrix(matrix, target))

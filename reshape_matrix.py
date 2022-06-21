class Solution:
    # Soluition 1: basic traverse in 2D array, O(n*m) time & space
    def matrixReshape(self, mat: list[list[int]], r: int, c: int) -> list[list[int]]:

        if len(mat)*len(mat[0]) != r*c:
            return mat
        else:
            m, n = 0, 0
            res = [[0]*c]*r     # initialize an array with all 0

            for i in range(len(mat)):
                for j in range(len(mat[0])):
                    res[m][n] = mat[i][j]
                    n += 1
                    if n == c:
                        n = 0
                        m += 1
                    if m == r:
                        break
            return res

    # Solution 2:
    def matrixReshape(self, mat: list[list[int]], r: int, c: int) -> list[list[int]]:
        
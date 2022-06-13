# Solution 1: hashset - O(n^2) time and space to the size of the board 

    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        row_set  = collections.defaultdict(set)
        col_set  = collections.defaultdict(set)
        block_set  = collections.defaultdict(set)
        
        for i in range(9):
            for j in range(9):
                
                if board[i][j] == ".":
                    continue
                if (board[i][j] in row_set[i] or
                    board[i][j] in col_set[j] or
                    board[i][j] in block_set[(i//3, j//3)]):
                    return False
                row_set[i].add(board[i][j])
                col_set[j].add(board[i][j])
                block_set[(i//3, j//3)].add(board[i][j])
                
        return True
"""
36. Valid Sudoku
Medium

6069

779

Add to List

Share
Determine if a 9 x 9 Sudoku board is valid. Only the filled cells need to be validated according to the following rules:

Each row must contain the digits 1-9 without repetition.
Each column must contain the digits 1-9 without repetition.
Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without repetition.
Note:

A Sudoku board (partially filled) could be valid but is not necessarily solvable.
Only the filled cells need to be validated according to the mentioned rules.
 

Example 1:


Input: board = 
[["5","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]
Output: true
Example 2:

Input: board = 
[["8","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]
Output: false
Explanation: Same as Example 1, except with the 5 in the top left corner being modified to 8. Since there are two 8's in the top left 3x3 sub-box, it is invalid.
 

Constraints:

board.length == 9
board[i].length == 9
board[i][j] is a digit 1-9 or '.'.
"""

from optparse import check_choice


def main(board):
    def check_rows(board):
        for i in board:
            temp = set()
            for j in i:
                if j == ".":
                    pass
                else:
                    if j in temp:
                        return False
                    temp.add(j)
        return True
        
    def check_cols(board):
        cur_col = []
        for i in range(9):
            temp = set()
            for j in range(9):
                cur_ele = board[j][i]
                if cur_ele == ".":
                    pass
                else:
                    if cur_ele in temp:
                        return False
                    temp.add(cur_ele)
        return True

    def check_cubes(board):
        centres = [
            [1, 1], [1, 4], [1, 7], 
            [4, 1], [4, 4], [4, 7], 
            [7, 1], [7, 4], [7, 7]
            ]
        for centre in centres:
            temp = set()
            start = [centre[0] - 1, centre[1] - 1]
            end = [centre[0] + 1, centre[1] + 1]
            for i in range(start[0], end[0] + 1):
                for j in range(start[1], end[1] + 1):
                    cur_ele = board[i][j]
                    if cur_ele == ".":
                        pass
                    else:
                        if cur_ele in temp:
                            return False
                        temp.add(cur_ele)

        return True
    print(check_cols(board))
    print(check_rows(board))
    print(check_cubes(board))
    if check_cols(board) and check_cubes(board) and check_rows(board):
        return True
    return False

"""
print(main(board = 
[["5","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]))

print(main(board = 
[["8","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]))
"""
print(main(board=
[[".",".",".",".","5",".",".","1","."],
[".","4",".","3",".",".",".",".","."],
[".",".",".",".",".","3",".",".","1"],
["8",".",".",".",".",".",".","2","."],
[".",".","2",".","7",".",".",".","."],
[".","1","5",".",".",".",".",".","."],
[".",".",".",".",".","2",".",".","."],
[".","2",".","9",".",".",".",".","."],
[".",".","4",".",".",".",".",".","."]]))

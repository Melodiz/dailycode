class Solution:
    def exist(self, board, word):
        def find(i, j, k):
            # print(i+1, j+1, word[k-1], board[i][j])
            if k == len(word):
                return True
            if i < 0 or i >= len(board) or j < 0 or j >= len(board[0]) or board[i][j] != word[k]:
                return False
            temp = board[i][j]
            board[i][j] = ''
            if find(i+1, j, k+1) or find(i-1, j, k+1) or find(i, j+1, k+1) or find(i, j-1, k+1):
                return True
            board[i][j] = temp
            return False
        for i in range(len(board)):
            for j in range(len(board[0])):
                if find(i, j, 0):
                    return True
        return False


# board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
board = [["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]]
# board = [["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]]
print(Solution.exist(Solution, board, "SEE"))

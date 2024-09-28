class Solution
{
public:
    bool find(vector<vector<char>>& board, string& word, int i, int j, int k, int m, int n)
    {
        if (k == word.length())
            return true;
        if (i < 0 || i >= m || j < 0 || j >= n || board[i][j] != word[k])
            return false;

        char temp = board[i][j];
        board[i][j] = '\0';
        if (find(board, word, i + 1, j, k + 1, m, n) ||
         find(board, word, i - 1, j, k + 1, m, n) ||
            find(board, word, i, j + 1, k + 1, m, n) ||
             find(board, word, i, j - 1, k + 1, m, n))
        {
            return true;
        }
        board[i][j] = temp;
        return false;
    }
    bool exist(vector<vector<char>>& board, string word)
    {
        int m = board.size();
        int n = board[0].size();
        for (int i = 0; i < m; ++i)
        {
            for (int j = 0; j < n; ++j)
            {
                if (find(board, word, i, j, 0, m, n))
                    return true;
            }
        }
        return false;
    }
};
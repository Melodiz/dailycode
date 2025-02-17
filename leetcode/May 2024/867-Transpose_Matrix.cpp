class Solution
{
public:
    vector<vector<int>> transpose(vector<vector<int>>& matrix)
    {
        int col = matrix[0].size();
        int row = matrix.size();
        vector<vector<int>> res(col, vector<int>(row));
        for (int i = 0; i < row; i++)
        {
            for (int j = 0; j < col; j++)
            {
                res[j][i] = matrix[i][j];
            }
        }
        return res;
    }
};
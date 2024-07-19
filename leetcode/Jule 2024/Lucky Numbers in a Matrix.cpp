class Solution {
public:
    vector<int> luckyNumbers (vector<vector<int>>& matrix) {
        vector<int> luckyNumbers;
        int rows = matrix.size(), cols = matrix[0].size();
        
        // Find the minimum element in each row
        vector<int> minRow(rows, INT_MAX);
        for (int i = 0; i < rows; ++i) {
            for (int j = 0; j < cols; ++j) {
                minRow[i] = min(minRow[i], matrix[i][j]);
            }
        }
        
        // Find the maximum element in each column
        vector<int> maxCol(cols, INT_MIN);
        for (int j = 0; j < cols; ++j) {
            for (int i = 0; i < rows; ++i) {
                maxCol[j] = max(maxCol[j], matrix[i][j]);
            }
        }
        
        // Check if each element is a lucky number
        for (int i = 0; i < rows; ++i) {
            for (int j = 0; j < cols; ++j) {
                if (matrix[i][j] == minRow[i] && matrix[i][j] == maxCol[j]) {
                    luckyNumbers.push_back(matrix[i][j]);
                }
            }
        }

        return luckyNumbers;
        
    }
};
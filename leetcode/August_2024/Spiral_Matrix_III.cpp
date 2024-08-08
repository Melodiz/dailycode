class Solution
{
public:
    vector<vector<int>> spiralMatrixIII(int rows, int cols, int rStart, int cStart)
    {
        vector<vector<int>> result = {{rStart, cStart}};
        int totalCells = rows * cols;
        int steps = 1; // initial step size
        int direction = 0; // 0: right, 1: down, 2: left, 3: up

        while (result.size() < totalCells)
        {
            for (int i = 0; i < 2; ++i) // there are two moves for each step size
            {
                for (int j = 0; j < steps; ++j)
                {
                    if (direction == 0) cStart++; // move right
                    else if (direction == 1) rStart++; // move down
                    else if (direction == 2) cStart--; // move left
                    else if (direction == 3) rStart--; // move up

                    if (rStart >= 0 && rStart < rows && cStart >= 0 && cStart < cols)
                    {
                        result.push_back({rStart, cStart});
                    }
                }
                direction = (direction + 1) % 4; // change direction
            }
            steps++; // increase step size after two moves
        }

        return result;
    }
};
#include <vector>
#include <functional>
#include <utility>

class Solution
{
public:
    int minDays(std::vector<std::vector<int>>& grid)
    {
        // Lambda function to count the number of islands in the grid
        auto countIslands = [&]() -> int {
            std::vector<std::vector<int>> visited(grid.size(), std::vector<int>(grid[0].size(), 0));
            int islandCount = 0;

            // Depth-First Search (DFS) to mark all cells in the current island
            std::function<void(int, int)> dfs = [&](int row, int col) {
                visited[row][col] = 1;
                for (auto [dRow, dCol] : {std::pair{-1, 0}, {1, 0}, {0, -1}, {0, 1}})
                {
                    int newRow = row + dRow, newCol = col + dCol;
                    if (newRow >= 0 && newRow < grid.size() && newCol >= 0 && newCol < grid[0].size() && grid[newRow][newCol] == 1 && !visited[newRow][newCol])
                    {
                        dfs(newRow, newCol);
                    }
                }
            };

            // Iterate through the grid to find and count all islands
            for (int r = 0; r < grid.size(); r++)
            {
                for (int c = 0; c < grid[0].size(); c++)
                {
                    if (grid[r][c] == 1 && !visited[r][c])
                    {
                        islandCount++;
                        dfs(r, c);
                    }
                }
            }
            return islandCount;
        };

        // If the initial grid does not have exactly one island, return 0
        if (countIslands() != 1) return 0;

        // Try removing each land cell to see if it disconnects the island
        for (int r = 0; r < grid.size(); r++)
        {
            for (int c = 0; c < grid[0].size(); c++)
            {
                if (grid[r][c] == 1)
                {
                    grid[r][c] = 0; // Temporarily remove the land cell
                    if (countIslands() != 1) return 1; // If the island count changes, return 1
                    grid[r][c] = 1; // Restore the land cell
                }
            }
        }

        // If no single cell removal disconnects the island, return 2
        return 2;
    }
};
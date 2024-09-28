#include <vector>
#include <algorithm>

class Solution
{
public:
    int maxDistance(std::vector<int>& position, int m)
    {
        std::sort(position.begin(), position.end());
        int left = 1; // minimum possible distance
        int right = position.back() - position[0]; // maximum possible distance

        while (left < right)
        {
            int mid = left + (right - left + 1) / 2; // use upper mid to avoid infinite loop
            if (canPlaceBalls(position, m, mid))
            {
                left = mid; // try for a larger distance
            }
            else
            {
                right = mid - 1; // try for a smaller distance
            }
        }
        return left;
    }

private:
    bool canPlaceBalls(const std::vector<int>& position, int m, int minDist)
    {
        int count = 1; // place the first ball
        int lastPos = position[0];

        for (int i = 1; i < position.size(); ++i)
        {
            if (position[i] - lastPos >= minDist)
            {
                count++;
                lastPos = position[i];
                if (count == m)
                {
                    return true;
                }
            }
        }
        return false;
    }
};
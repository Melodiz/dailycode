#include <iostream>
#include <vector>

using namespace std;

class Solution
{
public:
    int binarySearch(const vector<int>& sortedScore, int target, int left, int right)
    {
        while (left <= right)
        {
            int mid = left + (right - left) / 2;
            if (sortedScore[mid] == target)
                return mid;
            else if (sortedScore[mid] < target)
                right = mid - 1;
            else
                left = mid + 1;
        }
        return -1;// Return -1 if the target is not found
    }

    vector<string> findRelativeRanks(vector<int>& score)
    {
        vector<int> sortedScore = score;
        sort(sortedScore.begin(), sortedScore.end(), greater<int>());
        vector<string> res(score.size());

        for (int i = 0; i < score.size(); ++i)
        {
            int rank = binarySearch(sortedScore, score[i], 0, score.size() - 1) + 1;
            cout << score[i] << " " << rank << endl;
            if (rank == 1) { res[i] = "Gold Medal"; }
            else if (rank == 2) { res[i] = "Silver Medal"; }
            else if (rank == 3) { res[i] = "Bronze Medal"; }
            else { res[i] = to_string(rank); }
        }
        return res;
    }
};

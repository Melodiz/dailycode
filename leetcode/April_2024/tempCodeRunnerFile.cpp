#include <iostream>
#include <map>
#include <string>

using namespace std;

class Solution
{
public:
    int findRotateSteps(string ring, string key)
    {
        int n = ring.size();
        int m = key.size();
        int distance;
        map<char, map<char, int>> data;
        map<char, size_t> position;
        for (size_t i = 0; i < n; i++)
            position[ring[i]] = ring.find(ring[i]);
        for (size_t i = 0; i < n; i++)
        {
            for (size_t j = 0; j < n; j++)
            {
                distance = abs(position[ring[j]] - i);
                data[ring[i]][ring[j]] = min(distance, n - distance);
            }
        }
        int answer = key.size();
        size_t cur_letter = 0;
        for (size_t i = 0; i < m; i++)
        {
            answer += data[ring[cur_letter]][key[i]];
            cur_letter = position[key[i]];
        }
        return answer;
    }
};
#include <vector>
#include <unordered_map>
#include <algorithm>

using namespace std;

class Solution
{
public:
    vector<int> relativeSortArray(vector<int>& arr1, vector<int>& arr2)
    {
        unordered_map<int, int> m;
        for (int i = 0; i < arr2.size(); i++)
        {
            m[arr2[i]] = i;
        }
        sort(arr1.begin(), arr1.end(), [&m, this](int a, int b) { return this->cmp(a, b, m); });
        return arr1;
    }

private:
    bool cmp(int a, int b, unordered_map<int, int>& m)
    {
        if (m.find(a) != m.end() && m.find(b) != m.end())
        {
            return m[a] < m[b];
        }
        else if (m.find(a) != m.end())
        {
            return true;
        }
        else if (m.find(b) != m.end())
        {
            return false;
        }
        else
        {
            return a < b;
        }
    }
};
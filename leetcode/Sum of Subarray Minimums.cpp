#include "iostream"
using namespace std;

class Solution {
public:
    int rec(vector<int>& arr)
    {
        if (sizeof(arr) == 1)
        {
            return arr[0];
        }
        
    }


    int sumSubarrayMins(vector<int>& arr) {
        return rec(arr) % (10**9+7);
    }
    
};
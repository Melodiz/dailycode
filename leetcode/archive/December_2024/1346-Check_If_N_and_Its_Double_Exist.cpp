class Solution {
public:
    bool checkIfExist(std::vector<int>& arr) {
        std::unordered_set<int> check;
        for (size_t i = 0; i < arr.size(); ++i) {
            if (check.find(arr[i] * 2) != check.end() || (arr[i] % 2 == 0 && check.find(arr[i] / 2) != check.end())) {
                return true;
            }
            check.insert(arr[i]);
        }
        return false;
    }
};
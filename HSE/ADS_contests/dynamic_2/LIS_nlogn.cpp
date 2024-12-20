#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int binary_search(const vector<int>& data, int x) {
    int left = 0, right = data.size() - 1;
    while (left <= right) {
        int mid = (left + right) / 2;
        if (data[mid] == x) {
            return mid;
        } else if (data[mid] < x) {
            left = mid + 1;
        } else {
            right = mid - 1;
        }
    }
    return left;
}

int LIS(int n, long long k, long long b, long long m, int a0) {
    vector<int> data;
    long long ak = a0;
    data.push_back(a0);
    for (int i = 0; i < n - 1; ++i) {
        ak = (k * ak + b) % m;
        if (ak > data.back()) {
            data.push_back(ak);
        } else {
            int pos = binary_search(data, ak);
            data[pos] = ak;
        }
    }
    return data.size();
}

int main() {
    int n, a0;
    long long k, b, m;
    cin >> n >> a0 >> k >> b >> m;
    cout << LIS(n, k, b, m, a0) << endl;
    return 0;
}
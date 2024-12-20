#include <iostream>
#include <vector>
#include <algorithm>
#include <limits>

using namespace std;

int piggy_bank_min(int F, int N, const vector<pair<int, int>>& coins) {
    vector<int> min_sum(F + 1, numeric_limits<int>::max());
    min_sum[0] = 0;
    
    for (int w = 1; w <= F; ++w) {
        for (const auto& coin : coins) {
            int value = coin.first;
            int coin_weight = coin.second;
            if (coin_weight <= w && min_sum[w - coin_weight] != numeric_limits<int>::max()) {
                min_sum[w] = min(min_sum[w], min_sum[w - coin_weight] + value);
            }
        }
    }
    
    return min_sum[F] != numeric_limits<int>::max() ? min_sum[F] : -1;
}

int piggy_bank_max(int F, int N, const vector<pair<int, int>>& coins) {
    vector<int> max_sum(F + 1, numeric_limits<int>::min());
    max_sum[0] = 0;
    
    for (int w = 1; w <= F; ++w) {
        for (const auto& coin : coins) {
            int value = coin.first;
            int coin_weight = coin.second;
            if (coin_weight <= w && max_sum[w - coin_weight] != numeric_limits<int>::min()) {
                max_sum[w] = max(max_sum[w], max_sum[w - coin_weight] + value);
            }
        }
    }
    
    return max_sum[F] != numeric_limits<int>::min() ? max_sum[F] : -1;
}

int main() {
    int E, F, N;
    cin >> E >> F >> N;
    
    vector<pair<int, int>> coins(N);
    for (int i = 0; i < N; ++i) {
        cin >> coins[i].first >> coins[i].second;
    }
    
    int weight = F - E;
    int lower = piggy_bank_min(weight, N, coins);
    
    if (lower == -1) {
        cout << "This is impossible." << endl;
    } else {
        int upper = piggy_bank_max(weight, N, coins);
        cout << lower << " " << upper << endl;
    }
    
    return 0;
}
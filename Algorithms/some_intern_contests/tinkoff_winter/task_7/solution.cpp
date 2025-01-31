#include <iostream>
#include <vector>
#include <algorithm>

const int MOD = 998244353;

std::vector<std::vector<int>> build_binomial(int max_n) {
    std::vector<std::vector<int>> comb(max_n + 1, std::vector<int>(max_n + 1, 0));
    for (int i = 0; i <= max_n; ++i) {
        comb[i][0] = 1;
        for (int j = 1; j <= i; ++j) {
            comb[i][j] = (comb[i-1][j-1] + comb[i-1][j]) % MOD;
        }
    }
    return comb;
}

std::vector<int> optimized_solve(int n, int k, const std::vector<int>& a) {
    std::vector<long long> S(2*k + 1, 0);
    for (int x : a) {
        long long cur = 1;
        for (int l = 0; l <= 2*k; ++l) {
            S[l] = (S[l] + cur) % MOD;
            cur = (cur * x) % MOD;
        }
    }

    auto comb = build_binomial(2*k);
    
    int inv2 = (MOD + 1) / 2;
    
    std::vector<int> answers(k + 1, 0);
    for (int p = 1; p <= k; ++p) {
        long long res = 0;
        if (p % 2 == 0) {
            int q = p / 2;
            for (int r = 0; r < q; ++r) {
                long long tmp = ((S[r] * S[p-r]) % MOD - S[p] + MOD) % MOD;
                tmp = (tmp * comb[p][r]) % MOD;
                res = (res + tmp) % MOD;
            }
            long long tmp = ((S[q] * S[q]) % MOD - S[p] + MOD) % MOD;
            tmp = (tmp * inv2) % MOD;
            tmp = (tmp * comb[p][q]) % MOD;
            res = (res + tmp) % MOD;
        } else {
            int q = (p - 1) / 2;
            for (int r = 0; r <= q; ++r) {
                long long tmp = ((S[r] * S[p-r]) % MOD - S[p] + MOD) % MOD;
                tmp = (tmp * comb[p][r]) % MOD;
                res = (res + tmp) % MOD;
            }
        }
        answers[p] = res;
    }
    
    return std::vector<int>(answers.begin() + 1, answers.end());
}

int main() {
    int n, k;
    std::cin >> n >> k;
    std::vector<int> a(n);
    for (int i = 0; i < n; ++i) {
        std::cin >> a[i];
    }
    auto answers = optimized_solve(n, k, a);
    for (int answer : answers) {
        std::cout << answer << " ";
    }
    std::cout << std::endl;
    return 0;
}

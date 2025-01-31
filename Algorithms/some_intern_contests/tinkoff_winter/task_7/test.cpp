#include <iostream>
#include <vector>
#include <chrono>
#include <random>
#include <cassert>
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

std::vector<int> brute_force_solve(int n, int k, const std::vector<int>& a) {
    std::vector<int> answers(k, 0);
    for (int p = 1; p <= k; ++p) {
        long long result = 0;
        for (int i = 0; i < n; ++i) {
            for (int j = i + 1; j < n; ++j) {
                long long sum = a[i] + a[j];
                long long power = 1;
                for (int _ = 0; _ < p; ++_) {
                    power = (power * sum) % MOD;
                }
                result = (result + power) % MOD;
            }
        }
        answers[p-1] = result;
    }
    return answers;
}

std::vector<int> generate_test_case(int n, int max_ai) {
    std::random_device rd;
    std::mt19937 gen(rd());
    std::uniform_int_distribution<> dis(1, max_ai);
    
    std::vector<int> a(n);
    for (int i = 0; i < n; ++i) {
        a[i] = dis(gen);
    }
    return a;
}
void run_test(int n, int k, const std::vector<int>& a, bool check_correctness) {
    auto start = std::chrono::high_resolution_clock::now();
    auto optimized_result = optimized_solve(n, k, a);
    auto end = std::chrono::high_resolution_clock::now();
    auto optimized_duration = std::chrono::duration_cast<std::chrono::milliseconds>(end - start);

    std::cout << "n = " << n << ", k = " << k << std::endl;
    std::cout << "Optimized solution time: " << optimized_duration.count() << " ms" << std::endl;

    if (check_correctness) {
        start = std::chrono::high_resolution_clock::now();
        auto brute_force_result = brute_force_solve(n, k, a);
        end = std::chrono::high_resolution_clock::now();
        auto brute_force_duration = std::chrono::duration_cast<std::chrono::milliseconds>(end - start);

        std::cout << "Brute force solution time: " << brute_force_duration.count() << " ms" << std::endl;

        assert(optimized_result == brute_force_result);
        std::cout << "Results match!" << std::endl;
    }

    std::cout << std::endl;
}
int main() {
    // // Small test case
    // run_test(5, 3, {1, 2, 3, 4, 5}, true);

    // // Medium test case
    // run_test(100, 10, generate_test_case(100, 1000), true);

    // // Large test case
    // run_test(10000, 50, generate_test_case(10000, 10000000), false);

    // // Extreme test case (maximum allowed input)
    // run_test(200000, 299, generate_test_case(200000, 99999999), false);

    // // New extreme test case with maximum a_i values
    // std::vector<int> max_ai(30, 99999999);
    // run_test(30, 20, max_ai, true);

    // New test case with a_i in range [10^7, 10^8], n in range [10, 40], k in range [10, 40]
    std::random_device rd;
    std::mt19937 gen(rd());
    std::uniform_int_distribution<> n_dis(40, 100);
    std::uniform_int_distribution<> k_dis(30, 100);
    std::uniform_int_distribution<> a_dis(10000000, 99999999);

    int n = n_dis(gen);
    int k = k_dis(gen);
    std::vector<int> a(n);
    for (int& x : a) {
        x = a_dis(gen);
    }
    run_test(n, k, a, true);

    return 0;
}
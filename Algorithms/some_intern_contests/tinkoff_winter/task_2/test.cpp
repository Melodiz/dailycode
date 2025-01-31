#include <iostream>
#include <vector>
#include <algorithm>
#include <random>
#include <chrono>

std::vector<long long> some_f(long long limit = 1000000000000000000LL) {
    std::vector<long long> candidates;
    for (int i = 0; i < 60; ++i) {
        for (int j = i + 1; j < 60; ++j) {
            for (int k = j + 1; k < 60; ++k) {
                long long val = (1LL << i) + (1LL << j) + (1LL << k);
                if (val <= limit) {
                    candidates.push_back(val);
                }
            }
        }
    }
    std::sort(candidates.begin(), candidates.end());
    return candidates;
}

long long solve_query(long long x, const std::vector<long long>& candidates) {
    auto it = std::upper_bound(candidates.begin(), candidates.end(), x);
    if (it == candidates.begin()) return -1;
    return *(--it);
}

int main() {
    const int n = 10e4;
    std::vector<long long> nums(n);
    std::random_device rd;
    std::mt19937_64 gen(rd());
    std::uniform_int_distribution<long long> dis(1000000000000LL, 1000000000000000000LL);

    for (int i = 0; i < n; ++i) {
        nums[i] = dis(gen);
    }

    auto start_time = std::chrono::high_resolution_clock::now();
    
    std::vector<long long> some_stuff = some_f();
    
    for (const auto& num : nums) {
        solve_query(num, some_stuff);
    }
    
    auto end_time = std::chrono::high_resolution_clock::now();
    std::chrono::duration<double> elapsed = end_time - start_time;
    
    std::cout << "Time taken to process " << n << " numbers: " << elapsed.count() << " seconds" << std::endl;

    return 0;
}
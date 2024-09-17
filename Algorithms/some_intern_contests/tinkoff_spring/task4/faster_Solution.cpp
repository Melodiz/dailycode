#include <iostream>
#include <vector>
#include <cmath>
#include <set>
#include <cassert>
#include <fstream>
#include <sstream>
#include <ctime>

std::vector<int> sieve_eratosthenes(int n) {
    if (n < 2) return {};
    std::vector<bool> sieve(n + 1, true);
    sieve[0] = sieve[1] = false;
    for (int start = 3; start <= std::sqrt(n); start += 2) {
        if (sieve[start]) {
            for (int multiple = start * start; multiple <= n; multiple += start * 2) {
                sieve[multiple] = false;
            }
        }
    }
    std::vector<int> primes = {2};
    for (int num = 3; num <= n; num += 2) {
        if (sieve[num]) primes.push_back(num);
    }
    return primes;
}

size_t solution(size_t L, size_t R) {
    std::vector<int> primes = sieve_eratosthenes(std::sqrt(R) + 1);
    std::set<int> primes_set(primes.begin() + 1, primes.end());
    size_t counter = 0;
    for (int p : primes) {
        size_t q = 2;
        size_t num = std::pow(p, q - 1);
        while (num <= R) {
            if (num >= L && primes_set.find(q) != primes_set.end()) {
                counter++;
            }
            num *= p;
            q++;
        }
    }
    return counter;
}

void test() {
    std::vector<std::pair<int, int>> cases = {{1, 10}, {1, 100}, {1, 1000}, {1, 10000}, {1, 100000}, {1, 412441},
                                              {1, 414152}, {1, 41252}, {1, 19121}, {1, 4124}, {1, 415}, {1, 3}, {1, 2}};
    std::vector<int> expected = {2, 7, 16, 33, 79, 134, 135, 57, 43, 26, 11, 0, 0};
    std::ifstream file("task4/results.txt");
    std::string line;
    while (std::getline(file, line)) {
        std::istringstream iss(line);
        int l, r, dxe;
        iss >> l >> r >> dxe;
        cases.emplace_back(l, r);
        expected.push_back(dxe);
    }
    for (size_t i = 0; i < cases.size(); ++i) {
        assert(solution(cases[i].first, cases[i].second) == expected[i] && "Test case failed");
    }
    std::cout << "All test cases passed" << std::endl;
}

int main() {
    test();
    size_t L = 1;
    size_t R = 1e14;
    std::clock_t start = std::clock();
    size_t value = solution(L, R + 1);
    std::cout << "Value: " << value << std::endl;
    std::clock_t end = std::clock();
    std::cout << "Execution time: " << std::fixed << double(end - start) / CLOCKS_PER_SEC << " seconds" << std::endl;
    return 0;
}
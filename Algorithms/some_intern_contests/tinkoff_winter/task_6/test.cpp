#include <iostream>
#include <vector>
#include <random>
#include <chrono>
#include <algorithm>

using namespace std;

struct Point {
    long long x, y;
};

// Declare the solve function (implementation not shown)
int solve(int n, const vector<Point>& points);

void test_random_inputs(int num_tests) {
    const int MAX_N = 299;
    const long long COORD_RANGE = 1e10;

    random_device rd;
    mt19937_64 gen(rd());
    uniform_int_distribution<int> n_dis(4, MAX_N);
    uniform_int_distribution<long long> coord_dis(-COORD_RANGE, COORD_RANGE);

    for (int test = 1; test <= num_tests; ++test) {
        int n = n_dis(gen);
        vector<Point> points(n);

        for (int i = 0; i < n; ++i) {
            points[i] = {coord_dis(gen), coord_dis(gen)};
        }

        auto start = chrono::high_resolution_clock::now();
        int result = solve(n, points);
        auto end = chrono::high_resolution_clock::now();

        chrono::duration<double> elapsed = end - start;

        cout << "Test " << test << ":" << endl;
        cout << "n = " << n << endl;
        cout << "Result: " << result << endl;
        cout << "Execution time: " << elapsed.count() << " seconds" << endl;
        cout << endl;
    }
}

void test_max_input() {
    const int MAX_N = 299;
    const long long COORD_RANGE = 1e10;

    random_device rd;
    mt19937_64 gen(rd());
    uniform_int_distribution<long long> dis(-COORD_RANGE, COORD_RANGE);

    vector<Point> points(MAX_N);
    for (int i = 0; i < MAX_N; ++i) {
        points[i] = {dis(gen), dis(gen)};
    }

    auto start = chrono::high_resolution_clock::now();
    int result = solve(MAX_N, points);
    auto end = chrono::high_resolution_clock::now();

    chrono::duration<double> elapsed = end - start;

    cout << "Maximum input test:" << endl;
    cout << "n = " << MAX_N << endl;
    cout << "Result: " << result << endl;
    cout << "Execution time: " << elapsed.count() << " seconds" << endl;
}

int main() {
    test_random_inputs(10);  // Run 10 random tests
    test_max_input();        // Run test with maximum input
    return 0;
}
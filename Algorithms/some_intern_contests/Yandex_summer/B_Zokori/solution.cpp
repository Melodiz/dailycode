#include <iostream>
#include <vector>
#include <string>
#include <map>
#include <set>


int main() {
    std::ios_base::sync_with_stdio(false);
    std::cin.tie(NULL);

    int n;
    std::cin >> n;

    long long total_pairs = static_cast<long long>(n) * (n - 1) / 2;

    const int NUM_MARKERS = 10;
    const int MAX_MASKS = 1 << NUM_MARKERS;

    std::map<char, int> marker_to_bit;
    for (int i = 0; i < NUM_MARKERS; ++i) {
        marker_to_bit[static_cast<char>('C' + i)] = i;
    }

    std::vector<long long> counts(MAX_MASKS, 0);

    for (int i = 0; i < n; ++i) {
        std::string s;
        std::cin >> s;
        int mask = 0;
        std::set<char> unique_markers(s.begin(), s.end());
        for (char c : unique_markers) {
            mask |= (1 << marker_to_bit[c]);
        }
        counts[mask]++;
    }

    std::vector<long long> sos_dp = counts;
    for (int i = 0; i < NUM_MARKERS; ++i) {
        for (int mask = 0; mask < MAX_MASKS; ++mask) {
            if (mask & (1 << i)) {
                sos_dp[mask] += sos_dp[mask ^ (1 << i)];
            }
        }
    }

    long long disjoint_pairs_sum = 0;
    const int all_markers_mask = MAX_MASKS - 1;

    for (int mask = 0; mask < MAX_MASKS; ++mask) {
        if (counts[mask] > 0) {
            int complement_mask = all_markers_mask ^ mask;

            long long num_disjoint_fragments = sos_dp[complement_mask];

            disjoint_pairs_sum += counts[mask] * num_disjoint_fragments;
        }
    }

    long long num_disjoint_pairs = disjoint_pairs_sum / 2;

    long long result = total_pairs - num_disjoint_pairs;

    std::cout << result << std::endl;
    return 0;
}
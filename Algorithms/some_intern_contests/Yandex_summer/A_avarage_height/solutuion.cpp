#include <iostream>
#include <deque>
#include <unordered_map>

void setup_fast_io() {
    std::ios_base::sync_with_stdio(false);
    std::cin.tie(NULL);
}

int main() {
    setup_fast_io();

    int n;
    std::cin >> n;

    std::deque<long long> queue;
    std::unordered_map<long long, int> height_counts;
    __int128_t total_sum = 0;

    for (int i = 0; i < n; ++i) {
        char event_type;
        std::cin >> event_type;

        if (event_type == '+') {
            long long k;
            std::cin >> k;
            queue.push_back(k);
            total_sum += k;
            height_counts[k]++;
        } else {
            if (!queue.empty()) {
                long long removed_height = queue.front();
                queue.pop_front();
                total_sum -= removed_height;
                height_counts[removed_height]--;
                if (height_counts[removed_height] == 0) {
                    height_counts.erase(removed_height);
                }
            }
        }

        long long num_people = queue.size();
        if (num_people == 0) {
            std::cout << 0 << "\n";
            continue;
        }

        if (total_sum % num_people == 0) {
            long long average_height = (long long)(total_sum / num_people);
            if (height_counts.count(average_height)) {
                std::cout << height_counts[average_height] << "\n";
            } else {
                std::cout << 0 << "\n";
            }
        } else {
            std::cout << 0 << "\n";
        }
    }

    return 0;
}
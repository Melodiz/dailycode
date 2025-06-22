#include <iostream>
#include <vector>
#include <numeric>
#include <algorithm>

void readInput(int& numElements, int& numQueries, std::vector<int>& a, std::vector<int>& b) {
    std::cin >> numElements >> numQueries;
    a.resize(numElements);
    b.resize(numElements);
    for (int i = 0; i < numElements; ++i) {
        std::cin >> a[i] >> b[i];
    }
}

long long calculateSumA(const std::vector<int>& a) {
    long long sumA = 0;
    for (int val : a) {
        sumA += val;
    }
    return sumA;
}

void initializeIdsAndSort(const std::vector<int>& b, std::vector<int>& ids, std::vector<int>& positionFromId) {
    int n = b.size();
    ids.resize(n);
    positionFromId.resize(n);
    std::iota(ids.begin(), ids.end(), 0);
    std::sort(ids.begin(), ids.end(), [&](int i, int j) {
        return b[i] < b[j] || (b[i] == b[j] && i < j);
    });
    for (int i = 0; i < n; ++i) {
        positionFromId[ids[i]] = i;
    }
}

long long calculateSumB(const std::vector<int>& b, const std::vector<int>& ids) {
    long long sumB = 0;
    long long prefix = 0;
    for (int id : ids) {
        prefix += b[id];
        sumB += prefix;
    }
    return sumB;
}

void processQueries(int numQueries, std::vector<int>& a, std::vector<int>& b, std::vector<int>& ids, std::vector<int>& positionFromId, long long& sumA) {
    int n = a.size();
    while (numQueries--) {
        int id, newA, newB;
        std::cin >> id >> newA >> newB;
        sumA -= a[id-1];
        sumA += newA;
        a[id-1] = newA;

        b[id - 1] = newB;
        for (int i = positionFromId[id - 1]; i + 1 < n; ++i) {
            if (b[ids[i]] <= b[ids[i + 1]]) break;
            std::swap(ids[i], ids[i + 1]);
        }
        for (int i = positionFromId[id - 1]; i >= 1; --i) {
            if (b[ids[i - 1]] <= b[ids[i]]) break;
            std::swap(ids[i - 1], ids[i]);
        }

        for (int i = 0; i < n; ++i) {
            positionFromId[ids[i]] = i;
        }
        long long prefix = 0;
        long long sumB = 0;
        for (int i = 0; i < n; ++i) {
            prefix += b[ids[i]];
            sumB += prefix;
        }

        std::cout << sumA - sumB << "\n";
    }
}

void solve() {
    int numElements, numQueries;
    std::vector<int> a, b;
    readInput(numElements, numQueries, a, b);

    long long sumA = calculateSumA(a);

    std::vector<int> ids, positionFromId;
    initializeIdsAndSort(b, ids, positionFromId);

    long long sumB = calculateSumB(b, ids);
    std::cout << sumA - sumB << "\n";

    processQueries(numQueries, a, b, ids, positionFromId, sumA);
}

int main() {
    std::ios::sync_with_stdio(false), std::cin.tie(0), std::cout.tie(0);
    std::cout.setf(std::ios::fixed), std::cout.precision(9);

    solve();
    return 0;
}
#include <iostream>
#include <vector>
#include <string>
#include <algorithm>

const int MAX_CHAR = 128;

std::vector<int> sort_cyclic_shifts(const std::string& s) {
    int n = s.length();
    std::vector<int> p(n), c(n), cnt(std::max(MAX_CHAR, n), 0);

    // Count sort for the first character
    for (int i = 0; i < n; i++)
        cnt[s[i]]++;
    for (int i = 1; i < MAX_CHAR; i++)
        cnt[i] += cnt[i-1];
    for (int i = 0; i < n; i++)
        p[--cnt[s[i]]] = i;

    c[p[0]] = 0;
    int classes = 1;
    for (int i = 1; i < n; i++) {
        if (s[p[i]] != s[p[i-1]])
            classes++;
        c[p[i]] = classes - 1;
    }

    std::vector<int> pn(n), cn(n);
    for (int h = 0; (1 << h) < n; ++h) {
        for (int i = 0; i < n; i++) {
            pn[i] = p[i] - (1 << h);
            if (pn[i] < 0)
                pn[i] += n;
        }
        std::fill(cnt.begin(), cnt.begin() + classes, 0);
        for (int i = 0; i < n; i++)
            cnt[c[pn[i]]]++;
        for (int i = 1; i < classes; i++)
            cnt[i] += cnt[i-1];
        for (int i = n-1; i >= 0; i--)
            p[--cnt[c[pn[i]]]] = pn[i];
        cn[p[0]] = 0;
        classes = 1;
        for (int i = 1; i < n; i++) {
            std::pair<int, int> cur = {c[p[i]], c[(p[i] + (1 << h)) % n]};
            std::pair<int, int> prev = {c[p[i-1]], c[(p[i-1] + (1 << h)) % n]};
            if (cur != prev)
                ++classes;
            cn[p[i]] = classes - 1;
        }
        c.swap(cn);
    }
    return p;
}

std::vector<int> build_suffix_array(const std::string& s) {
    std::string s_with_term = s + '\0';
    std::vector<int> sorted_shifts = sort_cyclic_shifts(s_with_term);
    sorted_shifts.erase(sorted_shifts.begin());
    return sorted_shifts;
}

int main() {
    std::string input;
    std::getline(std::cin, input);

    std::vector<int> suffix_array = build_suffix_array(input);

    for (int i = 0; i < suffix_array.size(); i++) {
        std::cout << suffix_array[i]+1 << (i == suffix_array.size() - 1 ? '\n' : ' ');
    }

    return 0;
}
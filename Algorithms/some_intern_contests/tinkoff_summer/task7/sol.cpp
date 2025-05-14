#include <iostream>
#include <vector>
#include <unordered_map>
#include <cmath>
#include <algorithm>

using namespace std;

const int MOD = 998244353;
using ll = long long;

ll gcd(ll a, ll b) {
    while (b) {
        ll temp = a % b;
        a = b;
        b = temp;
    }
    return a;
}

vector<ll> get_all_divisors(ll n) {
    vector<ll> divisors;
    for (ll i = 1; i * i <= n; i++) {
        if (n % i == 0) {
            divisors.push_back(i);
            if (i != n / i) {
                divisors.push_back(n / i);
            }
        }
    }
    return divisors;
}

vector<pair<ll, ll>> find_b0_b1(ll A) {
    vector<pair<ll, ll>> data;
    vector<ll> div0 = get_all_divisors(A);
    for (ll b0 : div0) {
        ll b1 = A / b0;
        if (gcd(b1, b0) == 1) {
            data.emplace_back(b0, b1);
        }
    }
    return data;
}

// Fast exponentiation: (base^power) % MOD
ll mod_pow(ll base, ll power) {
    ll result = 1;
    while (power > 0) {
        if (power % 2 == 1) {
            result = (result * base) % MOD;
        }
        base = (base * base) % MOD;
        power /= 2;
    }
    return result;
}

ll solve(const vector<ll>& A) {
    unordered_map<ll, ll> data;
    auto initial_pairs = find_b0_b1(A[0]);
    for (const auto& [b0, b1] : initial_pairs) {
        data[b1] = A[0] % MOD;
    }

    for (size_t i = 1; i < A.size(); i++) {
        unordered_map<ll, ll> iteration_data;
        auto b0b1 = find_b0_b1(A[i]);
        for (const auto& [b0, b1] : b0b1) {
            for (const auto& [b_i, s_i] : data) {
                ll g = gcd(b_i, b0);
                ll b_new = (b1 * b_i) / g;
                ll power = i + 1;
                ll base = b0 / g;
                ll term = mod_pow(base, power);
                ll sum_new = (s_i * b_new) % MOD;
                sum_new = (sum_new * term) % MOD;
                iteration_data[b_new] = (iteration_data[b_new] + sum_new) % MOD;
            }
        }
        data = iteration_data;
    }

    ll result = 0;
    for (const auto& [key, val] : data) {
        result = (result + val) % MOD;
    }
    return result;
}

int main() {
    int n;
    cin >> n;
    vector<ll> arr(n);
    for (int i = 0; i < n; i++) {
        cin >> arr[i];
    }
    cout << solve(arr) << endl;
    return 0;
}
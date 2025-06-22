#include <iostream>
#include <vector>
#include <fstream>
#include <random>
#include <iomanip>

const int K_FACTORS = 10;

double dot_product(const std::vector<double>& v1, const std::vector<double>& v2) {
    double result = 0.0;
    for (size_t i = 0; i < v1.size(); ++i) {
        result += v1[i] * v2[i];
    }
    return result;
}

int main() {
    std::ios_base::sync_with_stdio(false);
    std::cin.tie(nullptr);

    std::ifstream input_file("input.txt");
    if (!input_file.is_open()) {
        std::cerr << "Error: Could not open input.txt" << std::endl;
        return 1;
    }

    int k_unused, U, M, D, T;
    input_file >> k_unused >> U >> M >> D >> T;

    struct Rating { int u, m, r; };
    std::vector<Rating> training_data;
    training_data.reserve(D);
    double total_r = 0.0;
    for (int i = 0; i < D; ++i) {
        int u, m, r;
        input_file >> u >> m >> r;
        training_data.push_back({u, m, r});
        total_r += r;
    }

    struct TestPair { int u, m; };
    std::vector<TestPair> test_data;
    test_data.reserve(T);
    for (int i = 0; i < T; ++i) {
        int u, m;
        input_file >> u >> m;
        test_data.push_back({u, m});
    }
    input_file.close();

    const double mu = total_r / D;

    std::vector<double> bu(U, 0.0);
    std::vector<double> bm(M, 0.0);

    std::default_random_engine generator;
    std::normal_distribution<double> distribution(0.0, 0.1);

    std::vector<std::vector<double>> pu(U, std::vector<double>(K_FACTORS));
    for (int i = 0; i < U; ++i) {
        for (int j = 0; j < K_FACTORS; ++j) {
            pu[i][j] = distribution(generator);
        }
    }

    std::vector<std::vector<double>> qm(M, std::vector<double>(K_FACTORS));
    for (int i = 0; i < M; ++i) {
        for (int j = 0; j < K_FACTORS; ++j) {
            qm[i][j] = distribution(generator);
        }
    }

    const double lr = 0.01;
    const double reg = 0.02;
    const int epochs = 100;

    for (int epoch = 0; epoch < epochs; ++epoch) {
        for (const auto& data : training_data) {
            int u = data.u;
            int m = data.m;
            double r = static_cast<double>(data.r);

            double pred = mu + bu[u] + bm[m] + dot_product(pu[u], qm[m]);
            double err = r - pred;

            bu[u] += lr * (err - reg * bu[u]);
            bm[m] += lr * (err - reg * bm[m]);

            std::vector<double> pu_old = pu[u];
            for (int i = 0; i < K_FACTORS; ++i) {
                pu[u][i] += lr * (err * qm[m][i] - reg * pu[u][i]);
                qm[m][i] += lr * (err * pu_old[i] - reg * qm[m][i]);
            }
        }
    }

    std::cout << std::fixed << std::setprecision(5);
    for (const auto& data : test_data) {
        int u = data.u;
        int m = data.m;
        double pred = mu + bu[u] + bm[m] + dot_product(pu[u], qm[m]);
        std::cout << pred << "\n";
    }

    return 0;
}
import numpy as np

def main():
    with open('input.txt', 'r') as f:
        k, U, M, D, T = map(int, f.readline().split())

        training_data = []
        total_r = 0
        for _ in range(D):
            u, m, r = map(int, f.readline().split())
            training_data.append((u, m, r))
            total_r += r
        
        mu = total_r / D
        
        test_data = []
        for _ in range(T):
            u, m = map(int, f.readline().split())
            test_data.append((u, m))

        bu = np.zeros(U, dtype=np.float64)
        bm = np.zeros(M, dtype=np.float64)
        pu = np.random.normal(0, 0.1, (U, 10)).astype(np.float64)  # Using d=10 as recommended
        qm = np.random.normal(0, 0.1, (M, 10)).astype(np.float64)
        lr = 0.01
        reg = 0.02

        for epoch in range(100):
            for u, m, r in training_data:
                pred = mu + bu[u] + bm[m] + np.dot(pu[u], qm[m])
                err = r - pred

                bu[u] += lr * (err - reg * bu[u])
                bm[m] += lr * (err - reg * bm[m])
                
                pu_old = pu[u].copy()
                pu[u] += lr * (err * qm[m] - reg * pu[u])
                qm[m] += lr * (err * pu_old - reg * qm[m])

        for u, m in test_data:
            pred = mu + bu[u] + bm[m] + np.dot(pu[u], qm[m])
            print(f"{pred:.5f}")

if __name__ == "__main__":
    main()
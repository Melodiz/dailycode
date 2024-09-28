class Solution
{
public:
    int checkRecord(int n)
    {
        int ring = pow(10, 9) + 7;
        vector<int> P(n + 1, 0);
        vector<int> L(n + 1, 0);
        vector<int> A(n + 1, 0);

        P[0] = 1;
        L[0] = 1;
        L[1] = 3;
        A[0] = 1;
        A[1] = 2;
        A[2] = 4;

        if (n == 1) return 3;

        for (int i = 1; i <= n; i++)
        {
            A[i - 1] %= ring;
            P[i - 1] %= ring;
            L[i - 1] %= ring;

            P[i] = ((A[i - 1] + P[i - 1]) % ring + L[i - 1]) % ring;

            if (i > 1) L[i] = ((A[i - 1] + P[i - 1]) % ring + (A[i - 2] + P[i - 2]) % ring) % ring;

            if (i > 2) A[i] = ((A[i - 1] + A[i - 2]) % ring + A[i - 3]) % ring;
        }

        return ((A[n - 1] % ring + P[n - 1] % ring) % ring + L[n - 1] % ring) % ring;
    }
};
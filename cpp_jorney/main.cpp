#include <iostream>
using namespace std;

// int rec(int numerator, int denominator, int result, int n)
// {
//     return 0;
// }

int result;

void rec(int n)
{
    (result = 1, n <= 1) || (rec(n - 1), result -= 1 / n, n % 2 == 0) || (rec(n - 1), result += 1 / n, n % 2 == 1);
}

int main()
{
    int n;
    cin >> n;
    rec(n); // call the func
    cout << result << endl;
    return 0;
}
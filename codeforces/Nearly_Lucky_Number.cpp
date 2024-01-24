#include "iostream"

using namespace std;

int main()
{
    long long num = 0;
    cin >> num;
    int amount = 0;

    while (num > 0)
    {
        if (num % 10 == 4 || num % 10 == 7)
        {
            num /=10;
            amount++;
        }
        else{
            num /=10;
        }
    }
    if (amount == 4 || amount == 7)
    {
        cout << "YES" << endl;
    }
    else
    {
        cout << "NO" << endl;
    }
    return 0;
    cout << "YES" << endl;
    return 0;
}
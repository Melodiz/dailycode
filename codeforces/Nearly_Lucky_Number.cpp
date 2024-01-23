#include "iostream"

using namespace std;

int main()
{
    long num = 0;
    cin >> num;
    short amount = 0;

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
    if (amount == 0){
        cout << "NO" << endl;
        return 0;
    }
    while (amount > 0)
    {
        if (amount % 10 == 4 || amount % 10 == 7)
        {
            amount /=10;
        }
        else{
            cout << "NO" << endl;
            return 0;
        }
        
    }
    cout << "YES" << endl;
    return 0;
}
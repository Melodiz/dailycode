#include <iostream>
using namespace std;

int main()
{
    int speed;
    int amount;

    cin >> speed;
    cin >> amount;
    if (speed >= 0)
    {
        cout << (speed*amount) % 109 << endl; 
    }
    else
    {
        cout << (109 + speed*amount % 109) % 109 << endl;
    }

    return 0;
}
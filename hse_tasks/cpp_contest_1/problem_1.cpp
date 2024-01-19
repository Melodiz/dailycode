#include <iostream>
using namespace std;

int check(int x1, int x2, int y1, int y2)
{
    if (y1 == x1 || y2 == x2 || abs(x1 - y1) == abs(x2 - y2))
    {
        cout << "YES" << endl;
    }
    else
    {
        cout << "NO" << endl;
    }
    return 0;
}

int main()
{
    int x1, x2, y1, y2;
    cin >> x1;
    cin >> x2;
    cin >> y1;
    cin >> y2;

    check(x1, x2, y1, y2);
    return 0;
}
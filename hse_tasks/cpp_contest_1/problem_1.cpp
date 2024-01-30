#include <iostream>

using namespace std;

bool canQueenMoveToCell(int x1, int x2, int y1, int y2)
{
    if (y1 == x1 || y2 == x2 || abs(x1 - y1) == abs(x2 - y2))
    {
        return true;
    }

    return false;
}

int main()
{
    size_t x1, x2, y1, y2;
    cin >> x1 >> x2 >> y1 >> y2;

    cout << (canQueenMoveToCell(x1, x2, y1, y2) ? "YES" : "NO") << '\n';

    return 0;
}

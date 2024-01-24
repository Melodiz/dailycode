#include "iostream"
#include <string>
using namespace std;

int main()
{
    size_t n = 0;
    cin >> n;

    string data = "";
    cin >> data;

    int a = 0;
    int b = 0;

    for (size_t i = 0; i < n; i++)
    {
        if (data[i] == 'A')
        {
            a++;
        }
        else
        {
            b++;
        }
    }
    if (a == b)
    {
        cout << "Friendship" << endl;
        return 0;
    }
    if (a > b)
    {
        cout << "Anton" << endl;
        return 0;
    }
    cout << "Danik" << endl;
    return 0;
}
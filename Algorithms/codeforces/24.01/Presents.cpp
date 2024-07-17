#include "iostream"
// #include <string>
using namespace std;

int main()
{
    size_t n = 0;
    cin >> n;
    
    short data[n];
    short to = 0;

    for (size_t i = 0; i < n; i++)
    {
        cin >> to;
        data[to-1] = i+1;
    }
    
    for (size_t i = 0; i < n; i++)
    {
        cout << data[i] << ' ';
    }
    cout << endl;
    return 0;
    
}
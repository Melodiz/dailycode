#include "iostream"
// #include <string>
using namespace std;

int main()
{
    size_t n = 0;
    size_t t = 0;
    cin >> n >> t;

    char data[n];
    char temp[n];

    for (size_t i = 0; i < n; i++)
    {
        cin >> data[i];
    }

    for (size_t i = 0; i < n; i++)
    {
        temp[i] = data[i];
    }

    for (size_t i = 0; i < t; i++)
    {
        for (size_t i = 0; i < n - 1; i++)
        {
            // cout << data[i] << '-' << data[i+1] << endl;
            // for (size_t i = 0; i < n; i++)
            // {
            //     cout << temp[i];
            // }
            // cout << endl;

            if (data[i] == 'B' && data[i + 1] == 'G')
            {
                // cout << data[i] << '-' << data[i + 1] << endl;
                temp[i] = 'G';
                temp[i + 1] = 'B';
            }
            // else
            // {
            //     temp[i] = data[i];
            // }
        }
        // temp[n] = data[n];
        // for (size_t i = 0; i < n; i++)
        // {
        //     cout << temp[i];
        // }
        // cout << endl;

        for (size_t i = 0; i < n; i++)
        {
            data[i] = temp[i];
        }
    }
    for (size_t i = 0; i < n; i++)
    {
        cout << data[i];
    }
    cout << endl;
    return 0;
}
#include "iostream"
// #include <string>
using namespace std;

int unique(int number)
{
    char seen[10] = {0};

    while (number)
    {
        int digit = number % 10;

        number /= 10;
        if (digit < 0)
        {
            /*
             * The number was negative.  Make it positive.
             * (Note: Checking the number is negative before the while
             * loop could fail when number is LLONG_MIN, so do it here
             * instead.)
             */
            digit = -digit;
            number = -number;
        }
        if (seen[digit]++)
            return 0; /* not unique */
    }
    return 1; /* unique */
}

int main()
{
    int n = 0;
    cin >> n;
    short a;

    for (size_t i = 0; i < n; i++)
    {
        cin >> a;
        if (a == 1)
        {
            cout << "HARD" << endl;
            return 0;
        }
    }
    cout << "EASY" << endl;

    return 0;
}
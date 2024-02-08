// Write a program that calculates the remainder
// of dividing a given “long” number by a given digit.

#include "iostream"
#include <string>
using namespace std;

int findRemainder(string number, int ring);

int findRemainder(string number, int ring)
{
    int ans = 0;
    int curNum = 0;
    for (size_t i = 0; i < number.length(); i++)
    {
        curNum = number[i] - '0';
        // to convert char into number (like ascii 66 - 60 = 6)
        ans = ans*10 + curNum;
        ans = ans%ring;
    }
    return ans;
    
}

int main()
{
    string number;
    int ring;
    cin >> ring;
    cin >> number;

    cout << findRemainder(number, ring) << endl;
    return 0;
}
#include <iostream>
using namespace std;
// check if number or string
bool IsDigit(string c)
{
    if (isdigit(c[0]) == false)
        return false;
    return true;
}
int main()
{
    string line;
    getline(cin, line);
    cout << IsDigit(line) << endl;
    
    return 0;
}


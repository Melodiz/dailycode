#include "iostream"
#include "string"
using namespace std;

int main()
{   int a;
    cin >> a;
    string word = "";
    cin >> word;

    for (size_t i = 0; i < word.length(); i++)
    {
        if (word[i]>=0x40 && word[i] <= 0x5A)
        {
            cout << "YES" << endl;
            return 0;
        }
        
    }
    cout << "NO" << endl;
    return 0;    
}
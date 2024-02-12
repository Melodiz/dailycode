#include <iostream>
#include <string>
using namespace std;

void reversedPermutation(int *data, size_t n);

void reversedPermutation(int *data, size_t n)
{
  for (int i = 0; i < n; i++) {
    for (int j = 0; j < n; j++) {
      if (data[j] == i + 1) {
        cout << j + 1 << " ";
        break;
      }
    }
  }
}

int main(){
    size_t n;
    cin >> n;

    int data[n];
    int num;

    for (size_t i = 0; i < n; i++)
    {
        cin >> num;
        data[i] = num;
    }
    reversedPermutation(data, n);
    return 0;
}
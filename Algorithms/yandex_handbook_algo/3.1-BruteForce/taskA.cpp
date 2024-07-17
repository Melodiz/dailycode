#include <iostream>


int main()
{
    int n;
    std::cin >> n;
    int ans = 1;
    for (int j = 1; j <= n; j++) { ans *= j; }
    std::cout << ans << std::endl;
    return 0;
}
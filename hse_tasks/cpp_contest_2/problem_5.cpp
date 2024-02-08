// Write a program that adds 1 to the natural number N
// (the length of the number N is up to 1000 characters).

#include "iostream"
#include <string>

std::string addOne(std::string num);

std::string addOne(std::string num)
{
    for (int i = num.size(); i-- > 0;)
    {
        if (num[i] != '9')
        {
            num[i] = char(num[i] + 1);
            return num;
        }
        num[i] = '0';
    }
    return '1' + num;
}

int main()
{
    std::string data = "";
    std::cin >> data;
    data = addOne(data);
    std::cout << data << std::endl;
    return 0;
}
#include <iostream>

int main()
{
    // int age;
    // std::cout << "enter your age:" << std::endl;

    // std::cin >> age;
    // std::cout << "your age is " << age << std::endl;

    std::string full_name;
    std::cout << "enter your name: " << std::endl;

    std::getline(std::cin, full_name);

    std::cout << full_name << std::endl;

    return 0;
}
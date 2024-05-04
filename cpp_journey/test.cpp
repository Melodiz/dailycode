#include <algorithm>
#include <cstdlib>
#include <ctime>
#include <fstream>
#include <iostream>
#include <string>
#include <vector>

struct Car {

    // fields
    std::string mark;
    std::string name;
    int max_speed;
    int weight;
    std::vector<int> colour;

    // Constructor
    // default constructor
    Car() : mark(""), name(""), max_speed(-1), weight(-1), colour({}){};

    // constructor
    Car(std::string _mark, std::string _name, int _max_speed, int _weight, std::vector<int> _colour) : mark(_mark), name(_name), max_speed(_max_speed), weight(_weight), colour(_colour){};

    Car(std::string _mark, std::string _name, int _max_speed, int _weight) : mark(_mark), name(_name), max_speed(_max_speed), weight(_weight), colour({}){};

    void print()
    {
        std::cout << "Mark: " << mark << std::endl;
        std::cout << "Name: " << name << std::endl;
        std::cout << "Max speed: " << max_speed << std::endl;
        std::cout << "Weight: " << weight << std::endl;
        std::cout << "Colour: " << colour[0] << " " << colour[1] << " " << colour[2] << " " << std::endl;
    }

    // overloaded operators
    bool operator<(const Car& other_car) const
    {
        return this->max_speed < other_car.max_speed;
    }
    bool operator>(const Car& other_car) const
    {
        // return max_speed > other_car.max_speed;
        return !(*this < other_car);
    }
};


int main()
{
    Car audi_a6("Audi", "A6", 300, 1600, {155, 0, 255});
    audi_a6.print();
    Car audi_a4("Audi", "A4", 250, 1400, {155, 0, 255});
    audi_a4.print();

    std::cout << (audi_a4 < audi_a6) << std::endl;
}
#include "vehicle.hpp"
#include <iostream>

// void test1()
// {
//     Vehicle veh1("Сart", 325);
//     std::cout << veh1.getInfo() << '\n';
// }

// void test2()
// {
//     Vehicle veh1("Сart", 325);
//     Car car1("lada", 700, 70);
//     Truck truck1("Iveco", 2000.0, 80.0, 2000.0);
//     Boat boat1("Azimut", 1500, 60);

//     Vehicle* carPtr = &car1;
//     Vehicle* truckPtr = &truck1;
//     Vehicle* boatPtr = &boat1;

//     std::cout << veh1.getInfo() << '\n';
//     std::cout << car1.getInfo() << '\n';
//     std::cout << truck1.getInfo() << '\n';
//     std::cout << boat1.getInfo() << '\n';
//     std::cout << carPtr->getInfo() << '\n';
//     std::cout << truckPtr->getInfo() << '\n';
//     std::cout << boatPtr->getInfo() << '\n';
// }

// void test3()
// {
//     Boat boat1("Reka", 500);
//     std::cout << Boat::knot2Speed(30) << '\n';
//     std::cout << boat1.knot2Speed(boat1.getKnotSpeed()) << '\n';
// }

// void test4()
// {
//     Car car1("lada", 700, 70);
//     Truck truck1("Mercedes", 1000);
//     Boat boat1("Reka", 500);

//     Vehicle* carPtr = &car1;
//     Vehicle* truckPtr = &truck1;
//     Vehicle* boatPtr = &boat1;
//     std::cout << carPtr->getType() << " " << carPtr->getSpeed() << '\n';
//     std::cout << truckPtr->getType() << " " << truckPtr->getSpeed() << '\n';
//     std::cout << boatPtr->getType() << " " << boatPtr->getSpeed() << '\n';
// }

void test5()
{
    Warehouse w;
    Truck truck1("Mercedes", 1000, 60, 6000);
    Truck truck2("NotMercedes", 7000);
    Boat boat1("Reka", 500, 50);
    Boat boat2("Azimut", 500, 60);
    Boat boat3("Kazanka", 500, 50);
    Car car1("Lada", 500, 112);
    Car car2("Renault", 500, 90);
    Car car3("KIA", 600, 60);
    w.addVehicle(&truck1);
    w.addVehicle(&truck2);
    w.addVehicle(&boat1);
    w.addVehicle(&boat2);
    w.addVehicle(&boat3);
    w.addVehicle(&car1);
    w.addVehicle(&car2);
    w.addVehicle(&car3);

    // if there is a wrong index
    try
    {
        const Vehicle* ptr = w[100];
    } catch (std::out_of_range& error)
    {
        std::cout << error.what() << '\n';
    }
    std::cout << "----------------" << '\n';

    // check 0-th item
    std::cout << w[0]->getInfo() << '\n';
    std::cout << "----------------" << '\n';

    // print warehouse
    std::cout << w;
    std::cout << "----------------" << '\n';

    // check 0-th item not changed
    std::cout << w[0]->getInfo() << '\n';
}

int main()
{
    // test1();
    // test2();
    // test3();
    // test4();/
    test5();
}

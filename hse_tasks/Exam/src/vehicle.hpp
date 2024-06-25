#ifndef __VEHICLE_H__
#define __VEHICLE_H__

#include <algorithm>
#include <iostream>
#include <string>
#include <vector>

const double KNOT_MULTIPLIER = 1.852;

class Vehicle
{
public:
    Vehicle(const std::string& name, double load) : _name(name), _load(load) {};
    virtual ~Vehicle() {}

    virtual std::string getType() const = 0;
    virtual double getSpeed() const = 0;

    virtual Vehicle* cloneMe() const = 0;

    // Vehicle& operator=(Vehicle& other)
    // {
    //     if (this != &other)
    //     {
    //         Vehicle* object = other.cloneMe();
    //         return &object;
    //     }
    // }

    std::string getInfo() const
    {
        return "name: " + _name + ", load: " + std::to_string(getLoad());
    }

    virtual double getLoad() const { return _load; }

    void setLoad(double load) { this->_load = load; }

    std::string getName() const { return _name; }

private:
    std::string _name;
    double _load;
};

class Car : public Vehicle
{
public:
    Car(const std::string& name, double load, double meanSpeed) : Vehicle(name, load), _meanSpeed(meanSpeed) {};

    Car(const std::string& name, double load) : Vehicle(name, load), _meanSpeed(90) {};

    std::string getType() const override { return "Landcraft"; }

    virtual std::string getInfo() const
    {
        // getInfo overloading (name: %name, load: %load, speed: %meanSpeed
        return Vehicle::getInfo() + ", speed: " + std::to_string(getSpeed());
    }
    Vehicle* cloneMe() const override { return new Car(*this); }


    double getSpeed() const override { return _meanSpeed; }

    double getLoad() const override { return Vehicle::getLoad(); }

    std::string getName() const { return Vehicle::getName(); }

private:
    double _meanSpeed;
};

class Truck : public Car
{

public:
    Truck(const std::string& name, double load, double meanSpeed, double extraCargo) : Car(name, load, meanSpeed), _extraCargo(extraCargo) {};

    Truck(const std::string& name, double load) : Car(name, load, 60), _extraCargo(0) {};

    Truck(const std::string& name, double load, double meanSpeed) : Car(name, load, meanSpeed), _extraCargo(0) {};

    double getLoad() const override { return (_extraCargo + Car::getLoad()); }
    Vehicle* cloneMe() const override { return new Truck(*this); }

    std::string getType() const override { return "Landcraft"; }
    double getSpeed() const override { return Car::getSpeed(); }

    virtual std::string getInfo() const override
    {
        // getInfo overloading (name: %name, load: %load, speed: %meanSpeed
        return "name: " + Car::getName() + ",  load: " + std::to_string(getLoad()) + ", speed: " + std::to_string(Car::getSpeed());
    }

private:
    double _extraCargo;
};

class Boat : public Vehicle
{
public:
    Boat(const std::string& name, double load,
         double meanKnotSpeed) : Vehicle(name, load), _meanKnotSpeed(meanKnotSpeed) {};

    Boat(const std::string& name, double load) : Vehicle(name, load), _meanKnotSpeed(30) {};

    Vehicle* cloneMe() const override { return new Boat(*this); }

    std::string getType() const override { return "Seacraft"; }
    double getSpeed() const override { return knot2Speed(getKnotSpeed()); }


    std::string getInfo() const
    {
        return Vehicle::getInfo() + ", knotSpeed: " + std::to_string(_meanKnotSpeed);
    }

    double getLoad() const override { return Vehicle::getLoad(); }

    double getKnotSpeed() const { return _meanKnotSpeed; }

    static double knot2Speed(double knotSpeed)
    {
        return 1.852 * knotSpeed;
    }


private:
    double _meanKnotSpeed;
};

class Warehouse
{
public:
    Warehouse() : vehicles() {};
    void addVehicle(Vehicle* vehicle)
    {
        vehicles.push_back(vehicle);
    }
    double getTotalLoad() const
    {
        double ans = 0;
        for (const Vehicle* veh: vehicles)
        {
            const Car* car = dynamic_cast<const Car*>(veh);
            const Truck* truck = dynamic_cast<const Truck*>(veh);
            const Boat* boat = dynamic_cast<const Boat*>(veh);
            if (truck && truck->getLoad() >= 0) { ans += truck->getLoad(); }
            if (car && car->getLoad() >= 0) { ans += car->getLoad(); }
            if (boat && boat->getLoad() >= 0) { ans += boat->getLoad(); }
        }
        return ans;
    }
    Vehicle* operator[](size_t index) const
    {
        if (index >= vehicles.size())
        {
            throw std::out_of_range("Index out of range");
        }
        return vehicles[index];
    }

    static bool comp(Vehicle* a, Vehicle* b)
    {
        if (a->getLoad() > b->getLoad()) { return true; }
        else if (a->getLoad() < b->getLoad() ) { return false; }
        if (a->getSpeed() > b->getSpeed()) { return true; }
        else if (a->getSpeed() < b->getSpeed()) { return false; }
        return a->getName() < b->getName();
    }

    friend std::ostream& operator<<(std::ostream& os, const Warehouse& data)
    {
        std::vector<Vehicle*> vehiclesCopy = data.vehicles;
        sort(vehiclesCopy.begin(), vehiclesCopy.end(), comp);
        for (const Vehicle* vech: vehiclesCopy)
        {
            os << vech->getInfo() << '\n';
        }
        return os;
    }

private:
    std::vector<Vehicle*> vehicles;
};


#endif// __VEHICLE_H__
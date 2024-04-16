#include <cmath>
#include <iostream>
#include <map>
#include <string>
#include <vector>

class Person
{
public:
    Person(const std::string& name) : _name(name){};
    virtual void getRank() const = 0;

    virtual void getInfo() const
    {
        std::cout << _name << '\n';
    }


protected:
    std::string _name;
};

class Student : virtual public Person
{
public:
    Student(const std::string& name, const double gpa) : Person(name), _gpa(gpa){};
    void getRank() const override
    {
        std::cout << "Student: " << std::endl;
    }
    void getInfo() const override
    {
        Person::getInfo();
        std::cout << _gpa << '\n';
    }

protected:
    double _gpa;
};

class Professor : virtual public Person
{
public:
    // Professor(const std::string& name, const short salary) : Person(name), _salary(salary)
    Professor(const std::string& name, const short salary) : Person(name), _salary(salary){};
    void getInfo() const override
    {
        Person::getInfo();
        std::cout << _salary << '\n';
    }
    void getRank() const override
    {
        std::cout << "Professor: " << std::endl;
    }

protected:
    short _salary;
};

class Univeristy
{
public:
    void addPerson(Person& person)
    {
        _persons.push_back(&person);
    }
    void printPersons() const
    {
        for (const Person* person: _persons)
        {
            person->getInfo();
        }
    }

private:
    std::vector<Person*> _persons;
};


class Assistant : public Professor, public Student
{
public:
    Assistant(const std::string& name, const short salary, const double gpa) : Person(name), Professor(name, salary), Student(name, gpa){};
    void getInfo() const override
    {
        Professor::getInfo();
        std::cout << _gpa << '\n';
    }
    void getRank() const override
    {
        std::cout << "Assistant: " << std::endl;
    }
};


int main()
{
    // Me.getInfo();
    Student Me2("ARC", 10.2);
    // Me2.getInfo();
    Assistant Me4("Nasia", 100, 10.2);
    // Me2.Person::getInfo();
    Professor Me3("adem", 1000);
    // Me3.getInfo();

    Univeristy univ;
    univ.addPerson(Me2);
    univ.addPerson(Me3);
    univ.addPerson(Me4);

    univ.printPersons();

    Person* p = &Me2;
    // p->getInfo();

    return 0;
}

#include <iostream>
#include <vector>
#include <string>
#include <stdexcept>

// Constants
const int GROUP_TAX = 2000;
const int BASE_SALARY = 1500;

// Abstract class Teacher
class Teacher {
public:
    Teacher(const std::string& name) : _name(name) {}
    virtual ~Teacher() {}
    const std::string& getName() const { return _name; }
    virtual double calcWages() const = 0;
    virtual Teacher* cloneMe() const = 0; // Pure virtual function for cloning
protected:
    std::string _name;
};

// Derived class AssociateTeacher
class AssociateTeacher : public Teacher {
public:
    AssociateTeacher(const std::string& name, int bonus) : Teacher(name), _bonus(bonus) {}
    int getBonus() const { return _bonus; }
    double calcWages() const override { return BASE_SALARY + _bonus; }
    Teacher* cloneMe() const override { return new AssociateTeacher(*this); } // Clone method
private:
    int _bonus;
};

// Override the cloneMe method in InvitedTeacher
class InvitedTeacher : public Teacher {
public:
    InvitedTeacher(const std::string& name, int stuGroups) : Teacher(name), _stuGroups(stuGroups) {}
    int getStuGroups() const { return _stuGroups; }
    double calcWages() const override { return GROUP_TAX * _stuGroups; }
    Teacher* cloneMe() const override { return new InvitedTeacher(*this); } // Clone method
private:
    int _stuGroups;
};

// TArray class
class TArray {
public:
    // Destructor
    ~TArray() {
        for (Teacher* teacher : _arr) {
            delete teacher;
        }
    }

    // Copy constructor
    TArray(const TArray& other) {
        for (Teacher* teacher : other._arr) {
            _arr.push_back(teacher->cloneMe());
        }
    }

    TArray(): _arr() {};

    // Copy assignment operator
    TArray& operator=(const TArray& other) {
        if (this != &other) {
            // Clean up existing resources
            for (Teacher* teacher : _arr) {
                delete teacher;
            }
            _arr.clear();

            // Copy new resources
            for (Teacher* teacher : other._arr) {
                _arr.push_back(teacher->cloneMe());
            }
        }
        return *this;
    }

    AssociateTeacher* addAssociateTeacher(const std::string& name, int bonus) {
        AssociateTeacher* teacher = new AssociateTeacher(name, bonus);
        _arr.push_back(teacher);
        return teacher;
    }

    InvitedTeacher* addInvitedTeacher(const std::string& name, int groupsNum) {
        InvitedTeacher* teacher = new InvitedTeacher(name, groupsNum);
        _arr.push_back(teacher);
        return teacher;
    }

    Teacher* operator[](size_t index) const {
        if (index >= _arr.size()) {
            throw std::out_of_range("Index out of range");
        }
        return _arr[index];
    }

    size_t getSize() const {
        return _arr.size();
    }

    friend std::ostream& operator<<(std::ostream& os, const TArray& tArr);

    std::vector<Teacher*> getTeachers() const { return _arr; }

protected:
    std::vector<Teacher*> _arr;
};


std::ostream& operator<<(std::ostream& os, const TArray& tArr) {
    for (const Teacher* teacher : tArr._arr) {
        os << teacher->getName() << "," << teacher->calcWages() << "\n";
    }
    return os;
}
//========================================
//==========< Problem 3 [2pts] >==========

std::pair<int, int> totalWagesOfTopTeachers(const TArray& tArr, int minGroups, int minBonus)
{
    int totalBonus = 0;
    int totalGroups = 0;
    for (const Teacher* teacher : tArr.getTeachers()) 
    {
        const AssociateTeacher* assocTeacher = dynamic_cast<const AssociateTeacher*>(teacher);
        const InvitedTeacher* invitedTeacher = dynamic_cast<const InvitedTeacher*>(teacher);

        if (assocTeacher && assocTeacher->getBonus() >= minBonus) 
        {
            totalBonus += assocTeacher->calcWages();
        }

        if (invitedTeacher && invitedTeacher->getStuGroups() >= minGroups) 
        {
            totalGroups += invitedTeacher->calcWages();
        }
    }
    return std::make_pair(totalGroups, totalBonus);
}

//========================================
//==========< Problem 4 [2pts] >==========

// TODO: Add all the stuff needed for the TArray class to comply with the Rule Of Three.
// What do you have to add into the class for that?

//========================================


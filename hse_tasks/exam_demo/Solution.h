/*! \file       solution.h
 *  \author     ---=Put your name here=---
 *  \version    1.0
 *  \date       29.06.2022
 *
 *  Final Exam. Solution module. Put ALL the declarations and definitions right here.
 *  All the class methods must be defined here (do not put their in a separated
 *  file). If you need to create a non-member auxilliary function, put its defintion
 *  here as well.
 *
 *      → Provide your solution here and upload this only file to Ya.Contest! ←
 *
 */

#ifndef SOLUTION_H
#define SOLUTION_H

#include <iostream>
#include <memory>
#include <stdexcept>
#include <string>
#include <vector>

//========================================
//==========< Problem 1 [3pts] >==========

class Teacher
{
public:
    Teacher(const std::string& name) : _name(name) {}

    virtual ~Teacher() {}

    const std::string& getName() const { return _name; }
    virtual double calcWages() const = 0;
    virtual bool getType() const = 0;

    virtual Teacher* cloneMe() const = 0;

    // TODO: For the Problem 4 add a pure virtual function Teacher* cloneMe() here and override
    // it properly in the descendant classes.

protected:
    std::string _name;
};

class AssociateTeacher : public Teacher
{
public:
    static const int BASE_SALARY = 1500;
    // TODO: To complete...

    AssociateTeacher(std::string name, int bonus) : Teacher(name), _bonus(bonus) {};

    const int getBonus() const { return _bonus; }
    double calcWages() const override { return BASE_SALARY + _bonus; }
    bool getType() const override { return true; }

    Teacher* cloneMe() const override { return new AssociateTeacher(*this); }

private:
    int _bonus;
};

class InvitedTeacher : public Teacher
{
public:
    static const int GROUP_TAX = 2000;
    // TODO: To complete...

    InvitedTeacher(std::string name, int stuGroups) : Teacher(name), _stuGroups(stuGroups) {};

    const int getStuGroups() const { return _stuGroups; }
    double calcWages() const override { return GROUP_TAX * _stuGroups; }
    bool getType() const override { return false; }

    Teacher* cloneMe() const override { return new InvitedTeacher(*this); }

private:
    int _stuGroups;
};

//========================================
//==========< Problem 2 [3pts] >==========

class TArray
{
public:
    // TODO: To complete...
    size_t getSize() const
    {
        return _arr.size();
    }

    TArray() : _arr() {}
    ~TArray()
    {
        for (Teacher* teacher: _arr) { delete teacher; }
    }

    AssociateTeacher* addAssociateTeacher(const std::string& name, int bonus)
    {
        AssociateTeacher* teacher = new AssociateTeacher(name, bonus);
        _arr.push_back(teacher);
        return teacher;
    }

    InvitedTeacher* addInvitedTeacher(const std::string& name, int groupsNum)
    {
        InvitedTeacher* teacher = new InvitedTeacher(name, groupsNum);
        _arr.push_back(teacher);
        return teacher;
    }
    Teacher* operator[](size_t index) const
    {
        if (index >= _arr.size()) { throw std::out_of_range("Index out of range"); }
        return _arr[index];
    }

    friend std::ostream& operator<<(std::ostream& os, const TArray& tArr);

    TArray(const TArray& other)
    {
        for (Teacher* teacher: other._arr)
        {
            _arr.push_back(teacher->cloneMe());
        }
    }

    TArray& operator=(const TArray& other)
    {
        if (this != &other)
        {
            // Clean up existing resources
            for (Teacher* teacher: _arr)
            {
                delete teacher;
            }
            _arr.clear();

            // Copy new resources
            for (Teacher* teacher: other._arr)
            {
                _arr.push_back(teacher->cloneMe());
            }
        }
        return *this;
    }


protected:
    std::vector<Teacher*> _arr;
};

std::ostream& operator<<(std::ostream& os, const TArray& tArr)
{
    for (const Teacher* teacher: tArr._arr)
    {
        os << teacher->getName() << "," << teacher->calcWages() << "\n";
    }
    return os;
}

//========================================
//==========< Problem 3 [2pts] >==========

std::pair<int, int> totalWagesOfTopTeachers(const TArray& tArr, int minGroups, int minBonus)
{
    double firstVal = 0;
    double secondVal = 0;
    for (int i = 0; i < tArr.getSize(); ++i)
    {
        const Teacher* teacher = tArr[i];
        const AssociateTeacher* assTeacher = dynamic_cast<const AssociateTeacher*>(teacher);
        const InvitedTeacher* invatedTeacher = dynamic_cast<const InvitedTeacher*>(teacher);

        if (assTeacher && assTeacher->getBonus() >= minBonus) { firstVal += assTeacher->calcWages(); }
        if (invatedTeacher && invatedTeacher->getStuGroups() >= minGroups) { secondVal += invatedTeacher->calcWages(); }
    }
    return std::make_pair(secondVal, firstVal);
}

//========================================
//==========< Problem 4 [2pts] >==========

// TODO: Add all the stuff needed for the TArray class to comply with the Rule Of Three.
// What do you have to add into the class for that?

//========================================

#endif

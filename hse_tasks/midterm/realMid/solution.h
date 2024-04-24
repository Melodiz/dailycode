/*! \file       solution.h
 *  \author     ---=Put your name here=---
 *  \version    1.0
 *  \date       18.04.2022
 *
 *  Midterm Test. Types aliases and definitions, and function skeletons.
 *
 *      → Provide your solution here and upload this only file to Ya.Contest! ←
 *
 */

#include <iostream>
#include <map>
#include <set>
#include <string>
#include <vector>
// TODO: do not forget to include all necessary headers here!

// Use the following datatypes and do not modify them!
// See notes in the task description.
using Ingredients = std::map<std::string, int>;

struct Dish {
    std::string name;
    std::set<std::string> ingredients;
};

using Dishes = std::vector<Dish>;
using DishesIngredients = std::pair<Dishes&, Ingredients&>;


//=========================[TASK 1]===========================================//

Ingredients readIngredients(std::istream& istr)
{
    Ingredients res;
    std::string line;
    std::getline(istr, line);
    int n = std::stoi(line);
    for (size_t i = 0; i < n; i++)
    {
        std::getline(istr, line);
        std::string _name = line.substr(0, line.find(" "));
        int _calls = std::stoi(line.substr(line.find(" ") + 1, line.length()));
        res[_name] = _calls;
    }

    return res;
}

// This is a complete implementation. Don't modify it, use it and consider it
// as an example
Dishes readDishes(std::istream& istr)
{
    Dishes res;

    size_t num;
    istr >> num;
    for (size_t i = 0; i < num; ++i)
    {
        Dish dish;
        istr >> dish.name;
        size_t ingNum;
        istr >> ingNum;
        for (size_t j = 0; j < ingNum; ++j)
        {
            std::string ingr;
            istr >> ingr;
            dish.ingredients.insert(ingr);
        }
        res.push_back(dish);
    }

    return res;
}

//=========================[TASK 2]===========================================//

std::ostream& operator<<(std::ostream& ostr, const Dish& dish)
{

    std::cout << dish.name << ": ";
    std::vector<std::string> data;
    for (auto& it: dish.ingredients) { data.push_back(it); }
    for (size_t i = 0; i < data.size() - 1; i++)
    {
        std::cout << data[i] << ", ";
    }
    std::cout << data[data.size() - 1];

    return ostr;
}

//=========================[TASK 3]===========================================//

int calcCalories(const Dish& dish, const Ingredients& ingrs)
{
    int total = 0;
    for (auto& it: dish.ingredients) { total += ingrs.at(it); }

    return total;
}


//=========================[TASK 4]===========================================//


// This is a complete implementation. Don't modify it and consider it
// as an example.
//
// ! It is NOT mandatory to use this method in the program.
std::ostream& operator<<(std::ostream& ostr, const Dishes& dishes)
{
    for (const Dish& dish: dishes)
    {
        ostr << dish << "\n";
    }
    return ostr;
}
// using Ingredients = std::map<std::string, int>;

// struct Dish {
//     std::string name;
//     std::set<std::string> ingredients;
// };

// using Dishes = std::vector<Dish>;
// using DishesIngredients = std::pair<Dishes&, Ingredients&>;

std::ostream& operator<<(std::ostream& ostr, const DishesIngredients& di)
{
    for (size_t i = 0; i < di.first.size(); i++)
    {
        std::cout << di.first[i] << "; ";
        std::cout << calcCalories(di.first[i], di.second) << std::endl;
    }

    // int total = 0;
    // for (auto& it: di.second) { total += ingrs.at(it); }
    // std::cout << calcCalories(di.first, di.second);


    return ostr;
}

//=========================[TASK 5]===========================================//

// using Ingredients = std::map<std::string, int>;

// struct Dish {
//     std::string name;
//     std::set<std::string> ingredients;
// };

// using Dishes = std::vector<Dish>;
// using DishesIngredients = std::pair<Dishes&, Ingredients&>;
// int calcCalories(const Dish& dish, const Ingredients& ingrs)

// struct Comparator {
//     const Ingredients& ingrs;
//     bool operator()(const Dish& dishA, const Dish& dishB) const
//     {
//         return calcCalories(dishA, ingrs) < calcCalories(dishB, ingrs);
//     }
// };

class Comparator
{
public:
    Ingredients& ingrs;
    Comparator(Ingredients& data) : ingrs(data){};
    // {
    //     ingrs = data;
    // }

    bool operator()(const Dish& dishA, const Dish& dishB) const
    {
        return calcCalories(dishA, ingrs) < calcCalories(dishB, ingrs);
    }
};
// bool comp(const Dish& dishA, const Dish& dishB) const
// {
//     return calcCalories(dishA, dishA.ingrs) < calcCalories(dish, dishA.ingrs);
// }

void sortDishesByCalories(DishesIngredients& di)
{
    sort(di.first.begin(), di.first.end(), Comparator(di.second));
}
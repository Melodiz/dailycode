#include <iostream>

/*
You are tasked with creating a program to manage a database
of students' information. Each student record consists of the
following fields: name, age, and grade. You need to implement
a structure to represent a student record, including various
overloaded operators for comparison and input/output operations.

In the main program, you should provide functionality to read
student records from a file, add new records, delete existing
records, modify records, and display all records. Additionally,
you should implement the ability to save the updated database
to a file.

Furthermore, you are required to store the collection of student
records in a container such as a vector or any other appropriate
container provided by the Standard Template Library (STL).

Your program should support the following operations:

Reading student records from a file and storing them in the database.
Adding a new student record to the database.
Deleting an existing student record from the database.
Modifying the information of an existing student record.
Displaying all student records.
Saving the updated database to a file.
*/

#include <iostream>
#include <fstream>
#include <vector>
#include <string>

struct Student
{
    std::string name;
    int age;
    double grade;

    // friend std::istream& operator>>(std::istream& in, Student& student) {
    //     in >> student.name >> student.age >> student.grade;
    //     return in;
    // }

    // friend std::ostream& operator<<(std::ostream& out, const Student& student) {
    //     out << "Name: " << student.name << ", Age: " << student.age << ", Grade: " << student.grade;
    //     return out;
    // }
};

std::ostream& operator<<(std::ostream& out, const Student& student)
{
    out << "Name: " << student.name << ", Age: " << student.age << ", Grade: " << student.grade;
    return out;
}


std::istream& operator>>(std::istream& in, Student& student) {
    in >> student.name >> student.age >> student.grade;
    return in;
}


void test01()
{
    Student mary{"Mary", 20, 5.3};
    // operator<<(std::cout, mary);
    std::cout << mary;
    std::cout << std::endl;

    // Student john;
    // std::cout << john << '\n';
    // std::cin >> john;
    // std::cout << john << '\n';
}

std::vector<Student> readRecordsFromFile(const std::string& sourceFile)
{
    std::fstream file;
    file.open(sourceFile, std::ios_base::in);

    if (!file.is_open())
    {
        return {};
    }

    std::vector<Student> ans;
    

    while (file && !file.eof())
    {
        Student temp;
        file >> temp;

        ans.push_back(temp);
    }
    
    return ans;
}

void test02()
{
    std::vector<Student> data = readRecordsFromFile("students.txt");
    for (size_t i = 0; i < data.size(); i++)
    {
        std::cout << data[i] << '\n';
    }
    
}

int main()
{
    // std::vector<Student> students;

    // readRecordsFromFile("students.txt", students);

    // addRecord(students);
    // deleteRecord(students, 1);
    // displayRecords(students);

    // writeRecordsToFile("updated_students.txt", students);
    test01();
    test02();
    return 0;
}

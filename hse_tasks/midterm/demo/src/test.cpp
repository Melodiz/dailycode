#include <iostream>
#include <string>
#include <vector>
#include <fstream>


void readRecords(std::ifstream& file)
{
    file.open("transactions_accounts.csv");
    bool flag = false;
    if (!file.is_open())
    {
        std::cout << "Error opening file" << std::endl;
    }
    while (file.good())
    {
        std::string line;
        std::getline(file, line);

        if (line.find("validity_timestamp") != -1)
            flag = true;

        if (!flag && line.substr(0, line.find(";")) != "id" && line.length() > 10)
        {
            std::cout << line << std::endl;

            std::string _id = line.substr(0, line.find(";"));
            line = line.substr(line.find(";") + 1);

            int _name = std::stoi(line.substr(0, line.find(";")));
            line = line.substr(line.find(";") + 1, line.length());

            std::string _type = line.substr(0, line.find(";"));
            line = line.substr(line.find(";") + 1, line.length());

            std::string _from = line.substr(0, line.find(";"));
            line = line.substr(line.find(";") + 1, line.length());

            std::string _to = line.substr(0, line.find(";"));
            line = line.substr(line.find(";") + 1, line.length());

            std::string _amount = line.substr(0, line.find(";"));
            line = line.substr(line.find(";") + 1, line.length());

            std::cout << "id: " << _id << std::endl;
            std::cout << "name: " << _name << std::endl;
            std::cout << "type: " << _type << std::endl;
            std::cout << "from: " << _from << std::endl;
            std::cout << "to: " << _to << std::endl;
            std::cout << "amount: " << _amount << std::endl;
            std::cout << std::endl;
        }
        else if (flag && line.find("validity_timestamp") == -1)
        {
            std::string _id = line.substr(0, line.find(";"));
            line = line.substr(line.find(";") + 1);

            std::string _name = line.substr(0, line.find(";"));
            line = line.substr(line.find(";") + 1, line.length());

            std::string _timestamp = line.substr(0, line.find(";"));
            line = line.substr(line.find(";") + 1, line.length());

            std::cout << "id: " << _id << std::endl;
            std::cout << "name: " << _name << std::endl;
            std::cout << "timestamp: " << _timestamp << std::endl;
            std::cout << std::endl;
        }
    }
}


int main()
{
    std::string path = "transactions_accounts.csv";
    std::ifstream file;
    readRecords(file);
}

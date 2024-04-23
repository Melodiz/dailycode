#include <climits>
#include <fstream>
#include <iostream>
#include <map>
#include <set>
#include <sstream>
#include <string>
#include <unordered_map>
#include <vector>


using UnixTS = unsigned int;

const unsigned short TRANSACTION_COL_N = 6;
const unsigned short ACCOUNT_COL_N = 3;

struct Transaction {
    std::string id;
    UnixTS date;
    std::string type;
    std::string from;
    std::string to;
    double amount;
    bool operator<(const Transaction& other) const;
};

class Account
{
public:
    Account();// default constructor
    Account(const std::string& id, const std::string& name, UnixTS validity_dt = UINT_MAX);
    void addTransaction(const Transaction& transaction);
    double getBalance(UnixTS = UINT_MAX) const;
    void printInfo() const;
    size_t getTransactionsCount() const;

private:
    std::string _id;
    std::string _name;
    std::set<Transaction> _transactions;
    UnixTS _validity_dt;
};

void Account::printInfo() const
{
    std::cout << "--------------------------------\n"
              << "id: " << _id << '\n'
              << "name: " << _name << '\n'
              << "validity datetime: " << _validity_dt << '\n'
              << "--------------------------------\n";
}

size_t Account::getTransactionsCount() const
{
    return _transactions.size();
}

Account::Account()
{
    _id = "00000000-0000-0000-0000-000000000000";
    _name = "Noname";
    _validity_dt = 0;
}
// Task 1 (5 points)
// Implement Account constructor with arguments
Account::Account(const std::string& id,
                 const std::string& name,
                 UnixTS validity_dt)
{
    std::set<Transaction> data;
    _transactions = data;
    _id = id;
    _name = name;
    _validity_dt = validity_dt;
}

// Task 2 (10 points)
// Implement operator< overloading for Transaction
bool Transaction::operator<(const Transaction& other) const
{
    Transaction obj = *this;
    if (obj.date < other.date)
        return true;
    if (obj.date > other.date)
        return false;
    if (obj.type == "deposit" && (other.type != "deposit"))
        return true;
    if (obj.type == "withdraw" && other.type == "transfer")
        return true;
    return false;
}

// Task 3 (10 points)
// Implement get balance to date method (default max value)
double Account::getBalance(UnixTS timestamp) const
{
    double balance = 0;
    std::string person_id = this->_id;
    std::vector<Transaction> data;
    for (auto& it: this->_transactions) { data.push_back(it); }

    for (size_t i = 0; i < data.size(); i++)
    {
        // std::cout << data[i].date << std::endl;
        if (data[i].date <= timestamp)
        {
            if (data[i].type == "deposit")
                balance += data[i].amount;
            else if (data[i].type == "withdraw")
                balance -= data[i].amount;
            else
            {
                if (!(data[i].from == data[i].to) && (data[i].from ==person_id))
                    balance -= data[i].amount;
                else if (!(data[i].from == data[i].to) && (data[i].to == person_id))
                    balance += data[i].amount;
            }
        }
    }
    return balance;
}

// Task 4 (15 points)
// Implement adding transaction to Account
void Account::addTransaction(const Transaction& transaction)
{
    _transactions.insert(transaction);
}


// Task 5 (20 points)
// Implement transaction and account reading from csv and fill accounts by transactions
using AccountContainer = std::unordered_map<std::string, Account>;
using TransactionContainer = std::set<Transaction>;

TransactionContainer readTransactions(std::ifstream& fileStream)
{
    TransactionContainer transactions;

    std::string line;
    std::getline(fileStream, line);
    size_t transactionsCount = std::stoul(line);
    std::getline(fileStream, line);

    for (size_t i = 0; i < transactionsCount; ++i)
    {
        std::stringstream ss(line);
        std::string field;
        Transaction transaction;
        for (unsigned short i = 0; i < TRANSACTION_COL_N; i++)
        {
            std::cout << line << std::endl;
        }
        // and here;
    }


    return transactions;
}

AccountContainer readAccounts(std::ifstream& fileStream)
{
    AccountContainer accounts;

    // put your code here;

    return accounts;
}

void fillAccounts(AccountContainer& accounts, const TransactionContainer& transactions)
{
    // put your code here;
}

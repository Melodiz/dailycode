#ifndef SOLUTION_H
#define SOLUTION_H

#include <algorithm>
#include <iostream>
#include <map>
#include <stdexcept>
#include <string>
#include <vector>
#include <set>

enum class CitationType
{
    WebPage,
    Article
};

class Citation
{
public:
    Citation(const std::string& title, int year)
        : _title(title), _year(year)
    {
    }

    virtual ~Citation() {}
    virtual void printCitation(std::ostream& ostr) const = 0;
    // task 3 function included here
    virtual std::string getInlineCitation() const = 0;
    virtual CitationType getCitationType() const = 0;
    virtual std::string getTitle() const { return ""; }
    virtual std::string getLastName() const { return "";}

protected:
    std::string _title;
    int _year;
};

// example 1 - Web Page
// you will need to modify it
class WebPage : public Citation
{
public:
    WebPage(const std::string& title, int year, const std::string& url) : Citation(title, year), _url(url){};

    void printCitation(std::ostream& ostr) const override
    {
        ostr << "Title: " << _title << std::endl;
        ostr << "Year: " << _year << std::endl;
        ostr << "URL: " << _url << std::endl;
    }
    std::string getInlineCitation() const override { return "[Web page, " + std::to_string(_year) + "]";}
    CitationType getCitationType() const override { return CitationType::WebPage; }
    std::string getTitle() const override { return _title; }

protected:
    std::string _url;
};


class PublishedWork : public Citation
{
public:
    PublishedWork(const std::string& title, const int year, std::string firstName, std::string lastName) : Citation(title, year), _firstname(firstName), _lastname(lastName){};
    
protected:
    std::string _firstname;
    std::string _lastname;
};


class Article : public PublishedWork
{
public:
    Article(const std::string& title, const int year, std::string firstName, std::string lastName, const std::string& journal) : PublishedWork(title, year, firstName, lastName), _journal(journal){};

    void printCitation(std::ostream& ostr) const override
    {
        ostr << "Title: " << _title << std::endl;
        ostr << "Year: " << _year << std::endl;
        ostr << "Author: " << _firstname << " " << _lastname << std::endl;
        ostr << "Journal: " << _journal << std::endl;
    }
    std::string getInlineCitation() const override {return  "[" + _lastname + ", " + std::to_string(_year) + "]";}

    CitationType getCitationType() const override { return CitationType::Article; }
    std::string getLastName() const override{ return _lastname; }

protected:
    std::string _journal;
};

// example 2 - Book
// included only as an example, not used in the tasks
// class Book : public PublishedWork
// {
// public:
//     Book(const std::string& title, int year, const std::string& firstname, const std::string& lastname, const std::string& publisher)
//         : PublishedWork(title, year, firstname, lastname),
//           _publisher(publisher)
//     {
//     }

//     void printCitation(std::ostream& ostr) const override
//     {
//         PublishedWork::printCitation(ostr);
//         ostr << "Publisher:" << _publisher << std::endl;
//     }

// protected:
//     std::string _publisher;
// };


// task 2
Citation* addCitation(std::map<std::string, Citation*>& citations, CitationType type, const std::map<std::string, std::string> data)
{
    Citation* citationToAdd;
    // your code
    if (type == CitationType::WebPage)
    {
        // WebPage page(data.at("title"), data.at("year"), data.at("url"));
        // citationToAdd = page*;
        std::string title = data.at("title");
        int year = std::stoi(data.at("year"));
        std::string url = data.at("url");
        citationToAdd = new WebPage(title, year, url);
    }
    else
    {
        std::string title = data.at("title");
        int year = std::stoi(data.at("year"));
        std::string firstname = data.at("firstname");
        std::string lastname = data.at("lastname");
        std::string journal = data.at("journal");
        citationToAdd = new Article(title, year, firstname, lastname, journal);
    }
    std::string keyData = data.at("key");
    citations[keyData] = citationToAdd;
    return citationToAdd;
}


// task 4
void insertInlineCitations(std::string& text, const std::map<std::string, Citation*>& citations)
{
    std::string keyData = "";
    std::string result  = "";
    size_t i = 0;
    while (i < text.length())
    {
        if (text[i] == '{')
        {
            while (text[i]!= '}') {keyData += text[i]; i++;}
            keyData += text[i];
            i++;
            result += citations.at(keyData)->getInlineCitation();
            keyData = "";
        }
        else{
            result += text[i];
            i++;}
    }
    text = result;
}


// task 5
void printBibliographyAppearance(std::string& text, const std::map<std::string, Citation*>& citations)
{
    std::string keyData = "";
    std::vector<std::string> keys;
    std::set<std::string> checkKeys;

    size_t i = 0;
    while (i < text.length())
    {
        if (text[i] == '{')
        {
            while (text[i]!= '}') {keyData += text[i]; i++;}
            keyData += text[i];
            i++;
            if (checkKeys.find(keyData) == checkKeys.end())
            {
                checkKeys.insert(keyData);
                keys.push_back(keyData);
            }
            keyData = "";
        }
        else{i++;}
    }

    for (size_t i = 0; i < keys.size(); i++)
    {
        std::cout << i+1 << '.' << std::endl;
        citations.at(keys[i])->printCitation(std::cout);
    }   
}


// task 6
// you may modify classes in any way you want to solve this task
// you may add additional functions

// Implement a function
// This function takes the same two input variables: 
// text - a long string of text containing keys, the same keys as the ones used in Task 2, 
// formatted as {keyword123} with curly braces. citations - the map of citations from 
// Task 2. 
// This  function  should  go  through  the  text  and  replace  all  occurrences  of  the  keys  with 
// corresponding indices of citations when ordered the following way. 
// 1. First, all Article citations, ordered by last names of their authors. Last names of the authors 
// may be assumed to be unique. 
// 2. Second, all WebPage citations, ordered by titles. Titles of web pages may be assumed to be 
// unique. 
// The first index is 1. 
// Don't consider uppercase/lowercase letters, use simple string comparison.
                                   

class ComplexSort
{
public:

    ComplexSort(const std::map<std::string, Citation*>& citations) : _citations(citations){};

    bool operator()(std::string a, std::string b) const
    {
        Citation* A = _citations.at(a);
        Citation* B = _citations.at(b);
        
        if (A->getCitationType() == CitationType::Article && B->getCitationType() == CitationType::WebPage)
            return true;
        else if (A->getCitationType() == CitationType::Article && B->getCitationType() == CitationType::Article)
        {
            if (A->getLastName() < B->getLastName())
                return true;
            return false;
        }
        else if (A->getCitationType() == CitationType::WebPage && B->getCitationType() == CitationType::WebPage)
        {
            if (A->getTitle() < B->getTitle())
                return true;
            return false;
        }
        return false;  
    }

protected: 
    std::map<std::string, Citation*> _citations;
};

void insertInlineAlphabetical(std::string& text, const std::map<std::string, Citation*>& citations)
{
    std::string keyData = "";
    std::vector<std::string> keys;
    std::set<std::string> checkKeys;
    size_t i = 0;
    while (i < text.length())
    {
        if (text[i] == '{')
        {
            while (text[i]!= '}') {keyData += text[i]; i++;}
            keyData += text[i];
            i++;
            if (checkKeys.find(keyData) == checkKeys.end())
            {
                checkKeys.insert(keyData);
                keys.push_back(keyData);
            }
            keyData = "";
        }
        else{i++;}
    }
    std::sort(keys.begin(), keys.end(), ComplexSort(citations));
    std::map<std::string, int> data;
    for (size_t j = 0; j < keys.size(); j++)
    {
        data[keys[j]] = j+1;
    }

    std::string result = "";
    i = 0;
    while (i < text.length())
    {
        if (text[i] == '{')
        {
            while (text[i]!= '}') {keyData += text[i]; i++;}
            keyData += text[i];
            i++;
            result += "[" + std::to_string(data[keyData]) + ']';
            keyData = "";
        }
        else{result += text[i]; i++;}
    }
    text = result;
}

#endif

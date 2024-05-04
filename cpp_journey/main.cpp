#include <algorithm>
#include <cmath>
#include <iomanip>
#include <iostream>
#include <string>
#include <vector>
#include <sstream>
#include <fstream>

struct Disease {
    std::string name;// name of the disease
    int severity;    // severity of the disease
    int duration;    // duration of the disease
    int probability; // probability of the disease

    int age;                            // mean age of people with the disease
    std::vector<std::string> symptoms;  // symptoms of the disease
    std::vector<std::string> treatments;// treatments of the disease
    std::vector<std::string> vaccines;  // vaccines of the disease

    // constructor
    Disease(const std::string& name, int severity, int duration, int probability, int age, std::vector<std::string>& symptoms, std::vector<std::string>& treatments, std::vector<std::string>& vaccines) : name(name), severity(severity), duration(duration), probability(probability), age(age), symptoms(symptoms), treatments(treatments), vaccines(vaccines){};
    // default constructor
    Disease() : name(""), severity(0), duration(0), probability(0), age(0), symptoms(std::vector<std::string>()), treatments(std::vector<std::string>()), vaccines(std::vector<std::string>()){};

    Disease(const std::string& _name, const int& _severity, const int& _duration, const int& _probability, const int& _age)
    {
        name = _name;
        severity = _severity;
        duration = _duration;
        probability = _probability;
        age = _age;
        symptoms = std::vector<std::string>();
        treatments = std::vector<std::string>();
        vaccines = std::vector<std::string>();
    }
    Disease(const std::string& name, int severity, int duration, int probability, int age, const std::vector<std::string>& symptoms, const std::vector<std::string>& treatments, const std::vector<std::string>& vaccines) : name(name), severity(severity), duration(duration), probability(probability), age(age), symptoms(symptoms), treatments(treatments), vaccines(vaccines) {}

    // print function
    void showData(const std::string _type) const
    {
        // use table format with indented alignment
        // also use std::setw() to set the width of the columns
        if (_type == "table")
        {
            // Format the table with clear edges
            // print _type
            std::cout << std::left << std::setw(20) << "Name:" << std::setw(20) << "Severity:" << std::setw(20) << "Duration:" << std::setw(20) << "Probability:" << std::setw(20) << "Age:" << std::endl;
            std::cout << std::left << std::setw(20) << name << std::setw(20) << severity << std::setw(20) << duration << std::setw(20) << probability << std::setw(20) << age << std::endl;

            std::cout << std::endl;
            std::cout << std::left << std::setw(20) << "Symptoms:" << std::setw(20) << "Treatments:" << std::setw(20) << "Vaccines:" << std::setw(20) << std::endl;
            int max_size = fmax(fmax(symptoms.size(), treatments.size()), vaccines.size());

            // print symptoms, treatments, vaccines as a table with indented alignment
            // add boader line between each column
            for (int i = 0; i < max_size; i++)
            {
                std::cout << std::left << std::setw(20) << (i < symptoms.size() ? symptoms[i] : "") << std::setw(20) << (i < treatments.size() ? treatments[i] : "") << std::setw(20) << (i < vaccines.size() ? vaccines[i] : "") << std::endl;
            }
            std::cout << std::endl;
        }
        else if (_type == "list")
        {
            // print _type
            std::cout << "Name: " << name << std::endl;
            std::cout << "Severity: " << severity << std::endl;
            std::cout << "Duration: " << duration << std::endl;
            std::cout << "Probability: " << probability << std::endl;
            std::cout << "Age: " << age << std::endl;

            // print symptoms, treatments, vaccines as a list with indented alignment
            // separate by comma
            std::cout << "Symptoms: ";
            for (int i = 0; i < symptoms.size(); i++)
            {
                std::cout << symptoms[i];
                if (i < symptoms.size() - 1)
                    std::cout << ", ";
            }
            std::cout << std::endl;

            std::cout << "Treatments: ";
            for (int i = 0; i < treatments.size(); i++)
            {
                std::cout << treatments[i];
                if (i < treatments.size() - 1)
                    std::cout << ", ";
            }
            std::cout << std::endl;

            std::cout << "Vaccines: ";
            for (int i = 0; i < vaccines.size(); i++)
            {
                std::cout << vaccines[i];
                if (i < vaccines.size() - 1)
                    std::cout << ", ";
            }
            std::cout << std::endl;
        }
    }

    // operator overloading
    bool operator==(const Disease& other) const
    {
        return name == other.name && severity == other.severity && duration == other.duration && probability == other.probability && age == other.age && symptoms == other.symptoms && treatments == other.treatments && vaccines == other.vaccines;
    }
    bool operator!=(const Disease& other) const { return !(*this == other); }

    bool operator<(const Disease& other) const
    {
        return severity < other.severity;
    }
    bool operator>(const Disease& other) const { return !(other < *this); }


};

void printDiseases(const std::vector<Disease>& diseases, const std::string& _type)
{
    for (const Disease& disease: diseases)
    {
        disease.showData(_type);
    }
}
void searchDiseaseByName(const std::vector<Disease>& diseases, const std::string& name)
{
    for (const Disease& disease: diseases)
    {
        if (disease.name == name)
        {
            Disease foundDisease = disease;
            std::cout << "Disease with name '" << name << "' found." << std::endl;
            foundDisease.showData("list");// Assuming you want to print the found disease in table format
            return;
        }
    }
    std::cout << "Disease with name '" << name << "' not found." << std::endl;
}


std::vector<Disease> fillDiseases()
{
    std::vector<Disease> diseases;

    diseases.push_back(Disease("Covid-19", 10, 14, 5, 30, {"Fever", "Cough", "Shortness of breath"}, {"Rest", "Fluids", "Medical care"}, {"Pfizer", "Moderna", "AstraZeneca"}));
    diseases.push_back(Disease("Influenza", 5, 7, 15, 25, {"Fever", "Cough", "Sore throat"}, {"Antiviral drugs", "Rest", "Fluids"}, {"Seasonal flu vaccine"}));
    diseases.push_back(Disease("Chickenpox", 3, 10, 20, 6, {"Rash", "Itching", "Fever"}, {"Antihistamines", "Paracetamol", "Topical ointments"}, {"Varicella vaccine"}));
    diseases.push_back(Disease("Measles", 8, 14, 9, 5, {"Fever", "Rash", "Cough"}, {"Vitamin A", "Supportive care"}, {"MMR vaccine"}));
    diseases.push_back(Disease("Malaria", 9, 30, 25, 20, {"Fever", "Chills", "Vomiting"}, {"Antimalarial drugs"}, {}));
    diseases.push_back(Disease("Tuberculosis", 7, 180, 10, 25, {"Cough", "Weight loss", "Night sweats"}, {"Antibiotics"}, {}));
    diseases.push_back(Disease("HIV/AIDS", 10, 3650, 30, 35, {"Weight loss", "Fever", "Night sweats"}, {"Antiretroviral therapy"}, {}));
    diseases.push_back(Disease("Ebola", 9, 21, 2, 40, {"Fever", "Headache", "Hemorrhage"}, {"Supportive care", "Fluids", "Oxygen"}, {}));
    diseases.push_back(Disease("Zika Virus", 2, 14, 5, 30, {"Rash", "Fever", "Conjunctivitis"}, {"Rest", "Fluids"}, {}));
    diseases.push_back(Disease("Dengue", 6, 14, 20, 25, {"High fever", "Severe headache", "Pain behind the eyes"}, {"Pain relievers", "Fluids"}, {}));

    return diseases;
}

std::vector<Disease> readDiseasesFromCSV(const std::string& filename)
{
    /*  The selected code is part of a function in the C++ program that reads data from a CSV file and stores it in a vector of Disease objects. 
    The function uses the std::stringstream class to parse each line of the CSV file and extract the data from each field.

    The function starts by opening the file and checking if it was successful. 
    If the file cannot be opened, the function returns an empty vector.

    The function then skips the first line of the CSV file, which contains the column headers. 
    It does this by using the std::getline function to read a line from the file and then ignoring it.

    The function then loops through each line of the CSV file, parsing each field 
    and adding it to a vector of strings. Once all fields have been read, 
    the function creates stringstream objects to parse the symptoms, treatments, and vaccines fields.

    It then loops through each of these fields, 
    splitting them on semicolons and adding each part to the appropriate vector. 
    Once all fields have been processed, 
    the function creates a Disease object with the parsed data and adds it to the vector of diseases.

    Finally, the function closes the file and returns the vector of diseases.*/

    std::vector<Disease> diseases;
    std::ifstream file(filename);
    if (!file.is_open())
    {
        std::cout << "Error opening file " << filename << std::endl;
        return {};
    }

    std::string line;
    // Skip the header line
    std::getline(file, line);

    while (std::getline(file, line))
    {
        std::stringstream ss(line);
        std::string field;
        std::vector<std::string> fields;// containg all fields in a line

        while (std::getline(ss, field, ','))
        {
            fields.push_back(field);
        }

        // line = "Covid-19,10,14,5,30,"Fever; Cough; Shortness of breath","Rest; Fluids; Medical care","Pfizer; Moderna; AstraZeneca""
        /* fields = {
                "Covid-19", [0]
                "10", [1]
                "14", [2]
                "5",  [3]
                "30", [4]
                "Fever; Cough; Shortness of breath", [5]
                "Rest; Fluids; Medical care", [6]
                "Pfizer; Moderna; AstraZeneca" [7]
                } */


        // Assuming all fields are present and in correct order
        // fields[i] is a string representing a field in the CSV file
        std::string name = fields[0];
        int severity = std::stoi(fields[1]);// string to int = s_to_i = stoi
        int duration = std::stoi(fields[2]);
        int probability = std::stoi(fields[3]);
        int age = std::stoi(fields[4]);

        std::vector<std::string> symptoms;
        std::vector<std::string> treatments;
        std::vector<std::string> vaccines;

        // Splitting symptoms, treatments, and vaccines by semicolon

        // fields[5] = "Fever; Cough; Shortness of breath";

        std::stringstream ssSymptoms(fields[5]);
        std::string symptom;
        while (std::getline(ssSymptoms, symptom, ';'))
        {
            symptoms.push_back(symptom);
        }
        // symptoms = {"Fever", "Cough", "Shortness of breath"}

        std::stringstream ssTreatments(fields[6]);
        std::string treatment;
        while (std::getline(ssTreatments, treatment, ';'))
        {
            treatments.push_back(treatment);
        }
        // treatments = {"Antiviral drugs", "Rest", "Fluids"}

        std::stringstream ssVaccines(fields[7]);
        std::string vaccine;
        while (std::getline(ssVaccines, vaccine, ';'))
        {
            vaccines.push_back(vaccine);
        }
        // vaccines = {"Seasonal flu vaccine"}

        Disease _disiase(name, severity, duration, probability, age, symptoms, treatments, vaccines);
        diseases.push_back(_disiase);
    }

    return diseases;
}

int main()
{
    // std::vector<Disease> diseases = fillDiseases();
    std::vector<Disease> diseases = readDiseasesFromCSV("diseases.csv");
    std::cout << diseases.size() << " diseases loaded." << std::endl;

    // printDiseases(diseases, "table");
    printDiseases(diseases, "list");

    searchDiseaseByName(diseases, "Ebola");
    searchDiseaseByName(diseases, "Covid-25");

    return 0;
}

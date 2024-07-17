///////////////////////////////////////////////////////////////////////////////
/// \file
/// \version    0.1.0
/// \date       30.01.2024
///
/// TASK DESCRIPTION
///
/// Create a function that copies the content of one file to another file.
///
///////////////////////////////////////////////////////////////////////////////
#include <iostream>
#include <cmath>
#include <cstdint>
#include <fstream>
#include <cassert>

void copyFile(const std::string &sourceFilePath, const std::string &destinationFilePath);

int main()
{
    copyFile("input.jpg", "output.jpg");
    return 0;
}
void copyFile(const std::string &sourceFilePath, const std::string &destinationFilePath)
{
    std::ifstream inputFile(sourceFilePath, std::ios_base::binary);
    if (!inputFile.is_open()){
        return;
    }

    std::ofstream outFile(destinationFilePath);
    if (!outFile.is_open()){
        return;
    }

    uint8_t buff;

    while (inputFile && !inputFile.eof())
    {
        // inputFile >> buff;
        // outFile << buff;
        // wont work for binary (in some cases), only for text

        buff = inputFile.get();
        outFile.put(buff);
    }
    // file streams are better to close explicitly;
    // outFile.flush(); // writes cache to real disks
    // executes at the file closing
    inputFile.close();
    outFile.close();

    return;

}

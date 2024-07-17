///////////////////////////////////////////////////////////////////////////////
/// \file
/// \version    0.1.0
/// \date       30.01.2024
///
/// TASK DESCRIPTION
///
/// Write a function to read a file containing integers
/// separated by spaces or newlines, sum these integers, and write the result to another file.
///////////////////////////////////////////////////////////////////////////////

#include <iostream>
#include <cmath>
#include <fstream>
#include <cassert>

int sumIntegersInFile(const std::string& inputFilePath, const std::string& outputFilePath);

int main()
{
    // assert(sumIntegersInFile("input.txt", "output.txt") == 11);
    sumIntegersInFile("input.txt", "output.txt");
    return 0;
}

int sumIntegersInFile(const std::string& inputFilePath, const std::string& outputFilePath)
{
    std::ifstream inputFile(inputFilePath);

    if (!inputFile.is_open()){
        return 0;
    }

    int ans = 0;
    int num = 0;

    while (inputFile && !inputFile.eof())
    {
        inputFile >> num;
        ans += num;
    }
    
    std::ofstream outFile(outputFilePath);

    if (!outFile.is_open()){
        return ans;
    }

    outFile << ans;

    return ans;

}

// ,
//   {
//     "name": "GCC 13.2.0 aarch64-apple-darwin23",
//     "compilers": {
//       "C": "/opt/homebrew/bin/aarch64-apple-darwin23-gcc-13",
//       "CXX": "/opt/homebrew/bin/aarch64-apple-darwin23-g++-13"
//     },
//     "isTrusted": true
//   }
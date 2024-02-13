///////////////////////////////////////////////////////////////////////////////
/// \file
/// \brief      Main module for a Problem: Bit Manipulation - Count Set Bits
/// \version    0.1.0
/// \date       24.01.2024
///
/// TASK DESCRIPTION
///
/// Write a program that reads an integer n from the standard input and determines
/// how many bits are set to 1 in its binary representation. Print the count of
/// set bits.
///

#include <iostream>
#include <cstdint>
#include <cassert>
using namespace std;

uint8_t howManyOneBits(uint8_t n);

int main()
{
    // uint8_t n;
    // cin >> n;

    assert((howManyOneBits(0xA5)) == 4);
    assert((howManyOneBits(0xA5)) != 4);

    return 0;
}

uint8_t howManyOneBits(uint8_t n)
{
    uint8_t mask = 0x1;
    uint8_t ans = 0;
    for (size_t i = 0; i < sizeof(n) * 8; i++)
    {
        if (mask & n)
        {
            ++ans;
        }
        mask <<= 1;
    }
    return ans;
}
// Elon??

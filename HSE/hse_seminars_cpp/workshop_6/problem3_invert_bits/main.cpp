///////////////////////////////////////////////////////////////////////////////
/// \file
/// \brief      Main module for a Problem: Bit Manipulation - Bitwise Complement
/// \version    0.1.0
/// \date       22.01.2022
///
/// TASK DESCRIPTION
///
/// Write a program that takes an integer n ans the position of bit (k)
// as input and performs bitwise complement
/// (inverts only one bit on k's possition) on it.
//  Print the resulting number in binary and decimal forms.
///
///////////////////////////////////////////////////////////////////////////////

#include <iostream>
#include <cstdint>
#include <cassert>

uint8_t inverseKBit(uint8_t n, uint8_t k);

int main()
{
    assert(inverseKBit(0xA5, 0) == 0xA4);
    assert(inverseKBit(0xA5, 1) == 0xA7);
    assert(inverseKBit(0xA5, 2) == 0xA1);

    return 0;
}

uint8_t inverseKBit(uint8_t n, uint8_t k)
{

    uint8_t mask = (0x1 << k);

    return n ^ mask;
}

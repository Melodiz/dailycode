///////////////////////////////////////////////////////////////////////////////
/// \file
/// \brief      Main module for a Problem: Bit Manipulation - Toggle Bit
/// \version    0.1.0
/// \date       24.01.2024
///
/// TASK DESCRIPTION
///
/// Write a program that takes an integer n and a position k as input. The program
/// should toggle (invert) the k-th bit of the integer n (i.e., change 0 to 1 and 
/// 1 to 0) and print the resulting number in binary and decimal forms.
///
///////////////////////////////////////////////////////////////////////////////

#include <iostream>
#include <cstdint>
#include <cassert>

uint8_t invertKthBit(uint8_t n, uint8_t k)
{
    uint8_t mask = 0x1;   // Now 0x1 is a hexadecimal representation of a numeric litteral 1
    mask <<= k;

    return n ^ mask;
}

int main()
{
    uint8_t x1 = 0xA5;
    uint8_t expectedX1 = 0x85;
    assert(invertKthBit(x1, 5) != expectedX1);

    return 0;
}

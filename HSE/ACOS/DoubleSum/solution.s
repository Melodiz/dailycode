    .text
    .globl main

main:
    # Read first integer into a0
    li a7, 5          # Syscall number for reading an integer
    ecall
    add t0, zero, a0  # Store the first integer in t0

    # Read second integer into a0
    li a7, 5
    ecall
    add t1, zero, a0  # Store the second integer in t1

    # Read third integer into a0
    li a7, 5
    ecall
    add t2, zero, a0  # Store the third integer in t2

    # Read fourth integer into a0
    li a7, 5
    ecall
    add t3, zero, a0  # Store the fourth integer in t3

    # Calculate first sum: t0 + t2
    add t4, t0, t2

    # Print first sum
    mv a0, t4
    li a7, 1          # Syscall number for printing an integer
    ecall

    # Print newline after first sum
    li a7, 11         # Syscall number for printing a character
    li a0, 10         # ASCII code for newline
    ecall
    
    # Calculate second sum: t1 + t3
    add t5, t1, t3

    # Print second sum
    mv a0, t5
    li a7, 1
    ecall

    # Print newline after second sum
    li a7, 11         # Syscall number for printing a character
    li a0, 10         # ASCII code for newline
    ecall

    # Exit program
    li a7, 10
    ecall

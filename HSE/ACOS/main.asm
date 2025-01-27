    .text
main:
    # Read integer
    addi a7, zero, 5
    ecall
    mv t0, a0  # Store input in t0

    # Print integer
    mv a0, t0
    addi a7, zero, 1
    ecall

    # Print newline 
    li a0, 10  # ASCII code for newline
    addi a7, zero, 11
    ecall

    # Print integer in hexadecimal
    mv a0, t0
    addi a7, zero, 34
    ecall

    # Exit program
    li a7, 10
    ecall
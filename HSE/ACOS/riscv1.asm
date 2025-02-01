.text
main:
    # read x
    addi a7, zero, 5  # Set syscall number for reading an integer
    ecall             # Make syscall to read integer into a0
    add t0, zero, a0  # Store the read integer in t0

    # read y 
    addi a7, zero, 5  # Set syscall number for reading an integer
    ecall             # Make syscall to read integer into a0
    add t1, zero, a0  # Store the read integer in t1
    
    mv t5, t0         # Copy x to t5 for future use
    mv t6, t1         # Copy y to t6 for future use
    
    # Task 1: Calculate (x >> 2) + ((y - 1) << 3)
    srli t2, t0, 2    # Logical right shift x by 2 bits (x >> 2)
    addi t3, t1, -1   # Subtract 1 from y
    slli t3, t3, 3    # Logical left shift (y - 1) by 3 bits ((y - 1) << 3)
    add t4, t2, t3    # Add the results of the two operations
    
    # Printing result of Task 1
    mv a0, t4         # Move result to a0 for printing
    li a7, 1          # Set syscall number for printing an integer
    ecall             # Make syscall to print integer
    li a7, 11         # Set syscall number for printing a character
    li a0, '\n'       # Newline character
    ecall             # Make syscall to print newline

    # Task 2: Calculate (x << y) - 10
    sll t0, t0, t1    # Logical left shift x by y bits (x << y)
    addi t0, t0, -10  # Subtract 10 from the result
    # Printing result of Task 2
    mv a0, t0         # Move result to a0 for printing
    li a7, 1          # Set syscall number for printing an integer
    ecall             # Make syscall to print integer
    li a7, 11         # Set syscall number for printing a character
    li a0, '\n'       # Newline character
    ecall             # Make syscall to print newline
    
    # Task 3: Calculate (x >> y) + 10
    mv t0, t5         # Restore original x from t5
    sra t3, t0, t1    # Arithmetic right shift x by y bits (x >> y)
    addi t3, t3, 10   # Add 10 to the result
    # Printing result of Task 3
    mv a0, t3         # Move result to a0 for printing
    li a7, 1          # Set syscall number for printing an integer
    ecall             # Make syscall to print integer
    li a7, 11         # Set syscall number for printing a character
    li a0, '\n'       # Newline character
    ecall             # Make syscall to print newline
    
    # Task 4: Calculate ((x << 2) - y + 5) >> 1
    mv t0, t5         # Restore original x from t5
    mv t1, t6         # Restore original y from t6
    
    slli t2, t0, 2    # Logical left shift x by 2 bits (x << 2)
    sub t3, t2, t1    # Subtract y from the result
    addi t3, t3, 5    # Add 5 to the result
    srai t4, t3, 1    # Arithmetic right shift the result by 1 bit
    # Printing result of Task 4
    mv a0, t4         # Move result to a0 for printing
    li a7, 1          # Set syscall number for printing an integer
    ecall             # Make syscall to print integer
    li a7, 11         # Set syscall number for printing a character
    li a0, '\n'       # Newline character
    ecall             # Make syscall to print newline
    
    # Task 5: Calculate x * 6 - y * 3
    mv t0, t5         # Restore original x from t5
    mv t1, t6         # Restore original y from t6

    slli t2, t0, 2    # Logical left shift x by 2 bits (x << 2) equivalent to 4 * x
    slli t3, t0, 1    # Logical left shift x by 1 bit (x << 1) equivalent to 2 * x
    add t2, t2, t3    # Add the two results to get 6 * x
    
    slli t3, t1, 1    # Logical left shift y by 1 bit (y << 1) equivalent to 2 * y
    add t3, t3, t1    # Add y to the result to get 3 * y
    sub t4, t2, t3    # Subtract 3 * y from 6 * x
    # Printing result of Task 5
    mv a0, t4         # Move result to a0 for printing
    li a7, 1          # Set syscall number for printing an integer
    ecall             # Make syscall to print integer
    li a7, 11         # Set syscall number for printing a character
    li a0, '\n'       # Newline character
    ecall             # Make syscall to print newline
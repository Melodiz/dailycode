main:
    # read x
    addi a7, zero, 5  # Set syscall number for reading an integer
    ecall             # Make syscall to read integer into a0
    add t0, zero, a0  # Store the read integer in t0

    # read y 
    addi a7, zero, 5  # Set syscall number for reading an integer
    ecall             # Make syscall to read integer into a0
    add t1, zero, a0  # Store the read integer in t1

    # Task 1: x & (-1 << 2)
    li t2, -1         # Load -1 into t2
    slli t2, t2, 2    # Logical left shift -1 by 2 bits
    and t3, t0, t2    # Perform bitwise AND with x
    # Print result of Task 1
    mv a0, t3
    li a7, 1
    ecall
    # Print newline
    li a7, 11
    li a0, '\n'
    ecall

    # Task 2: x | (-1 >> 30)
    li t2, -1         # Load -1 into t2
    srli t2, t2, 30   # Logical right shift -1 by 30 bits
    or t3, t0, t2     # Perform bitwise OR with x
    # Print result of Task 2
    mv a0, t3
    li a7, 1
    ecall
    # Print newline
    li a7, 11
    li a0, '\n'
    ecall

    # Task 3: Set the y-th bit of x to 1
    li t2, 1          # Load 1 into t2
    sll t2, t2, t1    # Shift 1 left by y bits
    or t3, t0, t2     # Set the y-th bit of x
    # Print result of Task 3
    mv a0, t3
    li a7, 1
    ecall
    # Print newline
    li a7, 11
    li a0, '\n'
    ecall

    # Task 4: Reset the y-th bit of x to 0
    li t2, 1          # Load 1 into t2
    sll t2, t2, t1    # Shift 1 left by y bits
    not t2, t2        # Invert bits to create mask
    and t3, t0, t2    # Reset the y-th bit of x
    # Print result of Task 4
    mv a0, t3
    li a7, 1
    ecall
    # Print newline
    li a7, 11
    li a0, '\n'
    ecall

    # Task 5: (x == (y + 3)) ? 0 : 1
    addi t2, t1, 3    # Calculate y + 3
    sub t3, t0, t2    # Subtract (y + 3) from x
    slt t4, zero, t3  # Check if x < (y + 3)
    slt t5, t3, zero  # Check if (y + 3) < x
    or t3, t4, t5     # (x == (y + 3)) ? 0 : 1
    # Print result of Task 5
    mv a0, t3
    li a7, 1
    ecall
    # Print newline
    li a7, 11
    li a0, '\n'
    ecall

    # Task 6: x > -5 & y < 5
    li t2, -5         # Load -5 into t2
    slt t4, t2, t0    # Check if x > -5
    li t2, 5          # Load 5 into t2
    slt t5, t1, t2    # Check if y < 5
    and t3, t4, t5    # x > -5 & y < 5
    # Print result of Task 6
    mv a0, t3
    li a7, 1
    ecall
    # Print newline
    li a7, 11
    li a0, '\n'
    ecall

    # Exit program
    li a7, 10
    ecall
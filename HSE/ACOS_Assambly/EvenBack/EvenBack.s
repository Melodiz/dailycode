    .data
array:   .space 400     # Allocate space for up to 100 integers (assuming 4 bytes per integer)

    .text
    .globl main

main:
    # Read N
    li a7, 5           # syscall 5 - read integer
    ecall
    mv s0, a0          # s0 = N
    
    # Initialize array index
    li s1, 0           # s1 = current index
    la s2, array       # s2 = array base address
    
read_loop:
    beqz s0, read_done # If N == 0, exit loop
    
    # Read integer
    li a7, 5           # syscall 5 - read integer
    ecall
    
    # Store integer in array
    sw a0, 0(s2)       # array[index] = input
    addi s2, s2, 4     # Move to next array element
    addi s1, s1, 1     # index++
    addi s0, s0, -1    # N--
    
    j read_loop
    
read_done:
    # Reset array pointer to the end of the array
    la s2, array       # s2 = array base address
    slli s3, s1, 2     # s3 = N * 4 (byte offset)
    add s2, s2, s3     # s2 points to the end of the array
    addi s2, s2, -4    # Adjust to point to the last element
    
print_loop:
    beqz s1, print_done # If index == 0, exit loop
    
    # Load integer from array
    lw a0, 0(s2)       # a0 = array[index]
    
    # Check if even
    li t0, 2
    rem t1, a0, t0     # t1 = a0 % 2
    bnez t1, skip_print # If not even, skip printing
    
    # Print even integer
    li a7, 1           # syscall 1 - print integer
    ecall
    
    # Print newline
    li a7, 11          # syscall 11 - print character
    li a0, 10          # ASCII code for newline
    ecall
    
skip_print:
    addi s2, s2, -4    # Move to previous array element
    addi s1, s1, -1    # index--
    
    j print_loop
    
print_done:
    # Print final newline (required even for empty output)
    li a7, 11          # syscall 11 - print character
    li a0, 10          # ASCII code for newline
    ecall
    
    # Exit program
    li a7, 10          # syscall 10 - exit
    ecall
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
    li s1, 0           # s1 = current index (also represents number of unique elements)
    la s2, array       # s2 = array base address
    
read_loop:
    beqz s0, read_done # If N == 0, exit loop
    
    # Read integer
    li a7, 5           # syscall 5 - read integer
    ecall
    mv t0, a0          # t0 = current input
    
    # Check if this number already exists in our array
    la t1, array       # t1 = start of array for checking
    li t2, 0           # t2 = loop counter for checking
    
check_dup_loop:
    beq t2, s1, not_duplicate  # If we've checked all elements, it's not a duplicate
    
    lw t3, 0(t1)       # t3 = array[t2]
    beq t3, t0, is_duplicate  # If array[t2] == current input, it's a duplicate
    
    addi t1, t1, 4     # Move to next array element
    addi t2, t2, 1     # Increment counter
    j check_dup_loop
    
is_duplicate:
    # Skip this number, it's a duplicate
    j next_iteration
    
not_duplicate:
    # Store the new unique integer in array
    sw t0, 0(s2)       # array[index] = input
    addi s2, s2, 4     # Move to next array element
    addi s1, s1, 1     # index++ (count of unique elements)
    
next_iteration:
    addi s0, s0, -1    # N--
    j read_loop
    
read_done:
    # Print all unique elements in the order they appeared
    la s2, array       # s2 = array base address
    li s0, 0           # s0 = loop counter
    
print_loop:
    beq s0, s1, print_done # If we've printed all unique elements, exit loop
    
    # Load integer from array
    lw a0, 0(s2)       # a0 = array[s0]
    
    # Print integer
    li a7, 1           # syscall 1 - print integer
    ecall
    
    # Print newline
    li a7, 11          # syscall 11 - print character
    li a0, 10          # ASCII code for newline
    ecall
    
    addi s2, s2, 4     # Move to next array element
    addi s0, s0, 1     # Increment counter
    
    j print_loop
    
print_done:
    # Exit program
    li a7, 10          # syscall 10 - exit
    ecall
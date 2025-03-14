    .data
newline: .string "\n"

    .text
    .globl main

main:
    # Read the number of integers, N
    li a7, 5              # syscall for read_int
    ecall
    mv t0, a0             # store N in t0

    # Initialize sum and index
    li t1, 0              # t1 will hold the sum
    li t2, 0              # t2 will be the index
    li t5, 2              # t5 will hold the value 2 for modulus operation

loop:
    beq t2, t0, print_result # if index equals N, exit loop

    # Read the next integer
    li a7, 5              # syscall for read_int
    ecall
    mv t3, a0             # store the current integer in t3

    # Calculate alternating sum
    rem t4, t2, t5        # t4 = t2 % 2
    beqz t4, add_to_sum   # if t4 is 0, add to sum
    sub t1, t1, t3        # else, subtract from sum
    j increment_index

add_to_sum:
    add t1, t1, t3        # add to sum

increment_index:
    addi t2, t2, 1        # increment index
    j loop

print_result:
    # Print the result
    mv a0, t1             # move sum to a0 for printing
    li a7, 1              # syscall for print_int
    ecall

    # Print newline
    li a7, 4              # syscall for print_string
    la a0, newline        # load address of newline
    ecall

    # Exit program
    li a7, 10             # syscall for exit
    ecall
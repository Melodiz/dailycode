    .data
newline: .string "\n"
array:   .space 400     # Allocate space for up to 100 integers (assuming 4 bytes per integer)

    .text
    .globl main

main:
    # Read the number of integers, N
    li a7, 5              # syscall for read_int
    ecall
    mv t0, a0             # store N in t0

    # Initialize index and even count
    li t1, 0              # t1 will be the index for input
    li t2, 0              # t2 will count the even numbers
    li t5, 2              # t5 will hold the value 2 for modulus operation
    la t6, array          # load the address of array into t6

read_loop:
    beq t1, t0, print_even # if index equals N, exit loop

    # Read the next integer
    li a7, 5              # syscall for read_int
    ecall
    mv t3, a0             # store the current integer in t3

    # Check if the integer is even
    rem t4, t3, t5        # t4 = t3 % 2
    bnez t4, increment_index # if t4 is not 0, it's odd, skip storing

    # Store even integer in array
    slli t7, t2, 2        # t7 = t2 * 4 (byte offset for storing)
    add t7, t7, t6        # t7 = address of array[t2]
    sw t3, 0(t7)          # store t3 at array[t2]
    addi t2, t2, 1        # increment even count

increment_index:
    addi t1, t1, 1        # increment index
    j read_loop

print_even:
    # Print even numbers in reverse order
    beqz t2, print_newline # if no even numbers, just print newline

print_loop:
    addi t2, t2, -1       # decrement even count
    slli t7, t2, 2        # t7 = t2 * 4 (byte offset for loading)
    add t7, t7, t6        # t7 = address of array[t2]
    lw a0, 0(t7)          # load the even number
    li a7, 1              # syscall for print_int
    ecall

    # Print newline after each number
    li a7, 4              # syscall for print_string
    la a0, newline        # load address of newline
    ecall

    bnez t2, print_loop   # if t2 is not zero, continue loop

print_newline:
    # Print a newline at the end
    li a7, 4              # syscall for print_string
    la a0, newline        # load address of newline
    ecall

    # Exit program
    li a7, 10             # syscall for exit
    ecall
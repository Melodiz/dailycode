    .data
newline: .string "\n"

    .text
    .globl main

main:
    # Read integer input
    li a7, 5              # syscall for read_int
    ecall
    mv t0, a0             # move input to t0 for processing

    # Convert to absolute value if negative
    bltz t0, make_positive
    j calculate_sum

make_positive:
    neg t0, t0            # negate the value to make it positive

calculate_sum:
    li t1, 0              # t1 will hold the sum of digits
    li t3, 10             # t3 will hold the divisor (10)

sum_loop:
    beqz t0, print_result # if t0 is 0, exit loop
    rem t2, t0, t3        # t2 = t0 % 10 (get last digit)
    add t1, t1, t2        # add digit to sum
    div t0, t0, t3        # t0 = t0 / 10 (remove last digit)
    j sum_loop

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
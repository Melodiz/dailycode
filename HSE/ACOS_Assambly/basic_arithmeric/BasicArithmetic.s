.data
    newline: .string "\n"

.text
.globl main

main:
    # Read x
    li a7, 5
    ecall
    mv s0, a0  # s0 = x

    # Read y
    li a7, 5
    ecall
    mv s1, a0  # s1 = y

    # 1. (x + 5) - (y - 7)
    addi t0, s0, 5  # t0 = x + 5
    addi t1, s1, -7  # t1 = y - 7
    sub t2, t0, t1  # t2 = (x + 5) - (y - 7)
    mv a0, t2
    jal print_result

    # 2. 2 * x * x - 3 * y + 4
    mul t0, s0, s0  # t0 = x * x
    li t1, 2
    mul t0, t0, t1  # t0 = 2 * x * x
    li t1, 3
    mul t1, t1, s1  # t1 = 3 * y
    sub t2, t0, t1  # t2 = 2 * x * x - 3 * y
    addi t2, t2, 4  # t2 = 2 * x * x - 3 * y + 4
    mv a0, t2
    jal print_result

    # 3. (x + 5) / y + 10 / (y - 1)
    # Check for division by zero
    beqz s1, skip_div1  # if y == 0, skip
    addi t0, s0, 5  # t0 = x + 5
    div t0, t0, s1  # t0 = (x + 5) / y
    addi t1, s1, -1  # t1 = y - 1
    beqz t1, skip_div1  # if y - 1 == 0, skip
    li t2, 10
    div t1, t2, t1  # t1 = 10 / (y - 1)
    add t2, t0, t1  # t2 = (x + 5) / y + 10 / (y - 1)
    mv a0, t2
    jal print_result
skip_div1:

    # 4. (x / y) * y + x % y
    # Check for division by zero
    beqz s1, skip_div2  # if y == 0, skip
    div t0, s0, s1  # t0 = x / y
    mul t0, t0, s1  # t0 = (x / y) * y
    rem t1, s0, s1  # t1 = x % y
    add t2, t0, t1  # t2 = (x / y) * y + x % y
    mv a0, t2
    jal print_result
skip_div2:

    # 5. x > y ? 1 : 0
    slt t0, s1, s0  # t0 = 1 if x > y, else 0
    mv a0, t0
    jal print_result

    # Exit program
    li a7, 10
    ecall

print_result:
    # Print integer result
    li a7, 1
    ecall

    # Print newline
    li a7, 11
    li a0, '\n'
    ecall

    ret
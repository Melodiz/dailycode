.text
main:
    # read x
    addi a7, zero, 5
    ecall
    add t0, zero, a0

    # read y 
    addi a7, zero, 5
    ecall
    add t1, zero, a0
    
    mv t5, t0	# copy x to t5 for future
    mv t6, t1	# copy y to t6 for future
    
    # Task 1
    srli t2, t0, 2	# x >> 2
    addi t3, t1, -1
    slli t3, t3, 3	# y - 1) << 3
    add t4, t2, t3	# t2+t3
    
    # Printing
    mv a0, t4 
    li a7, 1 
    ecall 
    li a7, 11 
    li a0, '\n'
    ecall

    # Task 2
    sll t0, t0, t1	# t0 = x << y
    addi t0, t0, -10
    # Printing
    mv a0, t0
    li a7, 1
    ecall
    li a7, 11
    li a0, '\n'
    ecall
    
    # Task 3
    mv t0, t5
    sra t3, t0, t1	# t2 = x >> y
    addi t3, t3, 10	# t3 = (x >> y) + 10
    # Printing
    mv a0, t3
    li a7, 1
    ecall
    li a7, 11
    li a0, '\n'
    ecall
    
    # Task 4
    mv t0, t5
    mv t1, t6
    
    slli t2, t0, 2	# t2 = x << 2
    sub t3, t2, t1
    addi t3, t3, 5
    srai t4, t3, 1	# t4 = ((x << 2) - y + 5) >> 1
    # Printing
    mv a0, t4
    li a7, 1
    ecall
    li a7, 11
    li a0, '\n'
    ecall
    
    # Task 5
    mv t0, t5
    mv t1, t6

    slli t2, t0, 2	# t2 = x << 2 aka x * 2^2
    slli t3, t0, 1	# t3 = x << 1 aka x * 2^1
    add t2, t2, t3	# t2 = 4x + 2x = x * 6 omg
    
    slli t3, t1, 1	# t3 = y << 1 aka y * 2^1
    add t3, t3, t1	# t3 = 2y + y = 3y
    sub t4, t2, t3
    # Printing
    mv a0, t4
    li a7, 1
    ecall
    li a7, 11
    li a0, '\n'
    ecall
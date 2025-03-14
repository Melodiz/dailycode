.globl main

main:
    li a7, 5
    ecall
    mv t0, a0
    
    li t1, 3
    blt t0, t1, case1
    
    li t1, 7
    beq t0, t1, case3
    
    li t1, 8
    bgt t0, t1, case4
    
    j case2
    
case1:
    li t2, 1
    li t3, 2
    
    beqz t0, power_done
    
power_loop:
    slli t2, t2, 1
    addi t0, t0, -1
    bnez t0, power_loop

power_done:
    neg t2, t2
    addi a0, t2, 2
    j print_result

case2:
    mv t1, t0
    mul t2, t0, t0
    mul t2, t2, t2
    li t3, 2
    mul t2, t2, t3
    
    mv t1, t0
    mul t3, t1, t1
    mul t3, t3, t1
    li t4, 7
    mul t3, t3, t4
    
    add t2, t2, t3
    
    li t3, 8
    mul t3, t3, t0
    
    sub a0, t2, t3
    j print_result

case3:
    li a0, -2
    j print_result

case4:
    li t1, 7
    mul t1, t1, t0
    neg t1, t1
    addi a0, t1, -5
    j print_result

print_result:
    li a7, 1
    ecall
    
    li a7, 11
    li a0, 10
    ecall
    
    li a7, 10
    ecall
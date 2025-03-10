.data
newline: .asciz "\n"

.text
.globl main

main:
    li a7, 5
    ecall
    mv t0, a0
    
    li t1, 3
    bge t0, t1, else_case
    
    li t2, 1
    
    beqz t0, power_done
    
power_loop:
    slli t2, t2, 1
    addi t0, t0, -1
    bnez t0, power_loop
    
power_done:
    neg t2, t2
    addi a0, t2, 2
    j print_result
    
else_case:
    li a0, -1
    
print_result:
    li a7, 1
    ecall
    
    li a7, 4
    la a0, newline
    ecall
    
    li a7, 10
    ecall
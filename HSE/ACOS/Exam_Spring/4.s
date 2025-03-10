.data
newline: .asciz "\n"

.text
.globl main

main:
    li a7, 5
    ecall
    mv s0, a0
    
    li t0, 8
    ble s0, t0, else_case
    
    li t1, 7
    mul t1, t1, s0
    neg t1, t1
    addi a0, t1, -5
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
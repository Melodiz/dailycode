.data
newline: .asciz "\n"

.text
.globl main

main:
    li a7, 5
    ecall
    mv s0, a0
    
    li t0, 7
    bne s0, t0, else_case
    
    li a0, -2
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
.data
newline: .asciz "\n"

.text
.globl main

main:
    li a7, 5
    ecall
    mv s0, a0
    
    li t0, 3
    blt s0, t0, else_case
    
    mul t0, s0, s0
    
    mul t1, t0, s0
    
    mul t2, t1, s0
    
    li t3, 2
    mul t3, t3, t2
    
    li t4, 7
    mul t4, t4, t1
    
    li t5, 8
    mul t5, t5, s0
    
    add t6, t3, t4
    
    sub a0, t6, t5
    
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
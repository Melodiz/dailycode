    .data
arr_storage:    .space 400

    .text
    .globl main

main:                      
    li      a7, 5         
    ecall
    mv      s0, a0       

    li      a7, 5
    ecall
    mv      s1, a0      

    la      t0, arr_storage
    li      t1, 0         
input_cycle:
    beq     t1, s0, input_end
    li      a7, 5               
    ecall
    sw      a0, 0(t0)           
    addi    t0, t0, 4           
    addi    t1, t1, 1           
    j       input_cycle
input_end:

    mv      a0, s0        
    la      a1, arr_storage

    beqz    s1, use_first_comparator
    la      a2, second_comparator
    j       invoke_sorter
use_first_comparator:
    la      a2, first_comparator

invoke_sorter:
    jal     array_sorter

    mv      t2, a0
    mv      t3, a1
output_cycle:
    beqz    t2, output_end
    lw      a0, 0(t3)
    li      a7, 1        
    ecall

    li      a7, 11
    li      a0, 10
    ecall

    addi    t3, t3, 4
    addi    t2, t2, -1
    j       output_cycle

output_end:
    li      a7, 10       
    ecall

array_sorter:
    addi    sp, sp, -16
    sw      ra, 12(sp)
    sw      s0, 8(sp)
    sw      s1, 4(sp)
    sw      s2, 0(sp)

    mv      s0, a0
    mv      s1, a1
    mv      s2, a2

    addi    t0, s0, -1
outer_iteration:
    blez    t0, sort_complete

    mv      t1, s0
    addi    t1, t1, -1
    mv      t3, s1
inner_iteration:
    lw      t4, 0(t3)
    lw      t5, 4(t3)

    mv      a0, t4
    mv      a1, t5
    jalr    ra, 0(s2)

    beqz    a0, swap_elements
    j       skip_swap
swap_elements:
    sw      t5, 0(t3)
    sw      t4, 4(t3)
skip_swap:
    addi    t3, t3, 4
    addi    t1, t1, -1
    bnez    t1, inner_iteration

    addi    t0, t0, -1
    j       outer_iteration

sort_complete:
    mv      a0, s0
    mv      a1, s1
    lw      ra, 12(sp)
    lw      s0, 8(sp)
    lw      s1, 4(sp)
    lw      s2, 0(sp)
    addi    sp, sp, 16
    ret

first_comparator:
    blt     a0, a1, return_true
    li      a0, 0
    ret
return_true:
    li      a0, 1
    ret

second_comparator:
    li      t0, 10
    rem     t1, a0, t0
    rem     t2, a1, t0
    ble     t1, t2, return_false
    li      a0, 1
    ret
return_false:
    li      a0, 0
    ret
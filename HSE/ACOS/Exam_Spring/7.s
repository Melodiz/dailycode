.globl func

func:
    addi sp, sp, -40
    sw s0, 0(sp)
    sw s1, 4(sp)
    sw s2, 8(sp)
    sw s3, 12(sp)
    sw s4, 16(sp)
    sw s5, 20(sp)
    sw ra, 24(sp)
    sw s6, 28(sp)
    sw s7, 32(sp)
    sw s8, 36(sp)
    
    mv s0, a0
    
    li s1, 3
    blt s0, s1, case1
    
    li s1, 7
    beq s0, s1, case3
    
    li s1, 8
    bgt s0, s1, case4
    
    j case2
    
case1:
    li s1, 1
    li s2, 2
    
    beqz s0, power_done
    
power_loop:
    slli s1, s1, 1
    addi s0, s0, -1
    bnez s0, power_loop

power_done:
    neg s1, s1
    addi a0, s1, 2
    j func_end

case2:
    mv s1, s0
    mul s2, s0, s0
    mul s2, s2, s2
    li s3, 2
    mul s2, s2, s3
    
    mul s4, s0, s0
    mul s4, s4, s0
    li s5, 7
    mul s4, s4, s5
    
    add s6, s2, s4
    
    li s7, 8
    mul s7, s7, s0
    
    sub a0, s6, s7
    j func_end

case3:
    li a0, -2
    j func_end

case4:
    li s1, 7
    mul s1, s1, s0
    neg s1, s1
    addi a0, s1, -5

func_end:
    lw s0, 0(sp)
    lw s1, 4(sp)
    lw s2, 8(sp)
    lw s3, 12(sp)
    lw s4, 16(sp)
    lw s5, 20(sp)
    lw ra, 24(sp)
    lw s6, 28(sp)
    lw s7, 32(sp)
    lw s8, 36(sp)
    addi sp, sp, 40
    
    ret
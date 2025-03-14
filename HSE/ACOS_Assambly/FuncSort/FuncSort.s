.macro print_int (%x)
   li a7, 1
   mv a0, %x
   ecall
.end_macro

.macro print_imm_int (%x)
   li a7, 1
   li a0, %x
   ecall
.end_macro

.macro read_int(%x)
   li a7, 5
   ecall
   mv %x, a0
.end_macro

.macro print_str (%x)
   .data
str:
   .asciz %x
   .text
   li a7, 4
   la a0, str
   ecall
.end_macro

.macro print_char(%x)
   li a7, 11
   li a0, %x
   ecall
.end_macro

.macro newline
   print_char('\n')
.end_macro

.data
array: .space 400  

.text
main:
    read_int(s0)

    la s1, array 
    mv t1, s0 
read_loop:
    beqz t1, read_done
    read_int(t2)    
    sw t2, 0(s1)     
    addi s1, s1, 4  
    addi t1, t1, -1
    j read_loop
read_done:
    la a0, array 
    slli t0, s0, 2 
    add a1, a0, t0    
    jal ra, bubble_sort

    la s1, array   
    mv t1, s0 
print_loop:
    beqz t1, print_done 
    lw t2, 0(s1)        
    print_int(t2)       
    print_char(' ')   
    addi s1, s1, 4    
    addi t1, t1, -1 
    j print_loop
print_done:
    newline            
    j exit

exit:
    li a7, 10         
    ecall

bubble_sort:
    addi sp, sp, -16  
    sw ra, 0(sp)
    sw s0, 4(sp)
    sw s1, 8(sp)
    sw s2, 12(sp)

    mv s0, a0         
    mv s1, a1  
outer_loop:
    mv s2, s0    
inner_loop:
    addi t0, s2, 4 
    bge t0, s1, end_inner_loop 

    lw t1, 0(s2)      
    lw t2, 0(t0)       
    ble t1, t2, no_swap

    sw t2, 0(s2)
    sw t1, 0(t0)
no_swap:
    addi s2, s2, 4
    j inner_loop
end_inner_loop:
    addi s1, s1, -4
    bne s0, s1, outer_loop

    lw ra, 0(sp) 
    lw s0, 4(sp)
    lw s1, 8(sp)
    lw s2, 12(sp)
    addi sp, sp, 16
    ret





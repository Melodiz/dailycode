.data
array: .word
.text

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

.macro cmp1 
  	ble a0, a1, leq
    	li a0, 0
    	j done_cmp1
leq:
    	li a0, 1
done_cmp1:
.end_macro

.macro cmp2
  	li s9, 10
  	rem a0, a0, s9
  	rem a1, a1, s9
  	bge a0, a1, greater
less_or_equal1:
    	li a0, 0
    	j done_cmp2
greater:
    	li a0, 1
done_cmp2:
.end_macro


.macro swap_two(%x, %y)
  	lw s0, (%x)
  	lw s1, 0(%y)
  	mv s2, s0
  	sw s1, 0(%x)
  	sw s2, 0(%y)
.end_macro

main:
	read_int(t0)
	read_int(s11)
	mv t1, t0
	la t6, array
	j read_loop

read_loop:
	beqz t1, middle
	read_int(t2)
	sw t2, 0(t6)
	addi t6, t6, 4
	addi t1, t1, -1
	j read_loop
  
middle:
	la t5, array 
	addi t6, t6, -4
	mv s6, t6
	mv t1, t0

bubble_sort:
	mv t6, s6
	li s3, 0
	mv t1, t0
	la t5, array
inner_loop:
	beq t5, t6, pre_sort
	lw s4, 0(t5)
	mv s8, t5 
	lw s5, 4(t5)
	addi t5, t5, 4
	mv s10, t5
	mv a0, s4
	mv a1, s5
	jal cmp
	beqz a0, swap
	j inner_loop

cmp:
  	beqz s11, case1
case2:
    	cmp2
    	jr ra
case1:
    	cmp1
    	jr ra


pre_sort:
	beqz s3, pre_output
	j bubble_sort

swap:
  	swap_two(s8, s10)
  	addi s3, s3, 1
  	j inner_loop

pre_output:
	la t5, array
	addi t6, t6, 4

output_loop:
	beq t5, t6, done
	lw t2, 0(t5)
	addi t5, t5, 4
	addi t1, t1, -1
	print_int(t2)
	newline
	j output_loop

done:
	li a7, 10
	ecall
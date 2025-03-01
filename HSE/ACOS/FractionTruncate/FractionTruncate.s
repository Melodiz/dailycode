# Fraction Truncate
# Input: A, B, n
# Output: A/B truncated to n decimal places

.text
.globl main

main:
    # Allocate stack space
    addi sp, sp, -16
    sw ra, 0(sp)
    
    # Get input A (no prompt)
    li a7, 5       # Read integer
    ecall
    mv s0, a0      # s0 = A
    
    # Get input B (no prompt)
    li a7, 5       # Read integer
    ecall
    mv s1, a0      # s1 = B
    
    # Get input n (no prompt)
    li a7, 5       # Read integer
    ecall
    mv s2, a0      # s2 = n
    
    # Convert A and B to doubles
    fcvt.d.w fa0, s0
    fcvt.d.w fa1, s1
    
    # Calculate A/B
    fdiv.d fa0, fa0, fa1
    
    # Call truncate_fraction with fa0=A/B and a0=n
    mv a0, s2
    jal ra, truncate_fraction
    
    # Print result (no prompt)
    fmv.d fa0, fa0
    li a7, 3       # Print double
    ecall
    
    # Clean up and exit
    lw ra, 0(sp)
    addi sp, sp, 16
    li a7, 10
    ecall

# truncate_fraction function
# Parameters:
#   fa0 - double precision value to truncate (A/B)
#   a0  - number of decimal places to keep (n)
# Returns:
#   fa0 - truncated value with exactly n decimal places
truncate_fraction:
    # Save registers
    addi sp, sp, -16
    sw ra, 0(sp)
    fsw fa0, 4(sp)
    sw a0, 12(sp)
    
    # Calculate 10^n
    li t0, 1       # t0 will hold 10^n
    li t1, 10      # Base 10
    li t2, 0       # Counter
    
loop_power:
    beq t2, a0, done_power
    mul t0, t0, t1
    addi t2, t2, 1
    j loop_power
    
done_power:
    # Convert 10^n to double
    fcvt.d.w ft0, t0
    
    # Multiply original value by 10^n
    fmul.d ft1, fa0, ft0
    
    # Truncate to integer using fcvt.w.d (convert to word)
    # Set rounding mode to round toward zero (rtz)
    frrm t3           # Read current rounding mode
    li t4, 1          # rtz mode is 1
    fsrm t4           # Set rounding mode to rtz
    
    # Convert to integer (will truncate)
    fcvt.w.d t5, ft1
    
    # Restore original rounding mode
    fsrm t3
    
    # Convert back to double
    fcvt.d.w ft2, t5
    
    # Divide by 10^n to get final result
    fdiv.d fa0, ft2, ft0
    
    # Restore registers and return
    lw ra, 0(sp)
    addi sp, sp, 16
    ret
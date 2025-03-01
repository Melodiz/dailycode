.data
    # Constants
    four: .double 4.0
    one: .double 1.0
    two: .double 2.0
    ten: .double 10.0
    neg_one: .double -1.0
    
    # Output format
    newline: .asciz "\n"

.text
.globl main
main:
    # Read input N (number of decimal places)
    li a7, 5              # System call for reading integer
    ecall
    mv s0, a0             # Store N in s0
    
    # Initialize variables for Leibniz formula
    la t1, four
    fld ft0, 0(t1)        # ft0 = 4.0 (final multiplier)
    la t1, one
    fld ft1, 0(t1)        # ft1 = 1.0 (numerator)
    
    # Initialize sum to 0.0
    li t0, 0
    fcvt.d.w ft6, t0      # Convert integer 0 to double
    
    la t1, one
    fld ft2, 0(t1)        # ft2 = 1.0 (first denominator)
    la t1, two
    fld ft3, 0(t1)        # ft3 = 2.0 (to increment denominator)
    la t1, one
    fld ft5, 0(t1)        # ft5 = 1.0 (sign)
    
    # Calculate required iterations based on N
    # We'll use a fixed number of iterations based on N
    li t2, 1000           # Base number of iterations
    mul t2, t2, s0        # Scale by N
    addi t2, t2, 1000     # Add minimum iterations
    
    # Calculate π using Leibniz formula
    li t1, 0              # Iteration counter
    
leibniz_loop:
    # Check if we've reached max iterations
    bge t1, t2, leibniz_done
    addi t1, t1, 1        # Increment counter
    
    # Calculate next term: sign * (1/denominator)
    fdiv.d ft7, ft1, ft2  # 1/denominator
    fmul.d ft7, ft7, ft5  # sign * (1/denominator)
    
    # Add term to sum
    fadd.d ft6, ft6, ft7  # sum += term
    
    # Update for next iteration
    fadd.d ft2, ft2, ft3  # Increment denominator by 2
    la t5, neg_one
    fld ft4, 0(t5)        # ft4 = -1.0
    fmul.d ft5, ft5, ft4  # Flip sign
    
    j leibniz_loop
    
leibniz_done:
    # Multiply sum by 4 to get π
    fmul.d ft6, ft6, ft0  # π = 4 * sum
    
    # Calculate 10^N for truncation
    la t1, ten
    fld ft7, 0(t1)        # ft7 = 10.0
    la t1, one
    fld ft8, 0(t1)        # ft8 = 1.0 (will be 10^N)
    li t1, 0              # Counter
trunc_power_loop:
    beq t1, s0, trunc_power_done
    fmul.d ft8, ft8, ft7  # Multiply by 10
    addi t1, t1, 1        # Increment counter
    j trunc_power_loop
trunc_power_done:
    # ft8 now contains 10^N
    
    # Truncate to N decimal places
    fmul.d ft9, ft6, ft8  # π * 10^N
    fcvt.w.d t3, ft9      # Convert to integer (truncating)
    fcvt.d.w ft9, t3      # Convert back to double
    fdiv.d ft6, ft9, ft8  # Truncated π = int(π * 10^N) / 10^N
    
    # Print result with N decimal places
    fmv.d fa0, ft6        # Move result to fa0 for printing
    li a7, 3              # System call for printing double
    ecall
    
    # Exit program
    li a7, 10             # System call for exit
    ecall
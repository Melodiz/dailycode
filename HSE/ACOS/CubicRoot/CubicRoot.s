.data
    # Constants
    one: .double 1.0
    three: .double 3.0
    
    # Output format
    newline: .asciz "\n"

.text
.globl main
main:
    # Read input A
    li a7, 7              # System call for reading double
    ecall
    fmv.d fs0, fa0        # Store A in fs0
    
    # Read input e
    li a7, 7
    ecall
    fmv.d fs1, fa0        # Store e in fs1
    
    # Initialize constants
    la t0, one
    fld fs2, 0(t0)        # Load 1.0 to fs2
    la t0, three
    fld fs3, 0(t0)        # Load 3.0 to fs3
    
    # Initial guess for cubic root
    # For |A| > 1, use |A|/3 as initial guess
    # For |A| < 1, use |A| as initial guess
    fabs.d ft0, fs0       # |A|
    flt.d t0, ft0, fs2    # Check if |A| < 1
    beqz t0, large_a      # If |A| >= 1, use |A|/3
    
    # For small A
    fmv.d ft4, ft0        # x = |A| (initial guess)
    j check_sign
    
large_a:
    fdiv.d ft4, ft0, fs3  # x = |A|/3 (better initial guess for large A)
    
check_sign:
    # If A < 0, we need to negate our guess for cubic root
    flt.d t0, fs0, fs2    # Check if A < 0
    beqz t0, newton_start # If A >= 0, proceed
    fneg.d ft4, ft4       # Negate initial guess if A < 0
    
newton_start:
    # Set iteration counter
    li t1, 0              # Iteration counter
    li t2, 10000            # Maximum iterations
    
newton_loop:
    # Check if we've reached max iterations
    bge t1, t2, newton_done
    addi t1, t1, 1        # Increment counter
    
    # Calculate x³
    fmv.d ft5, ft4        # ft5 = x
    fmul.d ft5, ft5, ft4  # ft5 = x²
    fmul.d ft5, ft5, ft4  # ft5 = x³
    
    # Calculate x³ - A
    fsub.d ft6, ft5, fs0  # ft6 = x³ - A
    
    # Check if |x³ - A| < e
    fabs.d ft7, ft6       # ft7 = |x³ - A|
    flt.d t0, ft7, fs1    # Check if |x³ - A| < e
    bnez t0, newton_done  # If precision reached, we're done
    
    # Calculate 3 * x²
    fmul.d ft7, ft4, ft4  # ft7 = x²
    fmul.d ft7, ft7, fs3  # ft7 = 3 * x²
    
    # Calculate (x³ - A)/(3 * x²)
    fdiv.d ft6, ft6, ft7  # ft6 = (x³ - A)/(3 * x²)
    
    # Calculate x_{n+1} = x_n - (x_n³ - A)/(3 * x²)
    fsub.d ft4, ft4, ft6  # x = x - (x³ - A)/(3 * x²)
    
    j newton_loop         # Continue iteration
    
newton_done:
    # Print result
    fmv.d fa0, ft4        # Move result to fa0 for printing
    li a7, 3              # System call for printing double
    ecall
    
    # Exit program
    li a7, 10             # System call for exit
    ecall
# binary_search function
# Parameters:
# a0 - pointer to sorted array
# a1 - value to find
# a2 - start index
# a3 - end index
# Return:
# a0 - index of found element or -1 if not found

.globl binary_search
binary_search:
    # Save return address to stack
    addi sp, sp, -4
    sw ra, 0(sp)
    
    # Check if start > end
    bgt a2, a3, not_found
    
    # Calculate mid = start + (end - start) / 2
    sub t0, a3, a2      # t0 = end - start
    srai t0, t0, 1      # t0 = (end - start) / 2
    add t0, a2, t0      # t0 = start + (end - start) / 2
    
    # Calculate address of data[mid]
    slli t1, t0, 2      # t1 = mid * 4 (assuming 4-byte integers)
    add t1, a0, t1      # t1 = &data[mid]
    lw t2, 0(t1)        # t2 = data[mid]
    
    # Check if data[mid] == value
    beq t2, a1, found
    
    # Check if data[mid] > value
    bgt t2, a1, search_left
    
    # Otherwise, search right half
    addi a2, t0, 1      # start = mid + 1
    jal ra, binary_search
    j done
    
search_left:
    addi a3, t0, -1     # end = mid - 1
    jal ra, binary_search
    j done
    
found:
    mv a0, t0           # return mid
    j done
    
not_found:
    li a0, -1           # return -1
    
done:
    # Restore return address and return
    lw ra, 0(sp)
    addi sp, sp, 4
    ret
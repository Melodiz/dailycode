#
   .macro output_integer (%reg)
   li a7, 1
   mv a0, %reg
   ecall
   .end_macro

   .macro output_constant_integer (%val)
   li a7, 1
   li a0, %val
   ecall
   .end_macro

   .macro input_integer(%dest)
   li a7, 5
   ecall
   mv %dest, a0
   .end_macro

   .macro output_text (%message)
   .data
text_buffer:
   .asciz %message
   .text
   li a7, 4
   la a0, text_buffer
   ecall
   .end_macro

   .macro output_symbol(%ascii_val)
   li a7, 11
   li a0, %ascii_val
   ecall
   .end_macro

   .macro line_break
   output_symbol('\n')
   .end_macro
   
.macro draw_horizontal_border(%width, %corner, %segment)
   # Save width to temporary register
   mv t0, %width              
   # Print left corner
   output_symbol(%corner)          
horizontal_loop: 
   # Check if we've reached the end
   beqz t0, horizontal_done 
   # Print horizontal segment
   output_symbol(%segment)          
   # Print corner/junction
   output_symbol(%corner)         
   # Decrement counter
   addi t0, t0, -1        
   # Continue loop
   j horizontal_loop        
horizontal_done:      
.end_macro

.macro draw_vertical_edges(%width, %edge)
   # Save width to temporary
   mv t0, %width
   # Print left edge
   output_symbol(%edge)
vertical_loop:
   # Check if we've reached the end
   beqz t0, vertical_done
   # Print space between edges
   output_symbol(' ')
   # Print right edge
   output_symbol(%edge)
   # Decrement counter
   addi t0, t0, -1
   # Continue loop
   j vertical_loop
vertical_done:
.end_macro
  
.text
program_start:
 # Read grid dimensions
 input_integer(s0)  # Width
 input_integer(s1)  # Height
grid_generation_loop:
 # Check if all rows are processed
 beqz s1, grid_complete
 # Draw top border of current row
 draw_horizontal_border(s0, '+', '-')
 # Move to next line
 line_break
 # Draw vertical edges of current row
 draw_vertical_edges(s0, '|')
 # Move to next line
 line_break
 # Decrement row counter
 addi s1, s1, -1
 # Continue with next row
 j grid_generation_loop
grid_complete: 
 # Draw bottom border to complete the grid
 draw_horizontal_border(s0, '+', '-')
1. Which of the following is not a key characteristic of RISC-V instruction set design?

   a) Simple and regular instruction formats  
   b) Optimized for frequent operations  
   c) Large and complex instruction set for flexibility  
   d) Trade-offs are necessary for good design  

   Answer: c) Large and complex instruction set for flexibility  

2. What is the primary purpose of PC-relative addressing in SB-format instructions in RISC-V?

   a) Supporting subroutine calls  
   b) Enabling program transitions in memory  
   c) Implementing efficient branching within a small address range  
   d) Optimizing cache memory usage  

   Answer: c) Implementing efficient branching within a small address range

3. Which of the following instruction formats does not use three registers as operands?

   a) R-format  
   b) I-format  
   c) S-format  
   d) SB-format  

   Answer: b) I-format

4. Which instructions in RISC-V use the U-format?

   a) addi, lw, jalr, slli  
   b) sw, sb  
   c) lui, auipc  
   d) beq, bge  

   Answer: c) lui, auipc

5. Which of the following is true about the Program Counter (PC) in RISC-V assembly?

   a) It always increments by 8 bytes after each instruction.  
   b) It is a special register that holds the address of the next instruction.  
   c) It cannot be modified manually.  
   d) It stores the opcode of the currently executed instruction.  

   Answer: b) It is a special register that holds the address of the next instruction.

6. Which instruction is used for an unconditional branch in RISC-V assembly?

   a) beqz  
   b) bnez  
   c) j  
   d) bge  

   Answer: c) j

7. Which of the following instructions correctly loads a value from memory into register t1 in RISC-V assembly?

   a) sw t1, 0(t2)  
   b) lb t1, 0(t2)  
   c) li t1, 0(t2)  
   d) mv t1, 0(t2)  

   Answer: b) lb t1, 0(t2)

8. Which segment of memory in RISC-V stores static data such as global variables and constants?

   a) .text  
   b) .stack  
   c) .heap  
   d) .data  

   Answer: c) data

9. Which register in RISC-V stores the return address when a function is called using jal?

   a) x0 (zero)  
   b) x1 (ra)  
   c) x2 (sp)  
   d) x8 (s0/fp)  

   Answer: b) x1 (ra)

10. What is the primary purpose of the stack in RISC-V assembly programming?

    a) To store the program counter (PC) of the running process  
    b) To provide a dynamic storage for variables that persist between function calls  
    c) To temporarily store registers and local variables during function calls  
    d) To execute instructions in sequence  

    Answer: c) To temporarily store registers and local variables during function calls

11. What does the instruction addi sp, sp, -16 achieve in a function call?

    a) Allocates 16 bytes on the stack  
    b) Frees 16 bytes from the stack  
    c) Jumps 16 bytes ahead in memory  
    d) Resets the stack pointer  

    Answer: a) Allocates 16 bytes on the stack

12. Which of the following statements about callee-saved registers is true?

    a) The caller must save these registers before calling a function  
    b) The callee must restore these registers before returning  
    c) These registers cannot be modified inside a function  
    d) They are used exclusively for function arguments  

    Answer: b) The callee must restore these registers before returning

.text
lui s0, 0x10010          # 0x10010437
addi s1, s0, 12          # 0x00c04493
sw s1, 0(s0)             # 0x00942023
lui t0, 0x30000          # 0x300002b7
addi t1, zero, 3         # 0x00300313
slti t2, t0, 16          # 0x0102d293
lw s1, 0(s0)             # 0x00042483
add t1, t1, t1           # 0x00931333
beq t0, t1, jump1        # 0x00628463
j jump2                   # 0x0100006f
auipc t2, 0              # 0x00000397
addi t2, t2, -4          # 0xffc38393
jalr t1                  # 0x00038067
addi t3, zero, 10        # 0x00a06893
ecall                    # 0x00000073
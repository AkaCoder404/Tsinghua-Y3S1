# 第4周

## 第8课

<center><h3> 10.9 PPT: RISV 指令系统 </h3></center>

### RISC-V 指令系统概述

- history.... 
- fastest 指令集 is arm
- features: simple, documentation is less than 150 pages (while intel's processor manual has more than 5000 pages), small number of instructions (40), plus other modular extension instructions, just a dozen of instructions.
- ARM: Application(OS), Real-Time, and Embedded. not compatible with each other
- modular instruction set design: can choose instruction set of RV32IC combination, and only use Machine Mode, while in high performance os scenarios, they can choose instruction set of RV32IMFDC, are combatable with each other.
  - each module is represented by an english letter
  - the most basic and only mandatory instruction set part of RISC-V is the basic integer instruction subset represented by the letter I. Using this integer instruction subset, a complete software compiler can be implemented
  - Other instruction subsets are optional modules, and representative modules include M/A/F/D/C6

### 课配置的通用寄存器组

- general purpose, control and status

### 规整的指令编码

- R,I,S,SB/B,UJ, J, U

privileged mode: MSU, machine mode, supervisor mode, user mode.  (M mode is required, the other two are optional)

look at 手册

![](C:\Users\ligeo\Pictures\risv-registers.png)

没有溢出，so you have to write code accurately yourself, because it won't tell you any errors



### RISC-V 指令与汇编语言概述

算术指令，逻辑指令，以为指令

乘法，除法， 

位操作指令 (bit operations)

### 数据传输指令

### 分支与跳转指令

pc, pointing to the current 指令

some other books, for huibian for example, say pc points to the next command 

### 伪指 pseudo instructions

give programmers more intuitive instructions, but they are not directly implemented through hardware

translated into actual hardware instructions through assembler

for example, move dst, src has no actual data movement, instead translated to 

addi dst, src, 0 or add dst, src, x049

riscv-v does not have move, instead load immediate and load address

### 函数调用

。。。 










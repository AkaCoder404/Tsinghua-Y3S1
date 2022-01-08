# 第5课

<center> <h3>DATE: 9-27 PPT: </h3></center>

# 实验预备课

## 可编程逻辑器介绍
## 硬件编程方法与原则
## 硬件编程流程
- FPGA

## 查找表 lookup table 
## 4 输入与门


## XilinxFPGA 主要部件
## Xilinix公司产品概述
## 典型的应用领域
## 发展趋势

# FPGA的片内资源



# 硬件设计的方法与原则

# 第6课

<center> 2.29 上课: 15 Verliog HD PPT </center>

## Verliog HD

### Verliog 要素

1. comments, ... 

### 整数的例子 

1. 8‘b11000101, 8'hd5 ...

### 位选择和域选择

1. mybyte[6], mybyte[5:2]

### 向量



### 运算符 

1. Arithmitic, Logic, Bitwise, Relational Operators (bne, beq, 等等), Equality Operators, Reduction Operators, Shift Operators, Conditional Operators (三目运算符), Concatenation Operators ({})*

不可综合 are used in 仿真器

可综合 can be applied to FPGA

### always 过程

### 赋值与 vs 非赋值

1. <= vs =

## Verliog 设计的描述风格

1. Structural (more code, but can see hiearchy), Behavior (easier, but can't visualize structure), DataFlow (mostly use this)
2. assign (faster + cleaner) > always (more complicated + more functionality)

given powerpoint, only read up to page 32


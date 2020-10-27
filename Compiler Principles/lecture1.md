# 第一课

<center> <h3>DATE: 9-15 PPT: </h3></center>

## Principles and Practice of Compiler Construction
- 有关信息
- 编译程序概述
- 教学内容预览

## 参考阅读
1. Modern Compiler Implementation in Java, C
2. Advanced Compiler Implementation in C
3. The Theory of Parsing, Translation and Compiling
4. Engineering a Compiler

## 实验计划：实现一个小型语言minidecaf (C的小子集)
master/complete a complete 翻译器, 6 steps, use Python + ANTLR4
1. PA1 完整编译器
2. PA2 常量表达式
3. PA3 变量语句
4. PA4 作用域与控制语句
5. PA5 函数和全局变量
6. PA6 指针和数组

## 考核计划, Grades
1. 出勤+ 书面作业 10%
2. 原本实验成绩 20%
3. 扩展实验 + 期末考试 = 50% + 20%


## 什么时编译程序？
It is a 翻译程序 (translator) from A 原语言 source language to B 目标语言 target language
- 需要分析原程序 analysis
- 根据分析结构进行综合 synthesis
simple languages such as 预处理程序 preprocessor and 汇编程序 assembler 
- high level language to lower level language (machine languages such as 汇编语言，及其语言，Bytecode)
C代码 -> C compiler -> 汇编代码

## 主要范型 paradigms
- 命令式语言 imperative languages (how it is realized) fortran, algol, C, ...
- 陈述语言 declarative languages (what does it do) 
	- functional : lisp, scheme ...
	- logic: prolog
- 面向对象语言 object oriented
- 并发/并行/分布式语言 concurrent/parallel/distributed 
- 其他： synchronous, database, scripting languages


## 编译程序的逻辑结构?
Compiler infrastructure 
- includes at least two parts, 分析 and 综合
- 前端 front end, analysis portion
- 后端 back end, sythesis
- 中端 middle end, operations on the code, creation and optimization

词法分析
- scan the character stream of the source program to identify words with lexical meaning, return the word category and word value, or lexical error information

语法分析 
- 树

语义分析 
- Perform semantic analysis on the program after grammatical analysis, and give a semantic error message when it does not meet the semantic rules
符号表
- collect various attributes for each 语义 for semantic analysis and its subsequent stages
- 出错处理 error reporting and error recovery
- 中间代码生成 > 语法树AST -> 三地址码TAC

## 编译程序的组织？

## 编译程序的伙伴程序？compiler program
- 解释程序 interpreter
- no object program file
- no distinction between translation stage and execution stage
- execute directly after translating each sentence of the source
- often used in implementation of virtual machines


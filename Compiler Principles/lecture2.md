# 第二课

<center> <h3>DATE: 9-22 PPT: </h3></center>

## 编译程序的组织
编译程序的遍 Passses/Phases
1. read a code from head to end
2. change one code space to another code space
3. 代码空间 = code + 符号表 + 其他有用信息

- 预处理程序 Preprocessor
    - Macro Def
    - File Inclusion
- 汇编程序 Assembler
- 装入和连接程序 Load and Link-editor
- 调试程序 Debugger

## 编译程序与T星图
- T-型图
    - S：source language implemented by compiler
    - T：implementation language of compiler
    - I：Target Language
- T-型图的叠加

## 教学内容预览

## 课后作业
- review 形式语言与自动机
- prepare materials/environment for 实验
- read 实验指导书 for 工具 such as ANTLR4


# Chapter 2 第二讲
## 词法分析概述
- 词法分析程序 Lexical Analyzer
- Scanner
- Lexemes
- Token

## 常用的单词描述工具
- EBNF, state transformation, regex, 有限状态自动机

## 技术个案
- 如何区分表示符与保留字？
- 字符退还？

## 词法分析程序自动构成的典型过程
1. User uses regular expressions as a form of description of lexical rules. Each type of lexical unit corresponds to a regular expression. All regular expressions are automatically constructed in text mode as an input lexical analysis program as an automatic construction tool
2. 自动构造工具 convert every finite expression to 自动机 using  Thompson and epsilon-NFA
3. （可选）
4. 
5. 
6. 

## 课后作业
非书面的


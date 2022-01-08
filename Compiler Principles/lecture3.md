# 第3课

<center> <h3> DATE 2-28 PPT: </h3> </center>

## 自顶向下 Top-Down 语法分析

### 基本思想

recognition and parsing

if follows context free grammars, then you can give 分析树 or （最左） derivation steps, otherwise error in processing

two types: 向下 vs 向上 

### 带回溯的自顶向下分析

一般方法：two types of nondeterminism, when the 推导 can go to two or more ways, but chooses the wrong 

改进的方法： always 推导 from one side, perhaps left, 

### 自顶向下预测分析 

lookahead n steps, so that we can decide which way to derive

- 得到唯一的最左推导, has to have limit
- 左递归 cannot be 推导, not 确定数目 ba^n 
- 左公因子 cannot be 推导

### LL(1) 分析

LL stands for Left Leftmost, scan from the left, derive from the leftmost, 1 represents the lookahead

two important concepts: first 集合 and follow 集合 

https://www.jambe.co.nz/UNI/FirstAndFollowSets.html 

预测集合 Predictive Set， definition

LL(1) 文法

LL(1) 分析的实现 methods: 递归下降 and 表驱动 

### 递归下降LL(1) 分析程序














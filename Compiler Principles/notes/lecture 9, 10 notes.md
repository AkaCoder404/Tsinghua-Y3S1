# 编译原理

[TOC]

# 介绍

For source programs with correct lexical and grammatical terms, the compiler can perform semantic analysis on it. In the semantic analysis stage, the first step is to collect or calculate the context-related information of the source program, and assign this information to the corresponding program unit to record. During this process, if problems with static consistency or integrity are found in the program, a static semantic error is reported.

If there are no static consistency or completeness issues, we say that the program has passed the static semantic check. The part related to static semantic checking in the semantic analysis process is called static semantic analysis. For a program that has passed the static semantic check, the compiler can translate it into a subsequent intermediate representation, that is, intermediate code generation. The process of intermediate code generation reflects how to interpret the dynamic semantics of the program at a lower level. For static semantic analysis and intermediate code generation, please refer to the next lecture of this course.

In the realization of the compiler, a classic method is to dominate the process of semantic analysis and translation by the analysis process of the grammatical analysis program. This course is called 《语法制导的语义计算》grammatically guided semantic computing. It is also called 《语法制导的翻译》grammar-guided translation in many books on compilation. For specific translation passes, such as the static semantic analysis and intermediate code generation in the next chapter, it can be called grammatically-directed static semantic analysis and syntax-directed intermediate code generation accordingly. In order to describe what kind of semantic calculation is done, we need to establish an appropriate semantic calculation model based on the grammar definition. If the grammar definition adopts a context-free grammar, the basic way to establish this semantic calculation model is to extend the context-free grammar, attach semantic information to the grammar symbols, and design appropriate semantic actions for the production, so as to tell the analysis engine to analyze the syntax Semantic actions that can be performed during the process.

In this lecture, we will introduce two important semantic computing models: attribute grammar and translation mode. Attribute grammar is a basic semantic computing model, which is suitable for understanding general principles; while the translation mode is an implementation-oriented semantic computing model, which helps to understand the automatic construction method of grammar-guided semantic computing programs (such as the work of Yacc tools). principle).

#  第5讲

## 符号表 Symbol Table

> a symbol table is a data structure used by a language translator such as a compiler or interpreter, where each identifier (or symbol) in a program's source code is associated with information relating to its declaration or appearance in the source. In other words, the entries of the symbol table store the information related to the entry's corresponding symbol. 

- 作用，常见属性，实现，作用域可见性

## 符号表的作用

- set the attribute information about the identifier (有关标识符) symbol
- the information will be used in different stages of compilation
- the content of the symbol table will be used for static semantic checking (静态语义检查) and intermediate code generation (产生中间代码), aka IR

> why do we need an intermediate code? https://www.tutorialspoint.com/compiler_design/compiler_design_intermediate_code_generations.htm

- During the generation of target  code, the symbol table is the basis for address allocation to symbol
- for a 多变扫描 compiler, the symbol table used in different passes will also be different, because the information concerned or the information that can be obtained in each pass will be different.
- establish information that reflects scope and visibility

## 符号表常见属性

- 符号名 symbol name
- 符号的类别 symbol category
- 符号的类型 symbol type
- 符号的存储类别和存储分配信息 symbol storage category and storage allocation information
- 符号的作用域信息 symbol scope information
- 其他属性，内情向量 inner vector, 记录结构成员信息 member information of record structure, 函数及过程的形参 function and procedure parameters

## 符号表的实现

common operations for symbol table 

- 创建符号表 create symbol table at the beginning of compilation, or into a scope
- 抽入表项 insert entry is preformed when a new identifier declaration is encountered
- 查询表项 query table entries are preformed when quoting identifiers
- 修改表项 modify table entries when new semantic value information is obtained
- 删除表项 delete an entry when the the identifier becomes invisible or any information about is no longer needed
- 解放符号表空间 release the symbol table space before the end of compilation or exit of scope

## 符号表的实现

实现符号表的常用的数据结构

general linear table: array, linked list, etc

ordered list: faster than unordered table, half search

binary search tree

hash table

## 符号表体现作用域信息

作用(scope) 和可见性(visibility)

all scopes share a global symbol table

each scope has its own symbol table

## 作用域及可见性

### 作用域 scopes

嵌套的作用域 nested scopes

open and closed scopes (corresponding to special points in the program)

the scope of the point is the current scope

the scope formed by the current scope and the program unit that contains it is called open scopes

the scope that does not belong to the open scope is called the closed scope

 ### 可见性 visibility

- at any point in the program, only the name declared in the open scope at that point is accessible
- if a name is declared in multiple open scopes, the declaration closest to a reference of the name is taken as the interpretation of the reference.
- new declarations can only appear in the current scope 

### 作用域与 符号表组织  single symbol table organization

all nested scopes share a global symbol table

each scope has a scope number 

only record symbols in open scope

when a scope becomes a closed scope, delete the name declared in the scope form the symbol table

## 例子

Dx: 基地址

Cx: 栈帧中控制单元数目

LEV： 层号

Each scope has its own symbol table

maintain a scope stack of symbol table, each open scope correspeonds to an entry in the stack, and the current open scope appears at the top of the stack

when a new scope is opened, a new symbol table will be created and pushed onto the stack

when the current scope becomes a closed scope, pop the corresponding symbol table from the top

![image-20201121133920020](C:\Users\ligeo\AppData\Roaming\Typora\typora-user-images\image-20201121133920020.png)



# 第6讲

## 语法制导的语义计算基础

The basis of semantic computing for grammatical guidance

基于属性文法的语义计算 Syntax Direct Definition (SDD)

属于翻译模式的语义计算 Syntax Direct Translation (SDT)

## 语法制导的（Syntax Directed) 语义计算

> syntax directed definition specifies the values attributes by associating semantic rules with the grammar productions

*Based on grammatical definitions, context free grammar*

Used in various semantic analysis and translation process: static semantic checking, IR code( even target code)

Design with 自动构造工具 (i.e. YACC)

- principles and methods: attribute grammar and translation mode

examples

## 属性文法 attribute grammar

expanded on the basis of context-free grammar as follows

- associate multiple attributes for each grammar symbol 
- associate a set of semnatic rules or semantic actions for each production of the grammar

**this course does not discuss attribute grammars with qualifications (有限条件)**

## 属性 attribute

can be used to describe any characteristic of a grammar sybol that we care about

- such as the: value, name, symbol, type of symbol, offset address, the gister to which the symbol is assigned, code fragments, etc... 

记号, attribute value of the  the associated attribute ```a``` of the grammar symbol ```X``` can be accessed through ```X.a```

## 概念

语义规则 (Semantic Rule): in attribute grammar, each production A -> α is associated with a set of semantic rules, used to describe how to calculate the attribute value of the current production grammar symbol or additional semantic action

### following semantic rules of attribute grammar 

- 复写 copy
- 基于语义函数 semantic function

## 两中属性

### 综合属性 synthesized attributes

“自下而上“  bottom up information transition

> Synthesized attribute is an attribute whose parse tree node value is determined by the attribute value at child nodes. To illustrate, assume the following production S → ABC if S is taking values from its child nodes (A, B, C), then it is said to be a synthesized attribute, as the values of ABC are synthesized to S.

### 继承属性 inherited attributes

“自上而下” top down information transition

> On other hand an attribute is said to be Inherited attribute if its parse tree node value is determined by the attribute value at parent and/or siblings node. In case of S → ABC if A can get values from S, B and C. B can take values from S, A, and C. Likewise, C can take values from S, A, and B then S is said to be Inherited Attribute.

## 综合属性代表自下而上传递的信息

Comprehensive attributes represent bottom-up information

This attribute grammar can be used to convert binary unsigned decimals to decimal decimals
Please think: How should the attributes involved in semantic actions be calculated?

## 基于属性文法的语义计算

1. 树遍历方法 tree traversal method: attribute calculation by traversing the analysis tree
2. 单边的方法 single pass method: attribute calculations while parsing

###  基于树遍历方法的语义计算

semantic calculation based on tree traversal method

Steps 

1. construct a parse tree of the input string

2. construct a 依赖图 dependency graph (dependency graph for each attributes of all nodes in the parse tree, and give a label number)

   if the dependency graph is acyclic (a graph with no circles), then the analysis tree is traversed according to a topological sort of the acyclic graph, and all attributes can be calculated.

   (if the dependency graph contains circles, the corresponding attribute grammar cannot use this method for semantic calculation. such attribute grammar is not well-defined. The so-called well-defined attribute grammar, if and only if its rule set can determine a unique value tree for all attribute sets in the analysis tree)

   is a directed tree, used to describe the interdependence between attributes in the analysis tree

3. according to semantic actions, establish directed edges in the dependency graph

4. if the dependency graph is acyclic, there is a topological sort. According to any topological sort, the calculation of the attribute value can be successfully completed. 

5. According to the calculation order, the attribute value corresponding to each node is obtained according to the semantic action

### 带标注 (annotated) 的语法分析树

The calculation process of the attribute value of each node in the syntax analysis tree is called annotating 标注 or decorating 修饰 the syntax analysis tree.
Use annotated syntax analysis tree to represent the calculation result of the attribute value

## 单遍的方法

Perform attribute calculations while parsing

bottom-up approach

top down approach

only applicable to the following two types of grammars

## S-属性文化

only includes synthesized attributes

### 计算

- usually bottom-up approach
- if LR analysis technology is used, the fields in the analysis stack can be expanded to form a semantic stack to store the value of the comprehensive attribute, and the calculation of the 综合属性的值 of the left grammatical symbol of the corresponding production occurs just before each step of reduction、

Semantic calculation of S-attribute grammar using LR analysis technology



## L-属性文化

can include synthesized attributes and inherited syntax

the calculation of the inherited attributes of a grammar symbol at the right end of the production only depends on the attributes of the grammar symbol on the left side of the symbol (for the grammar symbol on the left side of the production, it can only be inherited attributes)

### 计算

... 

## 翻译模式（Translation Scheme） 概念

Another description form suitable for grammatically guided semantic computing

Another description form suitable for grammatically guided semantic computing

It can embody a transition algorithm that calls semantic actions reasonably 

formally similar to attribute grammar, but it is allowed to be enclosed in {}. The set of semantic rules appears at any position on the right end of the production

The advantage of this is that the order of action and attribute calculation can be expressed explicitly, and this order is not reflected i the aforementioned attribute grammar.

### 受限的翻译模式

When designing the translation mode, certain restrictions must be made to ensure that each attribute value already exists when it is accessed

Two Types. S and L attribute grammar.

### 计算

only consider the 单遍方法

top down predictive analysis,(自上而下) bottom up shift-reduction techniques(自下而上)

## 基于翻译模式的自上而下语义计算

...

###  消除翻译模式中左递归的一种变换方法



## 基于翻译模式的自下而上语义计算



# 第七讲

## 静态语义分析与中间代码生成

Static semantic analysis and intermediate code generation

the logical position of static semantic analysis and intermediate code generation in the compiler

![image-20201121165957159](C:\Users\ligeo\Desktop\Y3S1\Tsinghua-Y3S1\Compiler Principles\lecture 9, 10, 11 notes.assets\image-20201121165957159.png)

Symbol tables

- add/change symbol table after name information is created, add/change the symbol table name information such as: type, type, offset,address, occupied space, etc.
- when you need to get name information, look up the symbol table
- the organization of the symbol table and reflect the name scope rules

## 与语义分析相关的工作

static semantic checking

- 静态语义检查 Semantic checks performed during compilation
- 动态语义检查 Semantic checking of the generated code during runtime
- 收集语义信息 
  - Collect the semantic information of the program for semantic checking
  - Collect the semantic information of the program for subsequent stages such as code generation. Some of the content is merged into the "Intermediate Code Generation" section for discussion

## 静态语义检查

final stage of program legality check before code generation

- 静态类型检查 static type checks : Check whether each operation complies with the definition of the language type system

- 名字的作用域 scope analysis of names: Establish a connection between name definition and use

- 控制流检查 control flow checks: The control flow statement must transfer control to a legal place (for example, a break statement must be surrounded by a legal statement)

- 唯一性检查 uniqueness checks: In many cases, the object can only be defined once (for example, the elements of the enumeration type cannot be repeated)

- 名字的上下文相关性检查 name related checks : The multiple occurrences of certain names should satisfy certain contextual relevance

## 类型检查

类型检查程序 type checker: responsible for type checking

- verify that the language structure matches the type expected by the context
- collect and establish necessary type information for relevant stages 
- implement a certain type system 类型检查

静态类型检查

- Type checking during compilation

动态类型检查

- Type checking during the operation of the target program

## 类型系统 （简介）

### 作用

maintain the type information of variables, expression and other units in the program

describe whether the behavior of the program is good/safe and reliable 

implementation of the canonical type checking process

### 类型系统的定义

语法范畴 Define legal program units

语义范畴 Define type expression

类型环境 Define the scope of identifiers and maintain the types of variables in the program

类型规则 Define type expressions for program units

 ### 类型系统相关话题

- 类型等价 equivalence: structure equivalence, name equivalence, unified algorithm
- 类型推导 inference: static/dynamic type inference
- 子类型 subtyping: type conversion, type compatibility, polymorphism, overloading
-  类型合理性/可靠性 soundness: well-typed programs are behaviorally safe

## 类型检查程序的设计

- grammar-directed method
- assign type expressions to various parts of the program as attribute value values
- design an appropriate translation model
- a type system that can implement the corresponding language

## 作用域分析

静态作用域 （5th lecture)

动态作用域 （8th lecture)

## 中间代码

different representations of the source program

- A bridge between the source language and the target language, avoiding the larger semantic span between the two, making the logical structure of the compiler simpler and clearer
- Facilitate the redirection of the compiler
- Facilitate optimization that has nothing to do with the target machine

## 中间代码的形式

different levels and different purposes

AST, TAC, P-code, Bytecode, SSA







# Problems

3. 以下属性文法可用于将二进制无符号小数转化为十进制小数（开始符号为 N）：

   ![image-20201122142010867](C:\Users\ligeo\Desktop\Y3S1\Tsinghua-Y3S1\Compiler Principles\lecture 9, 10, 11 notes.assets\image-20201122142010867.png)

attribute definitions

- N's synthesized attribute v represents the conversion result to decimal
- S's synthesized attribute v represents decimal number or fixed point decimal
- S's synthesized attribute l represents the length of the binary number
- S's inherited attribute f represents the decimal value "when the derivation of the 0,1 string's last number is 1"
- B's synthesized attribute f represents the decimal value that should correspond when the current digit of the binary number is 1. The meaning is similar to the inherited attribute f of the symbol 1

Example 4 For the attribute grammar of Example 3, consider the semantic calculation process for the input string 10.01. First, based on the analysis tree of the input string 10.01, the dependency graph is constructed according to the method described in Figure 3. A node in the dependency graph is established for each attribute of all nodes in the analysis tree, and a label number is given. As a result, the dependency graph has a total of 21 nodes, labeled 1-21, as shown in Figure 4. The directed edges in the dependency graph are shown in Figure 5.

Then, we can determine that the dependency graph described in Figure 5 is acyclic. Then, we can calculate all the attribute values according to any topological order of the nodes of the directed acyclic graph. For example, the following node sequence is a topological sort: 3, 5, 2, 6, 10, 8, 9, 7, 11, 4, 15, 12, 13, 16, 20, 18, 21, 19, 17, 14, 1. Calculate the attribute values corresponding to each node in this order, and you can get the result shown in Figure 6, where the attribute value corresponding to each node is given in the box closest to the node name

Dependency Graph Process:

```c 
for every_node_in_the_parse_tree_n do
    for every_attribute_a_involved_in_a_semantic_
        action_of_production_used_by_node_n do
            create_a_node_in_the_dependency_graph_for_a;
    for every_semantic_action_used_by_node_n_of_the_form_f(c1,...,ck) do
        create_a_node_in_the_dependency_graph_for_this_rule;
for every_node_in_the_parse_tree_n do
    for every_corresponding_attribute_b:=f(c1,...,ck)_of_node_n do
        for i:0 to k do
            create_a_directed_Edge_from_ci_to_b;
```





给定文法 G[S]：

在文法 G[S] 基础上设计如下翻译模式：

```
S → M {A .in_num := M .num }
	A b {B .in_num := A .num}
	B { if B .num=0 then S.accepted := true else S.accepted := false }
A → { A1 .in_num := A .in_num } A1 a {A. num := A1.num - 1}
A → {A .num := A .in_num }
B → {B1.in_num := B.in_num} B1 a {B. num := B1.num - 1}
B → {B1.in_num := B.in_num} B1 b {B. num := B1.num }
B → ε {B. num := B.in_num }
M → ε { M .num :=100 } 
```




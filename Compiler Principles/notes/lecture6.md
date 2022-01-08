# 第6课

<center><h3>Date: 10.20 PPT: </h3></center>

## 自底向上 Bottom-up 语法分析
Recognition and parsing

Steps
1. Start the reduction from the terminal string to be analyzed
2. Each step of reduction is to find a substring that matches the right part of a certain production in the current string, and then replace the substring with the left nonterminal of this production; if no such substring is found String, then go back to the state before the previous step reduction, select a different substring or a different production to try again;
3. Repeat the previous step until you reduce to the beginning of the grammar symbol
4. If there is no such reduction, it indicates that the terminal string has a syntax error

非确定性 non-determinism
1. In each step of reduction, deciding between which production to choose and which substring to match may be non-deterministi
2. These uncertainties lead to high complexity in the analysis process

## Reducible String (可归约串)
1. 短语
2. 直接短语
3. 句柄

## 自底向上分析的实现技术
- 移进——归约 (shift-reduce)

## Comparison to top down
- More powerful because during the derivation and reduction processes have the following difference: only a part of the deducible input string is observed during derivation, while the entire reducible input string has all appeared during reduction.
- Conducive to error handling: moved in after entering the symbol to view
- More complicated structure, difficult to construct by hand but there is a good automatic construction technology

## 移进一归约分析
- Use a push-down stack (analysis stack) and an analysis engine based on finite state control
- Analysis engines determines one of the following states based on the current state, current state content of stack, and the remaining inputs, then it enters one of the following states: 
  - reduce: reduce the phrase at the top of the stack in a certain way
  - shift: move one word from the input sequence
  - error: syntax error is found, enter error processing/recovery
  - accept: analysis accepted
- canonical derivation : if you reverse above process, it is the rightmost derivation

## 冲突
there are two types of 冲突

| shift reduce 冲突                                            | reduce reduce 冲突                                           |
| ------------------------------------------------------------ | ------------------------------------------------------------ |
| when we have one reduction and one move shifts (edge with terminal) at an item set | when we have an item set with more than one items with a dot at their rhs (reduction) |

Example

```
shift - reduce:
S -> if:
	if E then S
	| if E then S else S
	;
Consider: if E then if E then S else S
Current Stack: if E then if E then S
at this point, we can 
shift else S
or 
reduce if E then S
reduce - reduce:
A -> aA | aaA
consider aaab
stack is aaA, we can reduce either aaA or aA
```

## LR 分析

### LR 分析基础

- 表驱动方法 table method
- tracing  https://www.youtube.com/watch?v=Qa3IbLnX0DM&ab_channel=Education4u

### LR (0) 分析

- 增广文法 augmented grammar
- 活前缀 viable prefix

> http://www.cs.ecu.edu/karl/5220/spr16/Notes/Bottom-up/lr0machine.html
>
> https://www.comrevo.com/2016/08/how-to-construct-lr-0-parsing-table.html#:~:text=LR%20%280%29%20Parsing%20Table%3A%201%20Rows%20will%20have,another%20Closure.%203%20Check%20into%20following%20parsing%20table%3A
>
> https://lambda.uta.edu/cse5317/spring01/notes/node17.html



### SLR (1) 分析

https://www.comrevo.com/2016/08/how-to-construct-slr-1-parsing-table.html

解决冲突

1. 根据下一个输入符号是否属于要归约的非终结符的Follow集来决定是否进行归约
2. 如果 LR 0 状态（项目集）中的所有归约项中要归约的非终结符的Follow 集互不相交，则可以解决 归
   约归约 冲突
3. 如果 LR 0 状态（项目集）中的所有归约项中要归约的非终结符的Follow 集与所有移进项目要移进的符号集互不相交，则可以解决 移进归约 冲突

Make the reduction table entry only apply to the input symbols in the corresponding non-terminal Follow set

### LR(1) Parsing Table

https://www.comrevo.com/2016/08/how-to-construct-clr-1-parsing-table.html

### LALR (1) 分析

similar to LR(0), just group the LR(1) item sets with the same productions together, (without lookahead)

can cause new conflicts

## 二义文法在LR分析中的应用

Certain ambiguous grammars can construct an efficient LR parser

Ambiguity grammar is not LR grammar, but for some ambiguity grammar, artificially given reasonable restriction rules, it is possible to construct an efficient LR parser

## LR 分析中的出错处理

The empty entry of the LR analysis table corresponds to an error location

The report can be set according to the corresponding stack state and input symbol
Wrong information, simple recovery work


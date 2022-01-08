# Step 7, 8

## 块语句和作用域和更多语句

block statements, scope, and others

## Step 7

In this step, we will add the ability to support more block statements, each of which has its own scope.

What makes this step harder is that we have to consider duplicate names that may occur, among global and local, and each block might have the same name. In this step, we need to be able to determine which variable each variable name corresponds to. Only variables in the same scope cannot be declared more than once. 

修改MiniDecaf.g4

```C
function
	: type Identifier '(' ')'
compound_statement

compound_statement
	: '{' block_item*'}'

statement
	: 'return' expression ';'
	| expression? ';'
	| 'if' '(' expression ')' statement ('else' statement)?
	| compound_statement
	
```

### 思考题

1. 请将下述 MiniDecaf 代码中的 `???` 替换为一个 32 位整数，使得程序运行结束后会返回 0。

   ```c++
   int main() {
    int x = ???;
    if (x) {
        return x;
    } else {
        int x = 2;
    }
    return x;
   }
   ```

   it will return 0 when x = 0. 

2. 在实验指导中，我们提到“就 MiniDecaf 而言，名称解析的代码也可以嵌入 IR 生成里”，但不是对于所有语言都可以把名称解析嵌入代码生成。试问被编译的语言有什么特征时，名称解析作为单独的一个阶段在 IR 生成之前执行会更好？

## Step 8

In this step, we will add support for loops, as well as break and continue statements. 

MiniDecaf.g4的修改

```c
statement
    : 'return' expression ';'
    | expression? ';'
    | 'if' '(' expression ')' statement ('else' statement)?
    | compound_statement
    | 'for' '(' expression? ';' expression? ';' expression? ')' statement
    | 'for' '(' declaration expression? ';' expression? ')' statement
    | 'while' '(' expression ')' statement
    | 'do' statement 'while' '(' expression ')' ';'
    | 'break' ';'
    | 'continue' ';
```

### 思考题

1. 将循环语句翻译成 IR 有许多可行的翻译方法，例如 while 循环可以有以下两种翻译方式：

第一种（即实验指导中的翻译方式）：

1. `label BEGINLOOP_LABEL`：开始下一轮迭代
2. `cond 的 IR`
3. `beqz BREAK_LABEL`：条件不满足就终止循环
4. `body 的 IR`
5. `label CONTINUE_LABEL`：continue 跳到这
6. `br BEGINLOOP_LABEL`：本轮迭代完成
7. `label BREAK_LABEL`：条件不满足，或者 break 语句都会跳到这儿

第二种：

1. `cond 的 IR`
2. `beqz BREAK_LABEL`：条件不满足就终止循环
3. `label BEGINLOOP_LABEL`：开始下一轮迭代
4. `body 的 IR`
5. `label CONTINUE_LABEL`：continue 跳到这
6. `cond 的 IR`
7. `bnez BEGINLOOP_LABEL`：本轮迭代完成，条件满足时进行下一次迭代
8. `label BREAK_LABEL`：条件不满足，或者 break 语句都会跳到这儿

从执行的指令的条数这个角度（`label` 指令不计算在内，假设循环体至少执行了一次），请评价这两种翻译方式哪一种更好？


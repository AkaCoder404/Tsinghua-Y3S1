# Step 5，6

## 变量和语句

### Step5

This step covers variable declaration, variable assignment, and variable usage.

MiniDecaf.g4 的改变

```
function
	: type Indentifier '(' ')' '{' statement* '}'
	
statement
	: 'return' expression ';'
	| expression? ';'
	| declaration
	
declaration
	: type Identifier ('=' expression)? ';'
	
expression
	: assignment
	
assignment
	: logical_or
	| Identifier '=' expression
	
primary
	: Integer
	| '(' expression ')'
	| Identifier	
```

We must also check:

1. cannot declare the same variable twice
2. cannot use an undeclared variable

#### 思考题：

1. 描述程序运行过程中函数栈帧的构成，分成哪几个部分？每个部分所用空间最少是多少？

At any moment, a stack frame can be divided among three different sections with different functionalities, they are:

1. calculation stack: located at the top of the stack, it's values are used to calculate the expression (may be empty or may be in the process of calculating the expression)
2. stack space: used to store all the local variables that are currently availible
3. return address: old stack frame base address and other information

Thus, in order to build a stack frame, we need to construct these sections. We need to establish a stack frame before beggining the assembly of a function body statement. This is known as the prologue. We have to:

1. allocate stack frame space
2. save ```fp``` and return address (in the register ```ra```)

The destruction of the stack frame is known as the epilogue, where we have to:

1. set the return value
2. reclaim the stack frame space
3. recovery of ```fp``` , jump back to the return address (```ret``` yes ```jr ra```)

Finally, for each variable declaration, we need to 

1. set variable relative to ```fp``` offset
2. reserve variable space on the stack frame

1. 有些语言允许在同一个作用域中多次定义同名的变量，例如这是一段合法的 Rust 代码（你不需要精确了解它的含义，大致理解即可）

   ```c
   fn main() {
     let a = 0;
     let a = f(a);
     let a = g(a);
   }
   ```

其中`f(a)`中的`a`是上一行的`let a = 0;`定义的，`g(a)`中的`a`是上一行的`let a = f(a);`。

如果 MiniDecaf 也允许多次定义同名变量，并规定新的定义会覆盖之前的同名定义，请问在你的实现中，需要对定义变量和查找变量的逻辑做怎样的修改？

During our ```visitDeclaration(DeclarationContenxt ctx)``` function, instead of throwing an error when we try to declare a video already declared, when we check ```symbolTable``` for a previously declared variable, we can delete that entry, and then add the new declaration.

### Step6

This step covers if statments and conditional expressions, this is also known as ternary expressions

Minidecaf 的改变

1. if 表达式

```c
statement
    : 'return' expression ';'
    | expression? ';'
    | 'if' '(' expression ')' statement ('else' statement)?
  
```

2. 条件表达式

```c
assignment
    : conditional
    | Identifier '=' expression

conditional
    : logical_or
    | logical_or '?' expression ':' conditional
```

3. block_item (prepare for next part)

```c
function
    : type Identifier '(' ')' '{' block_item* '}'

block_item
    : statement
    | declaration
```



#### 思考题

1. Rust 和 Go 语言中的 if-else 语法与 C 语言中略有不同，它们都要求两个分支必须用大括号包裹起来，而且条件表达式不需要用括号包裹起来：

```Rust
if 条件表达式 {
  // 在条件为 true 时执行
} else {
  // 在条件为 false 时执行
}
```

请问相比 C 的语法，这两种语言的语法有什么优点？

Rust and Go have mandatory curly braces that do away with parenthesis for the condition. 

Rust's design is better for prevents mistakes that occur when you forget to add the braces. For example, in the following code 

```c
if (var == true)
	function_1()
	function_2()
	function_3()
```

```function_2()``` and ```function_3()``` will always occur no matter what var equals. If brackets become mandotory, then it would look like this, 

```c
if (var == true) {
	function_1()
	function_2()
	function_3()
}
```

where all the functions would execute, which is probably what was intended.  It makes it easier to visualize nested if statements as well. 

Aside from parenthesis making the code structure look better, parsing the C language, or having a parenthesis around the the conditon makes it much more easier to parse.


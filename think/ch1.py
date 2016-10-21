# ch1(The way of the program) notes

1.1 Introduction

Python is a high level language. Programs written in HLL needs to processed before they can be executed.

HLLs are portable(can run on any type of machine if there's a compiler/interpreter for the same). 

Two kinds of programs process high-level languages into low-level languages: interpreters
and compilers.

An interpreter reads a high-level program and executes it, meaning that it
does what the program says. It processes the program a little at a time, alternately reading
lines and performing computations.

source code--> interpreter--> output.

A compiler reads the program and translates it completely before the program starts run-
ning. In this context, the high-level program is called the source code, and the translated
program is called the object code or the executable. Once a program is compiled, you
can execute it repeatedly without further translation.

source code--> compiler--> object code--> executor--> output

Python programs are executed by an interpreter.
 
There are two ways to use the interpreter: 1. interactive mode and  2. script mode.

>>> (chevron/ the prompt) in interactive mode.

Executing  a python script: python nameofscript.py

1.3 Debugging

Tracking down errors.

Three types of errors that occur:
1. Syntax
2. Symentic
3. Runtime(some form of exceptions)

1.4 Formal and Natural languages

Parsing : Figuring out the structure of the program.

Learn to parse the program in your head, identifying the tokens and interpreting the structure.

Exercise 1.4. 

Start the Python interpreter and use it as a calculator. Python’s syntax for math
operations is almost the same as standard mathematical notation. For example, the symbols + , - and
/ denote addition, subtraction and division, as you would expect. The symbol for multiplication is
* .

If you run a 10 kilometer race in 43 minutes 30 seconds, what is your average time per mile? What
is your average speed in miles per hour? (Hint: there are 1.61 kilometers in a mile).

>>> (10/1.61)/(43.5/60)

# Average time per mile

>>>43.5/(10/1.61)

print round(43.5/(10/1.61)), 'mph'

---------------------------------------------The way of program------------------------------------------------

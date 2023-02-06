---
sidebar_position: 2
---

# Basics

## Hello World

Write a program that prints out the words, "Hello, World" to the terminal.

```bash
$ python hello.py
Hello, World
```

## Variables

Variables are extensively used in programming languages. They allow you to store variable information inside a *word* and then substitute that value inside operations using the word. This works exactly how it would work in a maths formula.

To assign a value to a variable we use the `=` operator. Variables in python typically follow the convention of "[Snake case](https://en.wikipedia.org/wiki/Snake_case)" so that they are easy to read. Variables cannot have spaces in them.

```python
this_is_a_variable = 5
my_name = "Jaedan"
```

In the examples above I have assigned values to each of the variables.

```python
print(my_name)
```

The above would print *Jaedan* to the console.

Variables can be reassigned freely.

```python
my_name = "Bob"
my_name = "James"
my_name = "Tom"
print(my_name)
```

This is what would print to the console.

```bash
Tom
```

### Operators

With this knowledge it may now be useful to know various operators inside Python. These are mostly universal to every programming language. Below are the operators that you will see the most, but there are a few more if you are willing to look them up. Operators are usually split into categories. First are the arithmetic operators.

| Operator | Description    |
| -------- | -------------- |
| +        | Addition       |
| -        | Subtraction    |
| *        | Multiplication |
| /        | Division       |
| **       | Power-to       |
| %        | Modulus        |

Next are the Assignment Operators. These allow you to quickly read and edit the value of a variable in one step. These are briefly looked at later.

| Operator | Description                                             |
| -------- | ------------------------------------------------------- |
| =        | Assign a value to a variable (We looked at this above!) |
| +=       | Increment a variable by                                 |
| -=       | Decrement a variable by                                 |

Next are the Comparison Operators. These allow you to compare two values and return a boolean.

| Operator | Description                          |
| -------- | ------------------------------------ |
| ==       | Is equal to (Note the Double equals) |
| !=       | Is not equal to                      |
| <        | Is less than                         |
| <=       | Is less than or equal to             |
| >        | Is greater than                      |
| >=       | Is greater than                      |

And finally for now it would be good to become familiar with some boolean operators. These allow you to combine True or False statements in various ways. These are slightly different to the operators above as they are actually english words. This may likely be your first introduction to a *keyword* in Python. Keywords are reserved words that have special meaning.

| Operator | Description                          |
| -------- | ------------------------------------ |
| and      | Is True only if a **and** b are True |
| or       | Is True if a **or** b is True        |
| not      | Is True if a is **not** True.        |

### Using the operators

Below is an example usage of each of the operators. In the comment below the print noted what it would say.

```python
# ------------ Arithmetic operators ------------ 
print(2 + 3)
# 5

print(10 - 6)
# 4

print(5 * 4)
# 20

print(10 / 4)
# 2.5

print(10 ** 3)
# 1000

print(14 % 5) # (The remainder of 14 / 5)
# 4
```

```python
# ------------ Assignment operators ------------ 
number = 5
# Assigns the variable 'number' to the integer 5

number += 3 # Increment number by 3. Same as writing 'number = number + 3'
print(number)
# 8

number -= 3 # Decrement number by 3. Same as writing 'number = number - 3'
            # This is effectively the opposite of above
print(number) 
# 5
```

```python
# ------------ Comparison operators ------------

print(5 == 5)
# True

print(5 != 10)
# True

print(10 < 10)
# False

print(10 <= 10)
# True

print(2 > 5)
# False

print(2 >= 5)
# False
```

```python
# ------------ Boolean operators ------------
age = 16
has_license = False
can_drive = age >= 16 and has_license
print(can_drive)
# Is False because has_license is False

is_raining = True
is_very_sunny = False
bring_umbrella = is_raining or is_very_sunny
print(bring_umbrella)
# Is True because is_raining is True. We need the umbrella!

good_weather = not bring_umbrella
print(good_weather)
# Is False because we determined that bring_umbrella is True.
```

If the examples above are not sufficient then it is best to look them up.

### Task: Quadratic formula

In maths a common formula is the [quadratic formula](https://en.wikipedia.org/wiki/Quadratic_formula). Using the scaffhold below, compute the two solutions of the quadratic. You will need to use the arithmetic operators for this task.

```python title=quadratic.py
# x^2 - 3x - 10

a = 1
b = -3
c = -10

# Your code here
first_solution = ...
second_solution = ...
# ^^^^^^^^^^^^^^

print("x = " + str(first_solution))
print("x = " + str(second_solution))
```

## User Input

Sometimes you may want to request input from the user so that they can interact with the program while it is running. We will start with a simple example. The `input()` function is what enables this. When we call the `input()` function, python will stop and wait for the user to type something in. When the user presses *enter* the function will return what the user typed in.

We can optionally put some text in the function `input()` and this text will be printed to the screen. For example:

```python title=hello_input.py
name = input("What is your name? ")
print("Hello " + name)
```

Output:

```bash
$ python hello_input.py
What is your name? Jaedan
Hello Jaedan
```

### Task: Colour

Write a program that asks the user what their favourite colour is and then prints, "{colour} is a nice colour". For example:

```bash
$ python colour.py
What is your favourite colour? Blue
Blue is a nice colour
```

:::note

The text 'Blue' above is written by the user.

:::

This challenge makes use of *variables*, *user input* and basic *string formatting*.

## Types

Everything inside of python has a type. Most of the types we will be working with are:

- Booleans: True or False
- Integers: Positive or Negative numbers with no decimal
- Floats: Approximate representations of decimal numbers (try `1.2 - 1`)
- Strings: Words. 'Strings' of letters.
- Lists: A collection that can contain multiple other things (discussed later).

### Task: Types

Complete the code below to understand what each of the data-types there are in Python:

```python
# Assign any example of the correct type to each variable.

my_boolean = # Your code here
my_integer = # Your code here
my_float = # Your code here
my_string = # Your code here

assert isinstance(my_boolean, bool)
assert isinstance(my_integer, int)
assert isinstance(my_float, float)
assert isinstance(my_string, str)
```

If the task is done correctly then the program will not error when it is run. There are a couple more types in Python that are useful but these are the main ones you need to know.

This challenge makes use of "types" <https://realpython.com/python-data-types/>. Understanding types is a fundamental building block of any programming language.

## If Statements

The most important keyword to know in any programming language. This allow you to control the execution of the program based upon a condition evaluating to True or False.

Consider the following example:

```python
if True:
    print("This will print")

if False:
    print("This will not")

if 5 < 10:
    print("This will print")

if 10 == 0:
    print("This will not")

foo = 7 * 7 == 49
bar = 144 / 12 == 10
if foo and not bar:
    print("This will print")
```

Each example is self-explanitory.

### Elif and Else

Sometimes when working with if statements you want evaluate some conditions if and only if another one fails. This is where the keywords **elif** and **else** come in handy. Let's start with **else**. Else goes after the if statement. If the statement evaluates to False, this code branch will be run instead. For example:

```python
if 4 < 1: # False
    # This will not be printed
    print("Maths is broken")
else:
    # This will be printed
    print("Maths is saved")
```

**Elif** is used *between the if and the else* if we want to evaulate another expression. For example:

```python
name = "James"
if name == "Dave":
    # This will not be printed
    print("Dave is a bot")
elif name == "James":
    # This will printed
    print("Genius")
else:
    # This will not be printed
    print("They aight")
```

As you can see if the name input is "James", then only the text "Genius" is printed.

### Task: Favourite Number

Write a program that asks the user for their favourite number and then depending on their input will give a different response. Below is an example execution of the program:

```bash
$ python if_statements.py
What is your favourite number? 7
Very lucky
```

```bash
$ python if_statements.py
What is your favourite number? 42
The meaning of life
```

```bash
$ python if_statements.py
What is your favourite number? 3
Three lives
```

But if the user inputs any other number say:

```bash
$ python if_statements.py
What is your favourite number? 5
Okay
```

## Loops

Loops alow you to repeat execution of a certain code block. There are two keywords that can be used to create a loop, **while** and **for**.

- While loops will continue to be run as long as the condition next to the while evaluates to True. This is very powerful and used correctly and drastically reduce the amount of code you need to write.

    ```python
    fruits = ["apple", "mango", "banana"]

    i = 0
    while i < 3:
        fruit = fruits[i]
        print(fruit)
        i += 1
    ```

    This code will *iterate* over the fruits list and print out each element. The square brackets `[]` allow me to retrieve a specific element by *index* in the list fruits.

    Index 0 is the first element in python and in most other programming languages.

- For loops work slightly differently. Instead of stopping until the condition evaluates to True, they instead try to iterate the object, storing the instance it finds in a variable. For loops are what we use the majority of the time instead of while loops. The above example can be simply rewritten using a for loop like below:

    ```python
    fruits = ["apple", "mango", "banana"]

    for fruit in fruits:
        print(fruit)
    ```

    Since the fruits list can be unpacked, the for loop will automatically unpack each fruit into the fruit variable for us to use. Under the hood, this "unpacking" is actually called an *iterator*. Since the "List" type in Python inherenty possesses an *iterator*, we can use the for loop on them. Other common types that have an iterator are:

    - Strings: Iterator returns each character in the string.
    - The `range(x)` function: Returns each number starting from 0 up to but not including `x`. Eg. range(4) returns 0, 1, 2, 3

While loops and for loops have two special keywords that uniquely iteract with them, **continue** and **break**. These keywords each allow you to override some default behaviour in loops. Below is what they do with examples:

- **continue** will *immediately* stop execution of the current iteration in the loop and start execution of the next iteration skipping any remaining steps left to do.

    ```python
    fruits = ["apple", "mango", "banana"]

    for fruit in fruits:
        if fruit == "mango"
            continue

        print(fruit)
    ```

    The above code will output "apple" and then "banana". Mango will not print because its print was skipped by continue.

- **break** will *immediately* stop execution of the loop completely, exiting the for or while loop.

    ```python
    fruits = ["apple", "mango", "banana"]

    for fruit in fruits:
        if fruit == "mango"
            break

        print(fruit)
    ```

    The above code will output only "apple". Once the loop hits the mango, the loop was **break**ed, cancelling the current iteration of mango, and cancelling the remaining iteration of banana.

While loops will continue to run until they are **break**ed or until the condition next to the while evaluates to False. This task will utilise this behaviour.

### Task: Understanding loops

Using the scaffhold below, modify the program so that it instead prints the even numbers from numbers 1 to 50.

```python
i = 0
while i <= 100:
    print(i)
    i += 1
```

### While true

A common way to use while loops is by writing:

```python
while True:
    # Do something infinitely
    pass
```

While True loops will continue to run *forever* unless the keyword **break** is used. While true loops or *infinite loops* as they're commmonly known are one of the main sources of "crashes" that new programmers will experience (technically it doesn't crash, but rather the program hangs or stalls). Used correctly, while True loops can be very useful. Consider the following bad example:

```python
i = 0
while True:
    print(i)
    i += 1
```

:::caution

This code will continue to run forever, printing out a counter that increases. The only way to kill the program is by pressing CTRL+C on your keyboard while the program is running. CTRL+C sends Python a KeyboardInterrupt that will crash the program (safely but) fairly ungracefully.

:::

A common example of while True loops are around user input. If I want to ask the user for input continuously, I can use a while True loop. Consider below:

```python
while True:
    name = input("What is your name? ")

    if name == "":
        break
    
    print("Hello " + name)
```

Only until the user inputs nothing does the program finish. Or until the user press CTRL+C as we discussed before.

### Task: Evens

Using the scaffhold below, write a program that iterates over the list of integers and only prints the integers that are even. Try to do this task using **for** loops.

```python
numbers = [-2, 3, 6, 2, 18, 9, 0, 123, 6542]
```

```bash
$ python even.py
-2
6
2
18
0
6542
```

:::tip Hint

The modulo operator `%` is great for this

:::

### Task: Fizzbuzz

Using the scaffhold below, print out the word **fizz** when the number is divisible by 3, **buzz** when the number is divisible by 5, and **fizzbuzz** when the number is divisible by 3 and 5. Print **boring** otherwise.

```python
for number in range(100): # Starts at 0, ends at 99
    # Your code here
    print(number)
```

Example output:

```bash
$ python fizzbuzz.py
boring
boring
boring
fizz
boring
buzz
fizz
boring
boring
fizz
buzz
boring
fizz
boring
boring
fizzbuzz
...and so on
```

This challenge makes use of *if* statements and *boolean operators*.

## Lists

We've briefly touched on lists in the previous sections but let's spend some time specifically looking at lists. Lists are just another data-type in Python. At their core, they are merely a way of containing a list of other data types. Who would've thought right?

## Command line arguments

Command-line arguments let you pass user input to the program on execution of the program. When running the program with `python game.py` each word after the program is called an **argument**. For example:

```bash
$ python game.py hello world
```

In this example, the program `game.py` is run with two arguments, "hello" and "world". If the real world, these arguments usually contain helpful information for the program to run, or allow you a way to configure the program without needing to change the source code itself. The challenge later will help you understand how command-line arguments can be read.

### Reading Command-line arguments

For some reason in Python, command-line arguments are stored inside a variable in python called `sys.argv` (short for system argument variables). `sys.argv` is a list containing all the arguments as strings. To access sys.argv we first need to input the `sys` module. By convention, importing modules usually goes at the top of the file. For example:

```python title=arguments.py
import sys

print(len(sys.argv)) # Prints the number of arguments
print(sys.argv) # Prints the arguments
```

Try running the code above like so:

```bash
python arguments.py
python arguments.py First
python arguments.py Here is a long list of arguments
```

What do you notice? *Note*: The first command-line argument is always the name of the file itself. This is expected behaviour.

### Task: Command line arguments

Write a program to read all the command line arguments and re-print all of them, except the first. Print each argument on a separate line. For example:

```bash
$ python command_line.py Hello World these are my arguments
Hello
World
these
are
my
arguments
```

Notice how `command.py` is not included in the output. There are many ways to solve this task. Consider looking at <https://www.programiz.com/python-programming/examples/list-slicing>

## Functions

Functions are another core building block of any programming language. They allow you to *reuse* code and split code into functional blocks. Many functions come implicitly with any programming language. For example, the `print()` function or `input()` function which you may have used a few times.

We can actually create our own functions and they are done using the **def** keyword in Python. Whenever we make a function we need to consider two things.

1. What are the inputs (parameters) of the function?
2. What is the output (return value) of the function?

Let's take the `input()` function as an example. While we do not know what the exact implementation of `input()` is, we do indeed know what the inputs and outputs are. When someone writes:

```python
name = input("What is your name? ")
```

The *parameter* to the function is the string "What is your name? " and the *return value* of the function is what the user typed into their keyboard. All functions in programming follow this principle. Parameters, and return values.

### Scope and variables

When creating our own functions, many people get confused about the "scope" of variables. Here's the key information you need to remember: **Any variables created inside a function only exist inside that function. This concept is the idea of scope. Variables' scope is inside the current function only.** Every programming language will enforce this. Here is an example:

```python
def hello():
    my_variable = 5

hello()
print(my_variable)
```

This will cause an error. The variable `my_variable` does not exist outside the function. We cannot try to read the local variable `my_variable` from outside the functionm, as *scope* means the variable doesn't exist there at all. If I wanted to **return** some information from the function then I would need to use the keyword **return**. Consider the following:

```python
def hello():
    my_variable = 5
    return my_variable

output = hello()
print(output)
```

The `hello()` function **returns** the number 5. So when we call `hello()`, it will evaulate to 5. We can then store that answer in a variable if we want and do whatever we like with it.

### Parameters

Most of the time we need to pass information to the function for it to do something. To support this we modify the definition of the function to include a parameter. Here is an example:

```python
def hello(name):
    print(f"Hello {name}")


hello("Dave")
hello("James")
hello("Bob")
```

See: [Python f-strings](https://realpython.com/python-f-strings/#f-strings-a-new-and-improved-way-to-format-strings-in-python)

When we pass a string to the function `hello()`, the `name` variable will contain "Dave", "James" and then "Bob".

We can add multiple parameters if we want with a comma.

```python
def hello(name, age):
    print(f"Hello {name}. Age: {age}")


hello("Dave", 25)
hello("James", 31)
hello("Bob", 50)
```

```bash
Hello Dave. Age: 25
Hello James. Age: 31
Hello Bob. Age: 50
```

### Copy

Let me make a final remark about functions and that is that parameters we pass to a function are *copied*. This is important to know. Consider the following:

```python
def modify(a):
    a += 10

number = 5
modify(number)
print(number)
```

What do you think would happen based upon the statement I made above? This is the output:

```bash
5
```

When we pass `number` to the function `modify`, it is copied. The local variable `a` is indeed 5 and then modified to be 15. But when we return from the function, the actual `number` has not been changed. Only the copy was changed.

This is actually really good behaviour, because we know that functions can't edit the information we pass to functions. If we want functions to do that, then we would need to explicitly *return* the information we want to keep and reassign that information to another variable. So let's go back to out example and fix it so that the modify function actually modifys.

```python showLineNumbers
def modify(a):
    a += 10
    return a

number = 5
number = modify(number)
print(number)
```

```bash
15
```

As you can see we explicitly returned 15 from the function and assigned it back to `number` on line 6. It's line 6 that is editing the `number` variable.

To reiterate, parameters are **copied**. Before moving onto the task I'll quickly make a note that this copy rule is only true when we are talking about Booleans, Integers, Floats, and Strings. The bahaviour of lists and other types is on the advanced page.

### Task: Divide by

Create a function that divides two numbers (the parameters), but instead of erroring when dividing by zero, it instead **returns** the number 0. Start with below as the scaffhold. Try to do this by using an if statement in the function.

```python title=divide_by_challenge.py
def divide_by(a, b):
    # Your code here
    pass

# For testing
assert divide_by(10, 2) == 5
assert divide_by(90, 5) == 18
assert divide_by(2, 4) == 0.5
assert divide_by(7, 0) == 0
```

Run with:

```bash
$ python divide_by_challenge.py
```

### Task: Quadratic v2

In an earlier task you computed the quadratic using fixed a, b, c values. One of the advantages of functions is the ability to reuse code. We are going to create a function called `solve_quadratic` that takes in three parameters a, b, c, and returns a list containing the two solutions. (Don't worry about lists yet. That is in the next section.)

Use the scaffhold below to adapt your code from the answer above.

```python title=quadratic2.py
def solve_quadratic(a, b, c):
    # Your code here

    return [first_solution, second_solution]


print(solve_quadratic(1, -3, -10))
print(solve_quadratic(4, -8, 4))
print(solve_quadratic(5, -6, 1))
print(solve_quadratic(1, -4, 6.25))
```

```bash
$ python quadratic2.py
[5.0, -2.0]
[1.0, 1.0]
[1.0, 0.2]
[(2+1.5j), (2-1.5j)]
```

### Appending to lists

Lists can be defined with elements already in them as I've done earlier with:

```python
fruits = ["apple", "mango", "banana"]
```

But a more common way to create lists is by creating an empty list and then *appending* to the list. The same list as above can be created using the following:

```python
fruits = []
fruits.append("apple")
fruits.append("mango")
fruits.append("banana")
```

It's more common because lists are very closely linked with loops and so *appending* to a list or reading an element from a list in a loop is extremely common. Here's an example:

```python showLineNumbers
fruits = ["apple", "mango", "banana"]
contains_n = []

for fruit in fruits:
    for letter in fruit:
        if letter == "n"
            contains_n.append(fruit)
            # Only breaks the inner for loop
            # Takes us back to line 4
            break

print(contains_n)
```

```bash
['mango', 'banana']
```

This above code is a very crude example of a filter, where I am filtering the fruits list to only contain the fruits that have the letter n in them. I do this by first iterating over the fruits, and then iterating over each letter in the fruit to test if the letter is "n". Now, the above isn't the most effective way to filter a list, but it works.

### Reading from lists

Again, we've already looked at one of the most common ways to read from lists; the for loop. But, sometimes we want to access a specific element in the list directly. We do this with the square bracket notation `[]`. So yes, while we define lists with square brackets, we also read from lists using square brackets too. Inside the square brackets we put the *index* we want to access. So if we want to access each element we would put:

```python
fruits = ["apple", "mango", "banana"]
apple = fruits[0]
mango = fruits[1]
banana = fruits[2]
```

As you can see, 0 is the first element in the list.

Here is another example which is fairly common:

```python
name = "James Smith"
name_list = name.split(" ")
# name_list = ["James", "Smith"]

first_name = name_list[0]
last_name = name_list[1]
```

The `.split()` *method* will split the string in two and return a list. We can then grab specific elements from the string.

:::info Methods and Functions

You may have noticed at this point that sometimes we call a function directly like `print()` but other times we call a function on an object itself like `thing.split()`. The latter is technically not a function, but rather a *method*. Until I explicitly talk about *methods* it is safe to assume that *methods* and *functions* are effectively the same.

:::

### IndexError

A common error that new programmers will encounter is the IndexError. This error occurs when you try to access an element in a list that does not exist. For example:

```python
fruits = ["apple", "mango", "banana"]
print(fruits[99])
```

There are not 100 elements in the list, so `fruits[99]` will raise an IndexError when this line of code is run. More often though, what will occur is what people call "off-by-one" errors. For example this is extremely common:

```python
fruits = ["apple", "mango", "banana"]
banana = fruits[3]
```

The above would error. Can you see why? The programmer was [off-by-one](https://en.wikipedia.org/wiki/Off-by-one_error).

:::tip

The index can also be a variable if the variable is an integer.

:::

### Task

Given the scaffhold below, finish the function so that it *returns* the sum of the first and last elements in a list of numbers.

```python
def sum_first_and_last(number_list):
    list_length = len(number_list) # hint
    # Your code here
    

assert sum_first_and_last([1, 2, 3, 4]) == 5
assert sum_first_and_last([1]) == 2 # First and last is 1
assert sum_first_and_last([9, 6, 3, -1]) == 8
assert sum_first_and_last([0.5, 0.5]) == 1
```

If correct, the code should not error.

## Exceptions

Exceptions or Errors in Python occur when something happens that Python doesn't know how to recover from. This is how applications crash. Some common errors in Python are:

- SyntaxError
- ZeroDivisionError
- IndexError
- ValueError
- FileNotFoundError

It doesn't take much to trigger an error. Some errors are unrecoverable fullstop (Syntax Errors -> You wrote invalid Python code and Python doesn't know how to interpret what you wrote). But most other errors can be recovered from as long as you as the coder anticipate them, and provide it with some steps to take if an error occurs. This can be done using the **try** and **except** block in Python.

### Try/Except

An easy way to crash python is try and divide another number by 0. For example:

```python
5 / 0
print("Hello")
```

```bash
Traceback (most recent call last):
  File "zero.py", line 1, in <module>
    5 / 0
ZeroDivisionError: division by zero
```

It didn't get to print "Hello" because a ZeroDivisionError was raised.

Now us as the programmer may want this to happen so that we can go and find the bug that is causing the divisor to be zero, but sometimes we don't. And so we may choose to ignore the error by *catching* or *excepting* if the error is raised. Consider the following:

```python
try:
    5 / 0
except ZeroDivisionError:
    print("oopsie")

print("Hello")
```

```bash
oopsie
Hello
```

As you can see, the error is no longer allowed to crash the program and execution can continue. This is especially helpful when asking for user input. User input is famously known for being bad and so often we will need to clean the input before using it. For example:

```python
number_string = input("Number to add with? ")

try:
    number = float(number_string)
except ValueError:
    number = 10

print(number + 5)
```

In this example, if the user inputs a number that can be converted to a float, then it will do so. If it can't, a ValueError is raised which we immediately catch and instead assign a default value of 10 and move on. But in this example, the problem should probably keep asking for input until the input is valid. Thankfully, this is where we can combine our knowledge of while loops.

```python
while True:
    try:
        number = float(input("Number to add with? "))
        break
    except ValueError:
        print("Sorry that is not a valid number, try again")
        
print(number)
```

This code will continue to ask for user input until it finally finds some valid input and is allowed to run the **break**, leaving the while True loop.

:::tip

Sometimes letting an error be thrown is better than catching it because some errors we can't recover from. A `FileNotFoundError` when trying to open a file may be a good example.

:::

:::info

Later the idea of "The Stack" is introduced. What happens when an error is raised is that the stack is continously popped until a try/except block is found. If it can't find one, the program crashes.

:::

### KeyboardInterrupt

There are many kinds of Errors in Python. This is one of them. This unique error that is raised when the user presses CTRL+C on their keyboard. We used it earlier to leave an infinite while True loop. But, like most other errors, this can be caught using a try/except block. This can be a useful tool for cancelling very large jobs, but while still exiting the program gracefully (without crashing).

:::caution

This presents a dangerous situation where a coder might decide to catch a KeyboardInterrupt and place them back into the while True loop. Consider:

```python
i = 0
while True:
    try:
        print(i)
        i += 1
    except KeyboardInterrupt:
        pass
```

If you want to, you can run this program. But without closing the terminal entirely it is extremely hard to stop execution of this program. You would essentially need to press CTRL+C twice SUPER fast. The first would be caught by the try block, and the second must happen while inside the except block. If you could get the second one to run exactly while inside the except block, the second KeyboardInterrupt would not be caught and would crash the program. But, this code is effectively impossible to crash without completely killing the process externally via the operating system by closing the terminal.

:::

### Task: User Division

Write a program that will continue to ask the user for two valid numbers, and then when it does, it will attempt to divide the two. If a ZeroDivisionError occurs, print "Division by 0". Try to do this task without using a single **if** statement.

```bash
$ python division.py
First number: 8
Second number: 4
2
```

Second example:

```bash
$ python division.py
First number: 8
Second number: blah
Not a number, try again.
Second number: 0
Division by 0
```

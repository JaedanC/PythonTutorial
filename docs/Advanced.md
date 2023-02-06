---
sidebar_position: 4
---

# Advanced

This document will go over the most complicated concepts:

- Recursion
- Magic methods
- Iterators
- Generators
- List Comprehensions
- `in` operator
- Lambda expressions
- Performance

## Recursion

Recursion is when you run the same function from inside the function.

> Recursion is when you run the same function from inside the function.
>> Recursion is when you run the same function from inside the function.
>>> Recursion is when you run the same function from inside the function.
>>>> Recursion is when you run the same function from inside the function.
>>>>> Recursion is when you run the same function from inside the function.

Recursion is specifically to do with functions and how you can call them. Understanding recursion though first requires you to understand what "The Stack" is. Whenever a function is called in Python, the existing state of the program is stored in a place in memory called the stack. I will represent the stack as a table.

| Frame | Stack |
| ----- | ----- |
|       |       |

Currently the stack is empty. Let's write a simple program to visualise how the stack works.

```python
def first(number):
    number += 5
    return number

def second(blah):
    blah += 7
    blah = first(blah)
    return blah

print(second(10))
```

Evaluating the execution of `second(10)` is a little complicated, so let's follow it using using stack.

- `second()` is called. The main execution is paused and placed on the stack:

| Frame | Stack         |
| ----- | ------------- |
| 1     | @ main line 9 |

- Then in `second()` is called `first()` is called

| Frame | Stack            |
| ----- | ---------------- |
| 1     | @ main line 9    |
| 2     | @ second line 38 |

- Then when `first()` returns, the old state is popped from the stack.

| Frame | Stack         |
| ----- | ------------- |
| 1     | @ main line 9 |

- Then when `second()` returns, the old state is popped from the stack.

| Frame | Stack |
| ----- | ----- |
|       |       |

This "Stack" is a real thing that under the hood that keeps track of the variables and location of execution so that when a function returns, it knows where to resume the execution from.

So here comes the fun part. Recursion. You can call the same function, from inside the function.

For example:

```python
def my_function(a, b):
    print(a, b)
    return my_function(a, b + 1)

my_function(1, 2)
```

```bash
1 2
1 3
1 4
...
1 994
1 995
1 996
Traceback (most recent call last):
  File "<stdin>", line 3, in my_function
  [Previous line repeated 992 more times]
RecursionError: maximum recursion depth exceeded while calling a Python object
```

Ah dang. We hit a Stack Overflow. Our stack got too big. We kept calling the function too many times and didn't let the function close. This is kinda like an infinite loop, but this one results in us eating all the resources of the computer until it crashes. Not great.

So this introduces us to the first key part in any recursive function. The exit strategy. This is also referred to as the "Base Case". How are we going to make sure the function has a stopping point. Consider the following:

```python
def my_function(a, b):
    if b == 100:
        return "Done"
    
    print(a, b)
    return my_function(a, b + 1)

print(my_function(1, 2))
```

```bash
1 1
1 2
1 3
...
1 97
1 98
1 99
'Done'
```

Nice. This time, the stack was able to close because I gave it an exit strategy when `b == 100`. Depending on what you want a recursive function to do, the exit strategy (or more multiple strategies) may be different.

One of the best cases for recursion is when searching a tree-like data structure. Below is an example of such a structure, and then how a recursive function may work to traverse the structure.

```python
class TreeNode:
    def __init__(self, left, right):
        self.left = left
        self.right = right

#                root
#               /    \
#              /      \
#             /        \
#            /          \
#           /            \
#          /              \
#         /\              /\
#        /  \            /  \
#       /    \          /    \
#      /      \        /      7
#     /\      /\      /\
#    /  \    /  \    /  \
#   0    5  8    4  6    2

root = \
    TreeNode(
        TreeNode(
            TreeNode(0, 5),
            TreeNode(8, 4)
        ),
        TreeNode(
            TreeNode(6, 2),
            7
        )
    )

def print_all_nodes(node):
    # Base case
    if not isinstance(node, TreeNode):
        print(node)
        return
    
    # The recursive case
    print_all_nodes(node.left)
    print_all_nodes(node.right)

print_all_nodes(root)
```

```bash
$ python nodes.py
0
5
8
4
6
2
7
```

### Another example

There will not be a task for this topic, as it is very situational. And often a recursive implementation can be done without recursion, with better performance. Usually the trade-off though is that a recursive solution may be elegant. The following recursive function breaks down an integer into a list of it's smallest factors.

For this example it is important to note that adding two lists just combines them into one list.

```python
def get_factors(number):
    # The recursive case is first.
    # If the number is divisible this should run.
    for i in range(2, number):
        if number % i == 0:
            return get_factors(i) + get_factors(number // i)
    
    # This is the base case. Is run when the number is
    # not divisible. Rare to see the base case after the
    # recursive case but it makes sense here.
    return [number]

print(get_factors(2520))
```

```bash
[2, 2, 2, 3, 3, 5, 7]
```

It may be a worthwhile exercise to think about how we may go about trying to do this problem without using recursion.

## Magic methods

In python there are some really cool ways to make your classes behave differently when exposed to various operations. These are done using *Magic methods*. These are special `__double_underscore__` methods that when overwritten can override the default behaviour.

In this section we'll go over some of my favourite magic methods, where to find a list of them, and some truely cursed things we can do with them.

### The good

My favourite magic method is `__repr__()`. This method is responsible for converting an class instance to a string. If you've ever tried printing an instance of a class you've made you might see something like this.

```python
class Game:
    def __init__(self, name, age_rating, platforms):
        self.name = name
        self.age_rating = age_rating
        self.platforms = platforms

deep_rock = Game("Deep Rock Galatic", 16, ["PC", "Xbox"])
print(deep_rock)
```

```bash
<__main__.Game object at 0x000002199EA37D60>
```

This isn't particularly useful. Thankfully we can override this behaviour by defining the `__repr__` method.

```python
class Game:
    def __init__(self, name, age_rating, platforms):
        self.name = name
        self.age_rating = age_rating
        self.platforms = platforms

    def __repr__(self):
        # This method expects a string to be returned
        output = f"Game: {self.name}\n" + \
            f"Age Rating: {self.age_rating}\n" + \
            f"Platforms: {self.platforms}"
        return output

deep_rock = Game("Deep Rock Galatic", 16, ["PC", "Xbox"])
print(deep_rock)
```

```bash
Game: Deep Rock Galatic  
Age Rating: 16
Platforms: ['PC', 'Xbox']
```

This is substantially better! Another common magic method that I like to override is `__add__`. This one allows you to define what happens when you added something to the instance. This method has a parameter. The parameter is what they are trying to add to the instance. For example in:

```python
deep_rock = Game("Deep Rock Galatic", 16, ["PC", "Xbox"])
player = Player("James", 20, ["Xbox"])
session = deep_rock + player
```

This is what is implicitly being called:

```python
session = deep_rock.__add__(player)
```

This is an exmaple of where this could be useful:

```python
class Collection:
    def __init__(self):
        self.games = []
    
    def add_game(self, game):
        self.games.append(game)
    
    def __repr__(self):
        return "{} game(s) in collection".format(len(self.games))


class Game:
    # Assume the same __init__ method
    def __add__(self, other):
        if isinstance(other, Game):
            collection = Collection()
            collection.add_game(self)
            collection.add_game(other)
            return collection
        assert False, "Must be a game"


deep_rock = Game("Deep Rock Galatic", 16, ["PC", "Xbox"])
mario_kart = Game("Mario Kart", 6, ["Switch"])
my_collection = deep_rock + mario_kart

print(my_collection)
```

```bash
2 game(s) in collection
```

This could be a great way to combine two custom objects, or create a new one from a combination. Just note that the type of the second object is usually not known, so unless you use `isinstance()` you will have to guess. Here is an example where I create a class to represent a vector.

```python
class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)
    
    def __repr__(self):
        return f"Vector({self.x}, {self.y})"


result = Vector(5, 80) + Vector(10, -30)
print(result)
```

In the example above I've assumed the second object will be other vectors. And then returned a new Vector from the result.

### How many magic methods are there?

A good way to find out is by running `dir(int)`. This will show you all the methods that are inherited by the `int` class. Googling any specific method will give you useful information.

<https://www.tutorialsteacher.com/python/magic-methods-in-python>

### Cursed Usage

Overwriting magic methods allows you to produce some truely cursed behaviour.

```python
class Number:
    def __init__(self, value):
        self.value = value
    
    def __add__(self, other):
        return 42

    def __repr__(self):
        return f"Number({self.value})"


result = Number(5) + Number(3)
print(result)
```

```bash
42
```

With great power comes great responsbility. We've only touched on a few of the magic methods in Python. I encourage you to investigate using more of them in your code if it makes sense to do so.

## Iterators

An iterator is a promise. If I ask for something, you'll give me something. If I ask for the next thing, you'll give me the next thing. If you run out of things to give me, tell me, I'll stop.

This is how iterators work internally. When you try to "iterate" over a data-type in python it will look for a iterator promise/contract on that type. If it can't find one, it errors. We can easily reproduce this by trying to iterate over an integer.

```python
for element in 5:
    pass
```

```bash
Traceback (most recent call last):     
  File "<stdin>", line 1, in <module>
TypeError: 'int' object is not iterable
```

This is where our magic methods come in. Some types in python have the method method `__iter__` implemented. This is the method that is called whenever is iterator is initially requested. After that, the `__next__` method is called on the object that is returned by `__iter__`. Let me give you an example. Let's create a class that represents a list, but when iterated, will iterate backwards.

```python
class ReverseList:
    def __init__(self, contents):
        self.contents = contents
    
    def __iter__(self):
        self.n = len(self.contents)
        return self
    
    def __next__(self):
        self.n -= 1
        if self.n < 0:
            raise StopIteration
        return self.contents[self.n]      

my_list = ReverseList([1, 2, 3, 4])

for number in my_list:
    print(number)
```

```bash
4
3
2
1
```

This is how we read the code:

1. When `for number in my_list` is first called, `my_list.__iter__()` is implicitly run to initialise the data structure to be iterated and to return the instance that contains the `__next__` method.
2. Then, the `my_list.__next__()` method is continously called to retrieve the next element. In this method I return the next element of the list working backwards.
3. When the list has been completely iterated over, I raise StopIteration which is a special error that python will silently catch. This tells python that `for number in my_list` has fully evaluated.

Now, technically there's nothing stopping you from returning something other than self in the `__iter__` method. It's not common but here's a reason to do it.

```python
class NormalIter:
    def ready(self, contents):
        self.contents = contents
        self.n = 0

    def __next__(self):
        if self.n < len(self.contents):
            element = self.contents[self.n]
            self.n += 1
            return element
        raise StopIteration

class ReverseIter:
    def ready(self, contents):
        self.contents = contents
        self.n = len(self.contents) - 1

    def __next__(self):
        if self.n >= 0:
            element = self.contents[self.n]
            self.n -= 1
            return element
        raise StopIteration

class MyList:
    def __init__(self, contents, iterator):
        self.contents = contents
        self.iterator = iterator
    
    def __iter__(self):
        self.iterator.ready(self.contents)
        return self.iterator

forwards = MyList([1, 2, 3, 4], NormalIter())
backwards = MyList([1, 2, 3, 4], ReverseIter())

print("Forwards")
for num in forwards:
    print(num)

print("Backwards")
for num in backwards:
    print(num)
```

```bash
Forwards
1        
2        
3        
4        
Backwards
4        
3        
2        
1 
```

As you can see we have decoupled the object and the iterator. This concept can be extended to traverse all kinds of weird data structures in many different ways.

:::note

If you really wanted to traverse a list backwards use:

```python
for item in reversed(my_list):
    pass
```

:::

## Generators

These work similarly to iterators but completely differently also. Generators introduce a new keyword `yield`. Before we move on, I need to stress that many people get confused between `return` and `yield`. The `yield` keyword is completely different to return and it only present in Python. This is why it is generally never spoken about. I have personally never written a generator, but knowing that they exist can be helpful.

A generator allows you to create a function and treat it like an iterator. Though typically as the name suggests, rather than iterating over something, it instead is generating some sequence. Let me give you an example generator where I mimic the bahaviour of range().

```python
def my_range(start, end):
    i = start
    while i < end:
        yield i
        i += 1


for number in my_range(1, 5):
    print(number)

print("Done")
```

```bash
1
2
3
4
```

What is happening here is very weird. The yield keyword acts like a return, but when the function is called again, it resumes execution immediately at the yield statement resuming execution from yield. The generator is considered consumed when the function returns normally. In the example above it's when the `while` loop completes.

I'm not going to talk about yield any more than that. If you really need a generator then you're probably fine looking up the details yourself. If you are still trying to grapple with functions themselves, then please just ignore that yield exists completely to avoid confusion. **return**, **return**, **return**.

## List Comprehensions

Now we are truely getting into powerful lazy territory. List comprehensions are a feature in Python that let you create lists in one line of code that may normally take 2 or more. Most simple list idioms can be replaced by a list compreshension. But beware, just because it's shorter, does not mean it is better. They can sometimes be hard to read.

Normally, we might construct a list like so:

```python
foo = []
for number in range(10):
    foo.append(number ** 2)
print(foo)
```

```bash
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
```

This can be shortened using list comprehensions like so:

```python
foo = [number ** 2 for number in range(10)]
print(foo)
```

What this is doing is unpacking `range()` and then the results of `number ** 2` will automatically be appended to the list. This is the essence of list comprehensions. They allow you to quickly unpack a for loop's calculation into a list. Here is another example, but a little more complicated.

```python
friends = ["James", "Bob", "Tim", "Josh", "Jim"]

j_names = []
for name in friends:
    if name.startswith("J"):
        j_names.append(name)
```

This for loop introduces an `if` expression. List comprehensions can account for this like so:

```python
friends = ["James", "Bob", "Tim", "Josh", "Jim"]
j_names = [name for name in friends if name.startswith("J")]
```

With this understanding, this is how you read a list comprehension:

```python
result = [item.do_something() for item in collection if condition]
```

1. What `collection` do you want to loop over and what variable should we store each `item` in?
2. What are you going to do with the `item`?
3. Should we ignore any items that do not satisfy a condition?

### Nesting them

Since list comprehensions evaluate to a list, there's nothing stopping us from nesting list comprehensions. I would advise against aggresively doing this though because it can become hard to read very quickly, but as dirty one-liners go nested list comprehensions is right up there.

Consider this example:

```python
grid = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

doubled = [[value * 2 for value in row] for row in grid]
print(doubled)
```

```bash
[[2, 4, 6], [8, 10, 12], [14, 16, 18]]
```

To do the same thing in a for loop would require:

```python
doubled = []
for row in grid:
    current = []
    for value in row:
        current.append(value * 2)
    grid.append(current)

```

This is a good example of when a list comprehension may be easier to read than a `for` loop.

### Dictionaries too

Dictionary comprehesions work too, and their format is similar but different. To create an entry in a dictionary you need both a key and a value. Consider the following example:

```python
friends = ["James", "Bob", "Tim", "Josh", "Jim"]
numbered = {i : name for i, name in enumerate(friends)}
print(numbered)
```

```bash
{0: 'James', 1: 'Bob', 2: 'Tim', 3: 'Josh', 4: 'Jim'}
```

Here we can see that I have created a dictionary whose keys are numerical and values are the names of the friends. A conditional can be added too like the list comprehensions:

```python
friends = ["James", "Bob", "Tim", "Josh", "Jim"]
numbered = {i : name for i, name in enumerate(friends) if name.startswith("J") and i % 2 == 0}
print(numbered)
```

```bash
{0: 'James', 4: 'Jim'}
```

Here you can see I've filtered both using `name` and `i`, but any valid condition works too.

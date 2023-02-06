---
sidebar_position: 3
---

# Intermediate

This document will go over some more complicated concepts like:

- Reading and writing to files
- Dictionaries
- Tuples and Unpacking
- Classes
- Modules

## Files

Reading and writing to files is actually fairly straight forward. All you need to know in Python is where the file is relative to where your running the program from. So for example if you have the current file layout in windows:

```bash
📂mystuff
  ┣ 📜program.py
  ┣ 📜data.csv
  ┗ 📂levels
    ┣ 📜first.txt
    ┗ 📜second.txt
```

If you run `python program.py` then to open `data.csv` you would simply write:

```python
f = open("data.csv")
contents = f.read()
f.close()
# do something
```

To open `first.txt` you would need to provide the file path too:

```python
f = open("levels/first.txt")
contents = f.read()
f.close()
```

### With blocks

In the above examples I've used the structure, open, do stuff, close. It is important to close the file when you are done otherwise the operating system will not let you look at the file until the program is finished. It's just good practice to close the file when you are done rather than letting the OS do it for you. Thankfully there is a way in python to automatically close it when you are done using the **with** keyword. Below is identical to above:

```python
with open("data.csv") as f:
    contents = f.read()
```

This is the preferred way to read files and this is what I will use from now on.

### Working with the contents

So it's all well and good being able to read the contents of a file, but what exactly does the contents variable hold now? After calling the `f.read()` *method*, `contents` contains a string of the *entire* file. For example:

```csv title=data.csv
name,age,number
James,24,01234567
Bob,36,30945703
Gary,47,98723850
```

Now let's print `contents`:

```bash
name,age,number
James,24,01234567
Bob,36,30945703
Gary,47,98723850
```

Wow, incredible, who would have guessed. What is important to know here that even though this is a text file, there are actually hidden characters in this file. This hidden character is the newline character (Denoted as \n in Python). This is typically what is written to a text file when you press enter. It is invisible, but it tells Notepad and other editors to show what's next on the next line. We can use this to our advantage to read each line separately.

```python
lines = contents.split("\n")
print(lines)
```

```bash
$ python read_csv.py
['name,age,number', 'James,24,01234567', 'Bob,36,30945703', 'Gary,47,98723850']
```

Cool, we now have a list whose elements are each a line from the file as a string. This may be what we want, but in most cases we'll want to do some further manipulation at that stage. Before going any further it is important to note in this example that python has a built-in module called `csv` that will do all this stuff for us, but for demonstrative purposes let's ignore that module.

Finally, let's consider one last example where I go to use the information from above. Let's say I wanted to print what Gary's age was. How would I do that? Well let's break down the steps in english first, before trying to tackle it in python:

- Iterate over the lines in the csv
    - Split the line into name, age, and number on the comma
    - If the name is gary
        - print the age

And in Python

```python
for line in lines:
    line_split = line.split(",")
    name = line_split[0]
    age = line_split[1]
    if name == "Gary":
        print(age)
```

**Note:** Reading csvs like this is really bad practice because strings are allowed to contain the "," character as long as they are enclosed in quotes. This is why the csv module exists so that us programmers don't need to reinvent the wheel.

This is only one example of working with files. Sometimes we will need to parse and validate the information inside a file. Sometimes the file format is consisteny, other times it isn't and so we have to use our savvy skills of try/except blocks to extract the information we desire. Working with files requires a unique approach each time, but this is why knowing the fundamentals is key first.

### Writing to files

Writing to a file is usually done using the `f.write()` method instead of `f.read()`. But we also need to tell python when we open the file that we intend to write to it.

```python
with open("new_file.txt", "w") as f:
    f.write("This is my new file\n")
```

By adding `"w"` to the open function, we are telling python that we intend to *overwrite* the file and then write to it. There are more options that you can do instead if you want to read the python documentation.

To write to an open file `f`, you call the `f.write()` method where you pass a string. If you want to write to a newline you can include a `"\n"` as we've seen earlier. Calling `f.write()` multiple times will continue to append text. Some people like to write files one line at a time, others not. This is personal preference usually.

Consier this example that writes out the csv we just read earlier.

```python
lines = [
    "name,age,number",
    "James,24,01234567",
    "Bob,36,30945703",
    "Gary,47,98723850"
]

with open("data_2.csv", "w") as f:
    for line in lines:
        f.write(line + "\n")
```

In this example, the only downside to just appending `"\n"` to each line is that the final line will be blank in `data_2.csv`

```csv
name,age,number
James,24,01234567
Bob,36,30945703
Gary,47,98723850

```

In this example to get around this we might instead choose call the `join()` method with the list with the `"\n"` character. This is exactly the opposite of the `.split()` method we used earlier.

```python
lines = [
    "name,age,number",
    "James,24,01234567",
    "Bob,36,30945703",
    "Gary,47,98723850"
]

with open("data_2.csv", "w") as f:
    f.write("\n".join(lines))
```

### Task

Let's simulate a game where a file may contain information about the level. Consider the following file:

`level.txt`

```txt
Level:1
Enemies:15
Pickups:potions,gear,weapons
```

Write a program that parses this file format. Pickups is comma-delimited. Finally, print the information to the screen in the following way:

```bash
Welcome to level 1. There are 15 enemies to beat.
On this level there are 3 things to find:
potions
gear
weapons
Good luck
```

This program should also work if you changed the numbers or amount of pickups in the file.

Start with:

```python
with open("level.txt") as f:
    level = f.read()
```

Remember to use the `.split()` method.

### Task Writing

**Note:** Feel free to read the dictionaries section before trying this task.

Write a function that takes in a level state and then writes that to a file. The level is saved as a dictionary like below. The format of the file should match that of the challenge above. The only thing extra to note here is that you must also take in the name of the file to write to.

```python
def save_level(filename, level_state):
    # Your code here
    # Remember to open the file with "w".
    pass


level = {
    "level": 1,
    "enemies": 15,
    "pickups": [ "potions", "gear", "weapons" ]
}

save_level("level_1_save.txt", level)
```

This program should also work if you changed the numbers or amount of pickups in the dictionary.

The `.join()` can be useful for this task.

## Dictionaries

Dictionaries are another *type* that we haven't looked at yet. They are similar but different to lists. Similar in that they can hold multiple values but different in how they are stored and accessed. Dictionaries very closely relate to json if you are familiar with the file format.

Dictionaries store a *value* at a specific *key*. These are usually called *key*, *value* pairs. To create a dictionary we use the curly braces `{}`.

```python
my_dictionary = {}
```

To add things to the dictionary we again use our square bracket notation:

```python
my_dictionary["secret"] = "my_password"
```

In this example the key is "secret" and the value is "my_password". What this lets us do is access "my_password" by only knowing the key. For example:

```python
password = my_dictionary["secret"]
```

Instead of writing to the key secret, we are now reading from it. The `password` variable will now contain the string "my_password". Dictionaries are great because in some sense they can provide structure to an arbitrary set of information. If I used the list:

```python
person = [
    "James",
    28,
    "Apple",
    3.14
]
```

You *might* be able to guess what each thing means. But let me use a dictionary instead:

```python
person = {
    "name": "James",
    "age": 28,
    "operating_system": "Apple",
    "favourite_number": 3.14
}
```

You now have labels attached to each of these pieces of data. And so it makes accessing this information later much easier as you don't need to know the order of the dictionary (unlike a list). You only need to know the keys making your code more readable. Compare the two.

```python
# Old way
name = person[0]
age = person[1]
os = person[2]
number = person[3]

# New way
name = person["name"]
age = person["age"]
os = person["operating_system"]
number = person["favourite_number"]
```

The second way is much more readible. The second is also much better for semi-unstructed data.

And so finally I'll note that with our information about lists and dictionaries, there's actually nothing stopping us from nesting dictionaries inside dictionaries and lists and vice versa. Let's look at a larger example.

```python
person = {
    "name": "James",
    "owns": {
        "books": [
            { "title": "Harry Potter" },
            { "title": "Hunger Games" },
            { "title": "Lord of the Rings" }
        ],
        "games": [
            { "title": "Counter-Strike" },
            { "title": "Overwatch" }
        ]
    },
    "naughts_and_crosses": [
        [0, 0, 1],
        [2, 1, 0],
        [1, 2, 2]
    ]
}
```

This example has:

- Lists inside lists
- Dictionaries inside dictionaries
- Lists inside dictionaries
- Dictionaries inside lists...

The point is, you can store whatever you like, wherever you like. Lists and Dictionaries are just like other types, except they can hold multiples of other things.

### Iterating Dictionaries

Like lists, sometimes you may want to iterate over a dictionary. However, sometimes you may want to access only all the keys, or only all of the values, or maybe you want both at the same time. Thankfully Python let's us choose how we want to iterate over dictionaries. Let's first consider this example:

```python
passwords = {
    "James": "batman",
    "Tim": "abc123",
    "Dave": "qwerty",
    "John": "asdf"
}

print("Only keys")
for key in passwords.keys():
    print(key)

print("\nOnly values")
for value in passwords.values():
    print(value)

print("\nBoth")
for key, value in passwords.items():
    print(key, value)
```

```bash
Only keys
James
Tim
Dave
John

Only values
batman
abc123
qwerty
asdf

Both
James batman
Tim abc123
Dave qwerty
John asdf
```

This example is fairly self-explanitory. Using the `.keys()`, `.values()` or `.items()` methods we can get the corresponding iterator for the information we desire.

### Task

Dictionaries are often the data type that json gets parsed to. Json is the file format the many online Web API's use to send information. Using your knowledge of Dictionaries and for loops, extract information from the dictionary below. Do not hard-code the answer. Try to extract the information from the dictionary.

```python
response = {
    "error": None,
    "data": [ # This is a list of dictionaries
        {
            "name": "John Smith",
            "hobby": ["Gaming", "Eating"]
        },
        {
            "name": "Terry Blue",
            "hobby": ["Reading"]
        },
        {
            "name": "Alex Brown",
            "hobby": ["Writing", "Cooking", "Sport"]
        }
    ]
}
```

For this task, print out the following information: I want to know Alex Brown's hobbies.

```bash
Alex Brown's hobbies are
Writing
Cooking
Sport
```

## Tuples and Unpacking

In this section I'm going to introduce a new data-type in Python that often gets confused with lists. Tuples are essentially non-editable lists. In Python, you can create a tuple using round brackets `()`.

```python
vector = (1, 2)
```

Before with lists we were able to create them using `[]` and them append to them with `.append()`. Tuples do not have an append function. They are *Immutable*. This means that to "edit" a tuple, is to actually create a new one entirely. Consider the following:

```python
new_tuple = (1, "Hello") + ("World", 4, False)
print(new_tuple)
```

```bash
(1, 'Hello', 'World', 4, False)
```

Just so we're clear, no tuples here are being *modified*. We have just created a new tuple using the old one.

So now you're probably wondering why I chose to put tuples under the Intermediate tutorial not the basic. This is where unpacking comes in.

### Unpacking

Unpacking is a feature in Python that lets you fully *unpack* an iterable. I'm going to go over the common uses of unpacking, but know that this concept is very powerful.

Before in python if we had an iterable (such as a list) and we wanted to get each of the elements in their own variable we would do this:

```python
vector = (5, 10, 15)
x = vector[0]
y = vector[1]
z = vector[2]
```

Wouldn't it be cool if we could do this:

```python
vector = (5, 10, 15)
x, y, z = vector
```

Well, actually we can. Above is valid python code. What's going on here is quite magical. Python is implicitly looping through vector and trying to assign all the elements in it to a variable on the left. What's crucial to understand here is that there is no such thing as *partial* unpacking. If you tried to write:

```python
x, y = vector
```

```bash
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>                                 im': 'value'}
ValueError: too many values to unpack (expected 2)
```

As you can see it errors because it found 3 items to unpack but you only gave it two variable to unpack to. Typically, if this is actually something you want to do, most people just use `_` as a placeholder to say that you are not meaning to use it. `_` is not special, it's just a variable like any other. But, by convention it means we won't use it.

```python
vector = (5, 10, 15)
x, y, _ = vector
print(x * y)
```

```bash
50
```

Some built-in functions in Python return tuples and we can leverage this to our advantage. The most popular function that does this is `enumerate()`. This function works a little bit like `range()` in that it can be looped over, but what makes enumerate so good is that it can replace code that looks like this:

```python
fruits = ["Apple", "Banana", "Mango"]
i = 0
```


## Classes

Classes frankly are the most powerful thing inside Python and many other programming languages. We usuallyn leave teaching them till last because understanding how they work touches on a bunch of concepts. If you've written a Python program, you've interacted with classes, even if you didn't know it.

Classes are templates that can be instantiated. Let me give you a real life example before talking code. Whenever a car company want to make a new car, they first have to define a reference template. Then, after that many cars are made using that template. Each car is an instance of the template. The template car might have a certain set of statistics or data associated with it, that over time will change for each instance. For example, the template car does not have any petrol in it. Instance cars started with no petrol, but over time they will have varying amounts of petrol in it. In python, we can create our own template using the new keyword **class**.

### Defining a class

Creating a new class is as simple as writing:

```python
class Car:
    pass
```

We have now created a new type called "Car". Now, let's make some instances of our template:

```python
astina = Car()
hilux = Car()
corolla = Car()
```

We can start adding information to the class with dot (`.`) notaion. Let me add some information to these cars.

```python
astina.name = "Mazda Astina"
astina.size = "Small"
astina.engine_size = 2.5
astina.fuel = 0

hilux.name = "Toyota Hilux"
hilux.size = "Large"
hilux.engine_size = 2.8
hilux.fuel = 24

corolla.name = "Toyota Corolla"
corolla.size = "Medium"
corolla.engine_size = 1.8
corolla.fuel = 3
```

So now each car is storing information about it's instance. We can now go and write some functions to interact with our Cars. Let me make a new function called `drive()`. The function will see if the car has fuel, and if it does it will print "driving" and reduce some fuel. If it does not have fuel it will print "stopped".

```python
def drive(car)
    if car.fuel > 0:
        # Reduce the cars fuel by 5 but stop the car from having negative fuel
        car.fuel = max(0, car.fuel - 5)
        print(f"{car.name} is driving")
    else:
        print(f"{car.name} is stopped")

# And so let's try it on our new cars
drive(astina)
drive(astina)
drive(astina)
print()

drive(hilux)
drive(hilux)
drive(hilux)
print()

drive(corolla)
drive(corolla)
drive(corolla)
```

```bash
Mazda Astina is stopped
Mazda Astina is stopped
Mazda Astina is stopped

Toyota Hilux is driving
Toyota Hilux is driving
Toyota Hilux is driving

Toyota Corolla is driving
Toyota Corolla is stopped
Toyota Corolla is stopped
```

And so as you can see we can now interact with the cars from inside a function. Now what I want the takeaway to be here is that we have created a template, and created some instances of the template, added some unique information to each instance, and then interacted with each instance from inside a function. Let's compile this program into one file and let's see if we can make it look even cleaner in the future.

```python
class Car:
    pass

astina = Car()
hilux = Car()
corolla = Car()

astina.name = "Mazda Astina"
astina.size = "Small"
astina.engine_size = 2.5
astina.fuel = 0

hilux.name = "Toyota Hilux"
hilux.size = "Large"
hilux.engine_size = 2.8
hilux.fuel = 24

corolla.name = "Toyota Corolla"
corolla.size = "Medium"
corolla.engine_size = 1.8
corolla.fuel = 3

def drive(car)
    if car.fuel > 0:
        # Reduce the cars fuel by 5 but stop the car from having negative fuel
        car.fuel = max(0, car.fuel - 5)
        print(f"{car.name} is driving")
    else:
        print(f"{car.name} is stopped")

# And so let's try it on our new cars
drive(astina)
drive(astina)
drive(astina)
print()

drive(hilux)
drive(hilux)
drive(hilux)
print()

drive(corolla)
drive(corolla)
drive(corolla)
```

### Constructors

Our first order of business is trying to clean up how we instantiate all those cars. If only we could write something like this:

```python
astina = Car("Mazda Astina", "Small", 2.5, 0)
```

Well we can, and that's precisely what a **constructor** let's us do. We essentially define a special sort of **function** called a **method** (yes methods are back). **Methods** are functions that exclusively tied to a class. In python (for some reason), they have made the constructor **method** `__init__()`. Let me show you an example. Let's go back to our template definition of the Car class.

```python
class Car:
    def __init__(self, name, size, engine_size, fuel):
        self.name = name
        self.size = size
        self.engine_size = engine_size
        self.fuel = fuel
```

What we are telling Python here is that whenever someone calls `Car(a, b, c, d)` I want you to actually call the **contructor** method and then save the parameters onto the instance. So when we write:

```python
astina = Car("Mazda Astina", "Small", 2.5, 0)

# This is exactly the same as
astina = Car()
astina.name = "Mazda Astina"
astina.size = "Small"
astina.engine_size = 2.5
astina.fuel = 0
```

Now, you may have noticed that the first parameter in the **contructor** is *self*. Now again, this is special. When we call `Car()` the first parameter is reserved for the instance itself. So when we add "Mazda Astina", that is skipping over the reserved *self* and assigning it to the name *parameter*.

What is actually happening under the hood when we call the constructor is this:

```python
astina = Car("Mazda Astina", "Small", 2.5, 0)

# Above is shorthand for
astina = Car()
Car.__init__(astina, "Mazda Astina", "Small", 2.5, 0)
```

So what's *really* happening under the hood is that the *function* `Car.__init__()` is being implicitly called with the first parameter automatically being assigned to the instance it's being called on.

### Methods

So why talk about "what's really happening under the hood"? Because it makes understand writing your own methods easier. Creating your own method, is almost identical to how we would create a function. Except, we need to include the *self* parameter first. So looking at our car example, let's clean up that `drive()` function we made earlier, and instead turn it into a *method* on the Car class.

```python
class Car:
    def __init__(self, name, size, engine_size, fuel):
        self.name = name
        self.size = size
        self.engine_size = engine_size
        self.fuel = fuel
    
    def drive(self):
        if self.fuel > 0:
            # Reduce the cars fuel by 5 but stop the car from having negative fuel
            self.fuel = max(0, self.fuel - 5)
            print(f"{self.name} is driving")
        else:
            print(f"{self.name} is stopped")
```

As you can see, the method is basically exactly the same. Instead of needing to pass the car as a parameter to the function, we instead use self. This means to drive a car we can now call:

```python
astina.drive()
```

And implicitly, under the hood python will actually call:

```python
Car.drive(astina)
```

From these two changes alone, we can cut down our file to be:

```python
class Car:
    def __init__(self, name, size, engine_size, fuel):
        self.name = name
        self.size = size
        self.engine_size = engine_size
        self.fuel = fuel
    
    def drive(self):
        if self.fuel > 0:
            # Reduce the cars fuel by 5 but stop the car from having negative fuel
            self.fuel = max(0, self.fuel - 5)
            print(f"{self.name} is driving")
        else:
            print(f"{self.name} is stopped")


astina = Car("Mazda Astina", "Small", 2.5, 0)
hilux = Car("Toyota Hilux", "Large", 2.8, 24)
corolla = Car("Toyota Corolla", "Medium", 1.8, 3)

astina.drive()
astina.drive()
print()

hilux.drive()
hilux.drive()
hilux.drive()
print()

corolla.drive()
corolla.drive()
corolla.drive()
```

Methods are a very powerful of interacting with classes. If we want to perform some complicated calulation on a class, we could create a method for it and hide all the messy details behind a very clean interface.

### Task

Create two classes called Game and Player. The Game class will contain information about specific games. The player class will contain information about players. This is how I want to be able to use your classes.

```python
# Name, Age rating, List of platforms the game is on
horror = Game("Resident Evil", 18, ["Xbox", "PC", "Playstation"])
racing = Game("Mario Kart", 6, ["Switch"])
shooter = Game("Doom", 15, ["PC", "Xbox", "Switch"])

# Name, Age, Preferred gaming platform
adult = Player("John Blue", 25, "Xbox")
child = Player("Timmy Green", 8, "Switch")

# Write a method on the Player class called: can_play(self, game).
# This method should return True only if the player is the same age or older than the rating
# and if their preferred platform is supported by the game.
```

Start with this:

```python
class Game:
    def __init__(self, name, age_rating, platforms):
        # Your code here
        pass

class Player:
    # Your code here
    pass


# You can use this for your own testing
horror = Game("Resident Evil", 18, ["Xbox", "PC", "Playstation"])
racing = Game("Mario Kart", 6, ["Switch"])
shooter = Game("Doom", 15, ["PC", "Xbox", "Switch"])

adult = Player("John Blue", 25, "Xbox")
child = Player("Timmy Green", 8, "Switch")

assert adult.can_play(horror)
assert not adult.can_play(racing)
assert adult.can_play(shooter)
assert not child.can_play(horror)
assert child.can_play(racing)
assert not child.can_play(shooter)
```

## Functions, and copies Part 2

Earlier I said that passing parameters to functions *copies* them, but not for all types. As a programmer it is important to know which types this applies for and why this is the case. Consider the following example.

```python
list_of_every_website_on_the_internet = [] # Imagine this is some HUGE list.
```

If we passed this list to a function, if it were to copy it, every time we call the function our performance would significantly Tank. That variable could be storing Gigabytes of information in memory. So Python, as an optimisation, will not copy lists. Instead, it will copy a reference to the list. What that means as programmers is that passing lists to functions means that functions can edit the list without our permission.

```python
def edit_list(a):
    a.append("haha")

foo = []
edit_list(foo)
print(foo)
```

```bash
['haha']
```

This counter-rule applies to basically anything other than the "primitive" types in Python:

- Integers
- Float
- Strings
- Boolean

Everything else is passed by reference (not copied):

- Lists
- Dictionaries
- Classes (instances)
- Basically anything else

### Task

Write a function that takes in an instance to the class "Grade" and checks to see if the student passed the assessment. If they did, assign the Grade to be passed.

```python
class Grade:
    def __init__(self, student):
        self.student = student
        self.result = None


def mark_student(grade, mark):
    # Your code here.
    # Mark is out of 100.
    # 0 - 49 is a "fail"
    # 50 - 64 is a "pass".
    # 65 - 74 is a "credit"
    # 75 - 84 is a "distinction"
    # 85 - 100 is a "high distinction"
    pass


# For testing
def test(student, mark, result):
    mark_student(student, mark)
    assert student.result == result

test(Grade("James"),   15, "fail")
test(Grade("Billy"),   51, "pass")
test(Grade("Matthew"), 65, "credit")
test(Grade("Tim"),     80, "distinction")
test(Grade("Bob"),     97, "high distinction")
```

## Modules

What we have learned thus far presents itself as a good foundation for working with code that other people have written. In many cases this will come in the form of a module. Whenever I think about modules there are three places they can come from, in order of complication. Built-in, personal, and external. Some built-in modules that are in Python we have already used like `sys`. But there are more, including but not limited to `os`, `csv`, and `math`. These are some of the common ones.

In this section we're going to go through modules where the details will be specific to the module you wish to access. But, the principles learnt in this section should apply to using the other modules.

One pitfill that I want to note early on though is what happens when you name a file badly. If you create a script called `csv.py`, you are effectly overwriting the built-in module called `csv.py` in the current directory and so need to be careful as to not import csv. This is why is may be a good idea to skim <https://docs.python.org/3/py-modindex.html> if you are truely experiencing a weird bug. Check to make sure you haven't named the file the same as a built-in module.

### Task: Built-in

First lets practice working with the built-in module `csv`. The module is all about reading and writing "Comma Separated Values" files. These are formatted like so:

```csv
Id,Name,Age,"Favourite Food"
1,James,18,Mango
3,Tim,40,Pasta
2,Ben,24,"Ice Cream"
```

Parsing these file manually can be quite tough, but with the csv module it is dirt simple... if you know how to do it. This is where our task comes in. Create a file called `details.csv` and copy the contents above to the file. Then, using the csv module print this out:

```bash
$ python csv_parser.py
Entry 1
    - Name: James
    - Age: 18
    - Favourite Food: Mango
Entry 3
    - Name: Tim
    - Age: 40
    - Favourite Food: Pasta
Entry 2
    - Name: Ben
    - Age: 24
    - Favourite Food: Ice Cream
```

Hint: <https://docs.python.org/3/library/csv.html#csv.DictReader>. Copying code can sometimes be a good idea!

### Personal

Think kind is not used as often, but can be handy to know. You can actually access code that you've written in other files very easily. The `import` keyword in python will look for the same name, and then you can import the contents of that file as a module. This is great if you have a file that contains a bunch of really helpful maths operations that you may want to reuse in multiple projects.

Assuming you completed the tasks above, let's access `game.py` to reuse the `Game` and `Player` classes we made earlier, but do so inside another file. First lets see how we would do that.

```python
import game

deep_rock = game.Game("Deep Rock Galatic", 16, ["PC", "Xbox"])
```

It's as simple as that. Since the name of the file is `game.py`, we access it with `import game` (Note: without the .py extension). As with other extensions we still need to use our dot notation to access the classes inside the module.

But sometimes we don't want to use dot notation. What if I instead want to just use `Game` directly. Well, luckily you can do that using:

```python
from game import Game, Player

james = Player("James", 20, ["Xbox"])
```

This way we only import the classes we want and we don't need to use the dot notation. You can do this for all kinds of modules, but I find myself using this more for when I know the contents of the module.

One thing to be careful of when doing this, is that importing a module actually also runs the code. So if you have a bunch of print statements in there, then as soon as you import the module in another file, those same print statements may be run. This is expected. You can get around this with a usual construct:

```python
if __name__ == "__main__":
    # Code in here will only be run if the file
    # was run directly. If it's imported, this
    # won't be run.
    pass
```

Feel free to read more but this is usually not required to be known. <https://realpython.com/if-name-main-python/>.

### External

This will definitely be different for whatever module you want to use. But typically online they will say something like:

"Run pip install module-name".

What this is saying to do is to open your terminal and type:

```bash
$ pip install module-name
```

Where you would replace "module-name" with whatever you want to install. This will install the module globally for your Python installation. So this step is only required once. Pip should have automatically installed when you installed Python. It is that simple to install. Using the module is exactly as we've done earlier. Either through `import` or with `from ___ import ___`.

My favourite external library is `requests`. You can install with `pip install requests` and then use the library with:

```python
import requests

res = request.get("www.google.com")
print(res.text)
```

The above accesses Google and prints out the source that your browser would know how to render and make pretty. Point is, it uses the module. How you want to use your module will depend entirely on the documentation for the module. Read it carefully.

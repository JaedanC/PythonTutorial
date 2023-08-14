---
sidebar_position: 1
slug: GettingStarted

---

# Getting Started

This tutorial will go over setting up your development environment.

## Installing Python

To get started with Python you will first need to install it. This can be done by going to the [official python website](https://www.python.org/) and downloading the latest version.

Run the installer that downloads.

- If it asks to install IDLE, uncheck it. It's rubbish.
- When you get to a page that mentions "installing to PATH" or something similar. Make sure this is checked.

To check if it's installed we will try to run it.

First, press the windows key and type "command prompt" (or "cmd" for short). That should open a new window. This is your *terminal* or *console*. Both terms are used interchangably. This is where you will run most python code from.

To see if python is installed type (without the `$`. The `$` will help me distinguish between terminal text and the output of a program later on):

```bash
$ python --version
```

Mine says this:

```bash
$ python --version
Python 3.10.8
```

Yours may be a different, more recent version. This is fine.

If instead you see:

```bash
$ python --version
'python' is not recognized as an internal or external command,
operable program or batch file.
```

Then reinstall python and make sure you enable the "install to path" setting. If you're sure you did, try restarting your computer and trying again.

## Installing an editor

The next step in becoming a coding pro is installing an editor. Code is just text, so technically you could use Notepad to write all code, and I've done that before when I'm truely feeling lazy. But 99% of the time programmers like to use an editors that were specifically designed for coding in. These editors will have pretty highlighting, code-completion suggestions, code-documentation, extensions and bunch of other cool features which we may touch later on.

I personally recommend installing "Visual Studio Code" (not to be confused with "Visual Studio"). Visual Studio Code can be downloaded from the [official website](https://code.visualstudio.com/). Install the latest version.

- Any setting to do with adding context menus is a personal preference. If you will be coding a lot, then this can be very useful. The context menus refer to right-clicking when in windows explorer. I have it turned because because I like the "Open with VSCode" button being there.

### Installing Extensions for VSCode

Open VSCode and go to the extensions tab on the left. (Can also be accessed with `Ctrl + Shift + X`). Search for "Python" and install the "Python" extension by Microsoft. At the time of writing this has 75 million downloads.

## Unhide file extensions

Before continuing follow these steps to unhide file extensions in Windows 10:

1. Open File Explorer.
2. Click on the View tab in the top menu.
3. Scroll down until you see the "File name extensions" option.
4. Check the box next to "File name extensions".

Why this is required is discussed at the end.

## Writing Code

Inside VSCode, go back to the Explorer tab on the left (`Ctrl + Shift + E`). Here you will see it ask you "Open Folder". Click on this, and navigate it to a place you would like to save your programs to. I like to keep all my coding projects inside a separate folder on my computer. You may want to set it up likewise.

After doing this, you can then edit the contents of this folder very easily using the explorer tab in VSCode. You can create new files, create new folders, rename files, move files etc.

## Running your first program

Python has two modes.

1. Interactive mode (also known as the interpreter).
2. Normal mode

Interactive mode is when you type just `python` in the terminal. This is not how we will be writing code. But, it can be useful to quickly dtry something out.

Normal mode is run with:

```bash
python some_file
```

This runs the file `some_file` with python. `some_file` is just a text file. It could be named anything. But by convention we also give the file the extension `.py`. This actually doesn't do anything, but it does let VSCode know to parse the text inside the file as Python, making it look colourful and pretty.

Start by creating a file called `hello_world.py` and copy this text inside the file.

```python
print("Hello, World!")
```

Make sure to save the file with `Ctrl + S`.

Then, we can open a terminal to the folder we have our code in with `Ctrl + ~` (The tilde button). This will open a new popup bar in VSCode that looks very similar to the "Command Prompt" terminal we opened earlier. They are effectively the same thing.

To run our new program type (again without the `$`):

```bash
$ python hello_world.py
```

This should output:

```bash
Hello, World!
```

Congratulations. You have just run your first python program.

## Tips

1. When inside the terminal you can press `Tab` to autocomplete the names of files for you.
2. Use `up` and `down` arrow keys while in the terminal to find and then re-run previous commands.
3. Don't forget to save the file every time you make a change. Make `Ctrl + S` a habit.
4. There are so many shortcuts in VSCode. I've been using it for years and I know only a few. [Shortcut list](https://code.visualstudio.com/shortcuts/keyboard-shortcuts-windows.pdf). What I've learnt over the years though is that if what you're trying to do it tedious, VSCode probably has a way to do it faster.

### Extra asides for the curious

Why do I need to make sure Python installs to the Path?

- In the terminal when I type `python`, what is actually happening under the hood is that windows is trying to find a program called "python.exe" to run. By default, windows will only search the current directly for "python.exe". But, what if "python.exe" is somewhere else? Well this is what the "Path" is for. The "Path" is a list of directories that windows will search in when you run a command to try and find that program. By installing Python to the "Path", we are saying, add the directory that we installed Python to the Path so that when I type `python` in the terminal, you know where to look.
- This lets us write our code wherever we want on our computer. I don't know why this isn't default but I digress.

Why do the files need to be given the .py extension?

- Actually they don't. In fact, all files on your computer don't need to have an extension at all. The extension doesn't change the contents of the file. What the extension does is tell windows or give windows the best guess on how to interpret the file. If you really wanted to, you could go and open a random file on your in Notepad even if it's not a `.txt` file. It won't be pretty, but it can be done.
- This fact open trips people up early on as they think that `.py` gives the file some sort of authority or specialness. No, all it does is let VSCode syntax highlight for you.
- We needed to unhide extensions in Windows 10 because by default it trys to stop you from able to change the extension when you rename a file. This is a good feature for most people. But for programmers, this can be a confusing feature to have enabled. The real name of a file includes the extension as well.
    - If you've ever created an excel spreadsheet, then you may not have known that this file has a `.xlsx` extension. Prior to unhiding the extensions, you may have an excel file on your computer called `report` but is now called `report.xlsx`. It was actually called `report.xlsx` all along, you just never saw the extension.
    - Even though you can see the truth now, it's still a good idea to not change the extension unless it's for the files you'll create while coding as it can still confuse Windows.

What is the Python interpreter?

- Python is unique programming language in that it is not a compiled language. What that means is that it will not try to make sure you write valid code before trying to run it. This is both a blessing and a curse. Other programming languages like C++ or Java are compiled. Meaning, if it isn't valid code it will refuse to compile at all and running it is impossible. This also means that the entire program must be written before trying to run it.
- Python is unique in that it just GOES as soon as it reads a line of code. The python interpreter is the most raw way of seeing this in action. You can pass the interpreter one line at a time of code and you could write an entire program that way. However I strongly recommend against this. I only ever use the interpreter to test simple arithmetic operations when I'm lazy.

Is this how all Python programs are run?

- No. When learning, this is how it is done. In real-day applications though, it is not uncommon to be running code from inside weird little development environments or boxes or in snippets. There are so many ways other applications may want to interface with Python. What is critical is that you understand the grass-roots basics so when these weird environments pop-up you can focus on working in them, not struggling with the Python language itself.

What about library "x" or package "y"? How do I learn "z"?

- Python has some great standard features, but much of the greatness comes from modules written by other talented developers. Using these is picked up later, but the underlying advice here is *learn how to teach yourself*. Your best reference will always be documentation and Google. Become familiar with Stack Overflow and other tutorial sites. The key to becoming a good programmer is being able to teach yourself.

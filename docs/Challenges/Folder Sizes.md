---
sidebar_position: 3
slug: FolderSizes
---

# Folder Sizes

:::note

Difficulty: ⭐⭐⭐⭐⭐

:::

Default windows does not have a feature to show the sizes of folders. To implement this ourselves we must recursively query the sizes of the files inside the directory to the get the size of the folder.

This program will also let the user traverse the file system and open file explorer to that location.

## Running the program

Imagine you have the file structure:

```txt
📂mystuff
  ┣ 📜size.py
  ┣ 📜data.csv
  ┗ 📂levels
    ┣ 📜first.txt
    ┗ 📜second.txt
```

This is what the execution of the program would be if the working directory was `mystuff`.

```bash
$ program size.py
```

```bash
.
[1] 📂  levels    (437000 kb)
[2] 📜  data.csv  (256 kb)
[3] 📜  size.py   (15 kb)
> help

[1-99]       File:      Prints the content of the file
             Directory: Opens the directory
..           Go up a directory. Do not go further up than
             the initial working directory.

open         Open the current directory in windows
open [1-99]  File:      Opens the file in windows
             Directory: Opens the directory in windows explorer

sort size    Sorts directories by size (default)
sort name    Sorts directories by name
help         Prints this message
exit         Closes the application

.
[1] 📂  levels    (437000 kb)
[2] 📜  data.csv  (256 kb)
[3] 📜  size.py   (15 kb)
> 0

./levels
[1] 📜  first.txt   (250000 kb)
[2] 📜  second.txt  (187000 kb)
> ..

.
[1] 📂  levels    (437000 kb)
[2] 📜  data.csv  (256 kb)
[3] 📜  size.py   (15 kb)
> open 1

```

At this point the `levels` folder should open in windows explorer.

```bash
.
[1] 📂  levels    (437000 kb)
[2] 📜  data.csv  (256 kb)
[3] 📜  size.py   (15 kb)
> open

```

At this point the `mystuff` folder should open in windows explorer.

```bash
.
[1] 📂  levels    (437000 kb)
[2] 📜  data.csv  (256 kb)
[3] 📜  size.py   (15 kb)
> sort name

.
[1] 📜  data.csv  (256 kb)
[2] 📂  levels    (437000 kb)
[3] 📜  size.py   (15 kb)
> exit

```

## OS functions

These are some functions that will be useful in this challenge:

- `os.walk()`
- `os.stat()`
- `os.startfile()`
- `os.path.abspath()`

Obtaining the sizes of directories requires you to recursively sum the size of the files and directories inside said directory.

Any other details are free to be interpreted. This program aims to challenge you to use a library not covered in the tutorials.

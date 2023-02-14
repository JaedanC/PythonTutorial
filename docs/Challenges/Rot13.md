---
sidebar_position: 1
---

# Rot13

:::note

Difficulty: ⭐

:::

This is a classic coding tasks where you will need to encode user input using rot13. This is simply "rotating" each letter through the alphabet 13 places.

## Encoding

Rot 13 converts like so:

```txt
From: abcdefghijklmnopqrstuvwxyz
To:   nopqrstuvwxyzabcdefghijklm
```

So when you run the program ask for input with `> ` and then continuously output the encoding of what they type.

## Example

```bash
$ python rot13.py
> Hello World
Uryyb Jbeyq
> This is encoded. But watch when I input Uryyb Jbeyq
Guvf vf rapbqrq. Ohg jngpu jura V vachg Hello World
> 
```

Close the program when the user presses CTRL+C, but don't crash the program.

## Details

Make sure that special characters are ignored. And make sure that captilisation is preserved in the output.

## Possible Solution

tab = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
test = 'pello WorlD'
test2=''
for i in range(len(test)):
    if test[i] not in tab:
        test2+=test[i]
    else:    
        tmp=test[i].lower()
        a=tab.index(tmp)+13
        if a>25:
            a-=25
        if test[i].isupper() :
            test2+=tab[a].upper()
        else:
            test2+=tab[a]

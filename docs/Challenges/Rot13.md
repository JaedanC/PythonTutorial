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

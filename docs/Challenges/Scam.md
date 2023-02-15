---
sidebar_position: 2
---

# Scam

:::note

Difficulty: ⭐⭐⭐

:::

This is a security question.

## The Game

Tim is trying to scam people of bitcoin on the internet. He is doing this by running a challenge. People have got to try and guess the answer to a question. If they don't guess correctly he wins.

> My favourite number is: _____ ?

Tim is going to scam people by having two answers to the question, and he'll reveal the real answer second.

To prove to people that he has the right answer, he first [hashes](https://en.wikipedia.org/wiki/Cryptographic_hash_function) his answer and posts it publically on the internet. Then, he allows the challenge to run for a week. Each person should try to guess the number, and then will hash their answer to see if they have the right answer.

## You are Tim

Your job is to find two answers to the question that share the same hash. Now, since we will use [MD5](https://www.geeksforgeeks.org/md5-hash-python/) to hash and finding duplicate hashes is very hard, treat the two hashes as a match if they have the same first 8 characters in the hash.

For example:

```txt
My favourite number is: 45 ?
```

```txt
o89v93bf98ajef0isheifjsei0iaejisf
```

And another answer

```txt
My favourite number is: 45726978346820 ?
```

```txt
o89v93bf9dw0ruwhyvet9c8wye9tv8nwe
```

- Notice how the first 12 characters are the same.
- Your solution to this question will then be 45 and 45726978346820.

The example above is not a real example. Your job is to find one. Use Python to find one. Consider using a [birthday attack](https://en.wikipedia.org/wiki/Birthday_attack) to try and find some matches.

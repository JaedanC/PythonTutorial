def solve_crossword(known):
    with open("words.txt", "r") as f:
        words = f.read().splitlines()

    possible_words = []
    for word in words:
        if len(word) != len(known):
            continue
        flag = True
        for i in range(len(word)):
            if known[i] != '?' and known[i] != word[i]:
                flag = False
                break
        if flag:
            possible_words.append(word)

    return possible_words

known = input("Enter the known letters for the word: ")
possible_words = solve_crossword(known)

print("Possible words:")
for word in possible_words:
    print(word)
import sys

word_file = sys.argv[1]
with open(word_file) as f:
    word_list = f.read().split("\n")

print("Please input your word by typing the known letters and '?' where you do not know the letter.")

def take_a_guess():
    guess = input(" > ").lower()

    for word in word_list:
        word = word.lower()

        if len(word) != len(guess):
            continue
        
        correct = 0
        for letter, guess_letter in zip(word, guess):
            if guess_letter == "?" or guess_letter == letter:
                correct += 1
        
        if correct == len(word):
            print(word)

try:
    while True:
        take_a_guess()
except KeyboardInterrupt:
    print()

import random

name = input("Enter name: ")

words = ['hangman', 'python' , 'zimbabwe']
word = random.choice(words)

print("Guess the the chracters")
guesses = ""
turns = 12

while turns > 0:
    failed = 0
    for char in word:
        if char in guesses:
            print(char)
        else:
            print("_")
            failed += 1
    if failed == 0:
        print("You win")
        print("The word is ", word)
        break

    guess = input("guess the characters: ")
    guesses += guess

    if guess not in word:
        turns -= 1
        print("wrong")
        print("You have ",turns, "left")

        if turns == 0:
            print("You lose!")
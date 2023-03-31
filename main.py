import time
name = input("Hello, what is your name?: ")
print(f"Hello, {name}. Time for you to play hangman!")
time.sleep(1)
print("Time to start guessing...")
time.sleep(0.6)

word = "aunmandumb"
guesses = ''
turns = 10
while turns > 0:
    wrong = 0
    for char in word:
        if char in guesses:
            print(char)
        else:
            print("_")
            wrong += 1
    if wrong == 0:
        print("You guessed the word!")
        break
    guess = input("Guess a letter: ")
    guesses += guess

    if guess not in word:
        turns -= 1
        print("wrong")
        print(f"You have {turns} more guesses remaining")
        if turns == 0:
            print("You lost")
            print("The word was " + word)
            print("Try again! Next time =)")
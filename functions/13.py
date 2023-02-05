import random
def func():
    print("Hello! What is your name?")
    name = input()
    print("Well, %s, I am thinking of a number between 1 and 20." % name)
    number = random.randint(1, 20)
    guess = None
    guess_count = 0

    while guess != number:
        print("Take a guess.")
        guess = int(input())
        guess_count += 1

        if guess < number:
            print("Your guess is too low.")
        elif guess > number:
            print("Your guess is too high.")

    print("Good job, %s! You guessed my number in %i guesses." % (name, guess_count))


func()
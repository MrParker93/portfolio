import sys
from functions import list_creator, choose_random_answer, give_hint

# Ensure the user inputs correct number of arguments
if len(sys.argv) != 2:
    print("Usage: python number_guessing.py [select difficulty: easy, moderate, hard, extreme]")
    sys.exit(1)

# Check which difficulty the user selected
if sys.argv[1].lower() == 'easy':

    # Create a list of positive numbers
    li = list_creator(10)

    # Randomly select a number as the answer from the list
    answer = choose_random_answer(li)

    # Number of guesses left
    guesses_left = 5

    # Loop until user is out of guesses
    while guesses_left > 0:

        if guesses_left == 1:
            print(f"You have {guesses_left} guess left")
        else:
            print(f"You have {guesses_left} guesses left.")

        guess = input("Guess a number between 0-9: ")

        if int(guess) > -1:
            try:
                if int(guess) == answer:
                    if guesses_left == 5:
                        print(f"Wow! You got it on your first guess!")
                        break
                    elif guesses_left == 4:
                        print(f"Congratulations! It took you {guesses_left - 2} guesses!")
                        break
                    elif guesses_left == 3:
                        print(f"Good job! You guessed correct in only {guesses_left - 1} guesses!")
                        break
                    elif guesses_left == 2:
                        print(f"Well done, you correctly guessed in {guesses_left + 1} guesses.")
                        break
                    elif guesses_left == 1:
                        print(f"Correct, it took you {guesses_left + 3} guesses.")
                        break
                else:
                    if guesses_left == 4:
                        give_hint(guesses_left, answer, li)
                    elif guesses_left == 3:
                        give_hint(guesses_left, answer, li)
                    elif guesses_left == 2:
                        give_hint(guesses_left, answer, li)

                guesses_left -= 1

                if guesses_left == 0:
                    print("Game over! You lose.")

            except ValueError as e:
                print(e)
                break
        else:
            print("Must enter a positive number.")

if sys.argv[1].lower() == 'moderate':

    li = list_creator(50)

    answer = choose_random_answer(li)

    guesses_left = 5

    while guesses_left > 0:

        if guesses_left == 1:
            print(f"You have {guesses_left} guess left")
        else:
            print(f"You have {guesses_left} guesses left.")

        guess = input("Guess a number between 0-49: ")

        if int(guess) > -1:
            try:
                if int(guess) == answer:
                    if guesses_left == 5:
                        print(f"Wow! You got it on your first guess!")
                        break
                    elif guesses_left == 4:
                        print(f"Congratulations! It took you {guesses_left - 2} guesses!")
                        break
                    elif guesses_left == 3:
                        print(f"Good job! You guessed correct in only {guesses_left - 1} guesses!")
                        break
                    elif guesses_left == 2:
                        print(f"Well done, you correctly guessed in {guesses_left + 1} guesses.")
                        break
                    elif guesses_left == 1:
                        print(f"Correct, it took you {guesses_left + 3} guesses.")
                        break
                else:
                    if guesses_left == 4:
                        give_hint(guesses_left, answer, li)
                    elif guesses_left == 3:
                        give_hint(guesses_left, answer, li)
                    elif guesses_left == 2:
                        give_hint(guesses_left, answer, li)

                guesses_left -= 1

                if guesses_left == 0:
                    print("Game over! You lose.")

            except ValueError as e:
                print(e)
                break
        else:
            print("Must enter a positive number.")

if sys.argv[1].lower() == 'hard':

    li = list_creator(100)

    answer = choose_random_answer(li)

    guesses_left = 5

    while guesses_left > 0:

        if guesses_left == 1:
            print(f"You have {guesses_left} guess left")
        else:
            print(f"You have {guesses_left} guesses left.")

        guess = input("Guess a number between 0-99: ")

        if int(guess) > -1:
            try:
                if int(guess) == answer:
                    if guesses_left == 5:
                        print(f"Wow! You got it on your first guess!")
                        break
                    elif guesses_left == 4:
                        print(f"Congratulations! It took you {guesses_left - 2} guesses!")
                        break
                    elif guesses_left == 3:
                        print(f"Good job! You guessed correct in only {guesses_left - 1} guesses!")
                        break
                    elif guesses_left == 2:
                        print(f"Well done, you correctly guessed in {guesses_left + 1} guesses.")
                        break
                    elif guesses_left == 1:
                        print(f"Correct, it took you {guesses_left + 3} guesses.")
                        break
                else:
                    if guesses_left == 4:
                        give_hint(guesses_left, answer, li)
                    elif guesses_left == 3:
                        give_hint(guesses_left, answer, li)
                    elif guesses_left == 2:
                        give_hint(guesses_left, answer, li)

                guesses_left -= 1

                if guesses_left == 0:
                    print("Game over! You lose.")

            except ValueError as e:
                print(e)
                break
        else:
            print("Must enter a positive number.")

if sys.argv[1].lower() == 'extreme':

    li = list_creator(1000)

    answer = choose_random_answer(li)

    guesses_left = 5

    while guesses_left > 0:

        if guesses_left == 1:
            print(f"You have {guesses_left} guess left")
        else:
            print(f"You have {guesses_left} guesses left.")

        guess = input("Guess a number between 0-999: ")

        if int(guess) > -1:
            try:
                if int(guess) == answer:
                    if guesses_left == 5:
                        print(f"Wow! You got it on your first guess!")
                        break
                    elif guesses_left == 4:
                        print(f"Congratulations! It took you {guesses_left - 2} guesses!")
                        break
                    elif guesses_left == 3:
                        print(f"Good job! You guessed correct in only {guesses_left - 1} guesses!")
                        break
                    elif guesses_left == 2:
                        print(f"Well done, you correctly guessed in {guesses_left + 1} guesses.")
                        break
                    elif guesses_left == 1:
                        print(f"Correct, it took you {guesses_left + 3} guesses.")
                        break
                else:
                    if guesses_left == 4:
                        give_hint(guesses_left, answer, li)
                    elif guesses_left == 3:
                        give_hint(guesses_left, answer, li)
                    elif guesses_left == 2:
                        give_hint(guesses_left, answer, li)

                guesses_left -= 1

                if guesses_left == 0:
                    print("Game over! You lose.")

            except ValueError as e:
                print(e)
                break
        else:
            print("Must enter a positive number.")
sys.exit()

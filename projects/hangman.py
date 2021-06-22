import random
import time
from man import HANGMAN_PICS

# Select the words used based on difficulty
easy = ["cat", "hello world", "giant", "paper", "today", "guess", "easy", "potato", "chew", "what"]
moderate = ["computer", "good day sir", "hangman", "moderate", "this is difficult", "wizard", "shoemaker"
            "tomorrow", "giraffe", "zookeeper"]
difficult = ["bookworm", "gossip", "awkward", "thumbscrew", "buzz", "funny buzzwords", "wavy", "voodoo",
             "joking", "psyche"]
extreme = ["jazz", "witchcraft", "whizzing", "grogginess", "zigzagging", "yachtsman", "razzmatazz", "espionage",
           "fluffiness", "triphthong"]

time.sleep(1)

# Present game
print("H A N G M A N")

time.sleep(1)

# Welcome user
name = input("What is your name?.. ")

# Show the user the range of difficulty
print(f"Hello {name}! Please select a difficulty: Easy, Moderate, Difficult, Extreme")

# Wait for 1 second
time.sleep(1)

# Prompt user to select difficulty
select_difficulty = input("Select difficulty: ").lower()


if select_difficulty == "easy":

    time.sleep(1)

    # Exciting message to the user
    print(f"Okay {name}! You've gone for the easy difficulty. Let's play Hangman!")

    time.sleep(0.5)

    # Tell user how the score system works
    print("Score 1 point per correct guess!")

    # Randomly select a word from easy list
    answer = random.choice(easy)

    # Hide the answer hangman style
    hidden_answer = len(answer) * "_"

    # Assign guesses and score to 0
    guesses = 0
    score = 0
    letters_guessed = ""

    while guesses != 10:

        # Check if user has guessed all the letters
        if "_" not in hidden_answer:

            # Congratulate user
            time.sleep(0.5)
            print(f"Amazing! You guessed the word!")
            print(f"Your final score is: {score}")
            print(f"The answer is: {answer}")
            break

        # Tell the user how many guesses they have left
        if guesses == 9:
            print(f"You have {10 - guesses} guess left")

            # Print the hidden answer and prompt user to guess a letter
            print(hidden_answer)

        else:
            print(f"You have {10 - guesses} guesses left.")

            # Print the hidden answer and prompt user to guess a letter
            print(hidden_answer)

        time.sleep(0.5)

        # Prompt user to guess
        guess = input("Guess a letter or a word: ")

        # Ensure user enters a letter
        if not guess:
            print("Enter a letter.")

        # Ensure user enters only letters
        elif not guess.isalpha():
            print("Only enter letters.")

        # Check if user guesses the entire word
        if guess == answer:

            # Congratulate user
            if guesses == 0:
                score += 5
                time.sleep(0.5)
                print(f"Amazing! You guessed the word in {guesses + 1} guess!")
                print(f"Your final score is: {score}!")
                print(f"The answer is: {answer}")
                break
            else:
                score += 5
                time.sleep(0.5)
                print(f"Amazing! You guessed the word in {guesses + 1} guesses!")
                print(f"Your final score is: {score}!")
                print(f"The answer is: {answer}")
                break

        # Check if the letter is in answer
        elif guess in answer:

            # Iterate over each letter in answer
            for letter in range(len(answer)):

                # Check if current letter is same as guess
                if guess == answer[letter]:

                    # Update hidden answer with letter
                    hidden_answer = hidden_answer[:letter] + guess + hidden_answer[letter + 1:]

            print("Nice guess!")

            time.sleep(0.5)

            # Add 1 point to the score
            score += 1

            # Display current score
            print(f"Current score: {score}")

            time.sleep(0.5)

        # If user guesses wrong
        elif guess not in answer:
            time.sleep(0.5)

            if guesses + 1 != 10:

                # Add incorrect guess to letters guessed
                letters_guessed += guess + " "

                print(f"Try again! Letters used: {letters_guessed}")

            time.sleep(0.5)

            # Display hangman
            print(HANGMAN_PICS[guesses])

            # Increment guesses made
            guesses += 1

            # If user loses game
            if guesses == 10:
                time.sleep(1)
                print("Game over!")

if select_difficulty == "moderate":

    time.sleep(1)

    # Exciting message to the user
    print(f"Okay {name}! You've gone for the moderate difficulty. Let's play Hangman!")

    time.sleep(0.5)

    # Tell user how the score system works
    print("Score 1 point per correct guess!")

    # Randomly select a word from easy list
    answer = random.choice(moderate)

    # Hide the answer hangman style
    hidden_answer = len(answer) * "_"

    # Assign guesses and score to 0
    guesses = 0
    score = 0
    letters_guessed = ""

    while guesses != 10:

        # Check if user has guessed all the letters
        if "_" not in hidden_answer:
            # Congratulate user
            time.sleep(0.5)
            print(f"Amazing! You guessed the word!")
            print(f"Your final score is: {score}!")
            print(f"The answer is: {answer}")
            break

        # Tell the user how many guesses they have left
        if guesses == 9:
            print(f"You have {10 - guesses} guess left")

            # Print the hidden answer and prompt user to guess a letter
            print(hidden_answer)
        else:
            print(f"You have {10 - guesses} guesses left.")

            # Print the hidden answer and prompt user to guess a letter
            print(hidden_answer)

        time.sleep(0.5)

        # Prompt user to guess
        guess = input("Guess a letter or a word: ")

        # Ensure user enters a letter
        if not guess:
            print("Enter a letter.")

        # Ensure user enters only letters
        elif not guess.isalpha():
            print("Only enter letters.")

        # Check if user guesses the entire word
        if guess == answer:

            # Congratulate user
            if guesses == 0:
                score += 5
                time.sleep(0.5)
                print(f"Amazing! You guessed the word in {guesses + 1} guess!")
                print(f"Your final score is: {score}!")
                print(f"The answer is: {answer}")
                break
            else:
                score += 5
                time.sleep(0.5)
                print(f"Amazing! You guessed the word in {guesses + 1} guesses!")
                print(f"Your final score is: {score}!")
                print(f"The answer is: {answer}")
                break

        # Check if the letter is in answer
        elif guess in answer:

            # Iterate over each letter in answer
            for letter in range(len(answer)):

                # Check if current letter is same as guess
                if guess == answer[letter]:

                    # Update hidden answer with letter
                    hidden_answer = hidden_answer[:letter] + guess + hidden_answer[letter + 1:]

            print("Nice guess!")

            time.sleep(0.5)

            # Add 1 point to the score
            score += 1

            # Display current score
            print(f"Current score: {score}")

        # If user guesses wrong
        elif guess not in answer:
            time.sleep(0.5)

            if guesses + 1 != 10:

                # Add incorrect guess to letters guessed
                letters_guessed += guess + " "

                print(f"Try again! Letters used: {letters_guessed}")

            time.sleep(0.5)

            # Display hangman
            print(HANGMAN_PICS[guesses])

            # Increment guesses made
            guesses += 1

            # If user loses game
            if guesses == 10:
                time.sleep(1)
                print("Game over!")

if select_difficulty == "difficult":

    time.sleep(1)

    # Exciting message to the user
    print(f"Okay {name}! You've gone for the difficult difficulty. Let's play Hangman!")

    time.sleep(0.5)

    # Tell user how the score system works
    print("Score 2 point per correct guess! Lose 1 point per incorrect guess!")

    # Randomly select a word from easy list
    answer = random.choice(difficult)

    # Hide the answer hangman style
    hidden_answer = len(answer) * "_"

    # Assign guesses and score to 0
    guesses = 0
    score = 0
    letters_guessed = ""

    while guesses != 10:

        # Check if user has guessed all the letters
        if "_" not in hidden_answer:
            # Congratulate user
            time.sleep(0.5)
            print(f"Amazing! You guessed the word!")
            print(f"Your final score is: {score}")
            print(f"The answer is: {answer}")
            break

        # Tell the user how many guesses they have left
        if guesses == 9:
            print(f"You have {10 - guesses} guess left")

            # Print the hidden answer and prompt user to guess a letter
            print(hidden_answer)
        else:
            print(f"You have {10 - guesses} guesses left.")

            # Print the hidden answer and prompt user to guess a letter
            print(hidden_answer)

        time.sleep(0.5)

        # Prompt user to guess
        guess = input("Guess a letter or a word: ")

        # Ensure user enters a letter
        if not guess:
            print("Enter a letter.")

        # Ensure user enters only letters
        elif not guess.isalpha():
            print("Only enter letters.")

        # Check if user guesses the entire word
        if guess == answer:

            # Congratulate user
            if guesses == 0:
                score += 5
                time.sleep(0.5)
                print(f"Amazing! You guessed the word in {guesses + 1} guess!")
                print(f"Your final score is: {score}!")
                print(f"The answer is: {answer}")
                break
            else:
                score += 5
                time.sleep(0.5)
                print(f"Amazing! You guessed the word in {guesses + 1} guesses!")
                print(f"Your final score is: {score}!")
                print(f"The answer is: {answer}")
                break

        # Check if the letter is in answer
        elif guess in answer:

            # Iterate over each letter in answer
            for letter in range(len(answer)):

                # Check if current letter is same as guess
                if guess == answer[letter]:

                    # Update hidden answer with letter
                    hidden_answer = hidden_answer[:letter] + guess + hidden_answer[letter + 1:]

            print("Nice guess!")

            time.sleep(0.5)

            # Add 1 point to the score
            score += 2

            # Display current score
            print(f"Current score: {score}")

            time.sleep(0.5)

            print(hidden_answer)

        # If user guesses wrong
        elif guess not in answer:
            time.sleep(0.5)

            if guesses + 1 != 10:

                # Add incorrect guess to letters guessed
                letters_guessed += guess + " "

                print(f"Try again! Letters used: {letters_guessed}")

            # Check if score is 0
            if score >= 0:
                # Take one point from score
                score -= 1

            time.sleep(0.5)

            # Display hangman
            print(HANGMAN_PICS[guesses])

            # Increment guesses made
            guesses += 1

            # If user loses game
            if guesses == 10:
                time.sleep(1)
                print("Game over!")

if select_difficulty == "extreme":

    time.sleep(1)

    # Exciting message to the user
    print(f"Okay {name}! You've gone for the extreme difficulty. Let's play Hangman!")

    time.sleep(0.5)

    # Tell user how the score system works
    print("Score 1 point per correct guess! Lose 1 point per incorrect guess!")

    # Randomly select a word from easy list
    answer = random.choice(extreme)

    # Hide the answer hangman style
    hidden_answer = len(answer) * "_"

    # Assign guesses and score to 0
    guesses = 0
    score = 0
    letters_guessed = ""

    while guesses != 10:

        # Check if user has guessed all the letters
        if "_" not in hidden_answer:

            # Congratulate user
            time.sleep(0.5)
            print(f"Amazing! You guessed the word!")
            print(f"Your final score is: {score}")
            print(f"The answer is: {answer}")
            break

        # Tell the user how many guesses they have left
        if guesses == 9:
            print(f"You have {10 - guesses} guess left")

            # Print the hidden answer and prompt user to guess a letter
            print(hidden_answer)

        else:
            print(f"You have {10 - guesses} guesses left.")

            # Print the hidden answer and prompt user to guess a letter
            print(hidden_answer)

        time.sleep(0.5)

        # Prompt user to guess
        guess = input("Guess a letter or a word: ")

        # Ensure user enters a letter
        if not guess:
            print("Enter a letter.")

        # Ensure user enters only letters
        elif not guess.isalpha():
            print("Only enter letters.")

        # Check if user guesses the entire word
        elif guess == answer:

            # Congratulate user
            if guesses == 0:
                score += 5
                time.sleep(0.5)
                print(f"Amazing! You guessed the word in {guesses + 1} guess!")
                print(f"Your final score is: {score}!")
                print(f"The answer is: {answer}")
                break
            else:
                score += 5
                time.sleep(0.5)
                print(f"Amazing! You guessed the word in {guesses + 1} guesses!")
                print(f"Your final score is: {score}!")
                print(f"The answer is: {answer}")
                break

        # Check if the letter is in answer
        elif guess in answer:

            # Iterate over each letter in answer
            for letter in range(len(answer)):

                # Check if current letter is same as guess
                if guess == answer[letter]:

                    # Update hidden answer with letter
                    hidden_answer = hidden_answer[:letter] + guess + hidden_answer[letter + 1:]

            print("Nice guess!")

            time.sleep(0.5)

            # Add 1 point to the score
            score += 2

            # Display current score
            print(f"Current score: {score}")

        # If user guesses wrong
        elif guess not in answer:
            time.sleep(0.5)

            if guesses + 1 != 10:

                # Add incorrect guess to letters guessed
                letters_guessed += guess + " "

                print(f"Try again! Letters used: {letters_guessed}")

            # Check if score is 0
            if score >= 0:
                # Take one point from score
                score -= 1

            time.sleep(0.5)

            # Display hangman
            print(HANGMAN_PICS[guesses])

            # Increment guesses made
            guesses += 1

            # If user loses game
            if guesses == 10:
                time.sleep(1)
                print("Game over!")

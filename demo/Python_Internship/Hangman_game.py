
import random


def hangman():
    # Step 1: Predefined list of words
    words = ["python", "computer", "program", "hangman", "science"]

    # Step 2: Randomly choose a word from the list
    word = random.choice(words)
    word_letters = list(word)  # Convert word into list of letters
    guessed = ["_"] * len(word)  # Hidden version for display
    attempts = 6  # Limit of incorrect guesses
    used_letters = []  # To keep track of letters already guessed

    print("🎯 Welcome to Hangman Game!")
    print("You have 6 incorrect guesses allowed.")
    print("Word to guess: ", " ".join(guessed))

    # Step 3: Main game loop
    while attempts > 0 and "_" in guessed:
        guess = input("\nEnter a letter: ").lower()

        # Step 4: Validate input
        if not guess.isalpha() or len(guess) != 1:
            print("⚠ Please enter a single valid alphabet letter.")
            continue

        # Step 5: Check if letter was already guessed
        if guess in used_letters:
            print("❗ You already guessed that letter. Try another one.")
            continue

        used_letters.append(guess)

        # Step 6: Check if guess is correct
        if guess in word_letters:
            print("✅ Good job! Letter found.")
            for i in range(len(word_letters)):
                if word_letters[i] == guess:
                    guessed[i] = guess
        else:
            attempts -= 1
            print(f"❌ Wrong guess! Attempts left: {attempts}")

        print("Word: ", " ".join(guessed))
        print("Used letters:", ", ".join(used_letters))

    # Step 7: End of game
    if "_" not in guessed:
        print("\n🎉 Congratulations! You guessed the word:", word)
    else:
        print("\n💀 Game Over! The correct word was:", word)


# Run the game
hangman()

"""
import random


def hangman():
    words = ["apple", "banana", "grape", "orange", "mango"]
    word = random.choice(words)
    guessed_letters = []
    incorrect_guesses = 0
    max_incorrect = 6

    print("Welcome to Hangman!")
    print("Guess the word one letter at a time.")
    print(f"You have {max_incorrect} incorrect guesses allowed.
          ")

    while incorrect_guesses < max_incorrect:
        display_word = ""
        for letter in word:
            if letter in guessed_letters:
                display_word += letter + " "
            else:
                display_word += "_ "
        print("Word: ", display_word.strip())

        guess = input("Enter a letter: ").lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single alphabetic character.
                  ")
            continue

        if guess in guessed_letters:
            print("You already guessed that letter. Try again.
                  ")
            continue

        guessed_letters.append(guess)

        if guess in word:
            print("Good guess!
                  ")
            else:
            incorrect_guesses += 1
            print(f"Wrong guess! You have {max_incorrect - incorrect_guesses} guesses left.
                  ")

            if all(letter in guessed_letters for letter in word):
                print(f"Congratulations! You guessed the word: {word}")
            break
    else:
        print(f"Sorry, you ran out of guesses. The word was: {word}")


if _name_ == "_main_":
    hangman()
"""
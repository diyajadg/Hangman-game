import random

def display_hangman(tries):
    stages = [
        '''
           ------
           |    |
                |
                |
                |
                |
        =========''',
        '''
           ------
           |    |
           O    |
                |
                |
                |
        =========''',
        '''
           ------
           |    |
           O    |
           |    |
                |
                |
        =========''',
        '''
           ------
           |    |
           O    |
          /|    |
                |
                |
        =========''',
        '''
           ------
           |    |
           O    |
          /|\\   |
                |
                |
        =========''',
        '''
           ------
           |    |
           O    |
          /|\\   |
          /     |
                |
        =========''',
        '''
           ------
           |    |
           O    |
          /|\\   |
          / \\   |
                |
        ========='''
    ]
    return stages[tries]

def hangman():
    word_list = ["PYTHON", "JAVA", "JAVASCRIPT", "HTML", "CSS"]
    word = random.choice(word_list).upper()
    word_set = set(word)
    guessed_letters = set()
    incorrect_guesses = 0
    max_incorrect_guesses = 6

    print("Welcome to Hangman!")
    print(display_hangman(incorrect_guesses))
    print("Word to guess:", "_ " * len(word))
    print("\n")

    while incorrect_guesses < max_incorrect_guesses:
        guess = input("Guess a letter: ").upper()

        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single letter.")
            continue

        if guess in guessed_letters:
            print(f"You've already guessed '{guess}'. Try again.")
            continue

        guessed_letters.add(guess)

        if guess in word_set:
            print(f"Good guess! '{guess}' is in the word.")
        else:
            incorrect_guesses += 1
            print(f"Oops! '{guess}' is not in the word.")
        
        word_display = [letter if letter in guessed_letters else "_ " for letter in word]
        print("Word to guess:", "".join(word_display))
        print(display_hangman(incorrect_guesses))
        print("\n")

        if set(word_display) == word_set:
            print("Congratulations! You've guessed the word correctly.")
            break
    else:
        print(f"Game over! The word was '{word}'.")

if __name__ == "__main__":
    hangman()

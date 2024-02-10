import random

def choose_word():
    words = ["apple", "banana", "orange", "grape", "strawberry", "melon", "pineapple"]
    return random.choice(words)

def display_word(word, guessed_letters):
    displayed_word = ""
    for letter in word:
        if letter in guessed_letters:
            displayed_word += letter
        else:
            displayed_word += "_"
    return displayed_word

def hangman():
    word_to_guess = choose_word()
    guessed_letters = []
    attempts = 6

    print("Welcome to Hangman!")
    print("The word has {} letters.".format(len(word_to_guess)))

    while True:
        print("\nWord: ", display_word(word_to_guess, guessed_letters))
        print("Guessed letters: ", guessed_letters)
        guess = input("Guess a letter: ").lower()

        if guess in guessed_letters:
            print("You've already guessed that letter!")
            continue

        guessed_letters.append(guess)

        if guess not in word_to_guess:
            attempts -= 1
            print("Incorrect guess! You have {} attempts left.".format(attempts))
            if attempts == 0:
                print("Sorry, you ran out of attempts! The word was '{}'.".format(word_to_guess))
                break
        else:
            print("Correct guess!")

        if all(letter in guessed_letters for letter in word_to_guess):
            print("Congratulations, you've guessed the word '{}'!".format(word_to_guess))
            break

if __name__ == "__main__":
    hangman()
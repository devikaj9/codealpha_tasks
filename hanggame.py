
import random


word_bank = [
    "laptop",
    "college",
    "student",
    "python",
    "coding",
    "network",
    "website",
    "mobile",
    "project",
    "algorithm"
]


secret_word = random.choice(word_bank)


letters_found = []
wrong_guesses = 0
max_wrong_guesses = 7

print("\n----------------------------------")
print("          HANGMAN GAME")
print("----------------------------------")
print("Try to find the hidden word!")
print("You can make", max_wrong_guesses, "wrong guesses.\n")


hidden_word = ["-"] * len(secret_word)

while wrong_guesses < max_wrong_guesses and "-" in hidden_word:

    print("Current word:", " ".join(hidden_word))
    print("Wrong guesses:", wrong_guesses, "/", max_wrong_guesses)

    if letters_found:
        print("Letters tried:", ", ".join(letters_found))

    user_letter = input("Enter a letter: ").lower().strip()

    
    if len(user_letter) != 1 or not user_letter.isalpha():
        print("Please enter exactly one letter.\n")
        continue

    
    if user_letter in letters_found:
        print("You have already tried that letter.\n")
        continue

    
    letters_found.append(user_letter)

    
    if user_letter in secret_word:

        print("Good job! That letter is in the word.\n")

        for position in range(len(secret_word)):
            if secret_word[position] == user_letter:
                hidden_word[position] = user_letter

    else:

        wrong_guesses += 1
        print("That letter is not in the word.\n")



if "-" not in hidden_word:

    print("----------------------------------")
    print("       YOU WON THE GAME!")
    print("----------------------------------")
    print("The hidden word was:", secret_word)
    print("You made", wrong_guesses, "wrong guesses.")

else:

    print("----------------------------------")
    print("          GAME OVER")
    print("----------------------------------")
    print("The hidden word was:", secret_word)
    print("Better luck next time!")

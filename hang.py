import random
from hangmanwords import word_list
from hangmanart import hang



# Randomly select a word from the word_list
chosen_word = random.choice(word_list)

# Print the chosen word (for debugging purposes)
# print(chosen_word)

# 2. Initialize the placeholder as an empty string
placeholder = ""

play = True

p = int(input("Press 1 to Play and 2 to Close: "))
if p == 2:
    print("Thanks for Playing")
    play = False
elif p == 1:
    play = True
else:
    play = False

while play == True:

    # 3. Convert the chosen word into a list of characters for easier manipulation
    chosen_word = list(chosen_word)
    blank = len(chosen_word)  # Get the length of the chosen word

    # Initialize the placeholder with underscores, one for each letter in the chosen word
    # placeholder = "_" * blank
    # placeholder = list(placeholder)  # Convert the string of underscores into a list

    for i in range(blank):
        placeholder += "_"

    print(placeholder)
    placeholder = list(placeholder)





    # Prompt the user to guess a letter and convert it to lowercase
    guess = input("Guess a letter: ")
    guess = guess.lower()


    # Validate user input to ensure it's not a digit
    while guess.isdigit():
        print("Please enter a letter")  # Prompt for valid input
        guess = input("Guess a letter:\n")  # Ask for input again
        guess = guess.lower()  # Convert to lowercase



    over = 0
    dead = 0
    while over <= 6:
        # Loop through each letter in the chosen word using its index
        for index, word in enumerate(chosen_word):
            if guess == word:  # Check if the guessed letter matches the current letter
                # Replace the underscore in the placeholder with the guessed letter
                # placeholder.pop(index)
                # placeholder.insert(index ,guess)
                placeholder[index] = guess



        if guess not in chosen_word:
            over += 1
            dead += 1
            if over == 6:
                print("***************YOU DIED***********************")
                over = 8
                print(chosen_word)

        hangman = hang[dead]
        print(hangman)



        # Convert the placeholder list back to a string for display
        placeholder = "".join(placeholder)  # Join the list into a single string
        print(placeholder)  # Print the current state of the guessed word
        placeholder = list(placeholder)
        if "_" in placeholder and over <= 6:
            guess = input("Guess a letter: ")
            guess = guess.lower()

        if guess in placeholder:
            print("you have already entered this letter before")

        if "_" not in placeholder:
            print("*******************YOU WIN***********************")
            over = 8
    p = int(input("Press 1 to Play and 2 to Close: "))
    if p == 2:
        print("Thanks for Playing")
        play = False
    elif p == 1:
        play = True


print("GAME OVER")


🎮 Hangman Game (Python CLI)
A simple Hangman game implemented in Python. This game randomly selects a word from a predefined list and prompts the user to guess letters. The user has 6 attempts to guess the word before they lose.

✨ Features
🧩 Random word selection from a predefined list

🔤 User input for guessing letters

🏴‍☠️ Hangman art display that increases with each incorrect guess

🎯 Win condition when the user guesses all letters correctly

💀 Game over after 6 incorrect guesses

🧰 How It Works
The game prompts the user to press 1 to start playing or 2 to quit.

The computer randomly selects a word from the word_list.

The user must guess the word one letter at a time.

The game provides feedback:

If the guess is correct, the word is updated.

If the guess is incorrect, a "hangman" drawing is updated.

The game ends when:

The user guesses the word correctly (win).

The user accumulates 6 incorrect guesses (lose).

📦 Requirements
Python 3.6+

hangmanwords.py and hangmanart.py files (these contain the word list and the hangman drawings)

🚀 How to Run
Clone or download the repo to your computer.

Ensure you have Python 3.x installed.

Run the game with the following command:

python hangman.py
🧠 Sample Gameplay
Press 1 to Play and 2 to Close: 1
________
Guess a letter: a
____a___
    +---+
    |   |
        |
        |
        |
        |
  =======

Guess a letter: e
e___e___
    +---+
    |   |
        |
        |
        |
        |
  =======
...

Press 1 to Play and 2 to Close: 2
Thanks for Playing
💡 Possible Enhancements
Add difficulty levels with longer or more complex words.

Implement a timer to add a time-based challenge.

Include a score system to track the number of games played and won.

# HangMan-Game
# **Hangman Game**

This is a Python implementation of the classic **Hangman** game. Test your vocabulary and guessing skills by attempting to reveal a hidden word, one letter at a time, before you run out of lives.

---

## **Features**
1. 🎲 **Random Word Selection**: A random word is chosen from a predefined list in each game.
2. 📝 **Progress Tracking**: Displays the word with correctly guessed letters filled in.
3. ❌ **Life Deduction**: Lose a life for each incorrect guess.
4. 🚫 **Duplicate Prevention**: Alerts players if they attempt to guess the same letter again.
5. 🏆 **Win/Lose Messages**: Clear feedback when the game concludes.

---

## **Files Included**
1. **`hangman_words.py`**  
   Contains the `word_list` variable with a list of possible words.
   
2. **`hangman_art.py`**  
   Provides ASCII art for each stage of the hangman, enhancing the gameplay experience.
   
3. **`main.py`**  
   Implements the core game logic, including input handling, word checking, and displaying the hangman.

---

## **Game Rules**
1. 🎮 The player starts with **6 lives**.
2. 🖋️ A random word is selected, and the player must guess its letters.
3. ✅ Correct guesses reveal the positions of the guessed letter in the word.
4. ❌ Incorrect guesses reduce the player’s remaining lives by one.
5. 🕹️ The game ends when:
   - The player successfully guesses the entire word (**Win**).
   - The player runs out of lives (**Lose**).

---

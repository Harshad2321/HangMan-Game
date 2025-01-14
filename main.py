import random,hangman_words,hangman_art
lives = 6
chosen_word = random.choice(hangman_words.word_list)
print(chosen_word)             #This is for the referrence that which word is being selected.You can remove it when implementing the game.
placeholder = ""
word_length = len(chosen_word)
for position in range(word_length):
    placeholder += "_"
print("Word to guess: " + placeholder)
game_over = False
correct_letters = []
while not game_over:
    print(f"****************************{lives}/6 LIVES LEFT****************************")
    guess = input("Guess a letter: ").lower()
    if guess == correct_letters:
        print(f"You have already guessed {guess}>")
    display = ""
    for letter in chosen_word:
        if letter == guess:
            display += letter
            correct_letters.append(guess)
        elif letter in correct_letters:
            display += letter
        else:
            display += "_"
    print("Word to guess: " + display)
    if guess not in chosen_word:
        lives -= 1
        print(f"The letter you typed is incorrect{guess}.You loose a life.")
        if lives == 0:
            game_over = True
            print(f"***********************You Lose!!!The word was{guess}**********************")
    if "_" not in display:
        game_over = True
        print("****************************YOU WIN****************************")
    print(hangman_art.stages[lives])

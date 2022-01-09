hangmanGame

Requirements: 
- Player has 7 lives
- Script must ONLY stop to either ask for guesses, or because the game has been won/lost
- Asking the user to make their next guess must use the following text (case sensitive and a space after the colon
are necessary): Please enter your next guess: 
- The text printed before Please enter your next guess:  must END in the word to be guessed
with the unknown letters starred out 
The string must not contain any other stars.
- The program must print either 'congratulations you win' or 'you lose' on exit (not case sensitive).
- When a game is played, a word must be picked randomly (from a uniform distribution) from the word_list.txt file.
- The word_list.txt file must be stored in the same path as your code and when you load the file don't include the path 
(i.e. "open('word_list.txt', ...)").

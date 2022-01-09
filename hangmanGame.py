import random
import sys 

hangman_pics = ["", "O", "O-", "O--", "O|--]", " O|--<", " Almost Dead! O|--<", "YOU ARE DEAD"]

#Class to define player with attribute of no. of lives.
#Used OOP in the interest of practice, and encapsulation. 

class Lives:

	def __init__(self, strikes = 7, correct = 0):
		self.strikes = strikes
		self.correct = correct 

	def show_lives(self):
		print('You have {} lives remaing'.format(self.strikes))

	def lose_life(self):
		self.strikes -= 1

	def reset_life(self):
		self.strikes = 7

#Function Definitions 
def intro():
	print('Welcome to Hangman.\nTo win, you must guess the letters in a secret word.')
	print("But be careful, you only have seven guesses before you will be hanged till death!")

def get_random_word():

	words_list = []
	my_file = open('word_list.txt', 'r')

	with my_file:
		
		for line in my_file:
			words_list.append(line.rstrip())

		random_word = random.choice(words_list)
	return random_word


def display_word(secret_word, guessed_letters):

	word_to_display = ""


	for letter in secret_word:
		if letter in guessed_letters:
			word_to_display += " " + letter + " "

		else:
			word_to_display += " *"

	return word_to_display

def game_board(hangman_pics, guessed_letters, secret_word, player):
	
	word_to_display = ""

	print('Your hangman so far is: {}'.format(hangman_pics[7 - player.strikes]))

	print('You have guessed correctly {} times'.format(player.correct))
	print('You have guessed incorrectly {} times'.format(7 - player.strikes))
	player.show_lives()

	print('this is your word so far {}'.format(display_word(secret_word, guessed_letters)))


def player_guess(player, secret_word, incorrect_guesses, correct_guesses, guessed_letters):

		letter_guess = input(' Please enter your next guess:').lower()

		if letter_guess.isalpha() == False :
			letter_guess = input(' No special characters allowed.  Please enter your next guess:')

		
		elif letter_guess not in guessed_letters :
			guessed_letters.append(letter_guess)

			if letter_guess not in secret_word:
				print(' That is incorrect!')
				player.lose_life()
				

			else :
				print(' That is correct!')
				player.correct += 1

		else:
			print("You've already guessed the letter {} , please choose another." .format(letter_guess))


def win_lose_check(player, secret_word, guessed_letters):

	current_word = display_word(secret_word, guessed_letters)

	if player.strikes == 0:
		print('You lose')
		print('Your secret word was: {}'.format(secret_word))
	
		
	if "*" not in current_word:
		print('Congratulations you win')
		print('Your full word is: {}'.format(display_word(secret_word, guessed_letters)))
		player.strikes = 0

		

def play_again():
	pass

def play_hangman():

	#Game
	
	#Instanciate Player and Stats

	player = Lives()
	incorrect_guesses = 0
	correct_guesses = 0
	guessed_letters = []

	#Intro 
	intro()
	player.show_lives()

	#Get Secret Word
	secret_word = get_random_word()

	while player.strikes > 0:

		#Show Game Board
		game_board(hangman_pics, guessed_letters, secret_word, player)

		#Player Guess
		player_guess(player, secret_word, incorrect_guesses, correct_guesses, guessed_letters)

		#Win or Lose Check 
		win_lose_check(player, secret_word, guessed_letters)
		

play_hangman()



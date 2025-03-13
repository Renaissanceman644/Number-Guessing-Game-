# prompt the user 
# randomly generate the no.
# set the counter for guesses
# loop

import random

lowest_num = 0
highest_num = 100

answer = random.randint(lowest_num, highest_num)

guesses = 0
print("Welcome To The Number Guessing Game. ")

is_running = True

while is_running:
		guess = input(f"Select a no. between {lowest_num} and {highest_num}. ")
		if guess.isdigit():
			guess = int(guess)
			guesses += 1
			if guess < lowest_num or guess > highest_num:
				print("Out of range. ") 
			elif guess < answer :
				print("Too low. ")
			elif guess > answer:
				print("Too high. ")
			else:
				print(f"Congratulations. The no. is {answer} !")
				print(f"Total no. of guesses is {guesses}. ")
				is_running = False
		else:
			print("Invalid Choice. ")
		
#import random functionality
import random
#generate a random integer between 1 and 100 and define a variable
random_number = random.randint(1,101)

print "Hello, what is your name?" 
name = raw_input()
print "Hello, %r. I'm thinking of a number between 1 and 100." % name
print "Try to guess my number in 9 tries or less."

guess = 0
count = 1


while True:
	if count <= 9:
		guess = int(raw_input("Your guess?  "))
		if guess < random_number:
			print "Your guess is too low. Guess higher."
			count += 1
		elif guess > random_number:
			print "Your guess is too high. Guess lower."
			count += 1
		else:
			print "Your guess is correct. You win! You guessed my number in %d tries." % count
			break
	else:
		print "You have guessed 9 times and didn't guess my number.  You lose."
		break



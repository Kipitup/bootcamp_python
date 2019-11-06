import random

print("This is an interactive guessing game!\nYou have to enter a number between 1 and 99 to find out the secret number.\nType 'exit' to end the game.\nGood luck!");
secret_nb = random.randint(0,100);
print(secret_nb);
attempts = 1;

while 1:
	try:
		user_input = input("What's your guess between 1 and 99?\n>> ");
		if isinstance(user_input, int) == False:
			print("Goodbye!");
			break;
		elif user_input > secret_nb:
			print("Too high !");
		elif user_input < secret_nb:
			print("Too low !");
		else:
			if attempts == 1:
				print("Congratulations! You got it on your first try!");
			elif secret_nb == 42:
				print("The answer to the ultimate question of life, the universe and everything is 42.\nCongratulations! You got it!\nYou won in " + str(attempts) + " attempts");
			else:
				print("Congratulations! You got it!\nYou won in " + str(attempts) + " attempts");
			break;
		attempts += 1;
	except:
		print("That's is not a correct number.");

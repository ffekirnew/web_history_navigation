from history import History
from random import randint
from turtle import Turtle, Screen

'''This will be the driver code for the project'''

if __name__ == "__main__":
	print("-----------------------------------------------------")
	print("Type 'EXIT' at anytime to exit the history navigator.")
	print("-----------------------------------------------------")
	new_history = History()
	user_exit = False
	while not user_exit:
		print("\n|", new_history)
		user_action = input("Type: f - forward, b - backward, a web page to browse.\n> ")

		if user_action == "EXIT":
			user_exit = True

		elif len(user_action) <= 1:
			if (user_action.upper() == 'F'):
				print(new_history.forward())
			elif (user_action.upper() == 'B'):
				print(new_history.backward())

		else:
			new_history.add(user_action)
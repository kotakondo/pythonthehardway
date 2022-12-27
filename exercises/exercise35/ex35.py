#!/bin/usr/env python3

from sys import exit

# def gold_room():
# 	choice = input("> ")
# 	if "0" in choice or "1" in choice:
# 		how_much = int(choice)
# 	else:
# 		deal("man, lean to type a number.")

# 	if how_much < 50:
# 		print("Nice, you're not greedy, you win.")
# 		exit(0)
# 	else:
# 		dead("you greedy bastard")

# def brea_rooom():
# 	bear_moved = False

# 	while True:
# 		choice = input("> ")

# 		if choice == "take honey":
# 			dead("bear looks at you then slaps your face off")
# 		elif choice == "taunt bear" and not bear_moved:
# 			bear_moved = True
# 		elif choice == "taunt bear" and bear_moved:
# 			dead("the bear gets pissed off")
# 		elif choice == "open door" and bear_moved:
# 			gold_room()
# 		else:
# 			print(" ig to no idea")

num = input("> ")

if "0" in num:
	print("0 is in num")
else:
	exit("hihihi")
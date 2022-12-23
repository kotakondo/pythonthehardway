#!/bin/usr/env python3

from sys import argv

script, user_name = argv
prompt = '>'

print(f"Hi {user_name}, I'm the {script} script.")
print(f"Do you like me {user_name}?")
likes = input(prompt)

print(f"""Alright, so you said {likes} about likiing me.""")
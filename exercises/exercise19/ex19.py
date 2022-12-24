#!/bin/usr/env python3

# I just wanna check if python functions are passing by reference

def simple_add(a, b):
	a = a + 1
	b = b + 2
	return f"a is {a}, b is {b}"

a = 10
b = 20

print(simple_add(a,b))
print(f"a: {a}")
print(f"b: {b}")

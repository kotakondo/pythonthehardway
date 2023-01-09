#!/bin/usr/env python3

a = list(range(5))
b = list(range(3, 10))

for c in a:
	print(c)
for c in a, b:
	print(c)
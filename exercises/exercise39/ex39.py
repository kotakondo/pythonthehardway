#!/bin/usr/env python3

states = {
	'Oregon': 'OR',
	'Florida': 'FL',
	'California': 'CA',
	'New York': 'NY',
	'Michigan': 'MI'
}

cities = {
	'CA': 'San Francisco',
	'MI': 'Detroit',
	'FL': 'Jacksonville'
}

cities['NY'] = 'New York'
cities['OR'] = 'Portland'

print('-' * 10)

print(cities.items())
print(list(cities.items()))

for abbrev, city in list(cities.items()):
	print(f"{abbrev} has the city {city}")

print('-' * 10)

state = states.get('Texas')
if not state:
	print("no texas:(")

# giving a default value
city = cities.get('TX', 'Does not exist')
print(f"the city is {city}")
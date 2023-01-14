
def scan(input_str):
	# get a word, then return a tuple of its category (eg. direction) and the word itself
	directions = ['north', 'south', 'east', 'west', 'down', 'up', 'left', 'right', 'back']
	verbs = ['go', 'stop', 'kill', 'eat']
	stops = ['the', 'in', 'of', 'from', 'at', 'it']
	nouns = ['door', 'bear', 'princess', 'cabinet']

	words = input_str.split()
	return_list = []
	for word in words:
		if word in directions:
			return_list.append(('direction', word))
		elif word in verbs:
			return_list.append(('verb', word))
		elif word in stops:
			return_list.append(('stop', word))
		elif word in nouns:
			return_list.append(('noun', word))
		elif word.isnumeric():
			return_list.append(('number', int(word)))
		else:
			return_list.append(('error', word))

	return return_list
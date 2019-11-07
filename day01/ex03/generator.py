import random

def generator(text, sep=" ", option=None):
	'''Option is an optional arg, sep is mandatory'''

	try:
		array = text.split(sep)
	except:
		print("ERROR")
		exit()
	if option is 'shuffle':
		random.shuffle(array)
	elif option is 'ordered':
		array.sort()
	elif option is 'unique':
		new = []
		for i in array:
			if i not in new:
				new.append(i)
		array = new
	elif option is not None:
		print("ERROR")
		exit()
	for word in array:
		yield word
text = "Le Lorem Ipsum est est simplement du faux texte."
for word in generator(text, sep=" ", option='shuffle'):
	print(word)

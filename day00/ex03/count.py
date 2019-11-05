import string

MISSING = object();

def text_analyzer(text=MISSING):
	"""This function counts the number of upper characters, lower characters, punctuation and spaces in a given text."""
	if text is MISSING:
		text = input("What is the text to analyse?\n");
	lenght = len(text);
	totalUpper = sum(1 for c in text if c.isupper());
	totalLower = sum(1 for c in text if c.islower());
	totalPunc = sum(1 for c in text if c in string.punctuation);
	totalLSpace = sum(1 for c in text if c == ' ');
	print("The text contains " + str(lenght) + " characters:");
	print("- " + str(totalUpper) + " upper letters");
	print("- " + str(totalLower) + " lower letters");
	print("- " + str(totalPunc) + " punctuation marks");
	print("- " + str(totalLSpace) + " spaces");

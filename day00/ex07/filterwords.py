import sys
import re
import string

if len(sys.argv) > 3:
	print("ERROR");

try:
	text = sys.argv[1];
	lenght = int(sys.argv[2]);
except:
	print("ERROR");

if all(i.isalpha() or i.isspace() or i in string.punctuation for i in text):
	text = text.translate({ord(c): None for c in string.punctuation})
	text = text.strip();
	text = text.split(' ');
	text = filter(lambda x: len(x) > lenght, text);
	print(list(text));
else:
	print("ERROR");

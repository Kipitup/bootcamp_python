import sys

text = '';
for i in range(1, len(sys.argv)):
	text += sys.argv[i] + ' ';
text = text.strip();
text = text.swapcase();
text = text[len(text)::-1];
print(text);

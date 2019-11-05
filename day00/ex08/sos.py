import sys

morse = {
	'A' : '.-',
	'B' : '-...',
	'C' : '-.-.',
	'D' : '-..',
	'E' : '.',
	'F' : '..-.',
	'G' : '--.',
	'H' : '....',
	'I' : '..',
	'J' : '.---',
	'K' : '-.-',
	'L' : '.-..',
	'M' : '--',
	'N' : '-.',
	'O' : '---',
	'P' : '.--.',
	'Q' : '--.-',
	'R' : '.-.',
	'S' : '...',
	'T' : '-',
	'U' : '..-',
	'V' : '...-',
	'W' : '.--',
	'X' : '-..-',
	'Y' : '-.--',
	'Z' : '--..',
	'0' : '-----',
	'1' : '.----',
	'2' : '..---',
	'3' : '...--',
	'4' : '....-',
	'5' : '.....',
	'6' : '-....',
	'7' : '--...',
	'8' : '---..',
	'9' : '----.'
}

text = '';
lenght = len(sys.argv);
for i in range(1, lenght):
	text += sys.argv[i] + ' ';
text = text.strip();
for c in text:
	if c.isalnum() == False and c.isspace() == False:
		print('ERROR');
		exit ();
text = text.upper();
for c in text:
	if c is ' ':
		print("/", end='');
	else:
		print(morse[c], end='');
	print(" ", end='');
print('');

import sys

usage = "Usage: python operations.py\nExample:\n\tpython operations.py 10 3";
if len(sys.argv) > 3:
	print("InputError: too many arguments\n" + usage);
	exit();
try:
	nb1 = int(sys.argv[1]);
	nb2 = int(sys.argv[2]);
	print("Sum:          " + str(nb1 + nb2));
	print("Difference: " + str(nb1 - nb2));
	print("Product:      " + str(nb1 * nb2));
	print("Quotient:     " + str(nb1 / nb2));
	print("Remainder: " + str(nb1 % nb2));
except ValueError:
	print("InputError: only numbers\n" + usage);
except IndexError:
	print("InputError: too few arguments\n" + usage);

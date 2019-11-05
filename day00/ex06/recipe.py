cookbook = {
	'sandwich': {
		'ingredients': ['ham', 'bread', 'cheese', 'tomatoes'], 'meal': 'lunch', 'prep_time': 10
	},
	'cake': {
		'ingredients': ['flour', 'sugar', 'eggs'], 'meal': 'dessert', 'prep_time': 60
	},
	'salad': {
		'ingredients': ['avocado', 'argula', 'tomatoes', 'spinach'], 'meal': 'lunch', 'prep_time': 15
	}
}

def print_recipe(name):
	print("Recipe for " + name);
	print("Ingredients list: ", end = ' ');
	print(cookbook[name]['ingredients']);
	print("To be eaten for ", end='');
	print(cookbook[name]['meal']);
	print("Takes ", end='');
	print(cookbook[name]['prep_time'], end='');
	print(" minutes of cooking.",);
	return ;

def del_recipe(name):
	del cookbook[name];

def add_recipe(name, ingredients, meal, prep_time):
	cookbook[name] = {'ingredients': ingredients, 'meal': meal, 'prep_time': prep_time};

def print_names():
	print("Here are all the recipes you have:")
	for i, v in cookbook.items():
		print("- " + i);

def menu():
	while 1:
		print("Please select an option by typing the corresponding number:");
		print("1: Add a recipe");
		print("2: Delete a recipe");
		print("3: Print a recipe");
		print("4: Print the cookbook");
		print("5: Quit");
		choice = input();
		print("-" * 30);
		if choice is "1":
			name = input("Please enter the recipe's name: ");
			while 1:
				ingredients = input("Please enter the recipe's ingredients (separated by '-'): ");
				ingredients = ingredients.split('-');
				for item in ingredients:
					if not item:
						print("The ingredients were not well formated");
						break;
				else:
					break;
			meal = input("Please enter the recipe's type of meal: ");
			prep_time = input("Please enter the recipe's preparation time: ");
			add_recipe(name, ingredients, meal, prep_time);
		elif choice is "2":
			name = input("Please enter the recipe's name: ");
			del_recipe(name);
		elif choice is "3":
			name = input("Please enter the recipe's name: ");
			print_recipe(name);
		elif choice is "4":
			print_names();
		elif choice is "5":
			print("Cookbook closed.");
			break;
		else:
			print("This option does not exist, please type the corresponding number.\nTo exit enter 5");
		print("\n" + "-" * 30);

menu();
# print_recipe('salad');
# add_recipe('eggs and bacon', ['egg', 'bacon'], 'breakfast', 12);
# print_recipe('eggs and bacon');
# del_recipe('eggs and bacon');
# print_names();
# print(cookbook);

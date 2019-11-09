def ft_map(function_to_apply, list_of_inputs):
	a_len = len(list_of_inputs)
	for i in range(a_len):
		yield function_to_apply(list_of_inputs[i])


def myfunc(a):
	return len(a)

x = ft_map(myfunc, ('apple', 'banana', 'cherry'))
print(list(x))

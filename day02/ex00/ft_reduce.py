def ft_reduce(function_to_apply, list_of_inputs):
	ret = 0
	a_len = len(list_of_inputs)
	for item in list_of_inputs:
		ret = function_to_apply(ret, item)
	return ret


ages = [5, 12, 17, 18, 24, 32]

adults = ft_reduce(lambda a,b : a if a > b else b, ages)
print(adults)

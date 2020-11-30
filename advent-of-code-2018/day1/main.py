def calculate_frequency(frequency_list):
	return sum(cast_int(frequency_list))

def cast_int(frequency_list):
	return map(int, frequency_list)

def calculate_first_reaches_twice(frequency_list):
	sums = set([0])
	length = len(frequency_list)
	last_sum = 0
	i = 0
	while True:
		current_value = last_sum + int(frequency_list[i % length])
		if current_value in sums:
			return current_value
		else:
			sums.add(current_value)
			last_sum = current_value
			i += 1

def is_duplicate(my_list):
	return len(my_list) != len(set(my_list))
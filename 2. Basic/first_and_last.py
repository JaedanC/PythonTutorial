def sum_first_and_last(number_list):
    list_length = len(number_list)
    return number_list[0] + number_list[list_length - 1]
    

assert sum_first_and_last([1, 2, 3, 4]) == 5
assert sum_first_and_last([1]) == 2 # First and last is 1
assert sum_first_and_last([9, 6, 3, -1]) == 8
assert sum_first_and_last([0.5, 0.5]) == 1
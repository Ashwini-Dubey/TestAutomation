'''
Filter function - requires the function to look for a condition and then reutrns only those elements from the
collection which satisfy the condition.
'''

countries_filter = ["India","Indonesia","Japan","Italy","France"]

filter_func = filter(lambda x: x.startswith("I"), countries_filter)

print(list(filter_func))
'''
Reduce Function - breaks the entire process into pair-wise operations and uses the result from each
operation with the successive element.
'''
from functools import reduce

list_reduce = ['Ashwini','Prachi','Rahul','Aashna']

reduce_func = reduce(lambda x,y : x+y , list_reduce)

print(reduce_func)
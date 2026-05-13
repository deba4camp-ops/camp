my_list = ['apple', 'banana', 'cherry']
print((f"List: {my_list}"))
print(my_list)
print(len(my_list))
my_list.append('date')
print(my_list)
## remove an element from last
my_list.pop()
print(my_list)
## remove an element from specific index
my_list.pop(1)
print(my_list)
my_tuple = (1, 2, 3, 4, 5)
print(f"Tuple: {my_tuple}")
print(my_tuple)
print(len(my_tuple))
## tuples are immutable, so we cannot modify them
## but we can create a new tuple by concatenating two tuples    
new_tuple = my_tuple + (6, 7)
print(f"New Tuple: {new_tuple}")
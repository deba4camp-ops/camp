# set_exm = {1, 2, 3, 4, 5}
# print(f"Set: {set_exm}")
# list_with_set_exm = [1, 2, 3, 4, 5, {1,2} ]
# print(f"List with Set: {list_with_set_exm}")
# tuple_exm = (1, 2, 3, 4, 5, [1,2], {1,2})
# print(f"Tuple: {tuple_exm}")

#SET - NOT ALLOWED - { {} }/{[]} - because sets are mutable and cannot be hashed
# set with list is not allowed because sets are mutable and cannot be hashed
# set_with_list_exm = {1, 2, 3, 4, 5, [1,2] }
# print(f"Set with List: {set_with_list_exm}")
# set_with_Set_exm = {1, 2, 3, 4, 5, {1,2} }
# print(f"Set with Set: {set_with_Set_exm}")

# #LIST
# list_with_set_exm = [1, 2, 3, 4, 5, {1,2} ]
# print(f"List with Set: {list_with_set_exm}")
# list_with_tuple_exm = [1, 2, 3, 4, 5, (1,2) ]
# print(f"List with Tuple: {list_with_tuple_exm}")
# list_with_list_exm = [1, 2, 3, 4, 5, [1,2] ]
# print(f"List with List: {list_with_list_exm}")

#TUPLE
tuple_with_list_exm = (1, 2, 3, 4, 5, [1,2] )
# print(f"Tuple with List: {tuple_with_list_exm}")
# tuple_with_tuple_exm = (1, 2, 3, 4, 5, (1,2) )
# print(f"Tuple with Tuple: {tuple_with_tuple_exm}") 
# tuple_with_set_exm = (1, 2, 3, 4, 5, {1,2} )
# print(f"Tuple with Set: {tuple_with_set_exm}")  
# tuples are immutable, but if they contain mutable objects like lists, we can modify those mutable objects
# tuple_with_list_exm[1].append(8)
# print(f"Tuple with List after append: {tuple_with_list_exm}")
# set_exm = {1, 3, 3, 4, 5}
# set_exm.add(6)
# print(f"Set: {set_exm}")
dict_exm = { (1,2): 'Alice', 
            'list': [1 ,2],
            # [1,2]: 'Bob', # this will raise an error because lists are mutable and cannot be used as keys in a dictionary
            'set': {1, 2},
            # {1,2}: 'Charlie', # this will raise an error because sets are mutable and cannot be used as keys in a dictionary
            'tuple': (1, 2)
              }
print(f"Dictionary: {dict_exm}")

# # print(f"Dictionary keys: {dict_exm.keys()}")
# # print(f"Dictionary values: {dict_exm.values()}")

# # tuple_with_list_set = (1, 2, 3, list_exm, set_exm)
# # print(f"Tuple with List and Set: {tuple_with_list_set}")

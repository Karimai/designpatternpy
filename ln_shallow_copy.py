import copy

original_lst = [1, 2, 3, 4, 5]

# shallow_copy_0 = original_lst
# shallow_copy_1 = original_lst[:]
# shallow_copy_2 = copy.deepcopy(original_lst)
shallow_copy_3 = copy.copy(original_lst)

original_lst[0] = 10

print(id(original_lst))
print(original_lst)
# print(id(shallow_copy_0))
# print(id(shallow_copy_1))
# print(id(shallow_copy_2))
print(id(shallow_copy_3))
print(shallow_copy_3)


original_list = [1, 2, 3, 4]
shallow_copy = original_list[:]
deep_copy = copy.deepcopy(original_list)

# Modify the first sublist in the original list
original_list[0] = 5

print("Original list:", original_list)
print("Shallow copy:", shallow_copy)
print("Deep copy:", deep_copy)

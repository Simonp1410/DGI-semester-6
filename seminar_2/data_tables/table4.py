import copy
def change_list(list):
    list[0] = copy.copy(list[0])
    list[0][0] = 4
    print(list)
    print(id(list))
    print('\n')
base_list = [1,2,3]
my_list = [base_list]*3
print(my_list)
print(id(my_list))
print('\n')
change_list(my_list)
print(my_list)
print(id(my_list))
print('\n')
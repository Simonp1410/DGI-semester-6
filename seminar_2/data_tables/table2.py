def change_list(list):
    list.append('привет!')
    print(list)
    print(id(list))
    print('\n')
my_list = ['РТ1, ']
print(my_list)
print(id(my_list))
print('\n')
change_list(my_list)
print(my_list)
print(id(my_list))
print('\n')
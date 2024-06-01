def change_string(str):
    str = 'РТ1, '+str
    print(str)
    print(id(str))
    print('\n')
my_str = 'привет!'
print(my_str)
print(id(my_str))
print('\n')
change_string(my_str)
print(my_str)
print(id(my_str))
print('\n')
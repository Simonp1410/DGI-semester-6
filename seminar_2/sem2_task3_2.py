def change_list(list):
    list.append('привет!')
    print('Значение списка после изменения значения =', list)
    print('Id списка после изменения значения =', id(list))
    print('\n')
my_list =['РТ1,'] 
print('Значение списка до вызова функции =', my_list) 
print('Id списка до вызова функции =', id(my_list)) 
print('\n') 

change_list(my_list)
print('Значение списка после вызова функции =', my_list) 
print('Id списка после вызова функции =', id(my_list)) 
print('\n')
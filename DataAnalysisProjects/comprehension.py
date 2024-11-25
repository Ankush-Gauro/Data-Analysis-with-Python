my_list = [1, 2, 3, 3, 5]
print(my_list)

squared_list = [i**2 for i in my_list ]
print(squared_list)

even_list = [i for i in my_list if i%2==0]
print(even_list)


myset = {x for x in range(1,10)}
print(myset)

my_dict = {num:num**2 for num in range(1,5)}
print(my_dict)
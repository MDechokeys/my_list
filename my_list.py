my_list=[10,20,30,40]
my_list.append(15)
print("after append:", my_list)
list_2=[50,60,70]
my_list.extend(list_2)
print("after extend:", my_list)
del my_list[-1]
print(my_list)
my_list.sort(reverse=False)
print("after sort:", my_list)
index=my_list.index(30)
print(index)
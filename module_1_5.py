immutable_var = 1,2,3,"Type"
print("Immutable_var:",immutable_var)
# immutable_var[0] = 2   #Изменение значений переменной
# print(immutable_var)   #Элементы кортежа нельзя изменить до тех пор, пока они не преобразованы в список.
mutable_list = [1,2,3,"Type"]
mutable_list.extend(["New"])
print("Mutable_list:",mutable_list)


# month_list = list(input('введите число:'))
# # month_list = ['winter', 'sping', 'summer', 'autumn']
# month_list = [(1, 2, 12), (3, 4, 5), (6, 7, 8), (9, 10, 11)]
# month_dick = {(1, 2, 12): 'winter'}, {(3, 4, 5): 'spring'}, {(6, 7, 8): 'summer'}, {(9, 10, 11): 'autumn'}
# if month_list == month_dick:
#     print(month_dick)
seasons_list = ['winter', 'spring', 'summer', 'autumn']
seasons_dict = {1 : 'winter', 2 : 'spring', 3 : 'summer', 4 : 'autumn'}
month = int(input("Введите месяц по номеру "))
if month ==1 or month == 12 or month == 2:
     print(seasons_dict.get(1))
     print(seasons_list[0])
elif month == 3 or month == 4 or month ==5:
     print(seasons_dict.get(2))
     print(seasons_list[1])
elif month == 6 or month == 7 or month == 8:
     print(seasons_dict.get(3))
     print(seasons_list[2])

elif month == 9 or month == 10 or month == 11:
     print(seasons_dict.get(4))
     print(seasons_list[3])
else:
     print("Такого месяца не существует")
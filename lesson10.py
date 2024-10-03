my_list = [42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]
separate_num = 0
print(my_list)
while separate_num < len(my_list):
    num = my_list[separate_num]
    separate_num = separate_num + 1
    if num == 0:
        continue
    elif num < 0:
        print("Дошёл до отрицательного числа:", num)
        break




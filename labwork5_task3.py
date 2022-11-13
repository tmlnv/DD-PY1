from random import randint


def get_unique_list_numbers():
    lst = list()
    n = 0
    while n < 15:
        num = randint(-10, 10)
        if num not in lst:
            lst.append(num)
            n += 1
    return lst


list_unique_numbers = get_unique_list_numbers()
print(list_unique_numbers)
print(len(list_unique_numbers) == len(set(list_unique_numbers)))


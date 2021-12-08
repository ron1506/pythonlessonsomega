from date import *
from talker import *


def factorial(num):
    """
    the function factorising a number.
    :param num: the number that need to be factorated.
    :return: the factorial of the numbeer.
    """
    if num == 0:
        return 1
    i = num
    num -= 1
    while num > 0:
        i *= num
        num -= 1
    return i


def is_prime(num):
    """
    the function gets a number and check's if its a prime number.
    :param num: the number we check weather its prime or not.
    :return: True if prime or False otherwise.
    """
    i = 2
    while i < num:
        if num % i == 0:
            return False
        i += 1
    return True


def gcd(num1, num2):
    """
    :param num1: a number
    :param num2: a number
    :return: the greatest divisior of the two numbers have in common.
    """
    divisior = 2
    gcd = 1
    if num1 < num2:
        while divisior <= num1:
            if num2 % divisior == 0 and num1 % divisior == 0:
                gcd = divisior
            divisior += 1
    else:
        while divisior <= num2:
            if num2 % divisior == 0 and num1 % divisior == 0:
                gcd = divisior
            divisior += 1
    return gcd


def squ_equ(a, b, c):
    """
    return the two solutions of the equesion:
    ax^2 + bx + c = 0
    :param a:
    :param b:
    :param c:
    :return:
    """
    delta = b ** 2 - 4 * a * c
    if delta < 0:
        print("no solutions.")
    elif a != 0:
        if delta == 0:
            print("x = ", (-b) / 2 * a)
        else:
            print("x1 = ", ((-b) + delta ** 0.5) / 2 * a)
            print("x2 = ", ((-b) - delta ** 0.5) / 2 * a)
    else:
        print("x = ", (-b) / c)


def fibonacci(n: int):
    """
    the function returns the the eivar in the n place in
    :param n: 
    :return: 
    """
    if n == 1 or n == 2:
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)


def sum_of_list():
    """
    gets the list length and builds the list by using input.
    :return: the list and the sum of the list.
    """
    num = int(input())
    sum = 0
    list_of_numbers = []
    while num != 0:
        num_to_append = input()
        sum += int(num_to_append)
        list_of_numbers.append(num_to_append)
        num -= 1
    print("list: ", list_of_numbers)

    print("sum: ", sum)


def is_perfect(num: int):
    sum = 0
    i = 1
    while i < num:
        if num % i == 0:
            sum += i
        i += 1
    return sum == num


def prime_and_perfect():
    prime_numbers = [i for i in range(1, 1001) if is_prime(i)]
    perfect_numbers = [i for i in range(1, 1001) if is_perfect(i)]
    print(prime_numbers)
    print(perfect_numbers)


def my_map(func, lst1):
    returned_list = []
    for item in lst1:
        returned_list.append(func(item))
    return returned_list


def odd_three(n: int):
    return n % 3


def group_me(func, lst):
    dic = {}
    for element in lst:
        if (func(element)) in dic:
            dic[func(element)].append(element)
        else:
            dic[func(element)] = [element]
    return dic


def word_count(file_name: str):
    with open(file_name, "rb") as file:
        file_as_string = file.read().decode()
        file_as_list = file_as_string.split(" ")
        return len(file_as_list)


def words_appear(file_name: str):
    dict = {}
    with open(file_name, "rb") as file:
        file_as_string = file.read().decode()
        file_as_list = file_as_string.split(" ")
        for item in file_as_list:
            if item in dict:
                dict[item] += 1
            else:
                dict[item] = 1
    return dict


def join_files(file_name1: str, file_name2: str, file_name3: str):
    try:
        with open(file_name1, "br") as file1:
            file1_byte = file1.read()
    except BaseException:
        print("file path not good")
    try:
        with open(file_name2, "br") as file2:
            file2_byte = file2.read()
    except BaseException:
        print("file path not good")
    try:
        with open(file_name3, "bw") as file3:
            file3.write(file1_byte)
            file3.write(file2_byte)
    except BaseException:
        print("file path not good")


def make_them_talk(talker_list: list, say_what: str):
    return_lst = []
    for talker in talker_list:
        if talker.age > 10:
            return_lst.append(": ".join([talker.first_name, talker.talk(say_what)]))
    print(return_lst)


def my_pow(num1: int, num2: int):
    res = 1
    for i in range(num2):
        res *= num2
    return num1


def main():
    # print(fibonacci(6))
    # print(sum_of_list())
    # print(gcd(16, 20))
    # print(squ_equ(1, 2, 1))
    # prime_and_perfect()
    # print(group_me(odd_three, [1, 3, 4, 5, 7, 9]))
    # print(my_map(odd_three, [1, 2, 3, 4]))
    # print(word_count(r"C:\ron omega\צבא\venv\tal"))
    # print(words_appear(r"C:\ron omega\צבא\venv\tal"))
    # join_files(r"C:\ron omega\צבא\venv\tal", r"C:\ron omega\צבא\ron", r"C:\ron omega\צבא\shavit")
    # d = Date('1.1.0')
    # d1 = Date('31.12.21')
    # print(d1 + d)
    # talker_list = [StutterTalker("ron", "aizen", 18), SlowTalker("shavit", "g", 9),
    #                HappyTalker("alon", "sh", 19), SlowTalker("tal", "f", 18)]
    # make_them_talk(talker_list, "I love cookies")
    num1 = int(input("enter first number: "))
    num2 = int(input("enter first number: "))
    print(my_pow(num1, num2))


if __name__ == '__main__':
    main()

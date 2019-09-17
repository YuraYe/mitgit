# ##### #### *** ##### ##### #


# Поиск количества цифр в числе
def count_digs_len(number):
    temp = number
    length = 0
    while temp > 0:
        temp = int(temp / 10)
        length += 1
    return length


# Сумма цифр в числе
def count_digs_sum(number):
    temp = number
    summ = 0
    while temp > 0:
        temp = int(temp // 10)
        summ += temp % 10
    return summ


# Алгоритм Евклида
# для поиска наибольшего общего делителя (НОД)
def euclid(a, b):
    while a != b:
        if a > b:
            a -= b
        else:
            b -= a
    return a


# Наибольший общий делитель (НОД)
def get_nod(*args):
    while b > 0:
        # c = a % b
        # a = b
        # b = c
        a, b = b, a % b
    return a


# Наименьшее общее кратное (НОК)
def get_nok(*args):
    return (a * b) // get_nod(args)


# Поиск всех делителей числа
def get_divisors(number):
    i = 1
    divs = set()
    while i <= number**0.5:
        if number % i == 0:
            divs.add(i)
            divs.add(number // i)
        i += 1
    return sorted(divs)


# Поиск модуля числа
def mod(x):
    return -x if x < 0 else x


# Корни квадратного уравнения
# Search for the roots of a quadratic equation
def get_qroots(a=1, b=0, c=0, god=False):
    x1, x2 = None, None
    if a == 0:  # not a quadratic equation
        print('Error: \'a\' cannot be a zero in quadratic equation!\nbx + c = 0 => x = -c/b')
        # 0x2 + bx + c = 0 => bx = -c => x = -c/b
        return -c * b
    elif b == 0 and c > 0:
        print('{}x^2 + {} = 0'.format(a, c))
        if god is True:
            # ax2 + c = 0 => ax2 = -c => x2 = -c/a => x = +- (-c/a)**0.5
            return (-c/a)**0.5, -(-c/a)**0.5
        else:
            print('Error: a^2 = -{} ^^'.format(c))
            return None
    elif b == 0:
        return (-c/a)**0.5, -(-c/a)**0.5
    else:
        D = b**2 - (4 * a * c)
        if D > 0:
            x1 = (-b + D**0.5) / (2 * a)
            x2 = (-b - D**0.5) / (2 * a)
            return x1, x2
        elif D == 0:
            D = b**2 - (4 * a * c)
            x1 = (-b + D**0.5 / (2 * a))
            return x1
        elif D < 0:
            if god is True:
                x1 = (-b + D ** 0.5) / (2 * a)
                x2 = (-b - D ** 0.5) / (2 * a)
                return x1, x2
            else:
                print('Error: D < 0')
                return None
    print('Error: WTF!!!')
    return None


# Ряд Фибоначчи до числа n
# n=100 =>  0 1 1 2 3 5 8 13 21 34 55 89
def fibonacci(n=100):
    result = []
    a, b = 0, 1
    while a < n:
        result.append(a)
        a, b = b, a+b
    return result


# Рубрика: догадайся сам ^^
def find_min(*args):
    used = []
    sm = args[0]
    for i in args:
        for u in used:
            if u < sm:
                sm = u
        used.append(i)
    return sm


# Продолжение рубрики: догадайся сам ^^
def find_max(*args):
    used = []
    big = args[0]
    for i in args:
        for u in used:
            if u > big:
                big = u
        used.append(i)
    return big


# Триугольник Паскаля
#     1
#    1 1
#   1 2 1
#  1 3 3 1
# 1 4 6 4 1
# class PascalTriangle:
#     height = 4
#     matrix = []
#
#     def gen(self):
#         for h in range(1, self.height + 1):
#             for w in range(1, h + 1):
#                 self.matrix[h][w] = self.matrix[h - 1][w] + self.matrix[h - 1][w - 1]
#                 print(self.matrix)


# ##### #### *** ##### ##### #

# a = int(input('a: '))
# b = int(input('b: '))
# c = int(input('c: '))
# draw('Hello BLUES!', Colors.bg.green)
# draw('Hello RED!', Colors.bg.red, Colors.fg.blue)

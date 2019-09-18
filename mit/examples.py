from mit import nomath, nostr
from mit.console import *


def test0():
    print("""
    Colors class:
    reset all colors with colors.reset
    two subclasses fg for foreground and bg for background.
    use as colors.subclass.colorname.
    i.e. colors.fg.red or colors.bg.green
    also, the generic bold, disable, underline, reverse, strikethrough,
    and invisible work with the main class
    i.e. colors.bold
    """)
    finite()


def test1():
    print('input_int(text, min=100, max=999)')
    print(input_int('Enter 3-n number (100-999): ', 100, 999))
    finite()


def test2():
    print('from colors import Color, draw')
    print('draw(string, Colors.fg.foreground, Color.bg.background)')
    draw('I am a best of the best!', Colors.fg.red, Colors.bg.blue)
    finite()


def test3():
    print('nomath.get_qroots(a=0, b=5, c=-6)')
    print(nomath.get_qroots(a=2, b=2, c=-4))
    finite()


def test4():
    print('nomath.get_nod(15, 440)')
    print(nomath.get_nod(15, 440))
    print()
    print('nomath.get_nok(15, 440)')
    print(nomath.get_nok(15, 440))
    finite()


def test5():
    print('nomath.get_divisors(36)')
    print(nomath.get_divisors(36))
    finite()


def test6():
    print('nomath.mod(-3)')
    print(nomath.mod(-3))
    finite()


def test7():
    print('nomath.euclid(10, 300000000)')
    print(nomath.euclid(10, 300000000))
    finite()


def test8():
    print('nomath.get_divisors(100)')
    print(nomath.get_divisors(100))
    finite()


def test9():
    print('nomath.count_dig_len(598879)')
    print(nomath.count_digs_len(598879))
    print()
    print('nomath.count_dig_sum(598879)')
    print(nomath.count_digs_sum(598879))
    finite()


def test10():
    print('nomath.fibonacci(1000)')
    print(nomath.fibonacci(1000))
    finite()


def test11():
    print('nomath.find_min(4, 6, -6, 423, 555, -3, 4)')
    print(nomath.find_min(4, 6, -6, 423, 555, -3, 4))
    print()
    print('nomath.find_max(4, 6, -6, 423, 555, -3, 4)')
    print(nomath.find_max(4, 6, -6, 423, 555, -3, 4))
    finite()


def test12():
    print('nostr.rev("Hello, World!")')
    print(nostr.rev('Hello, World!'))
    print()
    print('nostr.replace("Hello, World!", 3, "Q")')
    print(nostr.replace('Hello, World!', 3, 'Q'))
    print()
    print("nostr.replace('Hello, World!', (0, 1, 11, -2, -5), ('Love', '777', 'mb', '', '-OOO-')")
    print(nostr.replace('Hello, World!', (0, 1, 11, -2, -5), ('Love', '777', 'mb', '', '-OOO-')))
    finite()


# TODO: не забываем добавлять тесты ^^


def finite():
    print()

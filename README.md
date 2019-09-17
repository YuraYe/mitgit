# Python module with helpful data

## Current version: 1.1.7
Here you can find many functions and classes that you can use in your future work.

## Files
The main file (must be present for the folder to be considered a module)
> \_\_init\_\_.py

Input/output console operations and options
> console.py

Write test0() or test11() or something similar to test some commands
> examples.py

Alternative for included "math" library
> nomath.py

## All functions

### nomath
   Поиск количества цифр в числе
   > count_digs_len(number)

   Сумма цифр в числе
   > count_digs_sum(number)

   Алгоритм Евклида
   для поиска наибольшего общего делителя (НОД)
   > euclid(a, b)

   Наибольший общий делитель (НОД)
   > get_nod2(a, b)

   Наименьшее общее кратное (НОК)
   > get_nok2(a, b):
       return (a * b) // get_nod2(a, b)

   Наибольший общий делитель (НОД)
   > get_nod(\*args)

   Наименьшее общее кратное (НОК)
   TODO: работает не корректно!
   > get_nok(\*args)

   Поиск всех делителей числа
   > get_divisors(number)

   Поиск модуля числа
   > mod(x)

   Корни квадратного уравнения
   Search for the roots of a quadratic equation
   > get_qroots(a=1, b=0, c=0, god=False)

   Ряд Фибоначчи до числа n
   n=100 =>  0 1 1 2 3 5 8 13 21 34 55 89
   > fibonacci(n=100)

   Рубрика: догадайся сам ^^
   > find_min(\*args)

   Продолжение рубрики: догадайся сам ^^
   > find_max(\*args)

### console

Цветной вывод в терминал
> draw(string, color0, color1=None, color2=None, end='\n')

Прочитать из консоли список значений через разделитель
> read(txt='', sep=' ')

Проверка ввода на число в диапазоне
> input_int(text='', minv='none', maxv='none')


## Example

> For more information use:

```
from mit import examples

examples.test0()
examples.test1()
examples.test2()
# ...
examples.test11()

```

### Small example code

```
import mit

li = mit.read('Enter some numbers')
m = mit.nomath.find_max(li)

if m > 10:
   mit.draw('Hello, World!', mit.Colors.bg.green, mit.Colors.bold)
else:
   mit.draw('Hello, World!', mit.Colors.fg.purple, mit.Colors.underline)
```

## **see you soon! ^^**

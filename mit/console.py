# Разные цвета для текста
class Colors:
    """
    Colors class:
    reset all colors with colors.reset
    two subclasses fg for foreground and bg for background.
    use as colors.subclass.colorname.
    i.e. colors.fg.red or colors.bg.green
    also, the generic bold, disable, underline, reverse, strikethrough,
    and invisible work with the main class
    i.e. colors.bold
    """

    reset = '\033[0m'
    bold = '\033[01m'
    disable = '\033[02m'
    underline = '\033[04m'
    reverse = '\033[07m'
    crossed = '\033[09m'
    invisible = '\033[08m'

    class fg:
        black = '\033[30m'
        red = '\033[31m'
        green = '\033[32m'
        orange = '\033[33m'
        blue = '\033[34m'
        purple = '\033[35m'
        cyan = '\033[36m'
        lgrey = '\033[37m'
        dgrey = '\033[90m'
        lred = '\033[91m'
        lgreen = '\033[92m'
        yellow = '\033[93m'
        lblue = '\033[94m'
        pink = '\033[95m'
        lcyan = '\033[96m'

    class bg:
        black = '\033[40m'
        red = '\033[41m'
        green = '\033[42m'
        orange = '\033[43m'
        blue = '\033[44m'
        purple = '\033[45m'
        cyan = '\033[46m'
        lgrey = '\033[47m'


# Цветной вывод в терминал
def draw(string, color0, color1=None, color2=None, end='\n'):
    if color1 is None and color2 is None:
        print("{}{}\033[00m".format(color0, string, end=end))
        return
    elif color2 is None:
        print("{}{}{}\033[00m\033[00m".format(color0, color1, string, end=end))
    print("{}{}{}{}\033[00m\033[00m\033[00m".format(color0, color1, color2, string, end=end))


# Прочитать из консоли список значений через разделитель
def read(txt='', sep=' '):
    return map(input(txt).split(sep))


# Проверка ввода на число в диапазоне
def input_int(text='', minv='none', maxv='none'):
    num = 'Error'
    if minv != 'none' or maxv != 'none':
        if minv == 'none':
            minv = 0
        elif maxv == 'none':
            maxv = minv + 10
        while True:
            try:
                num = int(input(text))
                if int(num) < minv:
                    print(f'Number {num} is to small!')
                elif int(num) > maxv:
                    print(f'Number {num} is to long!')
                else:
                    break
            except ReferenceError:
                print('{} iNaN... try again'.format(num))
    else:
        try:
            num = int(input(text))
        except ReferenceError:
            print('{} isNaN... try again'.format(num))
    return num

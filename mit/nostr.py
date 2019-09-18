# Перевернуть строку: привет! => !тевирп
def rev(s):
    return s[::-1]


# Заменить по индексам на строки
def replace(string, indexes, new_values):
    try:
        iterator = iter(indexes) and iter(new_values)
    except TypeError:
        # not iterable
        start = string[:indexes]
        end = string[indexes + 1:]
        return start + new_values + end
    else:
        # iterable
        l = list(string)
        string = ''
        c = 0
        for i in indexes:
            l[i] = new_values[c]
            c += 1
        for i in l:
            string += i
    return string


# TODO: добавить ещё опций

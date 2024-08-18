def add_everything_up(a, b):
    if type(a) == float and isinstance(b, (int, float)):
        x = len(str(a).split('.')[1])
        a = a * x * 10 / x / 10
    elif type(b) == float and isinstance(a, (int, float)):
        y = len(str(b).split('.')[1])
        b = b * y * 10 / y / 10
    try:
        return a + b
    except TypeError as exc:
        return str(a) + str(b)

print(add_everything_up(123.456, 'строка'))
print(add_everything_up('яблоко', 4215))
print(add_everything_up(123.456, 7))

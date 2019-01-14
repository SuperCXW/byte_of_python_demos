def say_hello():
    print("hello")


say_hello()


def print_max(a, b):
    if a > b:
        print(a, 'is maxium')
    elif a == b:
        print('{0} is equals to {1}', a, b)
    else:
        print(b, 'is maxium')


print_max(1, 5)

x = 50


def func():
    global x

    print('x is', x)
    # x = 2
    print('changed local x to', x)


func()
print('x is still ', x)


def say(message, times=1):
    print(message * times)


say('hello')


def func1(a, b=5, c=10):
    print('a is', a, 'and b is ', b, 'and c is', c)


func1(1)
func1(c=3, a=12)


def total(a=5, *numbers, **phonebook):
    print('a', a)

    for single_item in numbers:
        print('single_item', single_item)

    for first_part, second_part in phonebook.items():
        print(first_part, second_part)


print(total(10, 1, 2, 3, 4, 5, 8, jack=123, john=2231, Inge=1560))

for i in range(0, 5):
    print(i)
else:
    print(2)

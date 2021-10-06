# 1. Напишите декоратор, замеряющий время выполнения функции.
# Декоратор должен вывести на экран время выполнения задекорированной функции
# 2. Зарегистрируйтесь на https://gitlab.com/ или на https://github.com/.
# Создайте публичный репозиторий и выложите на него это ДЗ. В лмс сдавайте ссылку на репозиторий


import time


def time_of_func(foo):

    def wrapped(*args, **kwargs):
        start_time = time.time_ns()
        res = foo(*args, **kwargs)
        print(time.time_ns() - start_time)
        return res

    return wrapped


@time_of_func
def my_number(a):
    if type(a) is int:
        return float(a)
    if type(a) is float:
        return a
    else:
        return


num = my_number(4.3)
print(num)

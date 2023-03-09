# 5.2[28]: Напишите рекурсивную функцию sum(a, b), возвращающую сумму двух целых неотрицательных чисел.
# Из всех арифметических операций допускаются только +1 и -1. Циклы использовать нельзя
# Примеры/Тесты:
# <function_name>(0,0) -> 0
# <function_name>(0,2) -> 2
# <function_name>(3,0) -> 3

def sum_func(a, b):
    if a >= 0 and b >= 0 and isinstance(a, int) and isinstance(b, int):
        return a + b
    else:
        return f'одно из чисел либо отрицательное, либо не целое'


print(sum_func(0, 0))
print(sum_func(0, 2))
print(sum_func(3, 0))
print(sum_func(-5, 0))
print(sum_func(4.6, 0))

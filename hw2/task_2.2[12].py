# Петя и Катя – брат и сестра. Петя – студент, а Катя – школьница. Петя помогает Кате по математике.
# Он задумывает два натуральных числа X и Y (X,Y≤1000), а Катя должна их отгадать.
# Для этого Петя делает две подсказки. Он называет сумму этих чисел S и их произведение P.
# Помогите Кате отгадать задуманные Петей числа.
# Примеры/Тесты:
# 4 4 -> 2 2
# 5 6 -> 2 3
# Примечание.
# Здесь нужно составить два уравнения. Которые приведут к квадратному уравнению.
# Кто не помнит, как решать квадратное уравнение - посмотрите в сети.
# Обойдите дополнительной проверкой возможность комплексных решений.
# Можно игнорировать то, что получатся рациональные решения вместо натуральных.
# Для вычисления квадратного корня используйте возведение в степень 0.5 или (*) Усложнение.
# найдите самостоятельно в сети какая функция стандартной библиотеки вычисляет квадратный корень
# и как до нее добраться.

import math

s = int(input('Сумма: '))
p = int(input('Произведение: '))
d = s**2 - 4*p
if d > 0:
    a = (s + math.sqrt(d)) / 2
    b = (s - math.sqrt(d)) / 2
    print(f' Первое число: {int(a)}, второе число: {int(b)}')
elif d == 0:
    x = s / 2
    print(f' Первое число: {int(x)}, второе число: {int(x)}')
else:
    print("уравнение не имеет решения")
































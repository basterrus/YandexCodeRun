"""
В трек аналитики второго сезона вошло 28 задач, однако кроме них была подготовлена ещё одна задача. Так как в сезон она не вошла, то предлагаем решить вам её сейчас.

Вам дано квадратное уравнение вида:
ax2+bx+c=0,ax 2
 +bx+c=0,
где a,ba,b и cc — целые числа, такие что a≠0a=0.

Напишите программу, которая решает это уравнение.
"""
import math


def main():
    temp = list(input().split(" "))
    a, b, c = float(temp[0]), float(temp[1]), float(temp[2])
    discr = b ** 2 - 4 * a * c

    if discr > 0:
        x1 = (-b + math.sqrt(discr)) / (2 * a)
        x2 = (-b - math.sqrt(discr)) / (2 * a)
        print("2")
        print("%.6f %.6f" % (x2, x1))
    elif discr == 0:
        x = -b / (2 * a)
        print("1")
        print("%.6f" % x)
    else:
        print("0")


if __name__ == '__main__':
    main()

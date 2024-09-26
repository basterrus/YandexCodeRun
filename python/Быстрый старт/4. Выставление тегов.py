"""
Большинство задач сезона CodeRun имеют теги, помогающие пользователям выбрать подходящий алгоритм для решения.
Известно, что для первой и второй задач каждого трека количество тегов равно 1
(t[1]=t[2]=1)(t[1]=t[2]=1), а для всех следующих количество тегов вычисляется по следующему правилу:
t[i]=t[i−1]+t[i−2],
t[i]=t[i−1]+t[i−2],
где t[i]
t[i] - количество тегов задачи с номером ii.

Было установлено, что на выставление одного тега требуется одна секунда.
Посчитайте, сколько всего времени потребуется для выставления всех тегов.
"""

import functools


def cache(func):
    """Кэш предыдущих вызовов функций"""
    cache = {}

    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        cache_key = args + tuple(kwargs.items())
        if cache_key not in cache:
            cache[cache_key] = func(*args, **kwargs)
        return cache[cache_key]

    return wrapper


@cache
def tags(n):
    if n == 0:
        return 0
    elif n == 1 or n == 2:
        return 1
    else:
        return tags(n - 1) + tags(n - 2)


def main():
    n = int(input())
    sum = 0
    # без кэша цикл ниже занимает 12 меинут времени на стенде яндекса, и задача не проходит
    for i in range(n + 1):
        sum += tags(i)
    print(sum)


if __name__ == '__main__':
    main()

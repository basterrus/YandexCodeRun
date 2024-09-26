"""
Дан список. Определите, является ли он монотонно возрастающим (то есть верно ли,
что каждый элемент этого списка строго больше предыдущего)
Выведите YES, если массив монотонно возрастает и NO в противном случае.
"""


def main():
    x = list(map(int, input().split()))
    check_list(x)


def check_list(x: list):
    for i in range(1, len(x)):
        if x[i] > x[i - 1]:
            continue
        else:
            print('NO')
            return
    print('YES')


if __name__ == '__main__':
    main()

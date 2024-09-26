"""
Напишите программу, которая находит в массиве элемент, самый близкий по величине к данному числу.
"""


def main():
    arr_size = int(input())
    arr = map(int, input().split(" "))
    num = int(input())
    max_num = 2001
    undefine = None

    for index in arr:
        if index == num:
            return (num)
        if index == undefine:
            continue
        if abs(num - index) < max_num:
            max_num = abs(num - index)
            undefine = index

    return undefine


if __name__ == '__main__':
    print(main())

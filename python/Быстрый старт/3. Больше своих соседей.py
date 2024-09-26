"""
Дан список чисел. Определите, сколько в этом списке элементов, которые больше двух своих соседей.
Выведите количество таких элементов.
"""


def main():
    nums = list(map(int, input().split()))
    res = 0

    for i in range(1, len(nums) - 1):
        if nums[i] > nums[i - 1] and nums[i] > nums[i + 1]:
            res += 1
    print(res)


if __name__ == '__main__':
    main()

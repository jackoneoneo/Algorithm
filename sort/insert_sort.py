'''
插入排序
时间复杂度: O(n^2)或者c * n^2
'''

import numpy as np


def insert_sort():
    arr = np.random.randint(1, 1000, size=100)
    print(arr)
    start = 1
    while start < len(arr):
        value = arr[start]
        temp = start - 1
        # 找到位置，坐下来
        while temp >= 0:
            if arr[temp] > value:
                arr[temp + 1] = arr[temp]
                temp -= 1
            else:
                break
        arr[temp + 1] = value
        start += 1
    return arr


if __name__ == '__main__':
    print(insert_sort())

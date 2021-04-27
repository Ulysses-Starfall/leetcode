# coding: utf-8
import random


def quick_sort(data):
    if len(data) >= 2:
        pivot = data[0]
        i, j = 1, len(data) - 1

        while i < j:
            if data[j] < pivot <= data[i]:
                data[i], data[j] = data[j], data[i]
            if data[i] < pivot:
                i += 1
            if data[j] >= pivot:
                j -= 1

        if data[i] < pivot:
            data = data[1:i + 1] + [pivot] + data[i + 1:len(data)]
            data[0:i] = quick_sort(data[0:i])
            data[i + 1:len(data)] = quick_sort(data[i + 1:len(data)])
        else:
            data = data[1:i] + [pivot] + data[i:len(data)]
            data[0:i - 1] = quick_sort(data[0:i - 1])
            data[i:len(data)] = quick_sort(data[i:len(data)])

    return data


def quick_sort2(data, start, end):
    if start < end:
        i = start
        j = end
        pivot = data[start]
        while i != j:
            while j > i and data[j] >= pivot:
                j -= 1
            if j > i:
                data[i] = data[j]
            while i < j and data[i] < pivot:
                i += 1
            if i < j:
                data[j] = data[i]

        data[i] = pivot
        quick_sort2(data, start, i - 1)
        quick_sort2(data, i + 1, end)


if __name__ == "__main__":
    test_data = random.sample(range(1, 10), 5)
    quick_sort2(test_data, 0, len(test_data) - 1)
    print(test_data)

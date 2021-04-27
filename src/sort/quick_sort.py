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
                i += 1
            while i < j and data[i] < pivot:
                i += 1
            if i < j:
                data[j] = data[i]
                j -= 1

        data[i] = pivot
        quick_sort2(data, start, i - 1)
        quick_sort2(data, i + 1, end)


def bubble_sort(data):
    if len(data) < 2:
        return data
    for i in range(len(data)):
        for j in range(i + 1, len(data)):
            if data[i] > data[j]:
                data[i], data[j] = data[j], data[i]

    return data


if __name__ == "__main__":
    import time

    start_time = int(time.time() * 1000)
    for _ in range(100000):
        test_data = random.sample(range(1, 100), 50)
        quick_sort(test_data)
    end_time = int(time.time() * 1000)

    print("quick sort 1 total time: ", end_time - start_time)

    start_time = int(time.time() * 1000)
    for _ in range(100000):
        test_data = random.sample(range(1, 100), 50)
        quick_sort2(test_data, 0, len(test_data) - 1)
    end_time = int(time.time() * 1000)

    print("quick sort 2 total time: ", end_time - start_time)

    start_time = int(time.time() * 1000)
    for _ in range(100000):
        test_data = random.sample(range(1, 100), 50)
        bubble_sort(test_data)
    end_time = int(time.time() * 1000)

    print("bubble sort total time: ", end_time - start_time)

import time
from colors import *


def merge(array, start, mid, end):
    p = start
    q = mid + 1
    tempArray = []

    for i in range(start, end + 1):
        if p > mid:
            tempArray.append(array[q])
            q += 1
        elif q > end:
            tempArray.append(array[p])
            p += 1
        elif array[p] < array[q]:
            tempArray.append(array[p])
            p += 1
        else:
            tempArray.append(array[q])
            q += 1

    for p in range(len(tempArray)):
        array[start] = tempArray[p]
        start += 1


def merge_sort(array, visualizer, speed):
    merge_sort_helper(array, 0, len(array) - 1, visualizer, speed)
    if visualizer.activeSorting:
        visualizer.draw(array, [YELLOW for x in range(len(array))])
    else:
        visualizer.draw(array, [RED for x in range(len(array))])


def merge_sort_helper(array, start, end, visualizer, speed):
    if start < end:
        if not visualizer.activeSorting:
            return
        mid = (start + end) // 2
        merge_sort_helper(array, start, mid, visualizer, speed)
        merge_sort_helper(array, mid + 1, end, visualizer, speed)

        merge(array, start, mid, end)

        visualizer.draw(
            array,
            [
                PURPLE
                if x >= start and x < mid
                else YELLOW
                if x == mid
                else DARK_BLUE
                if x > mid and x <= end
                else RED
                for x in range(len(array))
            ],
        )
        time.sleep(speed * 8)

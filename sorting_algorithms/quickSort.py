import time
from colors import *


def quick_sort(array, visualizer, speed):
    quick_sort_helper(array, 0, len(array) - 1, visualizer, speed)
    if visualizer.activeSorting:
        visualizer.draw(array, [YELLOW for x in range(len(array))])
    else:
        visualizer.draw(array, [RED for x in range(len(array))])


def quick_sort_helper(array, startIdx, endIdx, visualizer, speed):
    if startIdx > endIdx:
        return

    swap(array, startIdx, (startIdx + endIdx) // 2)
    visualizer.draw(
        array,
        [
            BLUE if x == startIdx or x == (startIdx + endIdx) // 2 else RED
            for x in range(len(array))
        ],
    )
    time.sleep(speed)

    current = startIdx
    for i in range(startIdx + 1, endIdx + 1):
        if not visualizer.activeSorting:
            return
        if array[i] < array[startIdx]:
            current += 1
            swap(array, current, i)
            visualizer.draw(
                array,
                [BLUE if x == current or x == i else RED for x in range(len(array))],
            )
            time.sleep(speed)

    swap(array, startIdx, current)
    visualizer.draw(
        array,
        [BLUE if x == startIdx or x == current else RED for x in range(len(array))],
    )
    time.sleep(speed)

    if current > startIdx:
        quick_sort_helper(array, startIdx, current - 1, visualizer, speed)
    if current < endIdx:
        quick_sort_helper(array, current + 1, endIdx, visualizer, speed)


def swap(array, i, j):
    array[i], array[j] = array[j], array[i]

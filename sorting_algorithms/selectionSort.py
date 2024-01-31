import time
from colors import *


def selection_sort(array, visualizer, speed):
    for i in range(len(array)):
        minIdx = i
        for j in range(i + 1, len(array)):
            if not visualizer.activeSorting:
                visualizer.draw(array, [RED for x in range(len(array))])
                return
            if array[minIdx] > array[j]:
                minIdx = j

        swap(array, i, minIdx)
        visualizer.draw(
            array,
            [BLUE if x == i or x == minIdx else RED for x in range(len(array))],
        )
        time.sleep(speed * 8)
    visualizer.draw(array, [YELLOW for x in range(len(array))])


def swap(array, i, j):
    array[i], array[j] = array[j], array[i]

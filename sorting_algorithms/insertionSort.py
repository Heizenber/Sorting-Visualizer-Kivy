import time
from colors import *


def insertion_sort(array, visualizer, speed):
    for i in range(1, len(array)):
        key = array[i]
        j = i - 1
        while j >= 0 and key < array[j]:
            if not visualizer.activeSorting:
                visualizer.draw(array, [RED for x in range(len(array))])
                return
            array[j + 1] = array[j]
            j -= 1
            visualizer.draw(
                array,
                [BLUE if x == j + 1 or x == j else RED for x in range(len(array))],
            )
            time.sleep(speed / 10)
        array[j + 1] = key
        visualizer.draw(
            array,
            [BLUE if x == j + 1 or x == key else RED for x in range(len(array))],
        )
        time.sleep(speed)
    visualizer.draw(array, [YELLOW for x in range(len(array))])

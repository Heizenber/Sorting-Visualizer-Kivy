import time
from colors import *
from kivy.clock import Clock


def bubble_sort(array, visualizer, speed):
    size = len(array)
    for i in range(size - 1):
        for j in range(size - i - 1):
            if not visualizer.activeSorting:
                visualizer.draw(array, [RED for x in range(len(array))])
                return
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]

                visualizer.draw(
                    array,
                    [BLUE if x == j or x == j + 1 else RED for x in range(len(array))],
                )
                time.sleep(speed / 20)
    visualizer.draw(array, [YELLOW for x in range(len(array))])

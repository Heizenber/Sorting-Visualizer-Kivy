from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.boxlayout import BoxLayout
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.graphics import Rectangle, Color
from kivy.utils import get_color_from_hex
from threading import Thread
from sorting_algorithms.bubleSort import bubble_sort
from sorting_algorithms.mergeSort import merge_sort
from sorting_algorithms.quickSort import quick_sort
from sorting_algorithms.selectionSort import selection_sort
from sorting_algorithms.insertionSort import insertion_sort
from colors import *
import random


Builder.load_file("visualizer.kv")

algorithms = {
    "Bubble Sort": bubble_sort,
    "Selection Sort": selection_sort,
    "Quick Sort": quick_sort,
    "Merge Sort": merge_sort,
    "Insertion Sort": insertion_sort,
}


class SortVisualizer(BoxLayout):
    activeSorting = True

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.visualizer = self.ids.visualize_canvas
        self.display_rectangles()
        self.bind(size=self.update)

    def display_rectangles(self):
        self.generate(int(self.ids.slider.value), self.visualizer)

    def set_active(self):
        self.activeSorting = False

    def on_resize(self):
        self.draw(self.rectangles, [RED for i in range(len(self.rectangles))])

    def set_speed(self):
        if self.ids.speed.text == "Slow":
            return 0.1
        elif self.ids.speed.text == "Medium":
            return 0.01
        else:
            return 0.001

    def generate(self, number, visualize):
        self.rectangles = [random.randint(5, 400) for i in range(number)]
        self.draw(self.rectangles, [RED for i in range(len(self.rectangles))])

    def sort(self):
        speed = self.set_speed()
        self.activeSorting = True

        self.sorting = Thread(
            target=algorithms[self.ids.algorithm.text],
            args=(self.rectangles, self, speed),
            daemon=True,
        ).start()

    def draw(self, rects, colorArray):
        self.visualizer.canvas.clear()
        width, height = Window.size
        rect_width = width / (len(rects) + 1)
        offset = 4
        spacing = rect_width / 6
        rect_width = rect_width - spacing
        canvas_height = height - height / 10 - 20
        normalized_rects = [i / max(rects) for i in rects]
        with self.visualizer.canvas:
            for i, height in enumerate(normalized_rects):
                Color(*get_color_from_hex(colorArray[i]))
                pos_y = 5
                pos_x = i * (rect_width + spacing) + offset + spacing
                size_y = height * canvas_height
                size_x = rect_width
                Rectangle(pos=(pos_x, pos_y), size=(size_x, size_y))
        
    # def calculate_dimensions(self, rects, width, height):
    #     rect_width = width / (len(rects) + 1)
    #     spacing = rect_width / 6
    #     rect_width = rect_width - spacing
    #     canvas_height = height - height / 10 - 20
    #     normalized_rects = [i / max(rects) for i in rects]
    #     return rect_width, spacing, canvas_height, normalized_rects

    # def draw_rectangle(self, i, height, rect_width, spacing, canvas_height):
    #     Color(*get_color_from_hex(colorArray[i]))
    #     pos_y = 5
    #     pos_x = i * (rect_width + spacing) + offset + spacing
    #     size_y = height * canvas_height
    #     size_x = rect_width
    #     Rectangle(pos=(pos_x, pos_y), size=(size_x, size_y))

    # def draw(self, rects, colorArray):
    #     self.visualizer.canvas.clear()
    #     width, height = Window.size
    #     rect_width, spacing, canvas_height, normalized_rects = self.calculate_dimensions(rects, width, height)
    #     with self.visualizer.canvas:
    #         for i, height in enumerate(normalized_rects):
    #             self.draw_rectangle(i, height, rect_width, spacing, canvas_height)

    def update(self, *args):
        self.draw(self.rectangles, [RED for i in range(len(self.rectangles))])


class Visualizer(Widget):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)


class VisualizeSortApp(App):
    def build(self):
        return SortVisualizer()


if __name__ == "__main__":
    VisualizeSortApp().run()

from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.boxlayout import BoxLayout
from kivy.lang import Builder
from kivy.core.window import Window
from threading import Thread
from kivy.graphics import Rectangle, Color
from kivy.utils import get_color_from_hex
from sorting_algorithms.bubleSort import bubble_sort
from sorting_algorithms.mergeSort import merge_sort
from sorting_algorithms.quickSort import quick_sort
from sorting_algorithms.selectionSort import selection_sort
from sorting_algorithms.insertionSort import insertion_sort
from kivy.clock import Clock
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

speed = {
    "Slow": 0.1,
    "Medium": 0.01,
    "Fast": 0.001,
}


class SortVisualizer(BoxLayout):
    activeSorting = True

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.visualizer = self.ids.visualize_canvas
        self.rectangles = []
        # self.display_rectangles()
        self.generate(self.ids.slider, int(self.ids.slider.value))
        Clock.schedule_once(self.bind_slider_value)
        self.bind(size=self.update)

    def bind_slider_value(self, *args):
        self.ids.slider.bind(value=self.generate)

    def display_rectangles(self):
        self.generate(int(self.ids.slider.value))

    def set_active(self):
        self.activeSorting = False

    def on_resize(self):
        Clock.schedule_once(self.update)

    def set_speed(self):
        return speed[self.ids.speed.text]

    def generate(self, instance, value):
        self.rectangles = [random.randint(5, 400) for i in range(value)]
        # Clock.schedule_once(lambda dt: self.update)
        self.update()
        # self.draw(self.rectangles, [RED] * len(self.rectangles))

    def sort(self):
        speed = self.set_speed()
        self.activeSorting = True

        
        def sorting_algorithm():
            # Run the sorting algorithm
            algorithms[self.ids.algorithm.text](self.rectangles, self, speed)


        
        # Start the sorting algorithm on a separate thread
        self.sorting = Thread(target=sorting_algorithm, daemon=True)
        self.sorting.start()

    def draw(self, rects, colorArray):
        Clock.schedule_once(lambda dt: self._draw(rects, colorArray))



    def _draw(self, rects, colorArray):
        # Clock.schedule_once(lambda dt: self.visualizer.canvas.clear())
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
        
    

    def update(self, *args):
        Clock.schedule_once(lambda dt: self.draw(self.rectangles, [RED for i in range(len(self.rectangles))]))
        # self.draw(self.rectangles, [RED for i in range(len(self.rectangles))])


class Visualizer(Widget):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)


class VisualizeSortApp(App):
    def build(self):
        return SortVisualizer()


if __name__ == "__main__":
    VisualizeSortApp().run()

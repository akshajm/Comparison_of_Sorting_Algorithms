from flask import Flask, render_template, request
from sorting_data import *
import numpy as np
import time

app = Flask(__name__)

SORTING_NAMES = ["All", "Heap sort", "Merge sort", "Insertion sort",
                 "Selection sort", "Bubble sort", "Quick sort", "Quick sort(3 median)"]


@app.route("/")
def main():
    return render_template('html/dashboard.html', sorting_names=SORTING_NAMES)


@app.route("/custom_sort", methods=["POST", "GET"])
def custom_sort():
    sort_type = request.form['sort']
    array = request.form['array'].replace(" ", "").split(",")
    array = list(map(int, array))
    x_axis = [0]
    y_axis = [0]
    sorted_data = {}
    if sort_type != 'All':
        start = time.time()
        x_axis.append(len(array))
        if sort_type == 'Heap sort':
            heap_sort_object = HeapSort(array)
            sorted_array = heap_sort_object.heap_sort()
        elif sort_type == 'Merge sort':
            sorted_array = merge_sort(array)
        elif sort_type == 'Insertion sort':
            insertion_sort_object = InsertionSort(array)
            sorted_array = insertion_sort_object.insertion_sort()
        elif sort_type == 'Selection sort':
            selection_sort_object = SelectionSort(array)
            sorted_array = selection_sort_object.selection_sort()
        elif sort_type == 'Bubble sort':
            bubble_sort_object = BubbleSort(array)
            sorted_array = bubble_sort_object.bubble_sort()
        elif sort_type == 'Quick sort':
            sorted_array = quick_sort(array)
        elif sort_type == 'Quick sort(3 median)':
            sorted_array = quick_sort_3_median(array)
        end = time.time()
        y_axis.append(end - start)
        plotly = Plotly(x_axis, y_axis, sort_type, "Input size", "Time(in seconds)", sort_type)
        graph_data = [plotly.get_trace()]
        layout = plotly.get_layout()

        sorted_data[sort_type] = [str(sorted_array), end - start]
    else:
        graph_data = []
        for zz in SORTING_NAMES[1:]:
            x_axis = [0]
            y_axis = [0]
            start = time.time()
            x_axis.append(len(array))
            if zz == 'Heap sort':
                heap_sort_object = HeapSort(array)
                sorted_array = heap_sort_object.heap_sort()
            elif zz == 'Merge sort':
                sorted_array = merge_sort(array)
            elif zz == 'Insertion sort':
                insertion_sort_object = InsertionSort(array)
                sorted_array = insertion_sort_object.insertion_sort()
            elif zz == 'Selection sort':
                selection_sort_object = SelectionSort(array)
                sorted_array = selection_sort_object.selection_sort()
            elif zz == 'Bubble sort':
                bubble_sort_object = BubbleSort(array)
                sorted_array = bubble_sort_object.bubble_sort()
            elif zz == 'Quick sort':
                sorted_array = quick_sort(array)
            elif zz == 'Quick sort(3 median)':
                sorted_array = quick_sort_3_median(array)
            end = time.time()
            y_axis.append(end - start)
            plotly = Plotly(x_axis, y_axis, zz, "Input size", "Time(in seconds)", "All sorting techniques")
            trace = plotly.get_trace()
            graph_data.append(trace)
            sorted_data[zz] = [str(sorted_array), end - start]
        layout = plotly.get_layout()
    return render_template('html/solution_page.html', graph_data=graph_data, sorted_data=sorted_data
                           , layout=layout, show_data="True")


@app.route("/comparison_page_solution")
def compare():
    comparison_sorting = [request.args['sort_a'], request.args['sort_b']]
    list_size = int(request.args['size'])
    iteration = list_size // 10
    graph_data = []
    for sorting_type in comparison_sorting:
        x_axis = [0]
        y_axis = [0]
        for i in range(1, 11):
            array = np.random.randint(0, list_size, size=iteration * i)
            start = time.time()
            x_axis.append(len(array))
            if sorting_type == 'Heap sort':
                heap_sort_object = HeapSort(array)
                _ = heap_sort_object.heap_sort()
            elif sorting_type == 'Merge sort':
                _ = merge_sort(array)
            elif sorting_type == 'Insertion sort':
                insertion_sort_object = InsertionSort(array)
                _ = insertion_sort_object.insertion_sort()
            elif sorting_type == 'Selection sort':
                selection_sort_object = SelectionSort(array)
                _ = selection_sort_object.selection_sort()
            elif sorting_type == 'Bubble sort':
                bubble_sort_object = BubbleSort(array)
                _ = bubble_sort_object.bubble_sort()
            elif sorting_type == 'Quick sort(3 median)':
                _ = quick_sort_3_median(array)
            elif sorting_type == 'Quick sort':
                _ = quick_sort(array)
            end = time.time()
            y_axis.append(end - start)
        plotly = Plotly(x_axis, y_axis, sorting_type, "Input size", "Time(in seconds)"
                        , [comparison_sorting[0], comparison_sorting[1]])
        trace = plotly.get_trace()
        graph_data.append(trace)
    layout = plotly.get_layout()
    return render_template('html/solution_page.html', graph_data=graph_data, layout=layout, show_data="False")


@app.route("/solution_page")
def solution():
    sort_type = request.args['sort']
    list_size = int(request.args['size'])
    iteration = list_size // 10
    x_axis = [0]
    y_axis = [0]

    if sort_type != 'All':
        for i in range(1, 11):
            array = np.random.randint(0, list_size, size=iteration * i)
            start = time.time()
            x_axis.append(len(array))
            if sort_type == 'Heap sort':
                heap_sort_object = HeapSort(array)
                _ = heap_sort_object.heap_sort()
            elif sort_type == 'Merge sort':
                _ = merge_sort(array)
            elif sort_type == 'Insertion sort':
                insertion_sort_object = InsertionSort(array)
                _ = insertion_sort_object.insertion_sort()
            elif sort_type == 'Selection sort':
                selection_sort_object = SelectionSort(array)
                _ = selection_sort_object.selection_sort()
            elif sort_type == 'Bubble sort':
                bubble_sort_object = BubbleSort(array)
                _ = bubble_sort_object.bubble_sort()
            elif sort_type == 'Quick sort':
                _ = quick_sort(array)
            elif sort_type == 'Quick sort(3 median)':
                _ = quick_sort_3_median(array)
            end = time.time()
            y_axis.append(end - start)
        plotly = Plotly(x_axis, y_axis, sort_type, "Input size", "Time(in seconds)", sort_type)
        graph_data = [plotly.get_trace()]
        layout = plotly.get_layout()
    else:
        graph_data = []
        for sorting_type in SORTING_NAMES[1:]:
            x_axis = [0]
            y_axis = [0]
            for i in range(1, 11):
                array = np.random.randint(0, list_size, size=iteration * i)
                start = time.time()
                x_axis.append(len(array))
                if sorting_type == 'Heap sort':
                    heap_sort_object = HeapSort(array)
                    _ = heap_sort_object.heap_sort()
                elif sorting_type == 'Merge sort':
                    _ = merge_sort(array)
                elif sorting_type == 'Insertion sort':
                    insertion_sort_object = InsertionSort(array)
                    _ = insertion_sort_object.insertion_sort()
                elif sorting_type == 'Selection sort':
                    selection_sort_object = SelectionSort(array)
                    _ = selection_sort_object.selection_sort()
                elif sorting_type == 'Bubble sort':
                    bubble_sort_object = BubbleSort(array)
                    _ = bubble_sort_object.bubble_sort()
                elif sorting_type == 'Quick sort':
                    _ = quick_sort(array)
                elif sort_type == 'Quick sort(3 median)':
                    _ = quick_sort_3_median(array)
                end = time.time()
                y_axis.append(end - start)
            plotly = Plotly(x_axis, y_axis, sorting_type, "Input size", "Time(in seconds)", "All sorting techniques")
            trace = plotly.get_trace()
            graph_data.append(trace)
        layout = plotly.get_layout()
    return render_template('html/solution_page.html', graph_data=graph_data, layout=layout, show_data="False")


if __name__ == "__main__":
    app.run()

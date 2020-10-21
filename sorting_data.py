class Sorting:
    def __init__(self, array):
        self.array = array

    def element_swap(self, i, j):
        self.array[i], self.array[j] = self.array[j], self.array[i]


class BubbleSort(Sorting):
    def __init__(self, array):
        super().__init__(array)

    def bubble_sort(self):
        for i in range(len(self.array)):
            for j in range(len(self.array) - 1 - i):
                if self.array[j + 1] < self.array[j]:
                    super().element_swap(j, j + 1)
        return self.array


class HeapSort(Sorting):
    def __init__(self, array):
        super().__init__(array)

    def heap_sort(self):
        self.build_max_heap()
        for end_index in reversed(range(1, len(self.array))):
            super().element_swap(0, end_index)
            self.sift_down(0, end_index - 1)
        return self.array

    def build_max_heap(self):
        first_parent = len(self.array) - 2 // 2
        for current_index in reversed(range(first_parent)):
            self.sift_down(current_index, len(self.array) - 1)

    def sift_down(self, start_index, end_index):
        child_one = 2 * start_index + 1
        while child_one <= end_index:
            child_two = (2 * start_index + 2) if (2 * start_index + 2) <= end_index else -1
            if self.array[child_one] > self.array[child_two] or child_two == -1:
                index_to_swap = child_one
            else:
                index_to_swap = child_two

            if self.array[start_index] < self.array[index_to_swap]:
                super().element_swap(start_index, index_to_swap)
                start_index = index_to_swap
                child_one = 2 * start_index + 1
            else:
                return


class InsertionSort(Sorting):
    def __init__(self, array):
        super().__init__(array)

    def insertion_sort(self):
        for i in range(1, len(self.array)):
            j = i
            while j > 0 and self.array[j] < self.array[j - 1]:
                self.element_swap(j, j - 1)
                j -= 1
        return self.array


class SelectionSort(Sorting):
    def __init__(self, array):
        super().__init__(array)

    def selection_sort(self):
        for i in range(len(self.array) - 1):
            current = i
            smallest = current
            for j in range(current + 1, len(self.array)):
                if self.array[j] < self.array[smallest]:
                    smallest = j
            self.element_swap(smallest, current)
        return self.array


def merge_sort(array):
    if len(array) <= 1:
        return array
    mid = len(array) // 2
    left_sub_array = array[0:mid]
    right_sub_array = array[mid:len(array)]
    left_sub_array = merge_sort(left_sub_array)
    right_sub_array = merge_sort(right_sub_array)
    return merge(left_sub_array, right_sub_array)


def merge(left_array, right_array):
    solution_array = []
    initial_index_left = initial_index_right = 0
    while initial_index_left < len(left_array) and initial_index_right < len(right_array):
        if left_array[initial_index_left] <= right_array[initial_index_right]:
            solution_array.append(left_array[initial_index_left])
            initial_index_left += 1
        else:
            solution_array.append(right_array[initial_index_right])
            initial_index_right += 1

    while initial_index_left < len(left_array):
        solution_array.append(left_array[initial_index_left])
        initial_index_left += 1

    while initial_index_right < len(right_array):
        solution_array.append(right_array[initial_index_right])
        initial_index_right += 1

    return solution_array


def quick_sort(array):
    quick_sort_helper(0, len(array) - 1, array)
    return array


def quick_sort_helper(start_index, end_index, array):
    if start_index >= end_index:
        return
    pivot_index = start_index
    left = start_index + 1
    right = end_index

    while left <= right:
        if array[left] > array[pivot_index] and array[right] < array[pivot_index]:
            array[left], array[right] = array[right], array[left]
        if array[left] <= array[pivot_index]:
            left += 1
        if array[right] >= array[pivot_index]:
            right -= 1

    array[pivot_index], array[right] = array[right], array[pivot_index]

    left_is_smaller = right - 1 - start_index < end_index - (right + 1)

    if left_is_smaller:
        quick_sort_helper(start_index, right - 1, array)
        quick_sort_helper(right + 1, end_index, array)
    else:
        quick_sort_helper(right + 1, end_index, array)
        quick_sort_helper(start_index, right - 1, array)


def get_median_value(left, middle, right):
    return sorted([left, middle, right])[1]


def quick_sort_3_median_helper(start, end, array):
    pivot = (start + end) // 2
    pivot_index = get_pivot_index(array, start, end, pivot)
    array[pivot_index], array[end] = array[end], array[pivot_index]
    left_index = start - 1
    for right_index in range(start, end):
        if array[right_index] <= array[end]:
            left_index = left_index + 1
            array[left_index], array[right_index] = array[right_index], array[left_index]
    array[left_index + 1], array[end] = array[end], array[left_index + 1]
    return left_index + 1


def quick_sort_3_median(array):
    return quick_sort_3_median_recursion(0, len(array) - 1, array)


def quick_sort_3_median_recursion(start_index, end_index, array):
    if start_index < end_index:
        pivot_index = quick_sort_3_median_helper(start_index, end_index, array)
        quick_sort_3_median_recursion(start_index, pivot_index - 1, array)
        quick_sort_3_median_recursion(pivot_index + 1, end_index, array)
    return array


def get_pivot_index(array, start, end, pivot):
    if array[start] < array[end]:
        return end if array[end] < array[pivot] else pivot
    else:
        return start if array[start] < array[pivot] else pivot


class Plotly:
    def __init__(self, x_axis_value, y_axis_value, name_of_trace, x_axis_name, y_axis_name, graph_title):
        self.x_axis_value = x_axis_value
        self.y_axis_value = y_axis_value
        self.name_of_trace = name_of_trace
        self.x_axis_name = x_axis_name
        self.y_axis_name = y_axis_name
        self.graph_title = graph_title

    def get_trace(self):
        return {
            'x': self.x_axis_value,
            'y': self.y_axis_value,
            'type': 'scatter',
            'name': self.name_of_trace
        }
        # aa = quick_sort_alternative([1,5,3,2,4])

    def get_layout(self):
        if type(self.graph_title) == list:
            return {
                'showlegend': True,
                'title': "{} vs {}".format(self.graph_title[0], self.graph_title[1]),
                'xaxis': {"title": {"text": self.x_axis_name}},
                'yaxis': {"title": {"text": self.y_axis_name}}
            }
        else:
            return {
                'showlegend': True,
                'title': "{}".format(self.graph_title),
                'xaxis': {"title": {"text": self.x_axis_name}},
                'yaxis': {"title": {"text": self.y_axis_name}}
            }

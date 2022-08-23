class Algol:
    @staticmethod
    def binary_search(items, item):
        low_index = 0
        high_index = len(items) - 1

        while low_index < high_index:
            middle_index = (low_index + high_index) // 2
            guess = items[middle_index]
            if guess == item:
                return middle_index
            if guess > item:
                high_index = middle_index - 1
            else:
                low_index = middle_index + 1
        return None

    @staticmethod
    def simple_moving_average(timeseries, window):
        result = []
        for begin_index in range(len(timeseries) - window):
            end_index = begin_index + window
            current_sum = 0
            for v in timeseries[begin_index:end_index]:
                current_sum += v
            current_avg = current_sum / window
            result.append(current_avg)
        return result

    @staticmethod
    def optimus_moving_average(timeseries, window):
        result = []
        current_sum = sum(timeseries[:window])
        result.append(current_sum / window)
        for i in range(0, len(timeseries) - window - 1):
            current_sum -= timeseries[i]
            current_sum += timeseries[i + window]
            current_avg = current_sum / window
            result.append(current_avg)
        return result

    @staticmethod
    def find_smallest(items: list):
        smallest = items[0]
        smallest_index = 0
        for i in range(1, len(items)):
            if items[i] < smallest:
                smallest = items[i]
                smallest_index = i
        return smallest_index

    @staticmethod
    def selection_sort(items: list):
        sorted_items = []
        for i in range(len(items)):
            smallest_index = Algol.find_smallest(items)
            sorted_items.append(items.pop(smallest_index))
        return sorted_items

    @staticmethod
    def recursion_find_number(items: list, item: int):
        for i in range(len(items)):
            if not items:
                return None
            if items[i] != item:
                Algol.recursion_find_number(items[i+1:], item)
            else:
                return i
        return None

    @staticmethod
    def recursion_down(num: int):
        if num < 0:
            return
        else:
            print(f'{num=}')
            Algol.recursion_down(num - 1)

    @staticmethod
    def recursion_factorial(num: int):
        if num == 1:
            return 1
        else:
            return num * Algol.recursion_factorial(num - 1)

    @staticmethod
    def recursion_nod(a: int, b: int):
        if a % b == 0:
            return b
        else:
            return Algol.recursion_nod(b, a % b)

    @staticmethod
    def recursion_summer(num: int):
        if num == 1:
            return 1
        else:
            return num + Algol.recursion_summer(num - 1)
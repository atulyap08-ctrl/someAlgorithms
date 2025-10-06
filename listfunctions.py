class List_Functions:
    def __init__(self):
        self.low = 0
        self.high = 0
        self.array = []
        self.middle = 0
        self.guess_val = 0

    def add_constant(self, array: list, const: float) -> list:
        self.u = 0
        for i in array:
            self.u = i + const
            i = self.u
            i += 1
        return array

    def reverse_array(self, numbers) -> list:
        self.number2 = []
        for i in reversed(numbers):
            # number2.insert(0,i)
            self.number2.append(i)

        return self.number2

    def find_highest(self, array) -> float:
        self.highest = array[0]
        for i in array:
            if i > self.highest:
                self.highest = i
            else:
                self.highest = self.highest
        return self.highest

    def fcd(a, no) -> None:
        count = 0
        for i in a:
            if i == no:
                count += 1
                if count > 1:
                    a.remove(no)
            else:
                count = count
        if count > 1:
            print(f"The element {no} has appeared more than once.")
            print(f"after deleting the duplicated values the clean array is: ")
            print(
                    f"""
                    New array:
        
                    {a}
        
                    """
                )
        elif count < 1:
            print(f"the element {no} does not exist.")
        elif count == 1:
            print(f"the element {no} has appeared only once.")

    def add_elements(self, array) -> float:
        self.a = 0
        for j in array:
            self.a = j + self.a
        return self.a

    def find_smallest(self, array) -> float:
        self.smallest = array[0]
        for i in array:
            if i < self.smallest:
                self.smallest = i
            else:
                self.smallest = self.smallest
        return self.smallest

    def selection_sort(self, array) -> list:
        self.fixd = []
        for x in range(len(array)):
            self.s = List_Functions.find_smallest(array)
            self.fixd.append(self.s)
            self.array.remove(self.s)
        return self.fixd

    def quick_sort(self, array):
        self.array_right = []
        self.array_left = []
        if len(array) <= 1:
            return array
        else:
            self.index = len(array) // 2
            self.pivot = array[self.index]
            array.remove(self.pivot)
            for j in array:
                if j > self.pivot:
                    self.array_right.append(j)
                elif j <= self.pivot:
                    self.array_left.append(j)

            return (
                List_Functions.quick_sort(self, self.array_left)
                + [self.pivot]
                + List_Functions.quick_sort(self, self.array_right)
            )

    def qsort_highest_to_lowest(self, array):
        self.array_right = []
        self.array_left = []
        if len(array) <= 1:
            return array
        else:
            self.index = len(array) // 2
            self.pivot = array[self.index]
            array.remove(self.pivot)
            for j in array:
                if j > self.pivot:
                    self.array_right.append(j)
                elif j <= self.pivot:
                    self.array_left.append(j)

            return (
                List_Functions.qsort_highest_to_lowest(self, self.array_right)
                + [self.pivot]
                + List_Functions.qsort_highest_to_lowest(self, self.array_left)
            )

    def binary_search(self, array: list, val_to_find):
        self.low = 0
        self.high = len(array) - 1
        self.array = List_Functions.quick_sort(self, array)
        while self.low < self.high:
            self.middle = (self.low + self.high) // 2
            self.guess_val: int = array[self.middle]
            if self.guess_val == val_to_find:
                #"the number {self.guess_val} exists in array."
                return True
            if self.guess_val > val_to_find:
                self.high = self.middle - 1
                # array2 = array[low:high]
                # binary_search_integers(array2, val_to_find)
            elif self.guess_val < val_to_find:
                self.low = self.middle + 1
                # arra3y = array[low:high]
                # binary_search_integers(arra3y,val_to_find)
            else:
                return False
        return False

    def add_elements_recursion(self, arr: list):
        if len(arr) == 0:
            return 0
        else:
            self.m = arr[0]
            arr.remove(arr[0])
            self.j = self.m + List_Functions.add_elements_recursion(self, arr)
            return self.j

    def concatenate(self, list2: list, list1: list):
        for i in list2:
            list1.append(i)
        return list1

    def concatenate2(self, list1: list, list2: list):
        self.list3 = list1 + list2
        return self.list3

    def concatenate3(self, list1: list, list2: list):
        self.list3 = [*list1, *list2]
        return self.list3

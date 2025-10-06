#quicksort and binary search.
import age as age
import gender as gender


def quicksort(array):
    if len(array) <= 1:
        return array
    else:
        i = len(array) // 2
        pivot = array[i]
        array.remove(pivot)
        larger = []
        smaller = []
        for l in array:
            if l > pivot:
                larger.append(l)
            elif l < pivot:
                smaller.append(l)

        return quicksort(smaller) + [pivot] + quicksort(larger)


def binary_search(array, value):
    start = 0
    end = len(array)-1
    array = quicksort(array)
    while start < end:
        middle = (start + end)//2
        guess_val = array[middle]
        if guess_val == value:
            return guess_val
        if guess_val < value:
            start = middle + 1
        if guess_val > value:
            end = middle - 1
    return None





k = [4, 5, 2, 3, 1]
print(binary_search(k, 3))

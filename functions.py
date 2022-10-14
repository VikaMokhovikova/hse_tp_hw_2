def _min(array):
    min_value = array[0]
    for i in range(1, len(array)):
        if array[i] < min_value:
            min_value = array[i]
    return min_value


def _max(array):
    max_value = array[0]
    for i in range(1, len(array)):
        if array[i] > max_value:
            max_value = array[i]
    return max_value

def _sum(array):
    summ = 0
    for i in range(len(array)):
        summ += array[i]
    return summ

def _mult(array):
    mult = array[0]
    for i in range(1, len(array)):
        mult *= array[i]
    return mult
def _min(array):
    min_value = array[0]
    for i in range(1, len(array)):
        if array[i] < min_value:
            min_value = array[i]
    return min_value


def _max(array):
    max_value = array[0]
    for i in range(1, len(array)):
        if array[i] >= max_value:
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


if __name__ == '__main__':
    with open('file1.txt', 'r') as file1:
        array = list(map(int, file1.readline().split()))
    print('Результат работы _min', _min(array))
    print('Результат работы _max', _max(array))
    print('Результат работы _sum', _sum(array))
    print('Результат работы _mult', _mult(array))

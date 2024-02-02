# Напишите программу на Python, которая будет находить сумму элементов массива из 1000000 целых чисел.
# Пример массива: arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, ...]
# Массив должен быть заполнен случайными целыми числами от 1 до 100.
# При решении задачи нужно использовать многопоточность, многопроцессорность и асинхронность.
# В каждом решении нужно вывести время выполнения вычислений.
# ============================================================
import threading
import time
from params import step, numbers

total_summ = 0


def sum_count(nums: list):
    global total_summ
    total_summ += sum(nums)


threads = []
start_time = time.time()

for start in range(0, len(numbers) - 1, step):
    slice = numbers[start:start + step]
    thr = threading.Thread(target=sum_count, args=(slice,))
    threads.append(thr)
    thr.start()

for thr in threads:
    thr.join()

print(f'Сумма элементов = {total_summ}.\nПосчитано за {time.time() - start_time} сек.')

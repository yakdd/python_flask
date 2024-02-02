import multiprocessing
import time
from params import step, numbers

total_summ = multiprocessing.Value('i', 0)


def sum_count(nums, tot_summ):
    with tot_summ.get_lock():
        tot_summ.value += sum(nums)


if __name__ == '__main__':
    processes = []
    start_time = time.time()

    for start in range(0, len(numbers) - 1, step):
        slice = numbers[start:start + step]
        proc = multiprocessing.Process(target=sum_count, args=(slice, total_summ))
        processes.append(proc)
        proc.start()

    for proc in processes:
        proc.join()

    print(f'Сумма элементов = {total_summ.value}.\nПосчитано за {time.time() - start_time} сек.')

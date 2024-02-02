import asyncio
import time
from params import step, numbers

total_summ = 0


async def sum_count(nums: list):
    global total_summ
    total_summ += sum(nums)


async def main():
    tasks = []
    for start in range(0, len(numbers) - 1, step):
        slice = numbers[start:start + step]
        tasks.append(asyncio.create_task(sum_count(slice)))
    await asyncio.gather(*tasks)


if __name__ == '__main__':
    start_time = time.time()
    asyncio.run(main())
    print(f'Сумма элементов = {total_summ}.\nПосчитано за {time.time() - start_time} сек.')
import multiprocessing
import time
from params import urls
from images_loader import images_loader


def main(urls):
    processes = []
    start = time.time()
    for url in urls:
        proc = multiprocessing.Process(target=images_loader, args=(url,))
        processes.append(proc)
        proc.start()

    for proc in processes:
        proc.join()

    print(f'Общее время загрузки {time.time() - start:.5f} секунд')


if __name__ == '__main__':
    main(urls)

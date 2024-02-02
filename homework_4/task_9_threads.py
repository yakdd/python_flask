# Написать программу, которая скачивает изображения с заданных URL-адресов и сохраняет их на диск.
# Каждое изображение должно сохраняться в отдельном файле, название которого соответствует названию
# изображения в URL-адресе.
# Например, URL-адрес: https://example/images/image1.jpg -> файл на диске: image1.jpg
# — Программа должна использовать многопоточный, многопроцессорный и асинхронный подходы.
# — Программа должна иметь возможность задавать список URL-адресов через аргументы командной строки.
# — Программа должна выводить в консоль информацию о времени скачивания каждого изображения и общем
# времени выполнения программы.
# ===============================================================
import threading
import time
from params import urls
from images_loader import images_loader


def main(urls):
    threads = []
    start = time.time()
    for url in urls:
        thr = threading.Thread(target=images_loader, args=(url,))
        threads.append(thr)
        thr.start()

    for thr in threads:
        thr.join()

    print(f'Общее время загрузки {time.time() - start:.5f} секунд')


if __name__ == '__main__':
    main(urls)

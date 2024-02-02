import requests
import time


def images_loader(url):
    start_for_image = time.time()
    response = requests.get(url)
    file_name = url.split('/')[-1]
    with open(file_name, 'wb') as file:
        file.write(response.content)
    print(f'Файл "{file_name}" загружен за {time.time() - start_for_image:.5f} секунд')

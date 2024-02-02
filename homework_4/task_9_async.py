import asyncio
import aiohttp
import time
from params import urls


async def images_loader(url):
    start_for_image = time.time()
    file_name = url.split('/')[-1]
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            content = await response.content.read()
            with open(file_name, 'wb') as file:
                file.write(content)
            print(f'Файл "{file_name}" загружен за {time.time() - start_for_image:.5f} секунд')


async def main(urls):
    tasks = []
    for url in urls:
        task = asyncio.ensure_future(images_loader(url))
        tasks.append(task)
    await asyncio.gather(*tasks)


if __name__ == '__main__':
    start = time.time()
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main(urls))
    print(f'Общее время загрузки {time.time() - start:.5f} секунд')

import asyncio
from asyncio import create_task
import requests

# можно подкинуть свой список в таком же формате
users = [("Alice", 2), ("Bob", 3), ("Charlie", 1), ("Diana", 4)]


# обьявляю карутину для отправки письма
async def send_notification(user, delay):
    print(f'Начинаю отправку сообщения {user} это займет {delay} cек')
    await asyncio.sleep(delay)
    print(f'Отправка сообщения {user} завершена')


async def main(users):
    tasks = []

    for user, delay in users:
        # cоздаю задачи для  представления выполнения карутин
        tasks.append(create_task(send_notification(user, delay)))
    # запускаю все задачи из списка
    await asyncio.gather(*tasks)


asyncio.run(main(users))

import asyncio

# можно подкинуть свой список в таком же формате
users = [("Alice", 2), ("Bob", 3), ("Charlie", 1), ("Diana", 4)]


# обьявляю карутину для отправки письма
async def send_email(recipient, delay):
    print(f'Начинаю отправку письма для {recipient}...')
    await asyncio.sleep(delay)  # установливаю задержку для имитации отправки
    print(f'Письмо для {recipient} отправлено!')


async def main():
    tasks = []
    if users:
        for mail in users:
            tasks.append(asyncio.create_task(send_email(*mail)))
            # cоздаю задачи для  представления выполнения карутин
        await asyncio.gather(*tasks)  # запускаю все задачи из списка
    else:
        print('список пользователей пуст')


asyncio.run(main())  # запускаю основную функцию

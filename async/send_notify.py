import threading
import time


# можно подкинуть свой список в таком же формате
users = [("Alice", 2), ("Bob", 3), ("Charlie", 1), ("Diana", 4)]


# обьявляю функцию для отправки писем
def send_notification(user, delay):
    print(f'Начинаю отправку сообщения {user} это займет {delay} cек')
    time.sleep(delay)
    print(f'Отправка сообщения {user} завершена')

# создаю файл main в котором запускюа потоки
def main(users):
    threads = []
    for user, delay in users:
       th = threading.Thread(target= send_notification,args=(user,delay)) # создание потока
       th.start() # запуск потоков
       threads.append(th)

    for thread in threads: #join для  ожидания завершения
        thread.join()

if __name__ == '__main__':
    main(users)

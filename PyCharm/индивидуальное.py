#!/usr/bin/env python3
# -*- coding: utf-8 -*

import sys

if __name__ == '__main__':
    print("Список команд:\n")
    print("add - добавить информацию;")
    print("list - вывести список ;")
    print(
        "select <тип> - вывод на экран фамилия, имя; знак Зодиака; дата рождения ")
    print("help - отобразить справку;")
    print("exit - завершить работу с программой.")
    # Список работников.
    workers = []

    # Организовать бесконечный цикл запроса команд.
    while True:
        # Запросить команду из терминала.
        command = input(">>> ").lower()
        # Выполнить действие в соответствие с командой.

        if command == 'exit':
            break

        elif command == 'add':
        # Запросить данные о работнике.
            name = input("Фамилия и инициалы? ")
            post = input("знак зодиака? ")
            year = int(input("Год поступления? "))

            # Создать словарь.
            worker = {'name': name, 'знак зодиака': post, 'year': year}

            # Добавить словарь в список.
            workers.append(worker)

            # Отсортировать список в случае необходимости.
            if len(workers) > 1:
                workers.sort(key=lambda item: item.get('name', ''))

        elif command == 'list':
            # Заголовок таблицы.
            line = '+-{}-+-{}-+-{}-+-{}-+'.format(
            '-' * 4,
            '-' * 30,
            '-' * 20,
            '-' * 8
            )
            print(line)

            # Вывести данные о всех сотрудниках.
            for idx, worker in enumerate(workers, 1):
                print(
                    '| {:>4} | {:<30} | {:<20} | {:>8} |'.format(
                        idx,
                        worker.get('name', ''),
                        worker.get('знак зодиака', ''),
                        worker.get('year', 0)
                    )
            )
            print(line)

        elif command.startswith('select '):

            # Получить текущую дату.
            today = date.today()

            # Разбить команду на части для выделения номера года.
            parts = command.split(' ', maxsplit=1)

            # Получить требуемый стаж.
            period = int(parts[1])

            # Инициализировать счетчик.
            count = 0

            # Проверить сведения работников из списка.
            for worker in workers:
                if today.year - worker.get('year', today.year) >= period:
                    count += 1
            print(
                '{:>4}: {}'.format(count, worker.get('name', ''))
            )

            # Если счетчик равен 0, то работники не найдены.
            if count == 0:
                print("информация не найдена.")

        elif command == 'help':
            # Вывести справку о работе с программой.
            print("Список команд:\n")
            print("add - добавить работника;")
            print("list - вывести список работников;")
            print("select <стаж> - запросить работников со стажем;")
            print("help - отобразить справку;")
            print("exit - завершить работу с программой.")

        else:
            print(f"Неизвестная команда {command}", file=sys.stderr)

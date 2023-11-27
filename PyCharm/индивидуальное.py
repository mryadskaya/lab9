#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys

if __name__ == '__main__':
    print("Список команд:\n")
    print("add - добавить информацию;")
    print("list - вывести список ;")
    print("select <тип> - вывод на экран фамилия, имя; знак Зодиака; дата рождения ")
    print("help - отобразить справку;")
    print("exit - завершить работу с программой.")

    # Список работников.
    birthday = []

    # Организовать бесконечный цикл запроса команд.
    while True:
        # Запросить команду из терминала.
        command = input(">>> ").lower()

        # Выполнить действие в соответствие с командой.
        match command:
            case 'exit':
                break

            case 'add':
                # Запросить данные о работнике.
                name = input("Фамилия и имя? ")
                zodiac = input("Знак зодиака? ")
                date = input("дата рождения? ")

                # Создать словарь.
                i = {'name': name, 'zodiac': zodiac, 'data': date}

                # Добавить словарь в список.
                birthday.append(i)

                # Отсортировать список в случае необходимости.
                if len(birthday) > 1:
                    birthday.sort(key=lambda item: item.get('data', ''))

            case 'list':
                # Заголовок таблицы.
                line = '+-{}-+-{}-+-{}-+-{}-+'.format(
                    '-' * 4,
                    '-' * 30,
                    '-' * 20,
                    '-' * 8
                )
                print(line)

                # Вывести данные о всех сотрудниках.
                for idx, i in enumerate(birthday, 1):
                    print(
                        '| {:>4} | {:<30} | {:<20} | {:>8} |'.format(
                            idx,
                            i.get('name', ''),
                            i.get('zodiac', ''),
                            i.get('data', '')
                        )
                    )
                print(line)

            case 'select ':
                # Разбить команду на части для выделения номера года.
                parts = input("Введите значение: ")

                # Проверить сведения работников из списка.
                count = 0
                for i in birthday:
                    for k, v in i.items():
                        if v == parts:
                            print("фамилия и имя - ", i["name"])
                            print("знак зодиака - ", i["zodiac"])
                            count += 1

                # Если счетчик равен 0, то работники не найдены.
                if count == 0:
                    print("информация не найдена.")

            case 'help':
                # Вывести справку о работе с программой.
                print("Список команд:\n")
                print("add - добавить информацию;")
                print("list - вывести список ;")
                print(
                    "select <тип> - ввывод на экран фамилия, имя; знак Зодиака; дата рождения")
                print("help - отобразить справку;")
                print("exit - завершить работу с программой.")

            case _:
                print(f"Неизвестная команда {command}")
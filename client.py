from configs import get_client_socket

from console_menu import MENU, print_menu, get_command, check_command

from funcs import send_mes, get_mes, client_check_connection,\
    exit_client


s = get_client_socket()

name = input("Введите свой никнейм: ")
menu = MENU
actions = (send_mes, exit_client)

if client_check_connection(s) is True:

    while True:
        print_menu(menu)
        command = get_command()

        if check_command(menu, command) is True:
            actions[command - 1](s, name)
            mes = get_mes(s)
            print(f"{mes['name']} -> {mes['text']}")
        else:
            print("Такой команды нет")
else:
    print("Не удалось подключиться.")
    s.close()


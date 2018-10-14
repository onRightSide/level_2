MENU = ("Послать сообшение", "Выйти")


def print_menu(menu):
    for i, m in enumerate(menu, start=1):
        print(f"{i}: {m}")


def get_command():
    while True:
        try:
            command = int(input("Введите номер команды: "))
            return command
        except ValueError:
            print("Неверно введен номер! Повторите ввод.")
            continue


def check_command(menu, command):
    if command in range(1, len(menu) + 1):
        return True
    else:
        return False


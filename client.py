from configs import get_client_socket, LOCAL_PORT, LOCAL_ADDRESS, CLIENT_PRESENCE, SERVER_APPROVAL, CLOSE

from common import send_prepared_mes, get_mes, form_mes


address = LOCAL_PORT
port = LOCAL_ADDRESS


def client_check_connection(s):
    send_prepared_mes(s, CLIENT_PRESENCE)
    answer = get_mes(s)
    if answer == SERVER_APPROVAL:
        return True
    else:
        return False


def exit_client(s):
    send_prepared_mes(s, CLOSE)
    s.close()
    exit()


def run():
    s = get_client_socket(address, port)

    name = input("Введите свой никнейм: ")

    if client_check_connection(s) is True:
        print("Соединение установлено")
        while True:
            text = input(f"{name} -> ")
            if "exit()" in text:
                exit_client(s)
            mes = form_mes(name, text)
            send_prepared_mes(s, mes)
            answer = get_mes(s)
            print(f"{answer['name']} -> {answer['text']}")
    else:
        print("Не удалось подключиться.")
        s.close()


if __name__ == "__main__":
    address = input("Адрес: ")
    port = int(input("Порт: "))
    run()


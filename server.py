from configs import CLOSE, get_server_socket, LOCAL_PORT, LOCAL_ADDRESS, CLIENT_PRESENCE, SERVER_APPROVAL, \
    SERVER_HELLO, SERVER_MOOD, SERVER_STANDART_ANSWER

from common import send_prepared_mes, get_mes


address = LOCAL_ADDRESS
port = LOCAL_PORT


def server_check_connection(s):

    mes = get_mes(s)

    if mes == CLIENT_PRESENCE:
        send_prepared_mes(s, SERVER_APPROVAL)
        return True
    else:
        return False


def form_answer(mes):
    if "Привет" in mes["text"]:
        return SERVER_HELLO
    elif "Как дела" in mes["text"]:
        return SERVER_MOOD
    else:
        return SERVER_STANDART_ANSWER


def run():
    s = get_server_socket(address, port)
    print("Ожидание соединения...")
    client, addr = s.accept()

    if server_check_connection(client) is True:
        print("Соединение установлено")
        while True:
            message = get_mes(client)
            if message == CLOSE:
                s.close()
                print("Соединение разорвано")
                exit()
            print(f"{message['name']} -> {message['text']}")
            answer = form_answer(message)
            send_prepared_mes(client, answer)
    else:
        print("Не удалось подключиться.")
        s.close()
        client.close()


if __name__ == "__main__":
    address = input("Адрес: ")
    port = int(input("Порт: "))
    run()


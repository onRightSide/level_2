import socket


LOCAL_ADDRESS = "localhost"
LOCAL_PORT = 9999

SERVER_NAME = "Server"

CLIENT_PRESENCE = {"presence": ""}
SERVER_APPROVAL = {"approval": ""}

SERVER_HELLO = {"name": SERVER_NAME,
                "text": "Привет!"}
SERVER_MOOD = {"name": SERVER_NAME,
               "text": "Да нормально"}
# SERVER_TIME =
SERVER_STANDART_ANSWER = {"name": SERVER_NAME,
                          "text": "На этом наши полномочия все"}

CLOSE = {"exit": ""}


def get_server_socket():
    s = socket.socket()
    address = input("Введите адрес сервера: ")
    while True:
        try:
            port = int(input("Введите порт: "))
            break
        except ValueError:
            print("Порт должен быть числом")
            continue
    s.bind((address, port))
    s.listen(1)
    return s


def get_client_socket():
    s = socket.socket()
    address = input("Введите адрес сервера: ")
    while True:
        try:
            port = int(input("Введите порт: "))
            break
        except ValueError:
            print("Порт должен быть числом")
            continue

    s.connect((address, port))
    return s




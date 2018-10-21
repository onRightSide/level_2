import socket


LOCAL_ADDRESS = "localhost"
LOCAL_PORT = 7777

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


def get_server_socket(address, port):
    s = socket.socket()
    s.bind((address, port))
    s.listen(1)
    return s


def get_client_socket(address, port):
    s = socket.socket()
    s.connect((address, port))
    return s




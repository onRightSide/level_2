import json

from configs import CLIENT_PRESENCE, SERVER_APPROVAL, CLOSE, \
    SERVER_HELLO, SERVER_MOOD, SERVER_STANDART_ANSWER


# Common

def pars_mes(mes):
    return json.loads(mes.decode("utf-8"))


def get_mes(s):
    return pars_mes(s.recv(1024))


def send_prepared_mes(s, mes):
    s.send(json.dumps(mes).encode("utf-8"))


def send_mes(s, name):
    mes = {"name": name, "text": input(f"{name} -> ")}
    s.send(json.dumps(mes).encode("utf-8"))


# Client

def client_check_connection(s):
    send_prepared_mes(s, CLIENT_PRESENCE)

    answer = get_mes(s)

    if answer == SERVER_APPROVAL:
        print("Соединение установлено")
        return True
    else:
        return False


def exit_client(s, *args):
    send_prepared_mes(s, CLOSE)
    s.close()
    print("Соединение разорвано")
    exit()


# Server

def server_check_connection(s):

    mes = get_mes(s)

    if mes == CLIENT_PRESENCE:
        send_prepared_mes(s, SERVER_APPROVAL)
        print("Соединение установлено")
        return True
    else:
        return False


def form_answer(mes):
    if "Привет" in mes["text"]:
        return SERVER_HELLO
    elif "Как дела?" in mes["text"]:
        return SERVER_MOOD
    else:
        return SERVER_STANDART_ANSWER


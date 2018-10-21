import json

from configs import CLIENT_PRESENCE, SERVER_APPROVAL, CLOSE, \
    SERVER_HELLO, SERVER_MOOD, SERVER_STANDART_ANSWER


# Common

def pars_mes(mes):
    return json.loads(mes)


def get_mes(s):
    return pars_mes(s.recv(1024).decode("utf-8"))


def form_mes(name, text):
    mes = {"name": name, "text": text}
    return mes


def send_prepared_mes(s, mes):
    s.send(json.dumps(mes).encode("utf-8"))
    return True


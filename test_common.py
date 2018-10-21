import unittest
import threading
import socket
import json

from common import pars_mes, get_mes, form_mes, send_prepared_mes
from configs import LOCAL_ADDRESS, LOCAL_PORT, CLOSE

TEST_JSON = {"name": "name", "text": "text"}
TEST_JSON_STRING = json.dumps(TEST_JSON)
TEST_CONNECTION_DATA = {"test": "test", "test_num": -1, "test_vector": [1, 2, 3]}


def test_server(*args):
    s = socket.socket()
    s.bind((LOCAL_ADDRESS, LOCAL_PORT))
    s.listen(1)

    client, addr = s.accept()

    if send_prepared_mes in args:
        send_prepared_mes(client, TEST_JSON)
        client.close()
        s.close()

    elif get_mes in args:
        client.send(json.dumps(TEST_JSON).encode("utf-8"))
        client.close()
        s.close()

    else:
        mes = json.loads(client.recv(1024).decode("utf-8"))

        if mes == TEST_CONNECTION_DATA:
            client.send(json.dumps(TEST_CONNECTION_DATA).encode("utf-8"))

        mes = json.loads(client.recv(1024).decode("utf-8"))

        if mes == CLOSE:
            client.close()
            s.close()


def test_client(*args):
    s = socket.socket()
    s.connect((LOCAL_ADDRESS, LOCAL_PORT))

    if send_prepared_mes in args:
        mes = json.loads(s.recv(1024).decode("utf-8"))
        s.close()
        return mes

    elif get_mes in args:
        mes = get_mes(s)
        s.close()
        return mes

    else:

        s.send(json.dumps(TEST_CONNECTION_DATA).encode("utf-8"))

        mes = json.loads(s.recv(1024).decode("utf-8"))

        if mes == TEST_CONNECTION_DATA:
            s.send(json.dumps(CLOSE).encode("utf-8"))
            s.close()

            return 0
        else:
            return -1


class TestCommon(unittest.TestCase):

    def test(self):

        t = threading.Thread(target=test_server)
        t.start()
        self.assertEqual(test_client(), 0)
        t.join()

    def test_pars_mes(self):

        self.assertEqual(pars_mes(TEST_JSON_STRING), TEST_JSON)

    def test_form_mes(self):

        self.assertEqual(form_mes("name", "text"), TEST_JSON)

    def test_send_prepared_mes(self):

        t = threading.Thread(target=test_server, args=(send_prepared_mes,))
        t.start()
        self.assertEqual(test_client(send_prepared_mes), TEST_JSON)
        t.join()

    def test_get_mes(self):

        t = threading.Thread(target=test_server, args=(get_mes,))
        t.start()
        self.assertEqual(test_client(get_mes), TEST_JSON)
        t.join()


if __name__ == "__main__":
    unittest.main()


import unittest
import threading
import socket
import json

from server import server_check_connection, form_answer
from configs import LOCAL_ADDRESS, LOCAL_PORT, CLIENT_PRESENCE, SERVER_HELLO, SERVER_MOOD,\
    SERVER_STANDART_ANSWER, CLOSE

ERROR_MES = {"error": ""}
TEST_CONNECTION_DATA = {"test": "test", "test_num": -1, "test_vector": [1, 2, 3]}
TEST_SERVER_HELLO = {"text": "Привет"}
TEST_SERVER_MOOD = {"text": "Как дела"}
TEST_SERVER_STANDART_ANSWER = {"text": "smth"}


def test_server(*args):
    s = socket.socket()
    s.bind((LOCAL_ADDRESS, LOCAL_PORT))
    s.listen(1)

    client, addr = s.accept()

    if server_check_connection in args:
        answer = server_check_connection(client)
        client.close()
        s.close()
        return answer
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

    if server_check_connection in args:
        s.send(json.dumps(CLIENT_PRESENCE).encode("utf-8"))
        s.recv(1024)
        s.close()
    else:

        s.send(json.dumps(TEST_CONNECTION_DATA).encode("utf-8"))

        mes = json.loads(s.recv(1024).decode("utf-8"))

        if mes == TEST_CONNECTION_DATA:
            s.send(json.dumps(CLOSE).encode("utf-8"))
            s.close()
            return 0
        else:
            return -1


class TestClient(unittest.TestCase):

    def test(self):

        t = threading.Thread(target=test_server)
        t.start()
        self.assertEqual(test_client(), 0)
        t.join()

    def test_server_check_connection(self):

        t = threading.Thread(target=test_client, args=(server_check_connection, ))
        t.start()
        answer = test_server(server_check_connection)

        self.assertTrue(answer)
        t.join()

    def test_form_answer(self):

        self.assertEqual(form_answer(TEST_SERVER_HELLO), SERVER_HELLO)
        self.assertEqual(form_answer(TEST_SERVER_MOOD), SERVER_MOOD)
        self.assertEqual(form_answer(TEST_SERVER_STANDART_ANSWER), SERVER_STANDART_ANSWER)


if __name__ == "__main__":
    unittest.main()

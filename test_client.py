import unittest
import threading
import socket
import json

from client import client_check_connection, exit_client
from configs import LOCAL_ADDRESS, LOCAL_PORT, SERVER_APPROVAL, CLIENT_PRESENCE, CLOSE

ERROR_MES = {"error": ""}
TEST_CONNECTION_DATA = {"test": "test", "test_num": -1, "test_vector": [1, 2, 3]}


def test_server(*args):
    s = socket.socket()
    s.bind((LOCAL_ADDRESS, LOCAL_PORT))
    s.listen(1)

    client, addr = s.accept()

    if client_check_connection in args:
        mes = json.loads(client.recv(1024).decode("utf-8"))

        if mes == CLIENT_PRESENCE:
            client.send(json.dumps(SERVER_APPROVAL).encode("utf-8"))
        else:
            client.send(json.dumps(ERROR_MES).encode("utf-8"))
        client.close()
        s.close()
    elif exit_client in args:
        mes = json.loads(client.recv(1024).decode("utf-8"))
        client.close()
        s.close()
        return mes
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

    if client_check_connection in args:
        answer = client_check_connection(s)
        s.close()
        return answer
    elif exit_client in args:
        exit_client(s)
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

    def test_client_check_connection(self):

        t = threading.Thread(target=test_server, args=(client_check_connection,))

        t.start()

        self.assertTrue(test_client(client_check_connection))
        t.join()

    def test_exit_client(self):

        t = threading.Thread(target=test_client, args=(exit_client,))

        t.start()

        self.assertEqual(test_server(exit_client), CLOSE)
        t.join()


if __name__ == "__main__":
    unittest.main()


from configs import CLOSE, get_server_socket

from funcs import send_prepared_mes, get_mes, server_check_connection,\
    form_answer


s = get_server_socket()
print("Ожидание соединения...")
client, addr = s.accept()

if server_check_connection(client) is True:

    while True:
        message = get_mes(client)
        if message == CLOSE:
            client.close()
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


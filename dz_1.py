# 1. Каждое из слов «разработка», «сокет», «декоратор» представить в строковом формате и проверить тип и содержание
# соответствующих переменных. Затем с помощью онлайн-конвертера преобразовать строковые представление в формат Unicode
# и также проверить тип и содержимое переменных.

str_arr = ["разработка", "сокет", "декоратор"]
for word in str_arr:
    print(word)
    print(type(word))
    print(len(word))
    print()

str_arr = ["\u0440\u0430\u0437\u0440\u0430\u0431\u043e\u0442\u043a\u0430", "\u0441\u043e\u043a\u0435\u0442",
           "\u0434\u0435\u043a\u043e\u0440\u0430\u0442\u043e\u0440"]
for bword in str_arr:
    print(bword)
    print(type(bword))
    print(len(bword))
    print()

# 2. Каждое из слов «class», «function», «method» записать в байтовом типе без преобразования в последовательность
# кодов (не используя методы encode и decode) и определить тип, содержимое и длину соответствующих переменных.

def code(_str, key):
    return "".join([chr(ord(char)+ord(key)-ord("a")) for char in _str])

str_arr = ["class", "function", "method"]
key = "1"

for word in str_arr:
    print(word)
    encoded = code(word, key)
    print(encoded)
    print(type(encoded))
    print(len(encoded))
    print()

# 3. Определить, какие из слов «attribute», «класс», «функция», «type» невозможно записать в байтовом типе.

str_arr = ["attribute", "класс", "функция", "type"]

for word in str_arr:
    print(word)
    try:
        word.encode('ascii')
    except UnicodeEncodeError:
        print(f"Слово {word} не может быть записано в байтовом типе")
        print()
        continue

    print(f"Слово {word} может быть записано в байтовом типе")
    print()

# 4. Преобразовать слова «разработка», «администрирование», «protocol», «standard» из строкового представления
# в байтовое и выполнить обратное преобразование (используя методы encode и decode).

str_arr = ["разработка", "администрирование", "protocol", "standart"]

for word in str_arr:
    print(word)
    encoded = word.encode('UTF-8')
    print(encoded)
    decoded = encoded.decode('UTF-8')
    print(decoded)
    print()

# 5. Выполнить пинг веб-ресурсов yandex.ru, youtube.com и преобразовать результаты из байтовового
# в строковый тип на кириллице.

import subprocess

args = [["ping", "yandex.ru"],["ping", "youtube.com"]]

for each in args:
    subproc_ping = subprocess.Popen(each, stdout=subprocess.PIPE)

    for line in subproc_ping.stdout:
        line = line.decode('cp866')
        print(line)

# 6. Создать текстовый файл test_file.txt, заполнить его тремя строками: «сетевое программирование»,
# «сокет», «декоратор». Проверить кодировку файла по умолчанию.
# Принудительно открыть файл в формате Unicode и вывести его содержимое

import chardet

with open("txt_1.txt", "rb") as f:
    print(chardet.detect(f.read()))

print()

with open("txt_1.txt", "r", encoding = "UTF-8") as f:
    print(f.read())


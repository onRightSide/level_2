import re
import csv
import os


def get_data():

    counter = -1
    os_prod_list = []
    os_name_list = []
    os_code_list = []
    os_type_list = []
    main_data = [["Изготовитель системы", "Название ОС", "Код продукта", "Тип системы"]]

    cur_dir = os.getcwd()
    print(cur_dir)

    for file in os.listdir(cur_dir):
        if file.endswith(".txt"):

            counter += 1
            txt = open(file, "r", encoding="UTF-8").read()

            os_prod_list.append(re.findall(r'Изготовитель системы:\s*\S*', txt)[0].split()[2])
            os_name_list.append(re.findall(r'Название ОС:\s*\S*', txt)[0].split()[2])
            os_code_list.append(re.findall(r'Код продукта:\s*\S*', txt)[0].split()[2])
            os_type_list.append(re.findall(r'Тип системы:\s*\S*', txt)[0].split()[2])


    for i in range(0, counter+1):
        info = []
        info.append(os_prod_list[i])
        info.append(os_name_list[i])
        info.append(os_code_list[i])
        info.append(os_type_list[i])
        print(info)
        main_data.append(info)

    return main_data

def write_to_csv(info_file):
    main_data = get_data()

    with open(info_file, 'w') as f:
        writer = csv.writer(f, delimiter=';')
        for row in main_data:
            writer.writerow(row)

info_file = 'hard_info.csv'
write_to_csv(info_file)

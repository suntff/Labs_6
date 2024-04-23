import os
import csv
import random

def Open(separator = ","):
    global data
    data = []
    # Открываем файл в режиме чтения ('r')
    with open('example.csv', newline='') as csvfile:
        # Создаем объект reader, который будет читать данные из файла
        reader = csv.reader(csvfile, delimiter=separator)
        # Проходим по каждой строке в файле и выводим ее
        for row in reader:
            data.append(row)

def Show(output_type="top",number_of_lines = 5, separator = ""):
    Open(separator=",")
    if len(data)<5:
        print("строк недостаточно")
    else:
        lens = [max(len(data[j][i]) for j in range(len(data))) + 2 for i in range(len(data[1]))]

        format_string = ' '.join('{{:<{}}}'.format(width) for width in lens)
        print(format_string.format(*data[0]))
        if output_type == "top":
            # Вывод данных
            for row in data[1:][:number_of_lines-1]:
                print(format_string.format(*row))
        if output_type == "bottom":
            for row in data[1:][::-1][:number_of_lines-1]:
                print(format_string.format(*row))
        if output_type == "random":
            using_numbers = []
            for i in range(number_of_lines - 1):
                rd = random.randint(1, len(data))
                using_numbers.append(rd)
                if i > 1:
                    while len(using_numbers) > len(set(using_numbers)):
                        rd = random.randint(1, len(data))
                        using_numbers.append(rd)
                print(format_string.format(*data[rd]))
def Info():
    print(len(data)-1,len(data[0]),sep="х")
    c = 0
    for i in range(len(data[0])):
        print(data[0][i],sum(data[j][i]!='' for j in range(1,len(data))),*set(type(data[j][i]) for j in range(1,len(data))))
def DelNaN():
    dl = []
    i = 0
    while i<len(data):
        for j in range(len(data[0])):
            if len(data[i][j])==0:
                del data[i]
                break
        else:
            i+=1
def MakeDS():
    width_learning = int(len(data[0])*0.7)
    height_learning = len(data)
    width_number_learning = random.sample(list(range(len(data[0]))),width_learning)
    learning = [[data[i][j] for j in width_number_learning] for i in range(len(data))]
    width_testing = len(data[0])-width_learning
    height_testing = len(data)
    width_number_testing = random.sample(list(range(len(data[0]))), width_testing)
    testing = [[data[i][j] for j in width_number_testing] for i in range(len(data))]
    # Создаем папку workdata, если она не существует
    if os.path.exists('workdata')==0:
        os.makedirs('workdata')
    # Создаем папки Learning и Testing внутри папки workdata
    learning_path = os.path.join('workdata', 'Learning')
    testing_path = os.path.join('workdata', 'Testing')
    os.makedirs(learning_path, exist_ok=True)
    os.makedirs(testing_path, exist_ok=True)
    # Создаем папки Learning и Testing внутри папки workdata
    learning_path = os.path.join('workdata', 'Learning')
    testing_path = os.path.join('workdata', 'Testing')
    os.makedirs(learning_path, exist_ok=True)
    os.makedirs(testing_path, exist_ok=True)

    # Записываем обучающий и тестовый файлы CSV
    with open(os.path.join(learning_path, 'train.csv'), 'w', newline='', encoding='utf-8') as train_file:
        writer = csv.writer(train_file)
        writer.writerows(learning)

    with open(os.path.join(testing_path, 'test.csv'), 'w', newline='', encoding='utf-8') as test_file:
        writer = csv.writer(test_file)
        writer.writerows(testing)
    print("Файлы созданы успешно")

Show()
Info()
DelNaN()
MakeDS()

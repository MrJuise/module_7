'''
Задача "Записать и запомнить":
Создайте функцию custom_write(file_name, strings), которая принимает аргументы file_name - название файла для записи,
strings - список строк для записи.
Функция должна:

    Записывать в файл file_name все строки из списка strings, каждая на новой строке.
    Возвращать словарь strings_positions, где ключом будет кортеж (<номер строки>, <байт начала строки>),
    а значением - записываемая строка. Для получения номера байта начала строки используйте метод tell() перед записью.
'''
def custom_write(file_name, strings):
    with open(file_name, 'w+', encoding='utf-8') as file:
        dic = {}
        line = 0
        for string in strings:
            line += 1
            te = file.tell()
            dic.update({(line, te) : string})
            file.write(f'{string}\n')
        return dic


info = [
    'Text for tell.',
    'Используйте кодировку utf-8.',
    'Because there are 2 languages!',
    'Спасибо!'
    ]

result = custom_write('test.txt', info)
print(result)
for elem in result:
    print(elem)

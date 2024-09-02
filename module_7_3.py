'''
Задача "Найдёт везде":
Напишите класс WordsFinder, объекты которого создаются следующим образом:
WordsFinder('file1.txt, file2.txt', 'file3.txt', ...).
Объект этого класса должен принимать при создании неограниченного количество названий файлов и записывать их в атрибут file_names в виде списка или кортежа.

Также объект класса WordsFinder должен обладать следующими методами:
get_all_words - подготовительный метод, который возвращает словарь следующего вида:
{'file1.txt': ['word1', 'word2'], 'file2.txt': ['word3', 'word4'], 'file3.txt': ['word5', 'word6', 'word7']}
Где:

    'file1.txt', 'file2.txt', ''file3.txt'' - названия файлов.
    ['word1', 'word2'], ['word3', 'word4'], ['word5', 'word6', 'word7'] - слова содержащиеся в этом файле.

'''

class WordsFinder:
    def __init__(self, *file_names):
        self.file_names = file_names
        self.all_words = {}
    def get_all_words(self):
        self.all_words = {}
        for file_name in self.file_names:
            with open(file_name, 'r', encoding='utf-8') as file:
                words = []
                for line in file:
                    lin_rep = line.lower().replace(',', '').replace('.', '').replace('=', '').replace('!', '').replace('?', '').replace(';', '').replace(':', '').replace('-', '')
                    words.extend(lin_rep.split())
                self.all_words[file_name] = words
        return self.all_words

    def find(self, word):
        word = word.lower()
        find = {}
        self.get_all_words()
        for file_name, words in self.all_words.items():
            if word in words:
                a = words.index(word)+1
                find[file_name] = a
        return find

    def count(self, word):
        word = word.lower()
        count = {}
        self.get_all_words()
        for file_name, words in self.all_words.items():
            a = words.count(word)
            count[file_name] = a
        return count




finder1 = WordsFinder('Walt Whitman - O Captain! My Captain!.txt',
                      'Rudyard Kipling - If.txt',
                      'Mother Goose - Monday’s Child.txt')
print(finder1.get_all_words())
print(finder1.find('the'))
print(finder1.count('the'))

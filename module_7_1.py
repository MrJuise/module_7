'''Задача "Учёт товаров":
Необходимо реализовать 2 класса Product и Shop, с помощью которых будет производиться запись в файл с продуктами.
Объекты класса Product будут создаваться следующим образом - Product('Potato', 50.0, 'Vagetables') и обладать следующими свойствами:'
'''

class Product:
    def __init__(self, name, weight, category):
        self.name = str(name)
        self.weight = float(weight)
        self.category = str(category)

    def __str__(self):
        prod = f'{self.name}, {self.weight}, {self.category}'
        return prod

class Shop:
    __file_name = 'products.txt'
    def get_products(self):
        with open(self.__file_name, 'r') as file:
            return file.read()

    def add(self, *products):
        for p in products:
            if p.name in self.get_products():
                print(f'Продукт {self.__str__()} уже есть в магазине')
            else:
                file = open(self.__file_name, 'a')
                file.write(f'{p}\n')
                file.close()



s1 = Shop()
p1 = Product('Potato', 50.5, 'Vegetables')
p2 = Product('Spaghetti', 3.4, 'Groceries')
p3 = Product('Potato', 5.5, 'Vegetables')

print(p2) # __str__

s1.add(p1, p2, p3)

print(s1.get_products())
# class Auto:
#     def __init__(self, model, year, proiz, vv, color, prise):
#         self.model = model
#         self.year = year
#         self.proiz = proiz
#         self.vv = vv
#         self.color = color
#         self. prise = prise
#     def print_Auto(self):
#         print(f'Модель Машины: {self.model} \n'
#               f'Год выпуска: {self.year} \n'
#               f'Производитель: {self.proiz} \n'
#               f'Объем двигателя: {self.vv} \n'
#               f'Цвет: {self.color} \n'
#               f'Цена: {self.prise} \n')
#     def print_model(self):
#         print(f'Модель: {self.model} \n')
#     def print_year(self):
#         print(f'Год: {self.year} \n')
#     def print_proiz(self):
#         print(f'Производитель: {self.proiz} \n')
#     def print_vv(self):
#         print(f'Объем двигателя: {self.vv} \n')
#     def print_color(self):
#         print(f'Цвет: {self.color} \n')
#     def print_prise(self):
#         print(f'Цена: {self.prise} \n')
#
#
# Automodil = Auto(input('Введите модель: '), int(input('Введите год выпуска: ')), input('Введите производителя: '), int(input('Введите объем двигателя: ')), input("Введите цвет машины: "), int(input("Введите цену: ")))
# Automodil.print_Auto()
# Automodil.print_model()
# Automodil.print_year()
# Automodil.print_proiz()
# Automodil.print_vv()
# Automodil.print_color()
# Automodil.print_prise()

# class Book:
#     def __init__(self,name, year, proiz, janr, avtor, prise):
#         self.name = name
#         self.year = year
#         self.proiz = proiz
#         self.janr = janr
#         self.avtor = avtor
#         self. prise = prise
#     def print_Book(self):
#         print(f'Название книги: {self.name} \n'
#               f'Год выпуска: {self.year} \n'
#               f'Издатель: {self.proiz} \n'
#               f'Жанр: {self.janr} \n'
#               f'Автор: {self.avtor} \n'
#               f'Цена: {self.prise} \n')
#     def print_namebook(self):
#         print(f'Название книги: {self.name} \n')
#     def print_year(self):
#         print(f'Год выпуска: {self.year} \n')
#     def print_proiz(self):
#         print(f'Издатель: {self.proiz} \n')
#     def print_janr(self):
#         print(f'Жанр: {self.janr} \n')
#     def print_avtor(self):
#         print(f'Автор: {self.avtor} \n')
#     def print_prise(self):
#         print(f'Цена: {self.prise} \n')
#
#
# Book1 = Book(input('Введите название книги: '), int(input('Введите год выпуска: ')), input('Введите издателя: '), input('Введите Жанр: '), input("Введите автора: "), int(input("Введите цену: ")))
# Book1.print_Book()
# Book1.print_namebook()
# Book1.print_year()
# Book1.print_proiz()
# Book1.print_janr()
# Book1.print_avtor()
# Book1.print_prise()

class Stadion:
    def __init__(self, name, year, strana, city, obem):
        self.name = name
        self.year = year
        self.strana = strana
        self.city = city
        self.obem = obem

    def print_Stadion(self):
        print(f'Название стадиона: {self.name} \n'
              f'Дата открытия: {self.year} \n'
              f'В какой стране: {self.strana} \n'
              f'В каком городе: {self.city} \n'
              f'Вместимость стадиона: {self.obem} \n')

    def print_name(self):
        print(f'Название стадиона: {self.name} \n')
    def print_year(self):
        print(f'Дата открытия: {self.year} \n')
    def print_strana(self):
        print(f'В какой стране: {self.strana} \n')
    def print_city(self):
        print(f'В каком городе: {self.city} \n')
    def print_obem(self):
        print(f'Цвет: {self.obem} \n')


Stadon1 = Stadion(input('Введите название стадиона: '), int(input('Введите дату открытия: ')), input('Введите страну в котором он расположен: '), input('Введите в каком городе расположен: '), input("Введите вместимость стадиона: "))
Stadon1.print_Stadion()
Stadon1.print_name()
Stadon1.print_year()
Stadon1.print_strana()
Stadon1.print_city()
Stadon1.print_obem()
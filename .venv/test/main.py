class Pet:

    def _init_(self, kind, name, weigth):
        self.kind = kind
        self.name = name
        self.weigth = weigth
        self.voice = []
        self.nutrition = []
        self.product = []
        self.gender = []

    def feed(self, food):
        print(f'{self.kind} {self.name} "покормлен"')

    def gather(self, name):
        if self.kind == 'гусь' or 'курица' or 'утка':
            if self.gender == 'самка':
                print(f' "у" {name} "собраны" {self.nutrition}')
            else:
                print(f'{name} "самец и не может дать" {self.product}')
        elif self.kind == 'корова' or 'коза':
            if self.gender == 'самка':
                print(f'{name} "подоена"')
            else:
                print(f'{name} "самец и не дает" {self.nutrition}')
        elif self.kind == 'овца':
            print(f'{name} "пострижена"')

    def say(self, name):
        print(f'{self.kind} {name} "говорит" {self.voice}')

pets = [
    {"kind": "гусь", "name": "Серый", "weigth": "15", "voice": "га-га-га", "nutrition": "зерно", "product": "яйца",
     "gender": "самец"},
    {"kind": "гусь", "name": "Белый", "weigth": "13", "voice": "га-га-га", "nutrition": "зерно", "product": "яйца",
     "gender": "самец"},
    {"kind": "корова", "name": "Манька", "weigth": "230", "voice": "мууу", "nutrition": "сено", "product": "молоко",
     "gender": "самка"},
    {"kind": "овца", "name": "Барашек", "weigth": "140", "voice": "беее", "nutrition": "трава", "product": "шерсть",
     "gender": "самец"},
    {"kind": "овца", "name": "Кудрявый", "weigth": "120", "voice": "беее", "nutrition": "трава", "product": "шерсть",
     "gender": "самец"},
    {"kind": "курица", "name": "Ко-ко", "weigth": "5", "voice": "ко-ко", "nutrition": "зерно", "product": "яйца",
     "gender": "самка"},
    {"kind": "курица", "name": "Кукареку", "weigth": "6", "voice": "ко-ко", "nutrition": "зерно", "product": "яйца",
     "gender": "самка"},
    {"kind": "коза", "name": "Рога", "weigth": "55", "voice": "меее", "nutrition": "трава", "product": "молоко",
     "gender": "самка"},
    {"kind": "коза", "name": "Копыта", "weigth": "45", "voice": "меее", "nutrition": "трава", "product": "молоко",
     "gender": "самка"},
    {"kind": "утка", "name": "Кряква", "weigth": "9", "voice": "кря", "nutrition": "зерно", "product": "яйца",
     "gender": "самка"},
]


def main(pets):
    while True:
        print('Для взаимодействия с животным нажмите: - 1',
              'Вес животных: - 2',
              'Для выхода нажмите: - 0', sep='\n')
        command = input(': ')
        if command == '2':
            print('Общий вес животных нажмите - a', 'Самое тяжелое животное - нажмите b', sep='\n')
            command = input(': ')
            max_weight = set()
            for pet in pets:
                max_weight.add(int(pet['weigth']))
            if command == 'a':
                print(sum(max_weight))
            elif command == 'b':
                for pet in pets:
                    if int(pet['weigth']) == max(max_weight):
                        print(f'{pet['kind']} {pet['name']} "весит" {pet['weigth']}')
        elif command == '1':
            print('введите имя животного')
            name = input(':')
            for pet in pets:
                if pet['name'] == name:
                    pet1 = Pet()
                    pet1.kind = pet['kind']
                    pet1.name = pet['name']
                    pet1.weigth = pet['weigth']
                    pet1.voice = pet['voice']
                    pet1.nutrition = pet['nutrition']
                    pet1.product = pet['product']
                    pet1.gender = pet['gender']

            print('Введите команду: ', 'для кормежки - p', 'для сбора (молоко, яйца, шерсть) - g',
                  'для поговорить - s', 'для выхода - q', sep='\n')
            command = input(': ')
            if command == 'p':
                pet1.feed(food)
            elif command == 'g':
                pet1.gather(pet1.name)
            elif command == 's':
                pet1.say(pet1.name)
            elif command == 'q':
                break
            else:
                print('Неверная команда')
        elif command == '0':
            break


main(pets)


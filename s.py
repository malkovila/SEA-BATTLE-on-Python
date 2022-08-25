from random import randint

class Cell:
    def __init__(self):
        self.is_status = False #0 - закрыта, 1 - открыта
        self.is_ship = False # 0 - нет корабля, 1 - есть
        self.is_fire = False

class Ship:
    def __init__(self, pole,  length, tp=1):
        self._length = length
        self._tp = tp
        self._is_move = True
        self._cells = []
        self.pole = pole

    def chek_all_cells(self):
        if all(i.is_fire for i in self._cells):
            print('Корабль подбит')
            for i in self._cells:
                self.mine_around(i, self.pole)
            self._cells.clear()


    def mine_around(self, embedded_elem, data_set):
        indx = (-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)
        for elem in data_set:
            if embedded_elem in elem:
                for f, g in indx:
                    if 0 <= self.pole.index(elem) + f < 10 and 0 <= elem.index(embedded_elem) + g < 10:
                        self.pole[self.pole.index(elem) + f][elem.index(embedded_elem) + g].is_fire = True
                        self.pole[self.pole.index(elem) + f][elem.index(embedded_elem) + g].is_status = True
    def move(self, go):
        if self._tp == 1 or self._tp == 2 and self._is_move == True:
            self.fd(self._cells[-1], self.pole)
            self.find_index(self._cells[-1], self.pole)
    def fd(self, embedded_elem, data_set):
        for elem in data_set:
            if embedded_elem in elem:
                print('y =', self.pole.index(elem))  # индекс внешнего элемента
                print('x =',elem.index(embedded_elem))  # индекс внутреннего
    def find_index(self, embedded_elem, data_set):
        indx = (-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)
        if self._tp == 1:
            for elem in data_set:
                if embedded_elem in elem:
                    if(0 <= elem.index(embedded_elem) + 1 + g < 10 and 0 <= self.pole.index(elem) + f < 10 for g, f in indx):
                        if all(self.pole[self.pole.index(elem) + f][elem.index(embedded_elem) + 1 + g].is_ship == False for f, g in indx if self.pole[self.pole.index(elem) + f][elem.index(embedded_elem) + 1 + g] != self._cells[-1]):
                            self._cells.append(self.pole[self.pole.index(elem)][elem.index(embedded_elem) + 1])
                            self._cells[-1].is_ship = True
                            self._cells[-1].is_status = True
                            self._cells[0].is_status = False
                            self._cells[0].is_ship = False
                            self._cells.pop(0)
                    if (0 <= elem.index(embedded_elem) - len(self._cells) + g < 10 and 0 <= self.pole.index(elem) + f < 10 for g,f in indx):
                        if all(self.pole[self.pole.index(elem) + f][elem.index(embedded_elem) - len(self._cells) + g].is_ship == False for f, g in indx if self.pole[self.pole.index(elem) + f][elem.index(embedded_elem) - len(self._cells) + g] != self._cells[0]):
                            self._cells.insert(0, self.pole[self.pole.index(elem)][elem.index(embedded_elem) - len(self._cells)])
                            self._cells[0].is_status = True
                            self._cells[0].is_ship = True
                            self._cells[-1].is_ship = False
                            self._cells[-1].is_status = False
                            self._cells.pop(-1)

        if self._tp == 2:
            for elem in data_set:
                if embedded_elem in elem:
                    if (0 <= self.pole.index(elem) + 1 + f < 10 and 0 <= elem.index(embedded_elem) + g < 10 for f, g in indx):
                        if all(self.pole[self.pole.index(elem) + 1 + f][elem.index(embedded_elem) + g].is_ship == False for f, g in indx if self.pole[self.pole.index(elem) + 1 + f][elem.index(embedded_elem) + g] != self._cells[-1]):
                            self._cells.append(self.pole[self.pole.index(elem) + 1][elem.index(embedded_elem)])
                            self._cells[-1].is_ship = True
                            self._cells[-1].is_status = True
                            self._cells[0].is_status = False
                            self._cells[0].is_ship = False
                            self._cells.pop(0)
                    if (0 <= elem.index(embedded_elem) + g <= 9 and 0 <= self.pole.index(elem) - len(self._cells) + f <= 9 for f, g in indx):
                        if all(self.pole[self.pole.index(elem) - len(self._cells) + f][elem.index(embedded_elem) + g].is_ship == False for f, g in indx if self.pole[self.pole.index(elem) - len(self._cells) + f][elem.index(embedded_elem) + g] != self._cells[0]):
                            self._cells.append(self.pole[self.pole.index(elem) - len(self._cells)][elem.index(embedded_elem)])
                            self._cells[0].is_status = True
                            self._cells[0].is_ship = True
                            self._cells[-1].is_ship = False
                            self._cells[-1].is_status = False
                            self._cells.pop(-1)


class GamePole:
    ships = []
    def __init__(self, size, name):
        self._size = size
        self.name = name
        self._h = []
        self.pole = (tuple(tuple(Cell() for i in range(self._size)) for j in range(self._size)))
        self._ships = [Ship(self.pole, 4, tp=randint(1, 2)), Ship(self.pole, 3, tp=randint(1, 2)),
                       Ship(self.pole, 3, tp=randint(1, 2)),
                       Ship(self.pole, 2, tp=randint(1, 2)), Ship(self.pole, 2, tp=randint(1, 2)),
                       Ship(self.pole, 2, tp=randint(1, 2)),
                       Ship(self.pole, 1, tp=randint(1, 2)), Ship(self.pole, 1, tp=randint(1, 2)),
                       Ship(self.pole, 1, tp=randint(1, 2)), Ship(self.pole, 1, tp=randint(1, 2))]
    def init(self):
        d = 0
        self.ships = self._ships.copy()
        while d != len(self._ships):
            h = 0
            x, y = randint(0, self._size - 1), randint(0, self._size - 1)
            n = []
            indx = (-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)
            if self._ships[d]._tp == 1:
                if x + self._ships[d]._length < self._size and y < self._size:
                    for i in range(self._ships[d]._length):
                        if not self.pole[y][x].is_ship:
                            if all((self.pole[y + f][x + g].is_ship == False for f, g in indx if
                                    0 <= x + g < self._size and 0 <= y + f < self._size)):
                                n.append(self.pole[y][x])
                                x += 1
            elif self._ships[d]._tp == 2:
                if y + self._ships[d]._length < self._size and x < self._size:
                    for i in range(self._ships[d]._length):
                        if not self.pole[y][x].is_ship:
                            if all((self.pole[y + f][x + g].is_ship == False for f, g in indx if
                                    0 <= y + f < self._size and 0 <= x + g < self._size)):
                                n.append(self.pole[y][x])
                                y += 1
            if len(n) == self._ships[d]._length:
                for i in n:
                    self._ships[d]._cells.append(i)
                    self._h.append(self._ships[d])
                    for o in self._ships[d]._cells:
                        o.is_ship = True
                        o.is_status = True
                d += 1
    def show_ships(self):
        for i in self._ships:
            for j in i._cells:
                j.is_status = True
    def how_many_ships(self):
        n1 = 0
        n2 = 0
        n3 = 0
        n4 = 0
        all = 0
        for i in self._ships:
            if len(i._cells) > 0:
                all+=1
                if i._length == 1:
                    n1 += 1
                if i._length == 2:
                    n2 += 1
                if i._length == 3:
                    n3 += 1
                if i._length == 4:
                    n4 += 1
        return all, n4, n3, n2, n1
    def check_win(self):
        if all(len(i._cells) == 0 for i in self._ships):
            print('Все коробли игрока', self.name, 'были подбиты. Игра окончена.')
            return True

    def get_pole(self):
        return self.pole
    def which_ship(self, cell):
        for i in self._ships:
            if cell in i._cells:
                return i
    def show(self):
        for i in self.pole:
            print(*map(lambda x: 'x' if x.is_fire else '#' if not x.is_status else '1' if x.is_ship else '0', i))
    def show_pc(self):
        for i in self.pole:
            print(*map(lambda x: '#' if not x.is_status and not x.is_fire and (x.is_ship or not x.is_ship) else 'x' if x.is_status and x.is_fire and x.is_ship else '*' if x.is_status and x.is_fire and not x.is_ship else '0', i))

class SeaBattle:
    def __init__(self, pole_1, pole_2):
        self.human_pole = pole_1
        self.computer_pole = pole_2
    def fight(self, who, coord_x, coord_y):
        if who == 'человек':
            if self.computer_pole.get_pole()[coord_y][coord_x].is_fire == False:
                self.computer_pole.get_pole()[coord_y][coord_x].is_fire = True
                self.computer_pole.get_pole()[coord_y][coord_x].is_status = True
                if self.computer_pole.get_pole()[coord_y][coord_x].is_ship:
                    print('Вы попали')
                    ship = self.computer_pole.which_ship(self.computer_pole.get_pole()[coord_y][coord_x])
                    ship.is_move = False
                    ship.chek_all_cells()
                elif self.computer_pole.get_pole()[coord_y][coord_x].is_ship == False:
                    print('Мимо')
            else:
                print('Клетка уже подбита')
        if who == 'computer':
            x = randint(0, 9)
            y = randint(0,9)
            if  self.human_pole.get_pole()[y][x].is_fire == False:
                self.human_pole.get_pole()[y][x].is_fire = True
                self.human_pole.get_pole()[coord_y][coord_x].is_status = True
                if self.human_pole.get_pole()[y][x].is_ship:
                    print('По вам попали', 'x =', x, 'y =', y)
                    ship = self.human_pole.which_ship(self.human_pole.get_pole()[y][x])
                    ship.is_move = False
                    ship.chek_all_cells()
                elif self.human_pole.get_pole()[y][x].is_ship == False:
                    print('компьютер не попал')
            else:
                sb.fight('computer', 0, 0)


human_field = GamePole(10, 'person')
comp_field = GamePole(10, 'comp')
human_field.init()
human_field.show_ships()
comp_field.init()
print(human_field.ships)
sb = SeaBattle(human_field, comp_field)
human_field.show()
print()
comp_field.show_pc()
while True:
    if human_field.check_win() or comp_field.check_win():
        break
    try:
        x, y = map(int, input('Введите координаты клетки' + '\n').split())
    except:
        continue
    command = input()
    if command == 'сколько':
        print('У противника:'+  str(comp_field.how_many_ships()[0]) + '. 4-палубы: ' + str(comp_field.how_many_ships()[1]) + ', 3-палубы: ' + str(comp_field.how_many_ships()[2])
              + ', 2-палубы: ' + str(comp_field.how_many_ships()[3]) + ', 1-палубы: ' + str(comp_field.how_many_ships()[4]))
        print('У вас: ' +  str(human_field.how_many_ships()[0]) + '. 4-палубы: ' + str(human_field.how_many_ships()[1]) + ', 3-палубы: ' + str(human_field.how_many_ships()[2])
              + ', 2-палубы: ' + str(human_field.how_many_ships()[3]) + ', 1-палубы: ' + str(human_field.how_many_ships()[4]))
    if command == 'переместить':
        a = int(input())
        if a == 4:
            try:
                human_field.ships[0].move(1)
            except:
                print('неверный индекс')

        if a == 3:
            try:
                human_field.ships[1].move(1)
            except:
                print('неверный индекс')

        if a == 2:
            try:
                human_field.ships[5].move(1)
            except:
                print('неверный индекс')
        if a == 1:
            try:
                human_field.ships[-1].move(1)
            except:
                print('неверный индекс')
    else:
        sb.fight('computer', 0, 0)
        print('Ваше поле')
        human_field.show()
        sb.fight('человек', x, y)
        print('Поле комп')
        comp_field.show_pc()

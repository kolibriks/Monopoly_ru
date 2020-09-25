# import sys
# sys.setExecutionLimit(600000)
import random
import time

print('-' * 10 + 'Monopoly' + '-' * 10)
print('_' * 28)
print('_' * 28)


class Player:
    def __init__(self, name):
        self.name = name
        self.cash = 10000
        self.site = 0
        self.num_f = 0

    def turn(self):
        print('Бросаю кубик..')
        time.sleep(1)
        s = (cube())
        print(s)
        time.sleep(1)
        self.site = self.site + s
        if self.site >= max_site:
            self.site -= max_site
            print('Вам начислили пенсию в размере 1500')
            time.sleep(1)
            self.cash += 1500
        print('Место на карте {}'.format(self.site))
        time.sleep(1)
        if maps[self.site][0] == 'филиал':
            Player.fil()
        elif maps[self.site][0] == 'приз':
            print('Вы попали на конкурс красоты, где выиграли приз 500')
            self.cash += 500
        elif maps[self.site][0] == 'поле':
            print('Вы попали на поле. Тут пусто. Хнык-хнык')
        elif maps[self.site][0] == 'штраф':
            print('По причине превышения уровня красоты Вам впаяли штраф 500')
            self.cash -= 500
        elif maps[self.site][0] == 'шанс':
            Player.shanson()
        elif maps[self.site][0] == 'налог':
            Player.ploti()
        elif maps[self.site][0] == 'казино':
            Player.azino()
        else:
            print('Вы попали в домик. Хоть тут и никого нету, но рекомендую поскорее уходить')
        time.sleep(1)
        print('Ваши деньги: {}'.format(self.cash))
        time.sleep(1)

    def fil(self):
        if maps[self.site][1] == 'None':
            print('Вы попали на филиал, который никому не принадлежит')
            time.sleep(1)
            if self.cash - maps[self.site][2] < 0:
                print('Не хватает денег')
            else:
                Player.pokupon()
        else:
            print('Упс. Вы попали на филиал, который принадлежит {}. Платите {}'.format(maps[self.site][1],
                                                                                        maps[self.site][3]))
            for i in players:
                if i.name == maps[self.site][1]:
                    i.cash += maps[self.site][3]
                    self.cash -= maps[self.site][3]

    def pokupon(self):
        p = input('Цена {}. Покупаем? (Введите "да" для покупки, "нет" для отказа)'.format(maps[self.site][2]))
        time.sleep(1)
        if p == 'да':
            print('Продано')
            self.num_f += 1
            self.cash -= maps[self.site][2]
            maps[self.site][1] = self.name
        elif p == 'нет':
            print('Филиал не был куплен')
        else:
            print('Неправильно указано слово. Попробуйте ещё раз')
            time.sleep(1)
            Player.pokupon()

    def ploti(self):
        print('Плотите налоги, пожалуйста (за каждый филиал -100)')
        nal = self.num_f * 100
        self.cash -= nal

    def azino(self):
        ink = input('Вы попали в азино три топора. Укажите Вашу ставку (если не хотите играть, введите "0")')
        time.sleep(1)
        try:
            inp = int(ink)
        except:
            print('Ну и нах нам Ваши буквы? Введите число!')
            time.sleep(1)
            Player.azino()
        print('Барабанная дробь..')
        time.sleep(1)
        a1 = random.randint(1, 2)
        a2 = random.randint(1, 2)
        if a1 == a2:
            print('Поздравляем, Вы выиграли двойную сумму')
            self.cash += inp
        else:
            print('Вы проиграли поставленную сумму')
            self.cash -= inp

    def shanson(self):
        input('Вы попали на "Шанс". Нажмите любую клавишу')
        print('Бросаю кубик..')
        time.sleep(1)
        sh = random.randint(1, 6)
        if sh == 1:
            print('shield')
        elif sh == 2:
            print('pole')
        elif sh == 3:
            print('Вам пришла повестка в налоговую инспекцию')
            while maps[self.site][0] != 'налог':
                self.site = self.site + 1
                if self.site >= max_site:
                    self.site -= max_site
            time.sleep(1)
            print('Место на карте {}'.format(self.site))
            time.sleep(1)
            Player.ploti()
        elif sh == 4:
            print('Вы выиграли в лотерею. За каждый филиал получите бонус 100')
            bon = self.num_f * 100
            self.cash += bon
        elif sh == 5:
            print('Казино ждёт именно Вас')
            while maps[self.site][0] != 'казино':
                self.site = self.site + 1
                if self.site >= max_site:
                    self.site -= max_site
            time.sleep(1)
            print('Место на карте {}'.format(self.site))
            time.sleep(1)
            Player.azino()
        elif sh == 6:
            print('Вы выиграли приз 1500')
            self.cash += 1500
        else:
            print(' ')

    def nam(self):
        return self.name

    def mon(self):
        return self.cash

    def exit(self):
        site_for_none = []
        for_none = []
        for f in maps.keys():
            if maps[f][0] == 'филиал':
                if maps[f][1] == self.name:
                    maps[f][1] == 'None'
                    site_for_none.append(f)
        if len(site_for_none) != 0:
            for elem in site_for_none:
                for_none.append(str(elem))
            time.sleep(1)
            print('Были возвращены государству филиалы на местах {}'.format(', '.join(for_none)))


def num_players():
    hum = input('Сколько игроков? Игра поддерживает от 2 до 10 игроков')
    while True:
        try:
            if int(hum) < 2:
                print('Должно быть число больше 1')
            elif int(hum) > 10:
                print('Должно быть число меньше 11')
            else:
                return int(hum)
        except ValueError:
            print('"{}" это не число.'.format(hum))
        time.sleep(1)
        num_players()


def cube():
    return random.randint(2, 12)


human = num_players()
index = 0
max_site = 36
maps = {0: ['cтарт'], 1: ['приз'], 2: ['филиал', 'None', 2200, 350], 3: ['филиал', 'None', 2000, 300],
        4: ['филиал', 'None', 1800, 250], 5: ['поле'], 6: ['штраф'], 7: ['филиал', 'None', 1200, 150],
        8: ['филиал', 'None', 1000, 150], 9: ['филиал', 'None', 1500, 200], 10: ['шанс'], 11: ['казино'],
        12: ['филиал', 'None', 1200, 150], 13: ['филиал', 'None', 1000, 150], 14: ['филиал', 'None', 1500, 200],
        15: ['филиал', 'None', 700, 100], 16: ['филиал', 'None', 1000, 150], 17: ['филиал', 'None', 800, 150],
        18: ['налог'], 19: ['поле'], 20: ['филиал', 'None', 1500, 200], 21: ['филиал', 'None', 2200, 300],
        22: ['филиал', 'None', 2000, 250], 23: ['штраф'], 24: ['шанс'], 25: ['филиал', 'None', 1000, 150],
        26: ['филиал', 'None', 2000, 250], 27: ['филиал', 'None', 1500, 200], 28: ['поле'], 29: ['казино'],
        30: ['филиал', 'None', 1200, 150], 31: ['филиал', 'None', 1000, 150], 32: ['филиал', 'None', 1500, 200],
        33: ['филиал', 'None', 800, 100], 34: ['филиал', 'None', 1000, 150], 35: ['филиал', 'None', 500, 100]}

players = [Player(input('Введите имя игрока №{}'.format(i + 1))) for i in range(int(human))]
x = True
while x:
    Player = players[index]
    n = Player.nam()
    mon = Player.mon()
    if len(players) == 1:
        print(' ')
        time.sleep(1)
        print('{} победитель!!!'.format(n))
        time.sleep(1)
        print('Congrats')
        x = False
    else:
        print(' ')
        time.sleep(1)
        if mon < -5000:
            print('Игрока {} убили за неуплату долгов'.format(n))
            Player = players[index]
            Player.exit()
            players.remove(players[index])
            human -= 1
            index = index % human
        else:
            if mon < 0:
                print('Осторожно, у вас долги. Через плохую репутацию вы пока не можете покупать филиалы')
                print('Если будет долгов на суму, больше 5000, может быть плохо')
            time.sleep(1)
            print('Ход {}'.format(n))
            time.sleep(1)
            kk = input('Если хотите кинуть кубик, введите любой знак. Если хотите выйти, введите "выход"')
            if kk == 'выход':
                print('Игрок {} вышел'.format(n))
                Player = players[index]
                Player.exit()
                players.remove(players[index])
                human -= 1
                index = index % human

            else:
                Player = players[index]
                Player.turn()
                index = (index + 1) % human
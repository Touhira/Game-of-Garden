class Tomato:
    __states = {1: "посадили",
                2: "растет",
                3: "вырос",
                4: "сгнил"}

    def __init__(self, index):
        self._index = index
        self._state = list(Tomato.__states.items())[0]

    @property
    def state(self):
        return self._state[1]

    def grow(self):
        if self._state[0] != 4:
            self._state = list(Tomato.__states.items())[self._state[0]]
            return True
        return False

    def is_ripe(self):
        if self._state[0] == 3:
            return True
        return False


class TomatoBash(Tomato):
    def __init__(self, amount_tomatoes):
        self.tomatoes = [Tomato(i) for i in range(amount_tomatoes)]

    def grow_all(self):
        if all([t.grow() for t in self.tomatoes]) == False:
            return False
        return True

    def all_are_ripe(self):
        if all([t.is_ripe() for t in self.tomatoes]) == True:
            return True
        return False

    def dive_away_all(self):
        if self.all_are_ripe() == True:
            del self.tomatoes
            return True
        return False


class Gardener(TomatoBash):

    def __init__(self, name, object):
        self.name = name
        self._plante = object

    def work(self):
        if self._plante.grow_all() == False:
            print('Не Друг, я не оправдываюсь )')
            return False
        print('Мы растем )')
        return True

    def harvest(self):
        if self._plante.dive_away_all() == False:
            print('Ваши томаты еще не выросли, поухаживайте за ними')
        else:
            print('Отлично, вы собрали урожай!')
            return True

    @staticmethod
    def knowledge_base():
        print('''\n              *** Добро пожаловать в справку по садоводству ***
________________________________________________________________________________

        Вы играете за садовнка, на огороде которого растут помидоры.
Для садовника что самое главное? Правильно! собрать урожай, да как можно быстрее.

Задача - быстро взростить помидоры и успеть собрать урожай, пока он не сгнил, но 
            будь внимателен, я могу тебя ввести в заблуждение)

--------------------------------------------------------------------------------
    У помидоров есть 4 стадии. 1 - посадили, 2 - растет, 3 - вырос, 4 - сгнил    
--------------------------------------------------------------------------------
Чтобы посадить помидоры - введите: |посадить|
Чтобы ростить помидоры - введите: |растить|
Чтобы узнать на какой стадии сейчас помидоры - введите: |стадия|
Чтобы собрать урожай - введите: |собрать| 
________________________________________________________________________________

                        ### Удачи и хорошией игры! ###''')


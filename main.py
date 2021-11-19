from Garden import TomatoBash, Gardener
from time import time

if __name__ == '__main__':

    print('Добро пожаловать в игру, садоводство! Если хотите узнать правила, наберите: |справка|')

    while True:

        choice_start_game = input('\nНачать игру? y|n : ').lower()

        if choice_start_game == 'n':
            break
        elif choice_start_game == 'y':

            start_game_time = time()
            print('\nОтлично, поехали!\n')
            name = input('Введите имя садовода: ')

            while True:

                try:
                    t = TomatoBash(int(input('Введите количество томатов, которе хотите выростить: ')))
                    break
                except Exception:
                    print('Вы ввели некорректное значение, пожалуйста введите целое число.')

            g = Gardener(name, t)

            while True:

                choice = input('\nВведите действие: ').lower()

                if choice == 'справка':
                    Gardener.knowledge_base()

                elif choice == 'посадить':
                    print('Помидоры уже посажены. Чтобы посадить новые, необходимо собрать старые.')

                elif choice == 'растить':
                    if g.work() == False:
                        end_game_time = time()
                        print(f'Вы проиграли.... Но можем повторить '
                              f'У вас ушло на это {round(end_game_time - start_game_time)} секунд.')
                        break

                elif choice == 'стадия':
                    print(g._plante.tomatoes[0].state)

                elif choice == 'собрать':
                    if g.harvest() == True:
                        end_game_time = time()
                        print(f'Поздравляю, Вы победили! у вас ушло на это {round(end_game_time - start_game_time)} секунд.')
                        break

                else:
                    print('Вы ввели не корректное значение, такой команды нет.\n'
                          'Если забыли команды, вызовите справку, набрав: |справка|\n'
                          '         или введите корректное значение.')

        elif choice_start_game == 'справка':
            Gardener.knowledge_base()

        else:
            print('Вы ввели не корректное значение, такой команды нет.\n'
                  'Если забыли команды, вызовите справку, набрав: |справка|\n'
                  '         или введите корректное значение.')

    print('Cпасибо за игру! Заходи еще!')


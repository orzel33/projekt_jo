if __name__ == '__main__':
    print('Witaj użytkowniku! ')
    while True:
        print('Menu: ')
        print('0. Zakończ program')
        print('1. Pokaż listę aptek: ')
        print('2. Pokaż listę leków: ')
        print('3. Pokaż listę pacjentów: ')
        menu_option: str = input('Wybierz dostępną funkcję z menu: ')
        if menu_option == '0':
            break
        if menu_option == '1':
            print('0. Cofnij ')
            print('1. Edytuj dane apteki: ')
            print('2. Dodaj nową aptekę do listy: ')
            print('3. Usuń aptekę z listy: ')
            sub_menu1_option: str = input('Wybierz dostępną funckję z menu: ')
            if sub_menu1_option == '0':
                back_to_main_menu = True

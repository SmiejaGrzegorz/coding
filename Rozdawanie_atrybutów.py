total_points = 30

def opis_atrybutow():
    try:
        chose = input('Który atrybut wybierasz:')
        print(f'{chose}: {skills[chose]}')
    except KeyError:
        print('Nie ma takiego atrybutu...')


def attributes():
    global total_points
    if total_points < 0:
        print('Nie posiadasz więcej puntów...')
        return 0
    add_point = int(input('Ile punktów chcesz dodać:'))
    total_points -= add_point

    return add_point

def print_totalPoints():
    global total_points
    print('Zostało Ci', total_points,'punktów do rozdania.')

def reset():
    global total_points
    perks['siła'] = 2
    perks['mądrość'] = 2
    perks['zręczność'] = 2
    perks['zdrowie'] = 2
    total_points = 30


def show_all():
    print('Siła:', perks['siła'])
    print('Mądrość:', perks['mądrość'])
    print('Zręczność:', perks['zręczność'])
    print('Zdrowie:', perks['zdrowie'])




if __name__ == '__main__':

    perks = {'siła': 2,
             'mądrość': 2,
             'zręczność': 2,
             'zdrowie': 2}

    skills = {'siła': 'cecha wojoników; zwiększana podnosi poziom zadawanych obrażeń',
              'mądrość': 'cecha magów; od niej zależą obrażenia od magii oraz szybkość nauki nowych czarów',
              'zręczność': 'cecha zabójców oraz złodzieji; zwiększana podnosi poziom zadawnych obrażeń z ukrycia; zmniejsza '
                           'szansę wrogów na wykrycie Ciebie w ciemnościach',
              'zdrowie': 'zwiększane podnosi ogólny poziom witaloności twojej postaci'}

    menu_list = ['wyjście', 'opisy atrubutów', 'rozdawanie punktów', 'reset punktów', 'obecny stan atrybutów']

    while True:
        #Masz do wydania 30 punktów na dowolny atrybut tj. : siła, mądrość, zręczność i zdrowie.
        print('\nMENU:')
        print(10 * '=')
        for number, position in enumerate(menu_list):
            print(f'{number}: {position}')
        choice = int(input('Wybierz: '))
        if choice == 0:
            exit()

        elif choice == 1:
            opis_atrybutow()

        elif choice == 2:
            skill = input('Który atrybut chcesz wybrać: ')
            perks[skill] += attributes()
            print(f'{skill} wynosi: {perks[skill]}')
            print_totalPoints()

        elif choice == 3:
            reset()

        elif choice == 4:
            show_all()

        else:
            print('\t\nNiepoprawne polecenie. Spróbuj ponownie...')

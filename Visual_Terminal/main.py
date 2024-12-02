import requests


def main_menu():
    mes = int(input('------ Главное меню ------\n1.Клиенты\n2.Продавцы\n3.Закончить работу\n'))
    if mes == 1:
        _()
        main_menu_klient()
    elif mes == 2:
        _()
        main_menu_prodavec()
    elif mes == 3:
        print('Завершение работы!')
        pass


def main_menu_klient():
    mes = int(
        input('------ Клиенты --------\n1.Показать существующих\n2.Добавить нового\n3.Посмотреть машины\n4.Назад\n'))
    if mes == 1:
        _()
        widget_klient()
    elif mes == 2:
        _()
        add_new_user('Klient')
    elif mes == 3:
        _()
        get_info('Mashina')
    elif mes == 4:
        _()
        main_menu()


# Изменить
def main_menu_prodavec():
    mes = int(input('------ Продавцы ------\n1.Показать существующих\n2.Добавить нового\n3.Посмотреть продажи\n4.Добавить новую продажу\n5.Назад\n'))
    if mes == 1:
        _()
        widget_prodavec()
    elif mes == 2:
        _()
        add_new_user('Prodavec')
    elif mes == 3:
        _()
        get_info('Prodaga')
    elif mes == 4:
        _()
        post_info_prodaga()
    elif mes == 5:
        _()
        main_menu()


### ОБЩЕЕ ###
def _():
    print('*' * 24)


def add_new_user(user):
    last_id = int(requests.get('http://localhost:4388/ham/odata/' + user).json()['value'][-1]['$id'])
    new_user_id = last_id + 1
    print(new_user_id)
    r = ''

    while str(r) != '<Response [200]>':
        if r != '':
            print('Ошибка при заполнении, повторите')
            _()
        if user == 'Klient':
            data = [{
                "$type": "Klient",
                "fIO": input('Введите необходимые данные строго(!!!) по образцу:\nФИО: '),
            "pasport": input('Паспортные данные( ** ** ****** ): '),
            "organizaciya": input('Организация: '),
            "telefon": input('Номер телефона( +* (***) ***-**** ): '),
            "status": 0
            }]
        elif user == 'Prodavec':
            data = [{
                "$type": "Prodavec",
                "fIO": input('Введите необходимые данные строго(!!!) по образцу:\nФИО: '),
                "telefon": input('Номер телефона( +* (***) ***-**-** ): '),
                "prinyat": input('Дата начала работы( ****-**-** ): '),
                "dataRogdeniya": input('Дата рождения( ****-**-** ): ')
            }]
        requests.post('http://localhost:4388/ham/sql/SetNextHamId?id=' + str(new_user_id))
        r = requests.post('http://localhost:4388/ham/odata/' + user, json=data)
    print('Успешно!')
    _()
    if user == 'Klient':
        main_menu_klient()
    elif user == 'Prodavec':
        main_menu_prodavec()


def get_info(user):
    max_id = int(len(requests.get('http://localhost:4388/ham/odata/' + str(user)).json()['value']))
    array_info_about_mashina = [1, 2, 3, 4]
    array_info_about_prodaga = [1, 2, 3, 4]

    if user == 'Mashina':
        get_info_mashina(array_info_about_mashina)
    elif user == 'Prodaga':
        get_info_prodaga(array_info_about_prodaga)

    while True:
        mes = int(input('1.Влево\n2.Вправо\n3.Добавить новую запись\n4.Назад\n'))
        if mes == 1:
            i = 0
            if user == 'Mashina':
                for x in array_info_about_mashina:
                    array_info_about_mashina[i] -= 4
                    i += 1
                if array_info_about_mashina[0] < 0:
                    print('Ошибка!')
                    _()
                    main_menu_klient()
                _()
                get_info_mashina(array_info_about_mashina)
            elif user == 'Prodaga':
                for x in array_info_about_prodaga:
                    array_info_about_prodaga[i] -= 4
                    i += 1
                if array_info_about_prodaga[0] < 0:
                    print('Ошибка!')
                    _()
                    main_menu_prodavec()
                _()
                get_info_prodaga(array_info_about_prodaga)
        elif mes == 2:
            i = 0
            if user == 'Mashina':
                for x in array_info_about_mashina:
                    array_info_about_mashina[i] += 4
                    i += 1
                if array_info_about_mashina[3] > max_id:
                    print('Ошибка!')
                    _()
                    main_menu_klient()
                _()
                get_info_mashina(array_info_about_mashina)
            elif user == 'Prodaga':
                for x in array_info_about_prodaga:
                    array_info_about_prodaga[i] += 4
                    i += 1
                if array_info_about_prodaga[0] > max_id:
                    print('Ошибка!')
                    _()
                    main_menu_prodavec()
                _()
                get_info_prodaga(array_info_about_prodaga)
        elif mes == 3:
            if user == 'Mashina':
                print('Добавление новой машины на продажу недоступно')
                _()
                main_menu_klient()
            elif user == 'Prodaga':
                _()
                post_info_prodaga()
        elif mes == 4:
            break
    _()
    if user == 'Mashina':
        main_menu_klient()
    elif user == 'Prodaga':
        main_menu_prodavec()


### ТУТ ВСЕ ДЛЯ КЛИЕНТА ###
def widget_klient():
    max_id = int(len(requests.get('http://localhost:4388/ham/odata/Klient').json()['value']))
    array_info_about_klient = [1, 2, 3, 4]
    get_info_klient(array_info_about_klient)

    while True:
        mes = int(input('1.Влево\n2.Вправо\n3.Добавить нового\n4.Назад\n'))
        if mes == 1:
            i = 0
            for x in array_info_about_klient:
                array_info_about_klient[i] -= 4
                i += 1
            if array_info_about_klient[0] < 0:
                print('Ошибка!')
                _()
                main_menu_klient()
            _()
            get_info_klient(array_info_about_klient)
        elif mes == 2:
            i = 0
            for x in array_info_about_klient:
                array_info_about_klient[i] += 4
                i += 1
            if array_info_about_klient[-1] > max_id:
                print('Ошибка!')
                _()
                main_menu_klient()
            get_info_klient(array_info_about_klient)
        elif mes == 3:
            _()
            add_new_user('Klient')
        elif mes == 4:
            break
    _()
    main_menu_klient()


def get_info_klient(array_info_about_klient):
    data = []
    for x in array_info_about_klient:
        if x >= 100:
            response = requests.get('http://localhost:4388/ham/odata/Klient(1' + str(
                x) + ')?$expand=pokupki/mashiny,pokupki/prodavec').json()
        elif 100 > x >= 10:
            response = requests.get('http://localhost:4388/ham/odata/Klient(10' + str(
                x) + ')?$expand=pokupki/mashiny,pokupki/prodavec').json()
        elif x < 10:
            response = requests.get('http://localhost:4388/ham/odata/Klient(100' + str(
                x) + ')?$expand=pokupki/mashiny,pokupki/prodavec').json()

        if str(response['pokupki']) != '[]':
            pokupki = 'Купил ' + str(len(response['pokupki'][0]['mashiny'])) + ' машины ' \
                      + 'у продавца ' + str(response['pokupki'][0]['prodavec']['fIO'])
        else:
            pokupki = 'Покупок нет'

        data += [['##########################################',
                  'Личная карточка №' + str(x),
                  'Имя: ' + str(response['fIO']),
                  'Паспорт: ' + str(response['pasport']),
                  'Организация: ' + str(response['organizaciya']),
                  'Статус: ' + pokupki,
                  '##########################################']]

    print(data[0][0] + '   ' + data[1][0] + '   ' + data[2][0] + '   ' + data[3][0])
    print(data[0][1] + ' ' * int(42 - len(data[0][1])) + '   ' + data[1][1] + ' ' * int(42 - len(data[1][1])) + '   ' + data[2][1] + ' ' * int(42 - len(data[2][1])) + '   ' + data[3][1] + ' ' * int(42 - len(data[3][1])))
    print(data[0][2] + ' ' * int(42 - len(data[0][2])) + '   ' + data[1][2] + ' ' * int(42 - len(data[1][2])) + '   ' + data[2][2] + ' ' * int(42 - len(data[2][2])) + '   ' + data[3][2] + ' ' * int(42 - len(data[3][2])))
    print(data[0][3] + ' ' * int(42 - len(data[0][3])) + '   ' + data[1][3] + ' ' * int(42 - len(data[1][3])) + '   ' + data[2][3] + ' ' * int(42 - len(data[2][3])) + '   ' + data[3][3] + ' ' * int(42 - len(data[3][3])))
    print(data[0][4] + ' ' * int(42 - len(data[0][4])) + '   ' + data[1][4] + ' ' * int(42 - len(data[1][4])) + '   ' + data[2][4] + ' ' * int(42 - len(data[2][4])) + '   ' + data[3][4] + ' ' * int(42 - len(data[3][4])))
    print(data[0][5] + ' ' * int(42 - len(data[0][5])) + '   ' + data[1][5] + ' ' * int(42 - len(data[1][5])) + '   ' + data[2][5] + ' ' * int(42 - len(data[2][5])) + '   ' + data[3][5] + ' ' * int(42 - len(data[3][5])))
    print(data[0][6] + '   ' + data[1][6] + '   ' + data[2][6] + '   ' + data[3][6])


def get_info_mashina(array_info_about_mashina):
    data = []
    for x in array_info_about_mashina:
        if x >= 100:
            response = requests.get('http://localhost:4388/ham/odata/Mashina(5' + str(x) + ')?$expand=postavshik,prodaga/prodavec,prodaga/klient').json()
        elif 100 > x >= 10:
            response = requests.get('http://localhost:4388/ham/odata/Mashina(50' + str(x) + ')?$expand=postavshik,prodaga/prodavec,prodaga/klient').json()
        elif x < 10:
            response = requests.get('http://localhost:4388/ham/odata/Mashina(500' + str(x) + ')?$expand=postavshik,prodaga/prodavec,prodaga/klient').json()

        status = ['', '', '']
        try:
            status[0] = 'Продана ' + str(response['prodaga']['data']) + ' за ' + str(response['prodaga']['summa'])
            status[1] = 'Продавец ' + str(response['prodaga']['prodavec']['fIO'])
            status[2] = 'Покупатель ' + str(response['prodaga']['klient']['fIO'])
        except:
            status[0] = 'В продаже'
            status[1] = ''
            status[2] = ''
        data += [['##########################################',
                  'Номер карточки: ' + str(x),
                  'Модель: ' + str(response['modelj']),
                  'Серийный номер: ' + str(response['seriinyiNomer']),
                  'Год: ' + str(response['god']),
                  'Состояние: ' + str(response['sostoyanie']),
                  'Поставка: ' + str(response['postavka']),
                  'Цена: ' + str(response['cena']),
                  'Поставщик: ' + str(response['postavshik']['nazvanie'] + ', ' + str(response['postavshik']['telefon'])),
                  'Статус: ' + str(status[0]),
                  '        ' + str(status[1]),
                  '        ' + str(status[2]),
                  '##########################################']]

    print(data[0][0] + '   ' + data[1][0] + '   ' + data[2][0] + '   ' + data[3][0])
    print(data[0][1] + ' ' * int(42 - len(data[0][1])) + '   ' + data[1][1] + ' ' * int(42 - len(data[1][1])) + '   ' + data[2][1] + ' ' * int(42 - len(data[2][1])) + '   ' + data[3][1] + ' ' * int(42 - len(data[3][1])))
    print(data[0][2] + ' ' * int(42 - len(data[0][2])) + '   ' + data[1][2] + ' ' * int(42 - len(data[1][2])) + '   ' + data[2][2] + ' ' * int(42 - len(data[2][2])) + '   ' + data[3][2] + ' ' * int(42 - len(data[3][2])))
    print(data[0][3] + ' ' * int(42 - len(data[0][3])) + '   ' + data[1][3] + ' ' * int(42 - len(data[1][3])) + '   ' + data[2][3] + ' ' * int(42 - len(data[2][3])) + '   ' + data[3][3] + ' ' * int(42 - len(data[3][3])))
    print(data[0][4] + ' ' * int(42 - len(data[0][4])) + '   ' + data[1][4] + ' ' * int(42 - len(data[1][4])) + '   ' + data[2][4] + ' ' * int(42 - len(data[2][4])) + '   ' + data[3][4] + ' ' * int(42 - len(data[3][4])))
    print(data[0][5] + ' ' * int(42 - len(data[0][5])) + '   ' + data[1][5] + ' ' * int(42 - len(data[1][5])) + '   ' + data[2][5] + ' ' * int(42 - len(data[2][5])) + '   ' + data[3][5] + ' ' * int(42 - len(data[3][5])))
    print(data[0][6] + ' ' * int(42 - len(data[0][6])) + '   ' + data[1][6] + ' ' * int(42 - len(data[1][6])) + '   ' + data[2][6] + ' ' * int(42 - len(data[2][6])) + '   ' + data[3][6] + ' ' * int(42 - len(data[3][6])))
    print(data[0][7] + ' ' * int(42 - len(data[0][7])) + '   ' + data[1][7] + ' ' * int(42 - len(data[1][7])) + '   ' + data[2][7] + ' ' * int(42 - len(data[2][7])) + '   ' + data[3][7] + ' ' * int(42 - len(data[3][7])))
    print(data[0][8] + ' ' * int(42 - len(data[0][8])) + '   ' + data[1][8] + ' ' * int(42 - len(data[1][8])) + '   ' + data[2][8] + ' ' * int(42 - len(data[2][8])) + '   ' + data[3][8] + ' ' * int(42 - len(data[3][8])))
    print(data[0][9] + ' ' * int(42 - len(data[0][9])) + '   ' + data[1][9] + ' ' * int(42 - len(data[1][9])) + '   ' + data[2][9] + ' ' * int(42 - len(data[2][9])) + '   ' + data[3][9] + ' ' * int(42 - len(data[3][9])))
    print(data[0][10] + ' ' * int(42 - len(data[0][10])) + '   ' + data[1][10] + ' ' * int(42 - len(data[1][10])) + '   ' + data[2][10] + ' ' * int(42 - len(data[2][10])) + '   ' + data[3][10] + ' ' * int(42 - len(data[3][10])))
    print(data[0][11] + ' ' * int(42 - len(data[0][11])) + '   ' + data[1][11] + ' ' * int(42 - len(data[1][11])) + '   ' + data[2][11] + ' ' * int(42 - len(data[2][11])) + '   ' + data[3][11] + ' ' * int(42 - len(data[3][11])))
    print(data[0][12] + '   ' + data[1][12] + '   ' + data[2][12] + '   ' + data[3][12])


### ТУТ ВСЕ ДЛЯ ПРОДАВЦА ###
def widget_prodavec():
    max_id = int(len(requests.get('http://localhost:4388/ham/odata/Prodavec').json()['value']))
    array_info_about_prodavec = [1, 2, 3]
    get_info_prodavec(array_info_about_prodavec)

    while True:
        mes = int(input('1.Влево\n2.Вправо\n3.Добавить нового\n4.Назад\n'))
        if mes == 1:
            i = 0
            for x in array_info_about_prodavec:
                array_info_about_prodavec[i] -= 3
                i += 1
            if array_info_about_prodavec[0] < 0:
                print('Ошибка!')
                _()
                main_menu_prodavec()
            _()
            get_info_prodavec(array_info_about_prodavec)
        elif mes == 2:
            i = 0
            for x in array_info_about_prodavec:
                array_info_about_prodavec[i] += 3
                i += 1
            if array_info_about_prodavec[-1] > max_id:
                print('Ошибка!')
                _()
                main_menu_prodavec()
            get_info_klient(array_info_about_prodavec)
        elif mes == 3:
            _()
            add_new_user('Prodavec')
        elif mes == 4:
            break
    _()
    main_menu_prodavec()


def get_info_prodavec(array_info_about_prodavec):
    data = []
    for x in array_info_about_prodavec:
        if x >= 100:
            response = requests.get('http://localhost:4388/ham/odata/Prodavec(2' + str(x) + ')?$expand=prodagi').json()
        elif 100 > x >= 10:
            response = requests.get('http://localhost:4388/ham/odata/Prodavec(20' + str(x) + ')?$expand=prodagi').json()
        elif x < 10:
            response = requests.get('http://localhost:4388/ham/odata/Prodavec(200' + str(x) + ')?$expand=prodagi').json()

        if str(response['prodagi']) != '[]':
            prodagi = len(response['prodagi'])
        else:
            prodagi = 'Продаж нет'

        data += [['##########################################',
                  'Личная карточка №' + str(x),
                  'Имя: ' + str(response['fIO']),
                  'Телефон: ' + str(response['telefon']),
                  'Принят на работу: ' + str(response['prinyat']),
                  'Дата рождения: ' + str(response['dataRogdeniya']),
                  'Количество продаж: ' + str(prodagi),
                  '##########################################']]

    print(data[0][0] + '   ' + data[1][0] + '   ' + data[2][0])
    print(data[0][1] + ' ' * int(42 - len(data[0][1])) + '   ' + data[1][1] + ' ' * int(42 - len(data[1][1])) + '   ' + data[2][1] + ' ' * int(42 - len(data[2][1])))
    print(data[0][2] + ' ' * int(42 - len(data[0][2])) + '   ' + data[1][2] + ' ' * int(42 - len(data[1][2])) + '   ' + data[2][2] + ' ' * int(42 - len(data[2][2])))
    print(data[0][3] + ' ' * int(42 - len(data[0][3])) + '   ' + data[1][3] + ' ' * int(42 - len(data[1][3])) + '   ' + data[2][3] + ' ' * int(42 - len(data[2][3])))
    print(data[0][4] + ' ' * int(42 - len(data[0][4])) + '   ' + data[1][4] + ' ' * int(42 - len(data[1][4])) + '   ' + data[2][4] + ' ' * int(42 - len(data[2][4])))
    print(data[0][5] + ' ' * int(42 - len(data[0][5])) + '   ' + data[1][5] + ' ' * int(42 - len(data[1][5])) + '   ' + data[2][5] + ' ' * int(42 - len(data[2][5])))
    print(data[0][6] + ' ' * int(42 - len(data[0][6])) + '   ' + data[1][6] + ' ' * int(42 - len(data[1][6])) + '   ' + data[2][6] + ' ' * int(42 - len(data[2][6])))
    print(data[0][7] + '   ' + data[1][7] + '   ' + data[2][7])


def get_info_prodaga(array_info_about_prodaga):
    data = []
    for x in array_info_about_prodaga:
        if x >= 100:
            response = requests.get('http://localhost:4388/ham/odata/Prodaga(4' + str(x) + ')?$expand=prodavec,klient').json()
        elif 100 > x >= 10:
            response = requests.get('http://localhost:4388/ham/odata/Prodaga(40' + str(x) + ')?$expand=prodavec,klient').json()
        elif x < 10:
            response = requests.get('http://localhost:4388/ham/odata/Prodaga(400' + str(x) + ')?$expand=prodavec,klient').json()

        data += [['##########################################',
                  'Дата: ' + str(response['data']),
                  'Договор: ' + str(response['dogovor']),
                  'Сумма: ' + str(response['summa']),
                  'Продавец: ' + str(response['prodavec']['fIO']),
                  '          ' + str(response['prodavec']['telefon']),
                  'Клиент: ' + str(response['klient']['fIO']),
                  '        ' + str(response['klient']['telefon']),
                  '        ' + str(response['klient']['organizaciya']),
                  '##########################################']]

    print(data[0][0] + '   ' + data[1][0] + '   ' + data[2][0] + '   ' + data[3][0])
    print(data[0][1] + ' ' * int(42 - len(data[0][1])) + '   ' + data[1][1] + ' ' * int(42 - len(data[1][1])) + '   ' + data[2][1] + ' ' * int(42 - len(data[2][1])) + '   ' + data[3][1] + ' ' * int(42 - len(data[3][1])))
    print(data[0][2] + ' ' * int(42 - len(data[0][2])) + '   ' + data[1][2] + ' ' * int(42 - len(data[1][2])) + '   ' + data[2][2] + ' ' * int(42 - len(data[2][2])) + '   ' + data[3][2] + ' ' * int(42 - len(data[3][2])))
    print(data[0][3] + ' ' * int(42 - len(data[0][3])) + '   ' + data[1][3] + ' ' * int(42 - len(data[1][3])) + '   ' + data[2][3] + ' ' * int(42 - len(data[2][3])) + '   ' + data[3][3] + ' ' * int(42 - len(data[3][3])))
    print(data[0][4] + ' ' * int(42 - len(data[0][4])) + '   ' + data[1][4] + ' ' * int(42 - len(data[1][4])) + '   ' + data[2][4] + ' ' * int(42 - len(data[2][4])) + '   ' + data[3][4] + ' ' * int(42 - len(data[3][4])))
    print(data[0][5] + ' ' * int(42 - len(data[0][5])) + '   ' + data[1][5] + ' ' * int(42 - len(data[1][5])) + '   ' + data[2][5] + ' ' * int(42 - len(data[2][5])) + '   ' + data[3][5] + ' ' * int(42 - len(data[3][5])))
    print(data[0][6] + ' ' * int(42 - len(data[0][6])) + '   ' + data[1][6] + ' ' * int(42 - len(data[1][6])) + '   ' + data[2][6] + ' ' * int(42 - len(data[2][6])) + '   ' + data[3][6] + ' ' * int(42 - len(data[3][6])))
    print(data[0][7] + ' ' * int(42 - len(data[0][7])) + '   ' + data[1][7] + ' ' * int(42 - len(data[1][7])) + '   ' + data[2][7] + ' ' * int(42 - len(data[2][7])) + '   ' + data[3][7] + ' ' * int(42 - len(data[3][7])))
    print(data[0][8] + ' ' * int(42 - len(data[0][8])) + '   ' + data[1][8] + ' ' * int(42 - len(data[1][8])) + '   ' + data[2][8] + ' ' * int(42 - len(data[2][8])) + '   ' + data[3][8] + ' ' * int(42 - len(data[3][8])))
    print(data[0][9] + '   ' + data[1][9] + '   ' + data[2][9] + '   ' + data[3][9])


def post_info_prodaga():
    max_id_klient = str(len(requests.get('http://localhost:4388/ham/odata/Klient').json()['value']))
    last_id_prodaga = int(requests.get('http://localhost:4388/ham/odata/Prodaga').json()['value'][-1]['$id'])
    new_user_id = last_id_prodaga + 1
    r = ''

    while str(r) != '<Response [200]>':
        if r != '':
            print('Ошибка при заполнении, повторите')
            _()
        data = [{
            "$type": "Prodaga",
            "data": input('Введите необходимые данные строго(!!!) по образцу:\nДата( гггг-мм-дд): '),
            "dogovor": "",
            "summa": input('Сумма: '),
            "prodavec@ref": "Prodavec(2" + input('Ваш ID( *** ): ') + ")",
            "klient@ref": "Klient(1" + input('ID клиента (1-' + max_id_klient + ')( *** ): ') + ")",
        }]

        requests.post('http://localhost:4388/ham/sql/SetNextHamId?id=' + str(new_user_id))
        r = requests.post('http://localhost:4388/ham/odata/Prodaga', json=data)
    print('Успешно!')
    _()
    main_menu_prodavec()


if __name__ == '__main__':
    main_menu()

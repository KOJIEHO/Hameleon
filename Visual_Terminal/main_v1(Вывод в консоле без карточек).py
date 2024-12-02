import requests


def start():
    mes = int(input('---- Главное меню ----:\n1.Клиент\n2.Продавец\n3.Закончить работу\n'))
    if mes == 1:
        _()
        mes = int(input('---- Клиенты ----:\n1.Показать всех\n2.Добавить нового\n3.Назад\n'))
        if mes == 1:
            ### Список первых 20 пользователей + переход на некст страницу (?) + фильтры мб + еще какие-то приколы по алгоритму
            _()
            add_new_user('Klient')
            print('Успешно!')
            _()
            klient_menu()
        elif mes == 2:
            _()
            total_klient = int(len(requests.get('http://localhost:4388/ham/odata/Klient').json()['value']))
            mes = int(input('Введите ID пользователя\n'))
            if mes > total_klient or mes < 1:
                while mes > total_klient or mes < 1:
                    mes = int(input('Такого пользователя не существует. Введите ID пользователя повторно\n'))
            print('Успешно!')
            _()
            klient_menu()
        elif mes == 3:
            start()

    elif mes == 2:
        _()
        mes = int(input('---- Продавец ----:\n1.Регистрация\n2.Авторизация\n3.Назад\n'))
        if mes == 1:
            _()
            add_new_user('Prodavec')
            print('Успешно!')
            _()
            prodavec_menu()
        elif mes == 2:
            total_prodavec = int(len(requests.get('http://localhost:4388/ham/odata/Prodavec').json()['value']))
            _()
            mes = int(input('Введите ID пользователя\n'))
            if mes > total_prodavec or mes < 1:
                while mes > total_prodavec or mes < 1:
                    mes = int(input('Такого пользователя не существует. Введите ID пользователя повторно\n'))
            print('Успешно!')
            _()
            prodavec_menu()
        elif mes == 3:
            start()

    elif mes == 3:
        pass


### ОБЩЕЕ ###
def _():
    print('*'*20)


def add_new_user(user):
    last_id = int(requests.get('http://localhost:4388/ham/odata/' + user).json()['value'][-1]['$id'])
    new_user_id = last_id + 1
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


def get_info(user):
    max_id = int(len(requests.get('http://localhost:4388/ham/odata/' + str(user)).json()['value']))
    if user == 'Mashina':
        mes = int(input('Введите номер машины для продажи (1-' + str(max_id) + ')\n'))
    elif user == 'Prodaga':
        mes = int(input('Введите номер записи продажи (1-' + str(max_id) + ')\n'))
    if mes > max_id or mes < 1:
        while mes > max_id or mes < 1:
            if user == 'Mashina':
                mes = int(input('Номера машины не существует. Введите номер машины повторно\n'))
            elif user == 'Prodaga':
                mes = int(input('Номера такой продажи не существует. Введите номер продажи повторно\n'))
    actual_id = mes
    _()
    if user == 'Mashina':
        get_info_mashina(mes)
    elif user == 'Prodaga':
        get_info_prodaga(mes)
    while True:
        mes = int(input('1.Влево\n2.Вправо\n3.Назад\n'))
        if mes == 1:
            _()
            actual_id -= 1
            if actual_id == 0:
                print('Ошибка!')
                _()
                if user == 'Mashina':
                    klient_menu()
                elif user == 'Prodaga':
                    prodavec_menu()
            if user == 'Mashina':
                get_info_mashina(actual_id)
            elif user == 'Prodaga':
                get_info_prodaga(actual_id)
        elif mes == 2:
            _()
            actual_id += 1
            if actual_id > max_id:
                print('Ошибка!')
                _()
                if user == 'Mashina':
                    klient_menu()
                elif user == 'Prodaga':
                    prodavec_menu()
            if user == 'Mashina':
                get_info_mashina(actual_id)
            elif user == 'Prodaga':
                get_info_prodaga(actual_id)
        elif mes == 3:
            break
    _()
    if user == 'Mashina':
        klient_menu()
    elif user == 'Prodaga':
        prodavec_menu()


### ТУТ ВСЕ ДЛЯ КЛИЕНТА ###
def klient_menu():
    mes = int(input('----Меню клиента----\n1.Посмотреть доступные предложения\n2.Назад\n'))
    if mes == 1:
        _()
        get_info('Mashina')
    elif mes == 2:
        _()
        start()


def get_info_mashina(mes):
    if mes >= 100:
        response = requests.get('http://localhost:4388/ham/odata/Mashina(5' + str(mes) + ')?$expand=postavshik,prodaga').json()
    elif 100 > mes >= 10:
        response = requests.get('http://localhost:4388/ham/odata/Mashina(50' + str(mes) + ')?$expand=postavshik,prodaga').json()
    elif mes < 10:
        response = requests.get('http://localhost:4388/ham/odata/Mashina(500' + str(mes) + ')?$expand=postavshik,prodaga').json()

    try:
        status = 'Продана ' + str(response['prodaga']['data']) + ' за ' + str(response['prodaga']['summa']) + + ', продавец ' + str(response['prodaga']['prodavec']['fIO']) + ', покупатель ' + str(response['prodaga']['klient']['fIO'])
    except:
        status = 'В продаже'

    data = 'Номер карточки: ' + str(mes) \
           + '\nМодель: ' + str(response['modelj']) \
           + '\nСерийный номер: ' + str(response['seriinyiNomer']) \
           + '\nГод: ' + str(response['god']) \
           + '\nСостояние: ' + str(response['sostoyanie']) \
           + '\nПоставка: ' + str(response['postavka']) \
           + '\nЦена: ' + str(response['cena']) \
           + '\nПоставщика: ' + str(response['postavshik']['nazvanie'] + ', ' + str(response['postavshik']['telefon'])) \
           + '\nСтатус: ' + status \
           + '\n************************************'
    print(data)


### ТУТ ВСЕ ДЛЯ ПРОДАВЦА ###
def prodavec_menu():
    mes = int(input('----Меню продавца----\n1.Посмотреть существующие записи\n2.Добавить новую запись о продаже\n3.Назад\n'))
    if mes == 1:
        _()
        get_info('Prodaga')
    elif mes == 2:
        _()
        post_info_prodaga()
        print('Успешно!')
        _()
        prodavec_menu()
    elif mes == 3:
        _()
        start()


def get_info_prodaga(mes):
    if mes >= 100:
        response = requests.get('http://localhost:4388/ham/odata/Prodaga(4' + str(mes) + ')?$expand=prodavec,klient').json()
    elif 100 > mes >= 10:
        response = requests.get('http://localhost:4388/ham/odata/Prodaga(40' + str(mes) + ')?$expand=prodavec,klient').json()
    elif mes < 10:
        response = requests.get('http://localhost:4388/ham/odata/Prodaga(400' + str(mes) + ')?$expand=prodavec,klient').json()

    data = 'Дата: ' + str(response['data']) \
           + '\nДоговор: ' + str(response['dogovor']) \
           + '\nСумма: ' + str(response['summa']) \
           + '\nПродавец: ' + str(response['prodavec']['fIO']) + ', ' + str(response['prodavec']['telefon']) \
           + '\nКлиент: ' + str(response['klient']['fIO']) + ', ' + str(response['klient']['organizaciya']) + ', ' + str(response['klient']['telefon'])
    print(data)


def post_info_prodaga():
    max_id_klient = str(len(requests.get('http://localhost:4388/ham/odata/Klient').json()['value']))
    last_id = int(requests.get('http://localhost:4388/ham/odata/Prodaga').json()['value'][-1]['$id'])
    new_user_id = last_id + 1
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
    prodavec_menu()


if __name__ == '__main__':
    start()


    # r = requests.get('http://localhost:4388/ham/odata/Klient')
    # print(r.headers)
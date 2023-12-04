import requests
import csv


url = 'http://localhost:4388/ham/odata/Klient?$expand=pokupki/mashiny,pokupki/prodavec'
response = requests.get(url).json()

max_id = int(len(response['value']))
i = 1

with open("hameleon.csv", "w", newline="") as ham:
    writer = csv.writer(ham)
    writer.writerow(['Личная карточка №', 'Имя', 'Паспорт', 'Организация', 'Статус'])

    while i < max_id:
        a = response['value'][i]
        if str(response['value'][i]['pokupki']) != '[]':
            pokupki = 'Купил ' + str(len(a['pokupki'][0]['mashiny'])) + ' машины ' \
                      + 'у продавца ' + str(a['pokupki'][0]['prodavec']['fIO'])
        else:
            pokupki = 'Покупок нет'

        writer.writerow([str(i), str(a['fIO']), str(a['pasport']), str(a['organizaciya']), pokupki])

        print(str(i), str(a['fIO']), str(a['pasport']), str(a['organizaciya']), pokupki)
        i += 1

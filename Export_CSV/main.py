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
        if str(response['value'][i]['Pokupki']) != '[]':
            pokupki = 'Купил ' + str(len(a['Pokupki'][0]['Mashiny'])) + ' машины ' \
                      + 'у продавца ' + str(a['Pokupki'][0]['Prodavec']['FIO'])
        else:
            pokupki = 'Покупок нет'

        writer.writerow([str(i), str(a['FIO']), str(a['Pasport']), str(a['Organizaciya']), pokupki])

        print(str(i), str(a['FIO']), str(a['Pasport']), str(a['Organizaciya']), pokupki)
        i += 1
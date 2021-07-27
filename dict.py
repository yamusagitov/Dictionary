dict ={}
while True:
    fruites = input('Что хотите? ')
    price = int(input('Стоимость: '))
    dict.update([(fruites, price)])
    print(dict)


# groceries = []

# groceries = {'name': "plátano", 'price': 300},\
#             {'name': "pan", 'price': 150},\
#             {'name': "leche (de vaca)", 'price': 230},\
#             {'name': "huevo", 'price': 280},\
#             {'name': "carne", 'price': 800},\
#             {'name': "pescado", 'price': 500}

# taro_name = "Taro Yamada"
# taro_address = "Tokyo"

# print("------Lista de compras------")

# i = 0
# while len(groceries) > i:
#     print(f"{i}: {groceries[i]['name']}, {groceries[i]['price']}")
#     i += 1


# taro_basket = []
# shopping_end = None

# while shopping_end != 'yes':
#     print("Seleccione el numero de articulo")
#     number = int(input())
#     print("Ingrese la cantidad de producto")
#     quantity = input()

#     taro_basket.append([groceries[number], quantity])
#     print("Quieres terminar la comopra? yes/no")
#     shopping_end = input()

# sum = 0
# i = 0
# print(f"--------Lista de la compra({taro_name}/{taro_address})--------")

# while len(taro_basket) > i:
#     grocery = taro_basket[i][0]
#     quantum = int(taro_basket[i][1])
#     money = grocery['price'] * quantum
#     print(f"Nombre comercial (marca): {grocery['name']}, volumen: {quantum}, cantidad de dinero: {money}")
#     sum += money
#     i += 1

# print(f"--------importe total: {sum}----------")
# print("=================================")


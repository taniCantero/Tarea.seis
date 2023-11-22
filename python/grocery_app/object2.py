class Grocery:
    def __init__(self, name, price):
        self.name = name
        self.price = price

class User:
    def __init__(self, arg1, arg2=None, arg3=None):
        self.name = arg1
        self.address = arg2


class Customer(User):
    total = 0
    from shopping import _grocery_list, _shopping_list
    
    def __init__(self, name, address):
        super().__init__(name, address)
        self.basket = []

    def shopping(self, groceries):
        import datetime
        
        self.__grocery_list(groceries)
        shopping_end = None
        
        while shopping_end != 'yes':
            # Select product
            print('Seleccione el numero de articulo')
            number = int(input())
            # Cantidad de producto
            print("Ingrese la cantidad de producto")
            quantity = int(input())
            self.__entry(groceries[number], quantity)
            print('Quieres terminar de comprar? yes/no')
            shopping_end = input()
            
        self.__shopping_list(self.basket)
        order = [self.name, self.total, datetime.datetime.now().strftime("%Y-%m-%d")]
        return order

    def __grocery_list(self, groceries):
        print("------Lista de compras------")
        for i, grocery in enumerate(groceries):
            print(f"{i}: {grocery.name}, {grocery.price}")

    def __entry(self, grocery, quantity):
        self.basket.append([grocery, quantity])
    
    def __shopping_list(self, basket):
        print(f"====== lisda de compras({self.name}/{self.address}) ======")
        for grocery in basket:
            name = grocery[0].name
            price = grocery[0].price
            quantity = grocery[1]
            money = price * quantity
            print(f'Nombre comercial (marca): {name}, volumen: {quantity}, cantidad de dinero: {money}')
            self.total += money
        print(f'------ importe total: {self.total} -------')
        print('===============================')


class Seller(User):
    from shopping import ordering_list
    def __init__(self, name, shop, address=None):
        super().__init__(name, address)
        self.shop = shop
        self.orders = []
        
    def ordered(self, order):
        self.orders.append(order)
    
    def ordering_list(self):
        total = 0
        print(f'====== Lista de pedidos por cliente({self.name}, {self.shop})')
        for order in self.orders:
            print(f'Nombre del cliente: {order[0]}, cantidad de dinero: {order[1]}, fecha y hora: {order[2]}')
            total += order[1]
            
        print(f"--------------importe total：{total}")
        print("====================================")
        
groceries = []

# Instanciar cada producto y almacenarlo en la matriz de productos.
groceries = Grocery('plátano', 300),\
            Grocery('pan', 150),\
            Grocery('leche (de vaca)', 230),\
            Grocery('huevo', 280),\
            Grocery('carne', 800),\
            Grocery('pescado', 500)
            

ichiro = Seller("Ichiro Takahashi", "Una tienda")

taro = Customer('Taro Yamada', 'Tokyo')

order = taro.shopping(groceries)

ichiro.ordered(order)
ichiro.ordering_list()



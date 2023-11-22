from grocery import Grocery
from customer import Customer
from seller import Seller

# Creación de listas de productos（objeto）
groceries = []
groceries = Grocery("plátano", 300),\
            Grocery("pan", 150),\
            Grocery("leche (de vaca)", 230),\
            Grocery("huevo", 280),\
            Grocery("carne", 800),\
            Grocery("pescado", 500)

# Instanciación de vendedor (Ichiro Takahashi, Una tienda).
ichiro = Seller("Ichiro Takahashi", "Una tienda.")

# Taro Yamada
taro = Customer("Taro Yamada", "Tokyo")
hanako = Customer("Hanako Suzuki", "Nagoya")
tommy = Customer("Tommy Sasaki", "Osaka")


# Taro Yamada ＆lista de la compra
order = taro.shopping(groceries)
ichiro.ordered(order)

order = hanako.shopping(groceries)
ichiro.ordered(order)

order = tommy.shopping(groceries)
ichiro.ordered(order)

# Visualizacion de lista
ichiro.orderling_list()
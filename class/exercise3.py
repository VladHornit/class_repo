class Product:
    def __init__(self,product_name, price):
        self.product_name = product_name
        self.price = price


class Customer:
    def __init__(self):
        self.shoping_cart = []


    def add_product_to_cart(self, product):
        self.shoping_cart.append(product)


class Shop:
    def __init__(self):
        self.product_list = []
        #self.profit = profit


    def add_product_to_inventory(self, product, product_avaliable_quantity):
        product.product_avaliable_quantity = product_avaliable_quantity
        self.product_list.append(product)

    def print_inventory(self):
        #print(self.product_list.name, self.product_list.product_avaliable_quantity)
        print(self.product_list) # why it it shows not a list [<__main__.Product object at 0x100dfbbe0>] ?
        #print(self.product_list[0], self.product_list[1])


    def checkout(self, shoping_cart):
        n = 1
        while n <= len(self.shoping_cart):
            total_price = shoping_cart.price + shoping_cart.price
            n += 1

        self.product_list.remove(self.shoping_cart.product)


product_1 = Product("water", 1)
customer_1 = Customer()
shop_1 = Shop()

customer_1.add_product_to_cart(product_1)
shop_1.add_product_to_inventory(product_1, 5)
shop_1.print_inventory() # why it it shows not a list [<__main__.Product object at 0x100dfbbe0>] ?
shop_1.checkout(customer_1)


#print(shop_1.product_list) why it shows not a list?

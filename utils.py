
class Item:
    pay_rate = 1
    all =[]

    def __init__(self, item_name, price, quantity):
        self.item_name = item_name
        self.price = price
        self.quantity = quantity
        Item.all.append(self)


    def calculate_total_price(self):
        """
        Функция умножения цены на количество
        :return:
        """
        return self.price * self.quantity


    def apply_discount(self):
        """
        Функция умножения цены на скидку
        :return:
        """
        self.price *= Item.pay_rate
        return self.price


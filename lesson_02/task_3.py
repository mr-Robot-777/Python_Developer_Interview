"""
3. Усовершенствовать родительский класс таким образом,
чтобы получить доступ к защищенным переменным.
Результат выполнения заданий 1 и 2 должен быть идентичным.
"""


class ItemDiscount:
    def __init__(self, name, price):
        self.__name = name
        self.__price = price

    @property
    def name(self):
        return self.__name

    @property
    def price(self):
        return self.__price


class ItemDiscountReport(ItemDiscount):
    def get_parent_data(self):
        return f'Товар {self.name}, цена {self.price}' 


item = ItemDiscountReport('Диван', 11000)
print(item.get_parent_data())

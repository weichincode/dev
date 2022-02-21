class Item:
    def __init__(self, name, price, weight):
        self.name = name
        self.price = price
        self.weight = weight 

    def net_weight(self, weight, price):
        return weight / price
        # net_weight: Higher better


item1 = Item("kettle", 5.20, 200)

print(item1.net_weight)

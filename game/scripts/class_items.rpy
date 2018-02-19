init -50 python:
    class Item:
        def __init__ (self, name, id, cost, type, picto = 'images/noimage.gif', description = '', weight = 5):
            self.name = name
            self.id = id
            self.cost = cost
            self.description = description
            self.picto = picto
            self.type = type
            self.stolen = False
            self.weight = weight
        
        def steal(self):
            self.stolen = True
            
    class Tool(Item):
        def __init__ (self, purpose):
            self.purpose = purpose
            
    def genItems():
        smallMoneyBag = Item(
            name = 'Малый кошель',
            id = 'smallMoneyBag',
            cost = 15,
            description = 'Малый кожаный кошель, содержит небольшое количество монет.',
            picto = 'images/noimage.gif',
            type = ['money','pocket','location'],
            weight = 5
            )
        allItems.append(smallMoneyBag)
        
        moneyBag = Item(
            name = 'Кошель',
            id = 'moneyBag',
            cost = 30,
            description = 'Кожаный кошель, содержит монеты.',
            picto = 'images/noimage.gif',
            type = ['money','pocket','location'],
            weight = 10
            )
        allItems.append(moneyBag)
        
        bigMoneyBag = Item(
            name = 'Большой кошель',
            id = 'bigMoneyBag',
            cost = 100,
            description = 'Кожаный кошель, в нём может быть много монет.',
            picto = 'images/noimage.gif',
            type = ['money','pocket','location'],
            weight = 15
            )
        allItems.append(bigMoneyBag)
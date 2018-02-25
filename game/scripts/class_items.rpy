init -50 python:
    class Item:
        def __init__ (self, name, id, cost, type, picto = 'images/noimage.gif', description = '', weight = 5, durability = 1):
            self.name = name
            self.id = id
            self.cost = cost
            self.description = description
            self.picto = picto
            self.type = type
            self.stolen = False
            self.weight = weight
            self.durability = durability
        
        def steal(self):
            self.stolen = True
            
    class Tool(Item):
        def __init__ (self, effects):
            self.effects = effects
            
            
        def addEffect(self,effect):
            for x in allEffects:
                if x.id == effect:
                    self.effects.append(copy.copy(x))
                    
                    
    class Clothes(Item):
        def __init__ (self, parts, effects):
            self.parts = parts
            self.effects = effects
            
        def addEffect(self,effect):
            for x in allEffects:
                if x.id == effect:
                    self.effects.append(x)
                    
    def genClothes():
        
        womanClothes = Clothes(parts = ['body','hands','legs'], effects = [] )
        womanClothes.name = 'Женское платье'
        womanClothes.id = 'womanClothes'
        womanClothes.cost = 1000
        womanClothes.description = 'Женская одежда, помогает обаянию, но имеет штраф к ловкости.'
        womanClothes.picto = 'images/noimage.gif'
        womanClothes.type = ['clothes']
        womanClothes.weight = 15
        womanClothes.durability = 10000
        womanClothes.addEffect('dex2minus')
        womanClothes.addEffect('cha2plus')
        allItems.append(womanClothes)
        
        thiefArmor = Clothes(parts = ['body'], effects = [] )
        thiefArmor.name = 'Воровская броня'
        thiefArmor.id = 'thiefArmor'
        thiefArmor.cost = 1000
        thiefArmor.description = 'Броня вора, бонус к ловкости.'
        thiefArmor.picto = 'images/noimage.gif'
        thiefArmor.type = ['clothes']
        thiefArmor.weight = 15
        thiefArmor.durability = 10000
        thiefArmor.addEffect('dex2plus')
        thiefArmor.effects
        allItems.append(thiefArmor)
        
    def getClothById(id):
        for x in allItems:
            if x.id == id:
                return x
        
        
    def genItems():
        lockpick = Tool(effects = [])
        lockpick.name = 'Простая отмычка'
        lockpick.id = 'lockpick'
        lockpick.cost = 100
        lockpick.description = 'Простая отмычка, лучший друг взломщика!'
        lockpick.picto = 'images/noimage.gif'
        lockpick.type = ['tool']
        lockpick.weight = 1
        lockpick.durability = 10
        lockpick.addEffect('unlock')
        allItems.append(lockpick)
        
        instrument = Tool(effects = [])
        instrument.name = 'Инструмент для обезвреживания'
        instrument.id = 'instrument'
        instrument.cost = 100
        instrument.description = 'Инструмент для обезвреживания ловушек.'
        instrument.picto = 'images/noimage.gif'
        instrument.type = ['tool']
        instrument.weight = 10
        instrument.durability = 100
        instrument.addEffect('disarm')
        allItems.append(instrument)
        
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
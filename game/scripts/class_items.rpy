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
        def __init__ (self, effects, stolen = False):
            self.effects = effects
            self.stolen = stolen
            
            
        def addEffect(self,effect):
            for x in allEffects:
                if x.id == effect:
                    self.effects.append(copy.copy(x))
                    
                    
    class Clothes(Item):
        def __init__ (self, parts, effects, stolen = False):
            self.parts = parts
            self.effects = effects
            self.stolen = stolen
            
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
        allItems.append(thiefArmor)
        
        manClothes = Clothes(parts = ['body','hands','legs'], effects = [] )
        manClothes.name = 'Мужская одежда'
        manClothes.id = 'manClothes'
        manClothes.cost = 1000
        manClothes.description = 'Мужская одежда. Не имеет ни бонусов ни недостатков.'
        manClothes.picto = 'images/noimage.gif'
        manClothes.type = ['clothes']
        manClothes.weight = 15
        manClothes.durability = 10000
        allItems.append(manClothes)
        
        nothing = Clothes(parts = ['body'], effects = [] )
        nothing.name = 'Ничего не надето'
        nothing.id = 'nothing'
        nothing.cost = 1000
        nothing.description = 'Полностью обнажиться'
        nothing.picto = 'images/noimage.gif'
        nothing.type = ['clothes']
        nothing.weight = 15
        nothing.durability = 10000
        nothing.addEffect('dex2plus')
        nothing.effects
        allItems.append(nothing)
        
    def getClothById(id):
        for x in allItems:
            if x.id == id:
                return x
        
        
    def genItems():
        hairpin = Tool(effects = [])
        hairpin.name = 'Заколка для волос'
        hairpin.id = 'hairpin'
        hairpin.cost = 10
        hairpin.description = 'Заколка, для закалывания волос. Ловкие пальчики могут использовать её как отмычку!'
        hairpin.picto = 'images/items/lockpick.png'
        hairpin.type = ['tool']
        hairpin.weight = 1
        hairpin.durability = 10
        hairpin.addEffect('unlock1')
        allItems.append(hairpin)
        
        lockpick = Tool(effects = [])
        lockpick.name = 'Простая отмычка'
        lockpick.id = 'lockpick'
        lockpick.cost = 100
        lockpick.description = 'Простая отмычка, лучший друг взломщика!'
        lockpick.picto = 'images/items/lockpick.png'
        lockpick.type = ['tool']
        lockpick.weight = 1
        lockpick.durability = 1
        lockpick.addEffect('unlock')
        allItems.append(lockpick)
        
        instrument = Tool(effects = [])
        instrument.name = 'Инструмент для обезвреживания'
        instrument.id = 'instrument'
        instrument.cost = 100
        instrument.description = 'Инструмент для обезвреживания ловушек.'
        instrument.picto = 'images/items/instrument.png'
        instrument.type = ['tool']
        instrument.weight = 10
        instrument.durability = 1
        instrument.addEffect('disarm')
        allItems.append(instrument)
        
        cheatTool = Tool(effects = [])
        cheatTool.name = 'Мастер-Отмычка'
        cheatTool.id = 'cheatTool'
        cheatTool.cost = 100000
        cheatTool.description = 'Для разработки.'
        cheatTool.picto = 'images/items/instrument.png'
        cheatTool.type = ['tool']
        cheatTool.weight = 10
        cheatTool.durability = 100000
        cheatTool.addEffect('disarm1000')
        cheatTool.addEffect('unlock1000')
        allItems.append(cheatTool)
        
        coins = Item(
            name = 'Мелочь',
            id = 'coins',
            cost = 5,
            description = 'Маленькая горстка мелочи.',
            picto = 'images/noimage.gif',
            type = ['money','pocket','location'],
            weight = 5
            )
        allItems.append(coins)
        
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
        
        vexel = Item(
            name = 'Вексель Фрэнка',
            id = 'vexel',
            cost = 100,
            description = 'Вексель, который надо украсть для Фрэнка.',
            picto = 'images/noimage.gif',
            type = ['qwest'],
            weight = 15
            )
        allItems.append(vexel)
        
    def getItem(id):
        for x in allItems:
            if x.id == id:
                return x
        return False
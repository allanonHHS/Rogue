init -10 python:
    config.use_cpickle = True
    dynpicto = ''
init -2 python:
    #объявление массивов
    picto_m = []
    picto_mOld = []
    picto_f = []
    picto_fOld = []

    # Загружаем все имеющиеся картинки
    def weightChoice(dict):
        allWeight = sum(dict.values())
        rnd = rand(0,allWeight-1)
        upto = 0
        for element in dict:
            upto += dict.get(element)
            if rnd in range(0,upto):
                return element
        return None
        
    import os
    for path in config.searchpath:
        # Ищем каталоги с картинками во всех возможных RenPy каталогах ресурсов
        try:
            for x in os.listdir(os.path.join(path, 'images/picto/male/')):
                picto_m.append(os.path.join('images/picto/male/', x))
                
            for x in os.listdir(os.path.join(path, 'images/picto/maleOld/')):
                picto_mOld.append(os.path.join('images/picto/maleOld/', x))
                
            for x in os.listdir(os.path.join(path, 'images/picto/female/')):
                picto_f.append(os.path.join('images/picto/female/', x))
                
            for x in os.listdir(os.path.join(path, 'images/picto/femaleOld/')):
                picto_fOld.append(os.path.join('images/picto/femaleOld/', x))

        except OSError:
            pass
            
    def genChars(amount):
        tempArr = []
        for x in range(0,amount):
            if rand(1,2) == 1:
                tempChar = Char.random('male', 'images/noimage.gif')
            else:
                tempChar = Char.random('female', 'images/noimage.gif')
            tempChar.autoLevel(rand(0,2))
            if tempChar.lname in ['Дворянин', 'Дворянка']:
                tempChar.autoLevel(rand(5,10))
                tempChar.addItem('bigMoneyBag')
                if rand(1,2) == 1:
                    tempChar.addItem('bigMoneyBag')
                    
            elif tempChar.lname in ['Стражник']:
                tempChar.autoLevel(rand(8,10))
                tempChar.addItem('moneyBag')
                
            elif tempChar.lname in ['Наёмник']:
                tempChar.autoLevel(rand(5,15))
                tempChar.togglePerception()
                for x in range(0,10):
                    if rand(1,5) == 1:
                        tempChar.addItem(choice(['bigMoneyBag','moneyBag','smallMoneyBag']))
                    
            elif tempChar.lname in ['Вор']:
                tempChar.autoLevel(rand(2,5))
                tempChar.addSkill('stealth')
                tempChar.addItem(choice(['bigMoneyBag','moneyBag','smallMoneyBag']))
                tempChar.addItem('lockpick')
                
            elif tempChar.lname in ['Кузнец','Ремесленник','Ремесленница']:
                tempChar.autoLevel(rand(2,5))
                tempChar.addItem(choice(['moneyBag','smallMoneyBag','instrument','lockpick']))
                
            if tempChar.lname == 'Купец':
                tempChar.do = 'merchantSpeak'
                
            if tempChar.getSex() == 'female':
                tempChar.addItem('hairpin')
            
            if len(tempChar.inventory) == 0:
                tempChar.addItem('coins')

            tempChar.addSkill(choice(allSkills).id)
            tempArr.append(tempChar)
        return tempArr
        
    def genChar(type = 'guard'):
        if type == 'guard':
            tempChar = Char.random('male', 'images/noimage.gif')
            tempChar.autoLevel(rand(8,10))
            tempChar.togglePerception()
            tempChar.addSkill('perception')
            tempChar.lname = 'Стражник'
            tempChar.name = tempChar.fname + ' ' + tempChar.lname
        elif type == 'female':
            tempChar = Char.random('female', 'images/noimage.gif')
            tempChar.autoLevel(rand(1,3))
            tempChar.lname = 'REPLACE'
            tempChar.name = tempChar.fname + ' ' + tempChar.lname
        return tempChar
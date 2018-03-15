init:
    image daytime = ConditionSwitch(
        "hour < 5 or hour > 20", "#646464",
        "hour >=5  and hour <= 8", "#FFD6BD",
        "hour > 8  and hour <= 18", "#FFFFFF",
        "hour > 18  and hour <= 20", "#EB9191",
        )
    image black = '#000000'

init python:
#базовая функция перемещения. Использовать всегда и всюду
    from random import shuffle
    def move(where):
        if isinstance(where, basestring):
            for x in allLocs:
                if x.id == where:
                    where = x
                    break
        global curloc, prevloc, outside #Объявляем глобальную переменную курлок, которая явлеется объектом текущей локации
        prevloc = curloc # Сохраняем предыдущую локацию
        curloc = where # Присваиваем курлоку текущее назначение
        if 'generated' not in curloc.type:
            outside = curloc
        renpy.scene(layer='master') # Сброс картинок
        renpy.scene(layer='screens') # Сброс скринов
        renpy.show('black') # Базовый фон
        changetime(5)
        checkTriggers()
        resetStats([])
        addPeopleLoc(where)
        checkTraps(where)
        renpy.jump('location_label') #Прыгаем на наш костыль для вызовы скрина локации
        
    def checkTraps(location):
        tempArr = []
        for door in location.doors:
            if door.hidden == True:
                if isSuccess(player.useSkill('perception'), door.difficulty, hidden = True, exp = 5*door.difficulty):
                    door.hidden = False
                    
            if door.hidden == False:
                for item in door.container:
                    if isinstance(item, Trap) and item.found == False:
                        if isSuccess(player.useSkill('perception'), item.difficulty, 'Поиск ловушек', hidden = True, exp = 2*item.difficulty):
                            item.found = True
                            
    def resetStats(input):
        player.inventory.sort(key=lambda x: x.name)
        for x in input:
            x.normalize()
        player.normalize()
        player.recountEffects()
        player.checkDurability()
        player.checkLevel()
        player.setEnergy(min(max(player.getEnergy(),0),player.getMaxEnergy()))
        
    def addPeopleLoc(location):
        location.people = []
        if 'private' in location.type:
            peopleAmount = 0
        else:
            if hour in range(7,12):
                peopleAmount = rand(10,15)
            elif hour in range(13, 18):
                peopleAmount = rand(5,10)
            elif hour in range(18, 19):
                peopleAmount = rand(0,5)
            else:
                peopleAmount = 0
        
        
        if location.id in ['severGate', 'zapadGate', 'ugGate']:
            location.people.append(genChar('guard'))
            location.people.append(genChar('guard'))
            if rand(1,3) == 1 and hour in range(7,19):
                location.people.append(genChar('merchant'))
            
        if location.id in ['tavern']:
            if hour in range(12,23):
                location.people.append(frank)
                location.description[2] = 'За прилавком стоит сам  Френк - содержатель «Уюта для странника», суровый на вид, небритый, с цепким и хитрым взглядом.'
            else:
                location.people.append(frank_helper)
                peopleAmount = rand(0,2)
                location.description[2] = 'За прилавком стоит помощник Френка, меланхольный малый с отсутствующим выражением лица.'
            if hour in range(7,23):
                location.people.append(elsa)
                peopleAmount = rand(2,10)
                
        if location.id == 'elsaRoom':
            if hour < 7 or hour == 23:
                location.people.append(elsa)
            
            if hour == 23 and rand(1,2) == 1 and prevloc != curloc:
                renpy.jump('elsaFrankSex')
        
        if location.id == 'smallStore':
            peopleAmount = rand(0,5)
            if hour in range(7,12):
                location.people.append(michael_wife)
                location.description[1] = 'У прилавка немолодая женщина, по виду жена хозяина. С ней вам не о чём разговаривать. Возможно позже её место займёт более интересный собеседник.'
            elif hour in range(12,22):
                location.people.append(dick)
                location.description[1] = 'У прилавка стоит молодой плечистый парень, по-видимому, помощник хозяина.'
            else:
                location.description[1] = ''
                peopleAmount = 0
                if prevloc == curloc:
                    move('severPrigorod')
                
        if location.id == 'severGate':
            if hour == 7 and trigger[15] in [1,2,3]:
                location.people.append(michael)
                if michael.getItem('vexel') == False and trigger[15] >= 2:
                    michael.addItem('vexel')
            if player.getItem('vexel') != False:
                michael.removeItem('vexel')
        
        if trigger[15] >= 2 and trigger[16] == 0:
            trigger[16] = 1
            genHouse(getLocation('smallStore'), type = 'store', addtionalType = 'existStore', special = ['gen_bedroom','vexel'])
            
        if hour in range(7,22) or trigger[15] >= 2:
            getLocation('smallStore').getDoor('storeDoor1').lock(False)
        else:
            getLocation('smallStore').getDoor('storeDoor1').lock(True)
            
        if 'generated' in location.type:
            peopleAmount = 0
        
        location.people += genChars(peopleAmount)
        
    def clrscr():
        renpy.scene(layer='screens')
        
    def checkTriggers():
        if player.getHP() <= 0:
            renpy.jump('death')
        
        if trigger[1] == 0 and curloc.id in ['severArea','zapadArea','ugArea'] and player.getBodyPart().id == 'manClothes' and trigger[18] != 1:
            renpy.jump('enterCityMan')
            
        if trigger[1] == 0 and curloc.id in ['severArea','zapadArea','ugArea']  and player.getBodyPart().id != 'manClothes':
            renpy.jump('enterCity')
            
        if hour in range(7,22) and 'generated' in curloc.type:
            renpy.jump('breaking_catch')
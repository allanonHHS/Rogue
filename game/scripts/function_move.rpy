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
        global curloc, prevloc #Объявляем глобальную переменную курлок, которая явлеется объектом текущей локации
        prevloc = curloc # Сохраняем предыдущую локацию
        curloc = where # Присваиваем курлоку текущее назначение
        renpy.scene(layer='master') # Сброс картинок
        renpy.scene(layer='screens') # Сброс скринов
        renpy.show('black') # Базовый фон
        changetime(5)
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
                    if isinstance(item, Trap):
                        if isSuccess(player.useSkill('perception'), item.difficulty, hidden = True, exp = 2*item.difficulty):
                            item.found = True
                            
    def resetStats(input):
        player.inventory.sort(key=lambda x: x.name)
        for x in input:
            x.normalize()
        player.normalize()
        player.recountEffects()
        player.checkDurability()
        player.checkLevel()
        
    def addPeopleLoc(location):
        if 'private' in location.type:
            peopleAmount = 0
        else:
            peopleAmount = rand(0,10)
        peopleAmount = rand(0,10)
        location.people = genChars(peopleAmount)
        
    def clrscr():
        renpy.scene(layer='screens')
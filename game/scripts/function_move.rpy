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
                if door.difficulty < player.getPerception():
                    door.hidden == False
                    
            if door.hidden == False:
                for item in door.container:
                    if isinstance(item, Trap):
                        if item.difficulty < player.getPerception():
                            item.found = True
                            
    def resetStats(input):
        player.inventory.sort(key=lambda x: x.name)
        for x in input:
            x.normalize()
        player.normalize()
        player.recountEffects()
        player.checkDurability()
        
    def addPeopleLoc(location):
        if location.type == 'private':
            peopleAmount = 0
        else:
            peopleAmount = rand(5,30)
        peopleAmount = rand(5,30)
        location.people = genChars(peopleAmount)
        
    def clrscr():
        renpy.scene(layer='screens')
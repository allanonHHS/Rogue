init 10 python:
    def doorAction(door):
        if door.safe == True:
            return [Function(move, door.getLoc())]
        else:
            return [Show('unlock', None, door)]
            
    def doorEnter(door):
        for x in door.container:
            if isinstance(x, Lock):
                if x.state == 'closed':
                    return [Show('unlock', None, door)]
            if isinstance(x, Trap):
                if x.state == 'armed' and x.found == True:
                    return [Show('unlock', None, door)]
            if isinstance(x, Trap):
                if x.state == 'armed' and x.found == False:
                    return [Function(clrscr), Function(x.disarm), Jump(x.do)]
        return [Function(door.setSafe), Function(move, door.getLoc())]

    
    def unlock(lock, door):
        if isinstance(lock, Lock):
            if lock.difficulty < player.getUnlock():
                return [Function(lock.unlock), Function(changetime, 10), Show('unlockSuccess'),  Show('unlock', None, door)]
            else:
                if lock.do != '' and player.checkRescue(lock) == False:
                    return [Function(clrscr), Function(lock.unlock), Jump(lock.do)]
                else:
                    return [Function(changetime, 10), Show('unlockFail')]
        return NullAction
        
    def disarm(trap, door):
        if isinstance(trap, Trap):
            if player.getDisarmINT() > trap.difficulty and player.getDisarmDEX() > trap.difficulty:
                return [Function(trap.disarm), Function(changetime, 10), Show('unlockSuccess'),  Show('unlock', None, door)]
            else:
                if trap.do != '' and player.checkRescue(trap) == False:
                    return [Function(changetime, 10), Show('unlockFail')]
                else:
                    return [Function(clrscr), Function(trap.disarm), Jump(trap.do)]
        return NullAction
                    
    def checkDoorTrap(door):
        for item in door.container:
            if isinstance(item, Trap):
                if item.difficulty < player.getPerception():
                    item.find()

    
# Скрин, показывающй все локации
screen location(locObj):
    add locObj.image xpos 0.5 xanchor 0.5# Отображам картинку
    
    # frame xpos 0.01 ypos 0.01: # Слева отображаем имя локации
        # text(locObj.name) 
    
    frame xpos 0.01 ypos 0.9: # Внизу перебираем массив описаний и выводим строчку за строчкой
        has vbox
        for x in locObj.description:
            text(x)
            
    fixed xpos 0.83 ypos 0.1: # Перебираем массив локаций для перемещения, и делаем кнопки для каждой
        vbox:
            textbutton 'Осмотреться' xmaximum 300 xminimum 300 action [Function(changetime, 10)]
            for x in locObj.navigation:
                textbutton x.name xmaximum 300 xminimum 300 action [Function(move, x)]
                
            for x in locObj.doors:
                textbutton x.name + ':' + x.getLocName() xmaximum 300 xminimum 300 action doorAction(x)
                
    use stats(locObj)
    use displayTime
                
screen stats(locObj):
    frame xpos 0.01:
        has vbox
        $ temp = locObj.name
        text('Место : [temp]')
        add im.FactorScale('images/stand.png', 0.5)
        text(player.name)
        $ temp = player.getSTR()
        text ('Сила :[temp]')
        $ temp = player.getDEX()
        text ('Ловкость :[temp]')
        $ temp = player.getCON()
        text ('Выносливость :[temp]')
        $ temp = player.getINT()
        text ('Интеллект :[temp]')
        $ temp = player.getWIS()
        text ('Мудрость :[temp]')
        $ temp = player.getCHA()
        text ('Обаяние :[temp]')
            
screen unlock(door):
    frame xpos 0.5 ypos 0.5 xalign 0.5 yalign 0.5:
        has vbox
        # if development == 1:
            # text('Замки ' + str(len(door.getLocks())))
            # text('Ловушки ' + str(len(door.getTraps())))
        textbutton 'Осмотреть' xmaximum 250 xminimum 250 action [Function(changetime, 10), Show('unlock', None, door)]
        for x in door.container:
            if isinstance(x, Lock):
                if x.state == 'closed':
                    textbutton x.name + ':' + str(x.difficulty) action unlock(x, door) xmaximum 250 xminimum 250
                        
            if isinstance(x, Trap):
                if x.state == 'armed':
                    textbutton x.name + ':' + str(x.difficulty) action disarm(x, door) xmaximum 250 xminimum 250
                        
        if len(door.getLocks()) == 0:
            textbutton 'Войти' xmaximum 250 xminimum 250 action doorEnter(door)
        textbutton 'Уйти' xmaximum 250 xminimum 250 action Function(move, curloc)
                        
screen displayTime:
    vbox xalign 0.99 yalign 0.0:
        $ currtime = gettime('day')
        if minute < 10:
            $ temtime = '%s:0%s' % (hour, minute)
        else:
            $ temtime = '%s:%s' % (hour, minute)
        vbox:
            text currtime # style style.description xalign 0.99
            text temtime
                    
screen unlockSuccess:
    frame xpos 0.5 ypos 0.3:
        text ('Удача!')
    timer 1.0 action Hide("unlockSuccess")
    
screen unlockFail:
    frame xpos 0.5 ypos 0.3:
        text ('Неудача!')
    timer 1.0 action Hide("unlockFail")
                
# Костыль, с помощью которого вызываем скрин локаций
label location_label:
    call screen location(curloc)
    
                
            
            
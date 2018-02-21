init 10 python:
    import time
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
                    
    def checkDoorTrap(door):
        for item in door.container:
            if isinstance(item, Trap):
                if item.difficulty < player.getPerception():
                    item.find()
                    
    def checkPocket(char):
        if isSuccess(char.useSkill('perception'), player.useSkill('dexOfHand'),'Попытка вас заметить: '): #Если чар выбросил больше восприятия, чем мы воровства
            if isSuccess(char.useSkill('dex'), player.useSkill('dex'), 'Попытка вас поймать: '):
                if isSuccess(char.useSkill('str'), player.useSkill('str'), 'Попытка вас удержать: '):
                    clrscr()
                    renpy.jump('steal_catched')
                else:
                    clrscr()
                    renpy.jump('steal_escapeSTR')
            else:
                clrscr()
                renpy.jump('steal_escapeDEX')
        else:
            renpy.show_screen('stealScreen', char = char)
            renpy.restart_interaction()
                
            
    def stealAction(char, item):
        if isSuccess(char.useSkill('perception'), player.useSkill('dexOfHand'),'Попытка вас заметить: '): #Если чар выбросил больше восприятия, чем мы воровства
            if isSuccess(char.useSkill('dex'), player.useSkill('dex'), 'Попытка вас поймать: '):
                if isSuccess(char.useSkill('str'), player.useSkill('str'), 'Попытка вас удержать: '):
                    clrscr()
                    renpy.jump('steal_catched')
                else:
                    clrscr()
                    renpy.jump('steal_escapeSTR')
            else:
                clrscr()
                renpy.jump('steal_escapeDEX')
        else:
            player.stealItem(char, item)
            renpy.show_screen('stealScreen', char = char)
            renpy.restart_interaction()
            
            
    def unlock(lock, door):
        if isinstance(lock, Lock):
            if isSuccess(player.useSkill('breaking'), lock.difficulty, 'Взлом: '):
                lock.unlock()
                changetime(10)
                renpy.show_screen('unlock',door)
                renpy.restart_interaction()
            else:
                if lock.do != '' and isSuccess(player.useSkill(lock.rescue), lock.difficulty, 'Спасбросок: ') == False:
                    clrscr()
                    lock.unlock()
                    renpy.jump(lock.do)
                else:
                    changetime(10)
                    renpy.show_screen('unlock',door)
                    renpy.restart_interaction()
                    
    def disarm(trap, door):
        if isinstance(trap, Trap):
            if isSuccess(player.useSkill('int'), trap.difficulty, 'Знание ловушек: ')  and isSuccess(player.useSkill('disarm'), trap.difficulty, 'Обезвреживание: '):
                trap.disarm()
                changetime(10)
                renpy.show_screen('unlock',door)
                renpy.restart_interaction()
            else:
                if trap.do != '' and isSuccess(player.useSkill(trap.rescue), trap.difficulty, 'Спасбросок: ') == False:
                    clrscr()
                    trap.disarm()
                    renpy.jump(trap.do)
                else:
                    changetime(10)
                    renpy.show_screen('unlock',door)
                    renpy.restart_interaction()

    def inventoryAction(item):
        if 'money' in item.type:
            return [Function(player.incMoney, rand(0, item.cost)), Function(player.removeItem, item),  Show('inventory')]
        else:
            return [Show('inventory')]
            
            
    curried_checkPocket = renpy.curry(checkPocket)
    curried_stealAction = renpy.curry(stealAction)
    curried_unlock = renpy.curry(unlock)
    curried_disarm = renpy.curry(disarm)
    
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
            textbutton 'Карманы' xmaximum 300 xminimum 300 action [Show('inventory')]
            textbutton 'Осмотреться' xmaximum 300 xminimum 300 action [Function(changetime, 10)]
            null height 15
            for x in locObj.navigation:
                textbutton x.name xmaximum 300 xminimum 300 action [Function(move, x)]
                
            for x in locObj.doors:
                textbutton x.name + ':' + x.getLocName() xmaximum 300 xminimum 300 action doorAction(x)
    if development == 1:
        textbutton 'test' action Jump('test') xpos 0.5 ypos 0.5
                
    use stats(locObj)
    use displayTime
    use showLocPeople
    use diceTrows
    # if development == 1:
        # use testGen
                
screen stats(locObj):
    vbox:
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
        frame xpos 0.01:
            if 'sneak' in player.state:
                textbutton 'Прекратить красться' action [Function(player.toggleSneak)]
            else:
                textbutton 'Красться' action [Function(player.toggleSneak)]
    
            
screen unlock(door):
    zorder 10
    modal True
    frame xpos 0.5 ypos 0.5 xalign 0.5 yalign 0.5:
        has vbox
        if development == 1:
            text('Замки ' + str(len(door.getLocks())))
            text('Ловушки ' + str(len(door.getTraps())))
        text door.name xalign 0.5 xanchor 0.5
        textbutton 'Осмотреть' xmaximum 250 xminimum 250 action [Function(changetime, 10), Function(checkDoorTrap, door), Show('unlock', None, door)]
        for x in door.container:
            if isinstance(x, Lock):
                if x.state == 'closed':
                    textbutton x.name + ':' + str(x.difficulty):
                        action curried_unlock(x, door)
                        xmaximum 250 xminimum 250
                        
            if isinstance(x, Trap):
                if x.state == 'armed' and x.found == True:
                    textbutton x.name + ':' + str(x.difficulty):
                        action curried_disarm(x, door)
                        xmaximum 250 xminimum 250
                        
        if len(door.getLocks()) == 0:
            textbutton 'Войти' xmaximum 250 xminimum 250 action doorEnter(door)
        textbutton 'Уйти' xmaximum 250 xminimum 250 action Function(move, curloc)
        
    use diceTrows
                        
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
    frame xpos 0.5 ypos 0.3 xalign 0.5:
        text ('Удача!')
    timer 1.0 action Hide("unlockSuccess")
    
screen unlockFail:
    frame xpos 0.5 ypos 0.3 xalign 0.5:
        text ('Неудача!')
    timer 1.0 action Hide("unlockFail")
                
# Костыль, с помощью которого вызываем скрин локаций
label location_label:
    call screen location(curloc)
    
screen showChar(testChar):
    frame xpos 0.5 ypos 0.5 xalign 0.5 yalign 0.5:
        has vbox
        text (testChar.name)
        text ('Уровень :' + str(testChar.getLevel() ))
        text ('Жизни :' + str(testChar.getHP() ))
        text ('Сила :' + str(testChar.getSTR() ))
        text ('Ловкость :' + str(testChar.getDEX() ))
        text ('Выносливость :' + str(testChar.getCON() ))
        text ('Интеллект :' + str(testChar.getINT() ))
        text ('Мудрость :' + str(testChar.getWIS() ))
        text ('Обаяние :' + str(testChar.getCHA() ))
        text ('Сумма статов :' + str(testChar.getSTR() + testChar.getDEX() + testChar.getCON() + testChar.getINT() + testChar.getWIS() + testChar.getCHA() ))
        null height 15
        for x in testChar.inventory:
            text (x.name)
        
screen showLocPeople:
    frame xpos 0.12 ypos 0.0 xmaximum 250 xminimum 250:
        has vbox
        for x in curloc.people:
            textbutton x.name:
                hovered [Show('showChar', None, x)]
                unhovered [Hide('showChar')]
                action [Show('choiceCharAction', None, x)]
                xmaximum 250 xminimum 250
                
screen choiceCharAction(char):
    # tag pickPoket
    frame xpos 0.5 ypos 0.5 xalign 0.5 yalign 0.5:
        has vbox
        textbutton 'Поговорить' action []
        textbutton 'Проверить карманы' action  curried_checkPocket(char)
            
            
screen stealScreen(char):
    zorder 5
    modal True
    # tag pickPoket
    frame xpos 0.3 ypos 0.3:
        has vbox
        text ('В карманах у ' + char.fname)
        for x in char.inventory:
            textbutton x.name action curried_stealAction(char, x)
        if len(char.inventory) == 0:
            text ('Пусто')
        textbutton 'Уйти' action [Function(move, curloc)]
            
screen inventory:
    frame xpos 0.5 ypos 0.5 xalign 0.5 yalign 0.5:
        has vbox
        text ('В карманах у меня:')
        for x in player.inventory:
            textbutton x.name action inventoryAction(x)
        text (str(player.money) + ' Крон')
        textbutton 'Уйти' action [Function(move, curloc)]
        
screen diceTrows:
    frame xpos 0.53 ypos 0.01 xalign 0.5:
        has vbox
        python:
            while len(diceTrowsArr) > 5:
                diceTrowsArr.pop(0)
        for x in reversed(diceTrowsArr):
            text(x) style 'smallText'
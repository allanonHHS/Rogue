init 10 python:
    import time
    myItem = 0
    mySet = []
    voteDecision = False
    last_inventory = 'all'
    
    def inv_show_list(type) :
        if not type in ['all', 'stolen', 'tool', 'clothing', 'unsorted']:
            type = 'all'
        list = []
        showed = []
        for x in player.inventory:
            if type == 'all' and not x.id in showed and x.stolen == False and x.id != 'nothing':
                list += [x]
                showed += [x.id]
            elif type == 'stolen' and not x.id in showed and x.stolen == True:
                list += [x]
                showed += [x.id]
            elif type == 'tool' and isinstance(x, Tool) and not x.id in showed:
                list += [x]
                showed += [x.id]
            elif type == 'clothing' and isinstance(x, Clothes) and x.id != 'nothing':
                list += [x]
            elif type == 'unsorted' and x.id != 'nothing':
                list += [x]
        return list
        
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
                if isSuccess(player.useSkill('perception'), item.difficulty, hidden = True, exp = 2*item.difficulty):
                    item.find()
                    
    def checkPocket(char):
        if isSuccess(player.useSkill('dexOfHand'), char.useSkill('perception'), 'Проверка карманов: ', exp = 10*char.getLevel()) == False:
            if isSuccess(player.useSkill('dex'), char.useSkill('dex'), 'Попытка увернуться: ') == False:
                if isSuccess(player.useSkill('str'), char.useSkill('str'), 'Попытка вырваться: ') == False:
                    clrscr()
                    renpy.jump('steal_catched')
                else:
                    clrscr()
                    renpy.jump('steal_escapeSTR')
            else:
                clrscr()
                renpy.jump('steal_escapeDEX')
        else:
            renpy.hide_screen('choiceCharAction')
            renpy.show_screen('stealScreen', char = char)
            renpy.restart_interaction()
                
            
    def stealAction(char, item):
        if isSuccess( player.useSkill('dexOfHand'), char.useSkill('perception'), 'Воровство: ', exp = 10*char.getLevel()) == False:
            if isSuccess(player.useSkill('dex'), char.useSkill('dex'), 'Попытка увернуться: ') == False:
                if isSuccess(player.useSkill('str'), char.useSkill('str'), 'Попытка вырваться: ') == False:
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
            if isSuccess(player.useSkill('breaking'), lock.difficulty, 'Взлом: ', exp = lock.difficulty*5):
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
            if isSuccess(player.useSkill('int'), trap.difficulty, 'Знание ловушек: ', exp = trap.difficulty*5)  and isSuccess(player.useSkill('disarm'), trap.difficulty, 'Обезвреживание: ', exp = trap.difficulty*5):
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
        if 'storing' in curloc.type:
            return [Function(player.removeItem, item), Function(curloc.addItem, item), Show('inventory')]
        # elif 'clothes' in item.type:
            # return [Function(player.wearFunc, item), Show('inventory')]
        else:
            return [Show('inventory')]
            
    def useTool(tool, door):
        if tool not in player.wear:
            player.equipTool(tool)
        else:
            player.unequipTool(tool)
        renpy.show_screen('unlock',door)
        renpy.restart_interaction()
            
    def getItems(list):
        tempArr = []
        used = []
        for x in list:
            if x.name not in used:
                tempArr.append(x)
                used.append(x.name)
        return tempArr
        
    def getOutfitDisplay():
        if player.getBodyPart().id == 'nothing':
            return 'images/outfit/zero1.png'
        elif player.getBodyPart().id == 'thiefArmor':
            return 'images/outfit/zero13.png'
        elif player.getBodyPart().id == 'womanClothes':
            return 'images/outfit/zero3.png'
        else:
            return 'images/noimage.gif'
            
    def dropItems():
        itemsToRemove = []
        for x in player.inventory:
            if x.stolen == True:
                itemsToRemove.append(x)
                curloc.items.append(x)
        for x in itemsToRemove:
            player.inventory.remove(x)
            
    curried_checkPocket = renpy.curry(checkPocket)
    curried_stealAction = renpy.curry(stealAction)
    curried_unlock = renpy.curry(unlock)
    curried_disarm = renpy.curry(disarm)
    
# Скрин, показывающй все локации
screen location(locObj):
    add locObj.image xpos 0.5 xanchor 0.5# Отображам картинку
    
    # frame xpos 0.01 ypos 0.01: # Слева отображаем имя локации
        # text(locObj.name) 
    
    frame xpos 350 ypos 725: # Внизу перебираем массив описаний и выводим строчку за строчкой
        has vbox
        for x in locObj.description:
            text(x)
            
    fixed xpos 0.83 ypos 0.1: # Перебираем массив локаций для перемещения, и делаем кнопки для каждой
        vbox:
            textbutton 'Карманы' xmaximum 300 xminimum 300 action [Show('inventory')]
            textbutton 'Осмотреться' xmaximum 300 xminimum 300 action [Function(changetime, 5), Function(move, curloc)]
            if curloc.id in ['home']:
                textbutton 'Гардероб' xmaximum 300 xminimum 300 action Show('wardrobe')
            if 'storing' in locObj.type:
                textbutton 'Сложить ворованное' xmaximum 300 xminimum 300 action Function(dropItems)
            if len(locObj.items) > 0:
                textbutton 'Обыскать' xmaximum 300 xminimum 300 action Show('locationItems')
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
        frame xpos 0.01 xminimum 345 xmaximum 345:
            vbox:
                imagebutton:
                    idle im.FactorScale(getOutfitDisplay(), 0.5)
                    hover im.FactorScale(getOutfitDisplay(), 0.5)
                    hovered Show('detailedStats', None, locObj)
                    unhovered Hide('detailedStats')
                    action NullAction
                text(player.name)
                text('HP ' + str(player.getHP()) + ' / ' + str(player.stats.maxHP)) style 'param'
                text('EXP ' + str(player.getExp()) + ' / ' + str(player.getNextLevelExp())) style 'param'
                if statInc > 0 or skillInc > 0:
                    textbutton 'Повысить уровень' action Show('levelUp')
                else:
                    text 'Уровень [player.stats.level]' style 'param'
        null height 20
            
        frame xpos 0.01 xminimum 345:
            has vbox
            if 'sneak' in player.state:
                textbutton 'Прекратить красться' action [Function(player.toggleSneak)]
            else:
                textbutton 'Красться' action [Function(player.toggleSneak)]
            if 'alarm' in player.state:
                textbutton 'Не присматриваться' action [Function(player.togglePerception)]
            else:
                textbutton 'Быть внимательной' action [Function(player.togglePerception)]
                
screen detailedStats(locObj):
    frame xalign 0.5 ypos 150:
        has vbox
        text(player.name)
        text('HP ' + str(player.getHP()) + ' / ' + str(player.stats.maxHP)) style 'param'
        text 'Уровень [player.stats.level]' style 'param'
        hbox:
            vbox:
                text ('Сила:') style 'param'
                text ('Ловкость:') style 'param'
                text ('Выносливость:') style 'param'
                text ('Интеллект:') style 'param'
                text ('Мудрость:') style 'param'
                text ('Обаяние:') style 'param'
            null width 20
            vbox:
                text (str(player.getSTR())) style 'param'
                text (str(player.getDEX())) style 'param'
                text (str(player.getCON())) style 'param'
                text (str(player.getINT())) style 'param'
                text (str(player.getWIS())) style 'param'
                text (str(player.getCHA())) style 'param'
            null width 20
            vbox:
                text ('Умения:')
                for x in player.getAllSkills():
                    text ('[x.name]') style 'param'
            null width 20
            vbox:
                text ('Эффекты:')
                for x in player.effects:
                    text ('[x.name]') style 'param'
        
        
    
            
screen unlock(door):
    imagebutton:
        idle 'images/bg.png'
        hover 'images/bg.png'
        action Hide('unlock')
    zorder 1
    modal True
    frame ypos 250 xalign 0.5 xminimum 250:
        vbox xalign 0.5:
            if development == 1:
                text('Замки ' + str(len(door.getLocks())))
                text('Ловушки ' + str(len(door.getTraps())))
            text door.name xalign 0.5 xanchor 0.5
            if 'alarm' not in player.state:
                textbutton 'Быть внимательной' xmaximum 250 xminimum 250 action Function(player.togglePerception)
            textbutton 'Осмотреть' xmaximum 250 xminimum 250 action [Function(changetime, 10), Function(checkDoorTrap, door), Show('unlock', None, door)]
            for x in door.container:
                if isinstance(x, Lock):
                    if x.state == 'closed':
                        textbutton x.name + ':' + str(x.difficulty):
                            action [Function(unlock, x, door)]
                            xmaximum 250 xminimum 250
                            
                if isinstance(x, Trap):
                    if x.state == 'armed' and x.found == True:
                        textbutton x.name + ':' + str(x.difficulty):
                            action [Function(disarm, x, door)]
                            xmaximum 250 xminimum 250
                            
            if len(door.getLocks()) == 0:
                textbutton 'Войти' xmaximum 250 xminimum 250 action doorEnter(door)
            textbutton 'Уйти' xmaximum 250 xminimum 250 action Hide('unlock')
    $ adj = ui.adjustment()
    python:
        tab_i = inv_show_list('tool')
        tab_cols = 3
        tab_rows = round(float(len(tab_i))/float(tab_cols) +0.45)
        # tab_rows = 30
        tab_n = (tab_rows*tab_cols) - len(tab_i)
    side "c r":
        area (1130, 250, 260, 300)
        viewport:
            yadjustment adj
            mousewheel True
            draggable True
            frame:
                grid tab_cols tab_rows:   
                    xfill True
                    spacing 5
                    for x in tab_i:
                        # $ x.picto = 'images/noimage.gif'
                        imagebutton:
                            idle im.MatrixColor(im.FactorScale(x.picto,0.4), im.matrix.opacity(0.7))
                            # idle im.MatrixColor(im.FactorScale(x.picto,0.4), im.matrix.opacity(1.0))
                            hover im.MatrixColor(im.FactorScale(x.picto,0.4), im.matrix.opacity(1.0))
                            hovered Show('displayTool', None, x)
                            unhovered Hide('displayTool')
                            action Function(useTool, x, door)
                    for i in range(int(tab_n)):
                        vbox:
                            null
    use diceTrows
    for x in player.wear:
        if isinstance(x, Tool):
            use selectedTool(x)
    
screen displayTool(tool):
    zorder 1
    # frame xpos 1130 ypos 500:
    frame xpos renpy.get_mouse_pos()[0] ypos renpy.get_mouse_pos()[1]:
        hbox:
            add im.FactorScale(tool.picto,0.5)
            vbox:
                text tool.name
                text tool.description style 'smallText'
                
screen selectedTool(tool):
    
    frame xpos 858 ypos 130:
        hbox:
            add im.FactorScale(tool.picto,0.5)
            null width 10
            vbox:
                text (tool.name + ' - Используется')
                text tool.description style 'smallText'
                text ('Использований: ' + str(tool.durability)) style 'smallText'
    
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
    if renpy.get_mouse_pos()[0] < 650:
        $ xcoord = 650
    else:
        $ xcoord = renpy.get_mouse_pos()[0]
    frame xpos xcoord ypos renpy.get_mouse_pos()[1]:
    # frame xpos 0.5 ypos 0.5 xalign 0.5 yalign 0.5:
        has vbox
        text (testChar.name)
        text ('Уровень :' + str(testChar.getLevel() ))
        if development == 1:
            text ('Жизни :' + str(testChar.getHP() )) style 'param'
            text ('Сила :' + str(testChar.getSTR() )) style 'param'
            text ('Ловкость :' + str(testChar.getDEX() )) style 'param'
            text ('Выносливость :' + str(testChar.getCON() )) style 'param'
            text ('Интеллект :' + str(testChar.getINT() )) style 'param'
            text ('Мудрость :' + str(testChar.getWIS() )) style 'param'
            text ('Обаяние :' + str(testChar.getCHA() )) style 'param'
            text ('Сумма статов :' + str(testChar.getSTR() + testChar.getDEX() + testChar.getCON() + testChar.getINT() + testChar.getWIS() + testChar.getCHA() ))
            null height 15
            for x in testChar.inventory:
                text (x.name)
            null height 15    
            for x in testChar.getAllSkills():
                text x.name
        
screen showLocPeople:
    frame xpos 350 ypos 0.0 xmaximum 250 xminimum 250:
        has vbox
        text (curloc.name) xalign 0.5
        text ('Я вижу неподалёку') xalign 0.5
        for x in curloc.people:
            textbutton x.name:
                hovered [Show('showChar', None, x)]
                unhovered [Hide('showChar')]
                action [Show('choiceCharAction', None, x)]
                xmaximum 240 xminimum 240
                
screen choiceCharAction(char):
    zorder 1
    modal True
    imagebutton:
        idle 'images/bg.png'
        hover 'images/bg.png'
        action Hide('choiceCharAction')
    if renpy.get_mouse_pos()[0] < 650:
        $ xcoord = 650
    else:
        $ xcoord = renpy.get_mouse_pos()[0]
    frame xpos xcoord ypos renpy.get_mouse_pos()[1]:
        has vbox
        textbutton 'Поговорить' action [] xminimum 250
        textbutton 'Проверить карманы' action Function(checkPocket, char) xminimum 250
        textbutton 'Отойти' action Hide('choiceCharAction') xminimum 250
            
            
screen stealScreen(char):
    zorder 1
    modal True
    imagebutton:
        idle 'images/bg.png'
        hover 'images/bg.png'
        action Function(move, curloc)
    text (char.fname + ' носит с собой:') xpos 450 ypos 160
    $ adj = ui.adjustment()
    python:
        tempArr = []
        for x in char.inventory:
            if isinstance(x, Clothes) == False:
                tempArr.append(x)
        tab_i = tempArr
        tab_cols = 5.0
        tab_rows = round(float(len(tab_i))/float(tab_cols) +0.45)
        # tab_rows = 30
        tab_n = (tab_rows*tab_cols) - len(tab_i)
    side "c r":
        area (450, 190, 1050, 600)
        frame:
            viewport:
                yadjustment adj
                mousewheel True
                draggable True
                grid tab_cols tab_rows:   
                    xfill True
                    spacing 5
                    for x in tab_i:
                        textbutton x.name:
                            xminimum 200 xmaximum 200 yminimum 80
                            hovered Show('itemDetails', None, x)
                            unhovered Hide('itemDetails')
                            action curried_stealAction(char, x)
                    for i in range(int(tab_n)):
                        vbox:
                            null
    textbutton 'X' xpos 1500 ypos 190:
        action [Function(move, curloc)]
    use diceTrows
    
screen inventory:
    zorder 1
    modal True
    imagebutton:
        idle 'images/bg.png'
        hover 'images/bg.png'
        action Function(move, curloc)
    fixed xpos 450 ypos 60:
        hbox :
            key "game_menu" action Function(move, curloc)
            # textbutton _('Назад') action Function(move, curloc)
            textbutton _('Всё') action [SetVariable('last_inventory','all'), Show('inventory')]
            textbutton _('Украденное') action [SetVariable('last_inventory','stolen'), Show('inventory')]
            textbutton _('Инструменты') action [SetVariable('last_inventory','tool'), Show('inventory')]
            textbutton _('Одежда') action [SetVariable('last_inventory','clothing'), Show('inventory')]
            textbutton _('Несортировано') action [SetVariable('last_inventory','unsorted'), Show('inventory')]
    frame xpos 1400 ypos 50:
        text('[player.money] Крон.')
    $ adj = ui.adjustment()
    python:
        tab_i = inv_show_list(last_inventory)
        tab_cols = 5.0
        tab_rows = round(float(len(tab_i))/float(tab_cols) +0.45)
        tab_n = (tab_rows*tab_cols) - len(tab_i)
    side "c r":
        area (450, 90, 1050, 600)
        frame:
            viewport:
                yadjustment adj
                mousewheel True
                draggable True
                grid tab_cols tab_rows:   
                    xfill True
                    spacing 5
                    for x in tab_i:
                        textbutton x.name:
                            xminimum 200 xmaximum 200 yminimum 80
                            hovered Show('itemDetails', None, x)
                            unhovered Hide('itemDetails')
                            action [inventoryAction(x), Hide('itemDetails')]
                    for i in range(int(tab_n)):
                        vbox:
                            null
    textbutton 'X' xpos 1500 ypos 90:
        action [Function(move, curloc)]

screen itemDetails(item):
    zorder 1
    frame xpos renpy.get_mouse_pos()[0] ypos renpy.get_mouse_pos()[1]:
        vbox:
            add item.picto
            text(item.name)
            if item.stolen:
                text('Украдено')
            text('Цена:' + str(item.cost))
            text('Прочность:' + str(item.durability))
            text('Количество:' + str(player.countItems(item.id)))
            if development == 1:
                text(str(item))
                            
screen wardrobe:
    zorder 1
    modal True
    imagebutton:
        idle 'images/bg.png'
        hover 'images/bg.png'
        action Function(move, curloc)
    frame xpos 0.5 ypos 0.5 xanchor 0.5 yanchor 0.5:
        hbox:
            add getOutfitDisplay()
            vbox:
                text 'Одето:'
                # 'body','legs', 'arms', 'feet', 'belt', 'head'
                textbutton 'Тело:\n' + player.getBodyPart('body').name:
                    xmaximum 200 xminimum 200
                    action Function(player.undressPart,'body')
                textbutton 'Ноги:\n' + player.getBodyPart('legs').name:
                    xmaximum 200 xminimum 200
                    action Function(player.undressPart,'legs')
                textbutton 'Руки:\n' + player.getBodyPart('arms').name:
                    xmaximum 200 xminimum 200
                    action Function(player.undressPart,'arms')
                textbutton 'Ботинки:\n' + player.getBodyPart('feet').name:
                    xmaximum 200 xminimum 200
                    action Function(player.undressPart,'feet')
                textbutton 'Пояс:\n' + player.getBodyPart('belt').name:
                    xmaximum 200 xminimum 200
                    action Function(player.undressPart,'belt')
                textbutton 'Голова:\n' + player.getBodyPart('head').name:
                    xmaximum 200 xminimum 200
                    action Function(player.undressPart,'head')
            null width 20
            vbox xminimum 250:
                text 'В инвентаре:'
                for x in player.inventory:
                    if isinstance(x, Clothes) and x.id != 'nothing':
                        textbutton x.name:
                            xminimum 200 xmaximum 200
                            action [Function(player.wearFunc, x), Show('wardrobe')]
            null width 20
            textbutton 'X':
                action [Function(move, curloc)]
                
screen locationItems:
    imagebutton:
        idle 'images/bg.png'
        hover 'images/bg.png'
        action Function(move, curloc)
    zorder 1
    $ adj = ui.adjustment()
    python:
        tab_i = curloc.items
        tab_cols = 5.0
        tab_rows = round(float(len(tab_i))/float(tab_cols) +0.45)
        # tab_rows = 30
        tab_n = (tab_rows*tab_cols) - len(tab_i)
    side "c r":
        area (450, 90, 1050, 600)
        frame:
            viewport:
                yadjustment adj
                mousewheel True
                draggable True
                grid tab_cols tab_rows:   
                    xfill True
                    spacing 5
                    for x in tab_i:
                        textbutton x.name:
                            xminimum 200 xmaximum 200 yminimum 80
                            hovered Show('itemDetails', None, x)
                            unhovered Hide('itemDetails')
                            action If('private' not in curloc.type, true = [Function(player.stealItem, curloc, x), Hide('itemDetails')], false = [Function(player.takeItem, curloc, x),Hide('itemDetails')])
                    for i in range(int(tab_n)):
                        vbox:
                            null
    textbutton 'X' xpos 1500 ypos 90:
        action [Function(move, curloc)]
        
screen diceTrows:
    if showDiceThrows == 1:
        frame xpos 610 ypos 0.0 xanchor 0.0:
            has vbox
            python:
                while len(diceTrowsArr) > 5:
                    diceTrowsArr.pop(0)
            for x in reversed(diceTrowsArr):
                text(x) style 'smallText'
            
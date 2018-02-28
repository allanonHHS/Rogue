label generatePlayer:
    python:
        playerBody = FemaleBody(175)
        playerBody.parts['грудь'].size = 3
        playerBody.parts['анус'].size = 0
        playerBody.parts['вагина'].size = 0

        playerStats = Stats(
            str = 9,
            dex = 14,
            con = 13,
            int = 11,
            wis = 16,
            cha = 15,
            hp = 0,
            energy = 0,
            exp = 0,
            level = 1
            
        )

        player = Char(
            fname = 'Алиса',
            lname = 'Грейн',
            age = 20,
            body = playerBody,
            stats = playerStats,
            color = '#EE6A38',
            inventory = [],
            wear = [],
            picto = 'images/picto/player_picto.png',
            location = curloc,
            money = 100,
            skills = [],
            state = []
        )
        
        player.setHP(8 + player.getCONmod())
        player.stats.maxHP = 8 + player.getCONmod()
        player.setEnergy(500 + player.getCONmod()*100 + player.getSTRmod()*100)
        genEffect()
        genItems()
        genClothes()
        genSkills()
        trigger = []
        for x in range(0,1000):
            trigger.append(0)
        allLocs = genLocs()
        player.addItem('womanClothes')
        player.addItem('nothing')
        player.wearFunc(player.getItem('womanClothes'))
        
        
        if development == 1:
            for x in range(0,5):
                player.addItem('lockpick')
                player.addItem('instrument')
        # testChar.autoLevel(rand(1,20))
        
        # move('home')
    jump intro
        
label test:
    python:
        player.addSkill('acrobatics')
        # player.stats.level = 1
        temp = player.useSkill('breaking')[1]
        # temp3 = player.useSkill('asd')
        # temp2 = str(player.getAllSkills()[0].getPower(player))
        # temp2 = 0
        count5 = 0
        count10 = 0
        count15 = 0
        count20 = 0
        count25 = 0
        count30 = 0
        for x in range(0,1000):
            if isSuccess(player.useSkill('cha'), 5):
                count5 += 1
            if isSuccess(player.useSkill('cha'), 10):
                count10 += 1
            if isSuccess(player.useSkill('cha'), 15):
                count15 += 1
            if isSuccess(player.useSkill('cha'), 20):
                count20 += 1
            if isSuccess(player.useSkill('cha'), 25):
                count25 += 1
            if isSuccess(player.useSkill('cha'), 30):
                count30 += 1
                
    ' Успехов из 1000 для сложности 5: [count5]\n
    Успехов из 1000 для сложности 10: [count10]\n
    Успехов из 1000 для сложности 15: [count15]\n
    Успехов из 1000 для сложности 20: [count20]\n
    Успехов из 1000 для сложности 25: [count25]\n
    Успехов из 1000 для сложности 30: [count30]\n'
    $ move(curloc)
               
screen levelUp:
    zorder 2
    modal True
    add 'images/bg.png'
    frame xalign 0.5 yalign 0.5:
        hbox:
            add getOutfitDisplay()
            vbox spacing 4 xminimum 300 xmaximum 300:
                text ('Характеристики ([statInc]):')
                text ('Сила: ' + str(player.stats.str))
                text ('Ловкость:' + str(player.stats.dex))
                text ('Выносливость:' + str(player.stats.con))
                text ('Интеллект:' + str(player.stats.int))
                text ('Мудрость:' + str(player.stats.wis))
                text ('Обаяние:' + str(player.stats.cha))
                null height 50
                text ('Умения:')
                for x in player.skills:
                    text (x.name)
            null width 20
            vbox ypos 30:
                textbutton '+':
                        action [SensitiveIf(statInc > 0), SetVariable('statInc', statInc - 1), Function(player.incSTR, 1), Show('levelUp')]
                textbutton '+':
                        action [SensitiveIf(statInc > 0), SetVariable('statInc', statInc - 1), Function(player.incDEX, 1), Show('levelUp')]
                textbutton '+':
                        action [SensitiveIf(statInc > 0), SetVariable('statInc', statInc - 1), Function(player.incCON, 1), Show('levelUp')]
                textbutton '+':
                        action [SensitiveIf(statInc > 0), SetVariable('statInc', statInc - 1), Function(player.incINT, 1), Show('levelUp')]
                textbutton '+':
                        action [SensitiveIf(statInc > 0), SetVariable('statInc', statInc - 1), Function(player.incWIS, 1), Show('levelUp')]
                textbutton '+':
                        action [SensitiveIf(statInc > 0), SetVariable('statInc', statInc - 1), Function(player.incCHA, 1), Show('levelUp')]
            null width 20
            vbox xminimum 300 xmaximum 300:
                text ('Новое умение ([skillInc]):')
                for x in allSkills:
                    if 'player' in x.type and x.id not in player.getAllSkills('id'):
                        textbutton x.name:
                            hovered Show('showDescrition', None, x.description)
                            unhovered Hide('showDescrition')
                            action [SensitiveIf(skillInc > 0), SetVariable('skillInc', skillInc - 1), Function(player.addSkill, x.id), Show('levelUp')]
                            
            textbutton 'X':
                action [SensitiveIf(skillInc <= 0 and statInc <= 0), Function(player.incLevel), Function(player.recountMaxHP),Function(player.setHP, 1000), Function(move, curloc)]
        
screen showDescrition(textToDisplay):
    zorder 3
    frame xalign 0.5 yalign 0.6 xmaximum 400:
        text(textToDisplay)
    

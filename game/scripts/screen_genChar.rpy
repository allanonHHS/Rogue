label generatePlayer:
    python:
        quest_fields = []
        city_entry = []
        quest_elsa = []
        quest_frank = []
        
        trigger = []
        for x in range(0,1000):
            trigger.append(0)
            
        trigger[5] = -500
        trigger[9] = -500
        
        
        
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
        player.setEnergy(player.getMaxEnergy())
        genEffect()
        genItems()
        genClothes()
        genSkills()
        generatedLocs = []
        allLocs = genLocs()
        player.addItem('womanClothes')
        player.addItem('nothing')
        for x in range(0,5):
            player.addItem('hairpin')
        player.wearFunc(player.getItem('womanClothes'))
        
       
        if development == 1:
            player.addItem('cheatTool')
            # genHouse(getLocation('severPrigorod'), special = ['gen_bedroom','vexel'])
        genHouse(getLocation('tailor'), type = 'store', addtionalType = 'existStore', special = ['gen_storeroom','manClothes'])
        
        
        frank = Char.random('male', 'images/picto/frank_picto.png')
        frank.autoLevel(rand(5,10))
        frank.fname = 'Фрэнк'
        frank.lname = 'Трактирщик'
        frank.name = frank.fname + ' ' + frank.lname
        frank.say = Character (frank.fullName(), kind=adv, dynamic = False, color = frank.color, show_side_image = Image(frank.picto, xalign=0.01, yalign=0.99), window_left_padding = 170)
        frank.togglePerception()
        frank.addSkill('perception')
        frank.addSkill('insight')
        frank.do = 'speakFrank'
        
        
        elsa = Char.random('female', 'images/picto/elsa_picto.png')
        elsa.autoLevel(rand(1,3))
        elsa.fname = 'Эльза'
        elsa.lname = 'Служанка'
        elsa.name = elsa.fname + ' ' + elsa.lname
        elsa.say = Character (elsa.fullName(), kind=adv, dynamic = False, color = elsa.color, show_side_image = Image(elsa.picto, xalign=0.01, yalign=0.99), window_left_padding = 170)
        elsa.do = 'speakElsa'
        
        frank_helper = Char.random('male', 'images/picto/frank_helper_picto.png')
        frank_helper.autoLevel(rand(1,3))
        frank_helper.fname = 'Карл'
        frank_helper.lname = 'Помощник'
        frank_helper.name = frank_helper.fname + ' ' + frank_helper.lname
        frank_helper.say = Character (frank_helper.fullName(), kind=adv, dynamic = False, color = frank_helper.color, show_side_image = Image(frank_helper.picto, xalign=0.01, yalign=0.99), window_left_padding = 170)
        frank_helper.do = 'speakKarl'
        
        michael = Char.random('male', 'images/noimage.gif')
        michael.autoLevel(rand(5,10))
        michael.fname = 'Майкл'
        michael.lname = 'Зеленщик'
        michael.name = michael.fname + ' ' + michael.lname
        michael.say = Character (michael.fullName(), kind=adv, dynamic = False, color = michael.color, show_side_image = Image(michael.picto, xalign=0.01, yalign=0.99), window_left_padding = 170)
        michael.togglePerception()
        michael.addSkill('perception')
        michael.addSkill('insight')
        michael.addItem('bigMoneyBag')
        # michael.do = 'speakmichael'
        
        michael_wife = Char.random('female', 'images/noimage.gif')
        michael_wife.autoLevel(rand(5,10))
        michael_wife.fname = 'Жена'
        michael_wife.lname = 'Майкла'
        michael_wife.name = michael_wife.fname + ' ' + michael_wife.lname
        michael_wife.say = Character (michael_wife.fullName(), kind=adv, dynamic = False, color = michael_wife.color, show_side_image = Image(michael_wife.picto, xalign=0.01, yalign=0.99), window_left_padding = 170)
        michael_wife.togglePerception()
        michael_wife.addSkill('perception')
        michael_wife.addSkill('insight')
        # michael_wife.do = 'speakmichael_wife'
        
        dick = Char.random('male', 'images/picto/michael_helper_picto.png')
        dick.autoLevel(rand(1,2))
        dick.fname = 'Дик'
        dick.lname = 'Помощник'
        dick.name = dick.fname + ' ' + dick.lname
        dick.say = Character (dick.fullName(), kind=adv, dynamic = False, color = dick.color, show_side_image = Image(dick.picto, xalign=0.01, yalign=0.99), window_left_padding = 170)
        dick.togglePerception()
        dick.do = 'speakdick'
        
        
        
        move('severPrigorod')
    # jump intro
        
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
                action [SensitiveIf(skillInc <= 0 and statInc <= 0), Function(move, curloc)]
        
screen showDescrition(textToDisplay):
    zorder 3
    frame xalign 0.5 yalign 0.6 xmaximum 400:
        text(textToDisplay)
    

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
            skills = []
        )
        
        player.setHP(8 + player.getCONmod())
        player.setEnergy(500 + player.getCONmod()*100 + player.getSTRmod()*100)
        player.togglePerception()
        genEffect()
        genItems()
        genClothes()
        genSkills()
        player.addItem('womanClothes')
        player.addItem('thiefArmor')
        # player.wearFunc(getClothById('womanClothes'))
        
        if development == 1:
            for x in range(0,5):
                player.addItem('lockpick')
                player.addItem('instrument')
        # testChar.autoLevel(rand(1,20))
        move(home)
    jump intro
        
label test:
    python:
        player.addSkill('acrobatics')
        # player.stats.level = 20
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
            if isSuccess(player.useSkill('breaking'), 5):
                count5 += 1
            if isSuccess(player.useSkill('breaking'), 10):
                count10 += 1
            if isSuccess(player.useSkill('breaking'), 15):
                count15 += 1
            if isSuccess(player.useSkill('breaking'), 20):
                count20 += 1
            if isSuccess(player.useSkill('breaking'), 25):
                count25 += 1
            if isSuccess(player.useSkill('breaking'), 30):
                count30 += 1
                
    ' Успехов из 100 для сложности 5: [count5]\n
    Успехов из 100 для сложности 10: [count10]\n
    Успехов из 100 для сложности 15: [count15]\n
    Успехов из 100 для сложности 20: [count20]\n
    Успехов из 100 для сложности 25: [count25]\n
    Успехов из 100 для сложности 30: [count30]\n'
    $ move(curloc)
        
        


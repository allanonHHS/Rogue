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
            energy = 0
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
            picto = 'images/noimage.gif',
            location = curloc,
            money = 100,
            skills = []
        )
        
        player.setHP(10 + player.getCONmod())
        player.setEnergy(500 + player.getCONmod()*100 + player.getSTRmod()*100)
        player.togglePerception()
        move(home)
        


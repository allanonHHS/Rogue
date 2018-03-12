 # show eileen happy at Position(xpos = 0.5, xanchor=0.5, ypos=0.5, yanchor=0.5)


init:
    define me = Character("Разработчик", who_color="#79AEE8")
    define father = Character("Отец", who_color="#79AEE8")
    define mother = Character("Мать", who_color="#79AEE8")
    define kupec = Character("Купец", who_color="#79AEE8")
    define guard = Character("Стражник", who_color="#79AEE8")
    define captain = Character("Капитан", who_color="#79AEE8")
    define inquisitor = Character("Инквизитор", who_color="#B70300")
    
    image black = '#000000'
    
    python:
        development = 1
        curloc = '' # Курлок просто должна быть объявлена
        allDoors = []
        allLocks = []
        allTraps = []
        allItems = []
        allSkills = []
        allEffects = []
        diceTrowsArr = ['Броски']
        diceText = ''
        prevloc = ''
        outside = ''
        crutchLock = ''
        crutchDoor = ''
        crutchTrap = ''
        selectedChar = ''
        playerOutfit = ''
        intro = 0
        statInc = 0
        skillInc = 0
        showDiceThrows = 1
        level = []
        for x in range(0, 40):
            level.append(10000000)
        level[1] = 0
        level[2] = 300
        level[3] = 900
        level[4] = 2700
        level[5] = 6500
        level[6] = 14000
        level[7] = 23000
        level[8] = 34000
        level[9] = 48000
        level[10] = 64000
        level[11] = 85000
        level[12] = 100000
        level[13] = 120000
        level[14] = 140000
        level[15] = 165000
        level[16] = 195000
        level[17] = 225000
        level[18] = 265000
        level[19] = 305000
        level[20] = 355000
        level[21] = 405000
        
        currChar = ''
        
# Игра начинается здесь.
label start:
    jump generatePlayer
    # $ move(home)
    return

label after_load:
    python:
        genItems()
        genSkills()
        genEffect()
        diceTrowsArr = []
        newLocs = genLocs()
        for x in newLocs:
            for y in allLocs:
                if x.id == y.id:
                    x.people = y.people
                    x.items = y.items
                    x.doors = y.doors
                    y = x
                    if x.id == curloc.id:
                        curloc = x
        
        for x in player.skills:
            for y in allSkills:
                if x.id == y.id:
                    player.skills.remove(x)
                    player.skills.append(y)
                    
# Вы можете расположить сценарий своей игры в этом файле.

# Объявляйте изображения здесь, используя оператор image.
# Например, image eileen happy = "eileen_happy.png"

# Определение персонажей игры.
init:
    define me = Character("Разработчик", who_color="#79AEE8")
    image black = '#000000'
    
    python:
        development = 1
        curloc = '' # Курлок просто должна быть объявлена
        allDoors = []
        allLocks = []
        allTraps = []
        allItems = []
        allSkills = []
        diceTrowsArr = ['Броски']
        diceText = ''
        prevloc = ''
        crutchLock = ''
        crutchDoor = ''
        crutchTrap = ''
        selectedChar = ''
# Игра начинается здесь.
label start:
    $ curloc = home
    jump generatePlayer
    # $ move(home)
    return

label after_load:
    python:
        genSkills()
        for x in player.skills:
            for y in allSkills:
                if x.id == y.id:
                    player.skills.remove(x)
                    player.skills.append(y)
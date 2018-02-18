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
        prevloc = ''
# Игра начинается здесь.
label start:
    $ curloc = home
    jump generatePlayer
    # $ move(home)
    return

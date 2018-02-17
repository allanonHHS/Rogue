init 10 python:
    class Location:
        def __init__(self, id, name, description, image, type):
            self.id = id # Для удобства определения, что за локация. Мало ли. пригодится.
            self.name = name # Отображаемое имя
            self.description = description # Массив описаний.
            self.image = image # Картиинка для показа
            self.items = [] # Массив предметов в локации
            self.events = [] # Массив возможных эвентов в локации
            self.type = type # Тип локации
            self.people = [] # Массив людей в локации
            self.navigation = [] # Массив локаций, в которые можно перейти
        
        # Функция добавления возможной локации для перехода.
        def addNav(self, locObj):
            if locObj not in self.navigation:
                self.navigation.append(locObj)
# Генерация локаций
    home = Location(
        id = 'home',
        name = 'Мой дом',
        description = ['Мой дом.', 'Выглядит весьма бедно, но ведь я ещё и не начала!'],
        type = 'private',
        image = 'images/locations/home.png')
        
    chest = Location(
        id = 'chest',
        name = 'Мой сундук',
        description = ['Обычный сундук', 'Я храню в нём награбленное и свои личные вещи'],
        type = 'private',
        image = 'images/locations/chest.png')

# Проставление навигаций
    home.addNav(chest) # Из дома мы можем переместится в сундук
    chest.addNav(home) # Из сундука в дом

# Скрин, показывающй все локации
screen location(locObj):
    add locObj.image # Отображам картинку
    
    frame xpos 0.01 ypos 0.01: # Слева отображаем имя локации
        text(locObj.name) 
    
    frame xpos 0.01 ypos 0.9: # Внизу перебираем массив описаний и выводим строчку за строчкой
        has vbox
        for x in locObj.description:
            text(x)
            
    fixed xpos 0.9: # Перебираем массив локаций для перемещения, и делаем кнопки для каждой
        vbox:
            for x in locObj.navigation:
                textbutton x.name action [Function(move, x)]
                
# Костыль, с помощью которого вызываем скрин локаций
label location_label:
    call screen location(curloc)
    
                
            
            
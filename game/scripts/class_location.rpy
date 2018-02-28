init 10 python:
    class Location:
        def __init__(self, id, name, description, image, type):
            self.id = id # Для удобства определения, что за локация. Мало ли. пригодится.
            self.name = name # Отображаемое имя
            self.description = description # Массив описаний.
            self.image = image # Картиинка для показа
            self.items = [] # Массив предметов в локации
            self.doors = [] # Массив дверей в локации
            self.dos = [] # Массив возможных эвентов в локации
            self.type = type # Тип локации
            self.people = [] # Массив людей в локации
            self.navigation = [] # Массив локаций, в которые можно перейти
        
        # Функция добавления возможной локации для перехода.
        def addNav(self, locObj):
            if locObj not in self.navigation:
                self.navigation.append(locObj)
                
        def addDoor(self, type, locObj):
            tempArr = []
            doorFound = 0
            for door in self.doors:
                if door.navigation == locObj:
                    return False
                    
            for door in allDoors:
                if door.type == type:
                    tempArr.append(door)
            tempDoor = copy.copy(choice(tempArr))
            tempDoor.location = self
            tempDoor.addNav(locObj)
            self.doors.append(tempDoor)
            
            # Создаём дубликат двери на локации, куда ведёт наша дверь.
            for door in locObj.doors:
                if door.navigation == self:
                    doorFound = 1
                    door = copy.copy(tempDoor)
                    door.addNav(self)
                    door.location = locObj
                    
            # Если двери нет, создаём такую же дверь с той стороны        
            if doorFound == 0:
                anotherDoor = copy.copy(tempDoor)
                anotherDoor.addNav(self)
                anotherDoor.location = locObj
                locObj.doors.append(anotherDoor)
                
        def addItem(self, item):
            self.items.append(item)

            
    def genLocs():
# Генерация локаций
        allLocs = []
        home = Location(
            id = 'home',
            name = 'Мой дом',
            description = ['Мой дом.', 'Выглядит весьма бедно, но ведь я ещё и не начала!'],
            type = ['private'],
            image = 'images/locations/home.png')
        allLocs.append(home)
            
        chest = Location(
            id = 'chest',
            name = 'Мой сундук',
            description = ['Обычный сундук', 'Я храню в нём награбленное и свои личные вещи'],
            type = ['private','storing'],
            image = 'images/locations/chest.png')
        allLocs.append(chest)
        
        street = Location(
            id = 'street',
            name = 'Улица',
            description = ['Улица, как улица', 'Никого особо не видно.'],
            type = ['public'],
            image = 'images/locations/street.png')
        allLocs.append(street)
        
        # Проставление прямых навигаций
        home.addNav(chest) # Из дома мы можем переместится в сундук
        chest.addNav(home) # Из сундука в дом

        # Проставление дверей:
        street.addDoor('simpleDoor', home)
        # home.addDoor('simpleDoor', street)
    
        return allLocs
                
            
            
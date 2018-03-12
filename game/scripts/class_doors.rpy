init 9 python:
    import copy
    class Door:
        def __init__(self, id, name, description, image, container, durability = 100, type = 'simpleDoor',state = 'open', difficulty = 0, hidden = False, safe = False):
            self.id = id 
            self.name = name
            self.description = description
            self.image = image
            self.durability = durability
            self.difficulty = difficulty
            self.container = container
            self.navigation = ''
            self.location = ''
            self.type = type
            self.hidden = hidden
            self.state = state
            self.safe = safe
        
        def addNav(self, locObj):
            self.navigation = locObj
            
        def getLoc(self):
            return self.navigation
            
        def getLocName(self):
            return self.navigation.name
            
        def addLock(self, type):
            tempArr = []
            for x in allLocks:
                if x.type == type:
                    tempArr.append(x)
            self.container.append(copy.copy(choice(tempArr)))
            
        def addExactLock(self, lock):
            self.container.append(lock)
            
        def getLocks(self):
            tempArr = []
            for x in self.container:
                if isinstance(x, Lock):
                    if x.state == 'closed':
                        tempArr.append(x)
            return tempArr
            
        def addTrap(self, type):
            tempArr = []
            for x in allTraps:
                if x.type == type:
                    tempArr.append(x)
            self.container.append(copy.copy(choice(tempArr)))
            
        def getTraps(self):
            tempArr = []
            for x in self.container:
                if isinstance(x, Trap):
                    if x.state == 'armed':
                        tempArr.append(x)
            return tempArr
            
        def setSafe(self):
            self.safe = True
            for door in self.navigation.doors:
                if door.navigation == self.location:
                    door.safe = True
                    
        def checkTrap(self, char):
            for item in self.container:
                if isinstance(item, Trap):
                    if item.difficulty < char.getPerception():
                        item.found = True
                        
        def lock(self, locking = True):
            for x in self.container:
                if isinstance(x, Lock):
                    if locking:
                        x.state = 'closed'
                    else:
                        x.state = 'open'
            if locking:
                self.safe = False
            else:
                self.safe = True
                
            for door in self.navigation.doors:
                if door.navigation == self.location:
                    if locking:
                        door.safe = False
                    else:
                        door.safe = True
        
        def genLock(self, level):
            tempArr = []
            for x in allLocks:
                if x.type == level:
                    tempArr.append(x)
            tempLock = copy.copy(choice(tempArr))
            tempLock.setDifficulty(froms = int(tempLock.difficulty/2), to = tempLock.difficulty)
            self.container.append(tempLock)

    woodDoor = Door(
        id = 'woodDoor',
        type = 'simpleDoor',
        name = 'Деревянная дверь',
        description = ['Обычная деревянная дверь'],
        image = 'images/noimage.gif',
        container = []
        )
    woodDoor.addLock('simpleLock')
    allDoors.append(woodDoor)
    
    anotherDoor = Door(
        id = 'anotherDoor',
        type = 'simpleDoor',
        name = 'Другая дверь',
        description = ['Необычная деревянная дверь'],
        image = 'images/noimage.gif',
        container = []
        )
    anotherDoor.addLock('simpleLock')
    allDoors.append(anotherDoor)
    
    tavernDoor1 = Door(
        id = 'tavernDoor1',
        type = 'tavernDoor',
        name = 'Деревянная дверь',
        description = ['Обычная деревянная дверь'],
        image = 'images/noimage.gif',
        container = []
        )
    tavernDoor1.addLock('hardLock')
    allDoors.append(tavernDoor1)
    
    elsaDoor = Door(
        id = 'elsaDoor',
        type = 'elsaDoor',
        name = 'Деревянная дверь',
        description = ['Обычная деревянная дверь'],
        image = 'images/noimage.gif',
        container = []
        )
    elsaDoor.addLock('hardLock')
    allDoors.append(elsaDoor)
    
    storeDoor1 = Door(
        id = 'storeDoor1',
        type = 'storeDoor',
        name = 'Деревянная дверь',
        description = ['Обычная деревянная дверь'],
        image = 'images/noimage.gif',
        container = []
        )
    storeDoor1.addLock('lock15')
    allDoors.append(storeDoor1)
    
    woodDoor1 = Door(
        id = 'woodDoor1',
        type = 'level1',
        name = 'Деревянная дверь',
        description = ['Обычная деревянная дверь'],
        image = 'images/noimage.gif',
        container = []
        )
    allDoors.append(woodDoor1)
    
    woodDoor2 = Door(
        id = 'woodDoor2',
        type = 'level1',
        name = 'Потёртая деревянная дверь',
        description = ['Обычная деревянная дверь'],
        image = 'images/noimage.gif',
        container = []
        )
    allDoors.append(woodDoor2)
    
    woodDoor3 = Door(
        id = 'woodDoor3',
        type = 'level1',
        name = 'Покосившаяся деревянная дверь',
        description = ['Обычная деревянная дверь'],
        image = 'images/noimage.gif',
        container = []
        )
    allDoors.append(woodDoor3)
    
    woodDoor4 = Door(
        id = 'woodDoor4',
        type = 'level1',
        name = 'Обычная деревянная дверь',
        description = ['Обычная деревянная дверь'],
        image = 'images/noimage.gif',
        container = []
        )
    allDoors.append(woodDoor4)
    
    def getDoor(type):
        tempArr = []
        for door in allDoors:
            if type == door.type:
                tempArr.append(door)
        return choice(tempArr)
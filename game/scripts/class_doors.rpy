init 9 python:
    import copy
    class Door:
        def __init__(self, id, name, description, image, durability = 100, type = 'simpleDoor',state = 'open', difficulty = 0, hidden = False):
            self.id = id 
            self.name = name
            self.description = description
            self.image = image
            self.durability = durability
            self.difficulty = difficulty
            self.container = []
            self.navigation = ''
            self.type = type
            self.hidden = hidden
            self.state = state
        
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
                    tempArr.append(x)
            return tempArr
                    
            
    
    woodDoor = Door(
        id = 'woodDoor',
        type = 'simpleDoor',
        name = 'Деревянная дверь',
        description = ['Обычная деревянная дверь'],
        image = 'images/noimage.gif',
        )
    woodDoor.addLock('simpleLock')
    woodDoor.addLock('simpleLock')
    woodDoor.addTrap('simpleTrap')
    allDoors.append(woodDoor)
    
    anotherDoor = Door(
        id = 'anotherDoor',
        type = 'simpleDoor',
        name = 'Другая дверь',
        description = ['Необычная деревянная дверь'],
        image = 'images/noimage.gif',
        )
    anotherDoor.addLock('simpleLock')
    anotherDoor.addTrap('simpleTrap')
    anotherDoor.addTrap('simpleTrap')
    allDoors.append(anotherDoor)
        
            
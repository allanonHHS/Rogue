init 9 python:
    import copy
    class Door:
        def __init__(self, id, name, description, image, durability = 100, type = 'simpleDoor',state = 'open', difficulty = 0, hidden = False, safe = False):
            self.id = id 
            self.name = name
            self.description = description
            self.image = image
            self.durability = durability
            self.difficulty = difficulty
            self.container = []
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

                    
            
    
    woodDoor = Door(
        id = 'woodDoor',
        type = 'simpleDoor',
        name = 'Деревянная дверь',
        description = ['Обычная деревянная дверь'],
        image = 'images/noimage.gif',
        )
    woodDoor.addLock('simpleLock')
    woodDoor.addTrap('simpleTrap')
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
    anotherDoor.addLock('simpleLock')
    anotherDoor.addTrap('simpleTrap')
    anotherDoor.addTrap('simpleTrap')
    anotherDoor.addTrap('simpleTrap')
    allDoors.append(anotherDoor)
        
            
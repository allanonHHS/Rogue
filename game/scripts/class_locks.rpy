init 8 python:
    import copy
    class Lock:
        def __init__(self, id, name, description, image, durability = 10, difficulty = 1, type = 'simpleLock',state = 'closed', do = '', rescue = 'dex'):
            self.id = id 
            self.name = name
            self.description = description
            self.image = image
            self.durability = durability
            self.difficulty = difficulty
            self.type = type
            self.state = state
            self.rescue = rescue
            self.do = do
        
        def unlock(self):
            self.state = 'open'
            
        def lock(self):
            self.state = 'closed'
            
        def setDifficulty(self,to, froms = 1):
            self.difficulty = rand(froms, to)
            
            
    simpleLock = Lock(
        id = 'simpleLock',
        name = 'Простой замок',
        description = 'Обычный простой замок',
        image = 'images/noimage.gif',
        type = 'simpleLock',
        difficulty = 5
        )
    allLocks.append(simpleLock)
    
    level1lock1 = Lock(
        id = 'level1lock1',
        name = 'Простой замок',
        description = 'Обычный простой замок',
        image = 'images/noimage.gif',
        type = 'level1',
        difficulty = 5
        )
    allLocks.append(level1lock1)
    
    level1lock2 = Lock(
        id = 'level1lock2',
        name = 'Ржавый замок',
        description = 'Заржавевший и тугой замок.',
        image = 'images/noimage.gif',
        type = 'level1',
        difficulty = 5
        )
    allLocks.append(level1lock2)
    
    level1lock3 = Lock(
        id = 'level1lock3',
        name = 'Поцарапанный замок',
        description = 'Поцарапанный и потрёпанный от времени замок.',
        image = 'images/noimage.gif',
        type = 'level1',
        difficulty = 5
        )
    allLocks.append(level1lock3)
    
    lock20 = Lock(
        id = 'lock20',
        name = 'Сложный замок',
        description = 'Довольно сложный замок',
        image = 'images/noimage.gif',
        type = 'hardLock',
        difficulty = 20
        )
    allLocks.append(lock20)
    
    lock15 = Lock(
        id = 'lock15',
        name = 'Прочный замок',
        description = 'Прочный замок',
        image = 'images/noimage.gif',
        type = 'lock15',
        difficulty = 15
        )
    allLocks.append(lock15)
    
    def getLock(type):
        tempArr = []
        for lock in allLocks:
            if type == lock.type:
                tempArr.append(lock)
        return choice(tempArr)
    
    
    class Trap:
        def __init__(self, id, name, description, image, do = '', durability = 10, difficulty = 1, type = 'simpleTrap', state = 'armed', found = False, rescue = 'dex' ):
            self.id = id 
            self.name = name
            self.description = description
            self.image = image
            self.durability = durability
            self.difficulty = difficulty
            self.type = type
            self.state = state
            self.found = found
            self.do = do
            self.rescue = rescue
            
        def disarm(self):
            self.state = 'disarmed'
            
        def arm(self):
            self.state = 'armed'
            
        def find(self):
            self.found = True
            
    simpleTrap = Trap(
        id = 'simpleTrap',
        name = 'Простая ловушка',
        description = 'Обычная ловушка с иглой',
        image = 'images/noimage.gif',
        type = 'simpleTrap',
        difficulty = 15,
        do = 'trap_simpleTrap'
        )
    allTraps.append(simpleTrap)
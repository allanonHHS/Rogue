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
            
    simpleLock = Lock(
        id = 'simpleLock',
        name = 'Простой замок',
        description = 'Обычный простой замок',
        image = 'images/noimage.gif',
        type = 'simpleLock',
        difficulty = 15
        )
    allLocks.append(simpleLock)
            
    
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
init 8 python:
    import copy
    class Lock:
        def __init__(self, id, name, description, image, durability = 10, difficulty = 1, type = 'simpleLock',state = 'closed', event = ''):
            self.id = id 
            self.name = name
            self.description = description
            self.image = image
            self.durability = durability
            self.difficulty = difficulty
            self.type = type
            self.state = state
            self.event = ''
        
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
        def __init__(self, id, name, description, image, event = '', durability = 10, difficulty = 1, type = 'simpleTrap', state = 'armed', found = False):
            self.id = id 
            self.name = name
            self.description = description
            self.image = image
            self.durability = durability
            self.difficulty = difficulty
            self.type = type
            self.state = state
            self.found = found
            self.event = event
            
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
        event = 'trap_simpleTrap'
        )
    allTraps.append(simpleTrap)
init -21 python:
    import copy, codecs, sys, time
    from random import choice
    from random import randint
    from operator import itemgetter, attrgetter, methodcaller
    
    def dice(char):
        temp = randint(1, 20)
        if temp == 20:
            return 100
            
        if temp == 1:
            return - 100
            
        return randint(1, 20)
        
    def rand(a,b):
        if a == b:
            return a
        elif a < b:
            return 0
        return randint(a, b)
        
    def checkTraps(door):
        for x in door.container:
            if isinstance(x, Trap):
                if x.state == 'armed' and x.found == False:
                    if x.difficulty <= player.getPerception():
                        x.found = True
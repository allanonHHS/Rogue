init -21 python:
    import copy, codecs, sys, time
    import random
    from random import choice
    from random import randint
    from operator import itemgetter, attrgetter, methodcaller
    
    def dice(char):
        if char == player:
            temp = max(randint(1, 20), randint(1, 20))
        else:
            temp = randint(1, 20)
            
        if temp == 20:
            return 100
            
        if temp == 1:
            return - 100
            
        return randint(1, 20)
        
    def rand(a, b):
        if a - b >= 0 or b == 0:
            return a
        else :
            return random.randint(a,b)
        
    def randf(a, b):
        return random.uniform(a,b)
        
    def checkTraps(door):
        for x in door.container:
            if isinstance(x, Trap):
                if x.state == 'armed' and x.found == False:
                    if x.difficulty <= player.getPerception():
                        x.found = True
init -21 python:
    import copy, codecs, sys, time
    import random
    from random import choice
    from random import randint
    from operator import itemgetter, attrgetter, methodcaller
    
    def dice(char):
        if char == player:
            temp = randint(1, 20)
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
                        
    def isSuccess(what,where,*args):
        if len(args) > 0:
            desc = args[0]
        else:
            desc = ''
        if isinstance(what, list) and isinstance(where, list):
            if what[0] >= where[0]:
                diceTrowsArr.append(desc + what[1] +' Против ' + where[1] + ' = Успех!')
                # renpy.show_screen('paramShow')
                return True
            else:
                diceTrowsArr.append(desc + what[1] +' Против ' + where[1] + ' = Провал...')
                # renpy.show_screen('paramShow')
                return False
        if isinstance(what, list) and isinstance(where, int):
            if what[0] >= where:
                diceTrowsArr.append(desc + what[1] +' Против ' + str(where) + ' = Успех!')
                # renpy.show_screen('paramShow')
                return True
            else:
                diceTrowsArr.append(desc + what[1] +' Против ' + str(where) + ' = Провал...')
                # renpy.show_screen('paramShow')
                return False
        return False
init -21 python:
    import copy, codecs, sys, time
    import random
    from random import choice
    from random import randint
    from operator import itemgetter, attrgetter, methodcaller
    
    def dice(char):
        if char.hasSkill('luck'):
            temp = max(randint(1, 20), randint(1, 20))
        else:
            temp = randint(1, 20)
            
        if temp == 20:
            return 100
            
        if temp == 1:
            return - 100
            
        return temp
        
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
                        
    def isSuccess(what, where, desc = '', hidden = False, exp = 0):
        experience = ''
        if exp > 0:
            experience = 'EXP - ' + str(exp) + ' '
        if isinstance(what, list) and isinstance(where, list):
            if what[0] >= where[0]:
                if hidden == False:
                    diceTrowsArr.append(experience + desc + what[1] +' Против ' + where[1] + ' = Успех!')
                player.incExp(exp)
                return True
            else:
                if hidden == False:
                    diceTrowsArr.append(desc + what[1] +' Против ' + where[1] + ' = Провал...')
                return False
        if isinstance(what, list) and isinstance(where, int):
            if what[0] >= where:
                if hidden == False:
                    diceTrowsArr.append(experience + desc + what[1] +' Против ' + str(where) + ' = Успех!')
                player.incExp(exp)
                return True
            else:
                if hidden == False:
                    diceTrowsArr.append(desc + what[1] +' Против ' + str(where) + ' = Провал...')
                return False
        return False
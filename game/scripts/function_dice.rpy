init -21 python:
    import copy, codecs, sys, time
    from random import choice
    from random import randint
    from operator import itemgetter, attrgetter, methodcaller
    
    def dice(char):
        return randint(1, 20)
        
    def rand(a,b):
        if a == b:
            return a
        if a < b:
            return 0
        return randint(a, b)
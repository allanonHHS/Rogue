init -20 python:
    import copy, codecs, sys, time
    from random import choice
    from operator import itemgetter, attrgetter, methodcaller

    reload(sys)  
    sys.setdefaultencoding('utf8')
    
    ###################################################################
    # Класс частей тела
    ###################################################################

    class BodyPart():
        def __init__(self, name, visibility = False, sperm = False, size = 0, maxSize = 0, minSize = 0):
            self.name = name
            self.visibility = visibility
            self.sperm = sperm
            self.size = size
            self.minSize = minSize
            self.maxSize = maxSize

        def normalize(self):
            self.size = max(self.minSize, min(self.size, self.maxSize))

    # Общий класс тела с частями, общими для всех
    class Body(object):
        def __init__(self, height = 140, bodyparts = None):
            self.parts = {}
            self.parts['ноги'] = BodyPart('ноги', True)
            self.parts['лицо'] = BodyPart('лицо', True)
            self.parts['грудь'] = BodyPart('грудь', True, minSize = 0, maxSize = 10)
            self.parts['анус'] = BodyPart('анус', minSize = 0, maxSize = 10)
            self.parts['рот'] = BodyPart('рот')
            self.parts['руки'] = BodyPart('руки', True)
            self.height = height

            # Копируем и перезаписываем части тела, если надо
            if bodyparts:
                self.parts.update(bodyparts)

        @classmethod
        def random(cls):
            body = cls(height = rand(140, 170))
            body.parts['анус'].size = randf(0, 1)
            return body

        def normalize(self):
            for _,v in self.parts.iteritems():
                v.normalize()

        def sex(self):
            return 'U wot m8'

        def partsWithSperm(self):
            return [v for k,v in self.parts.iteritems() if v.sperm]


    # Мужское тело
    class MaleBody(Body):
        def __init__(self, height, bodyparts = None, anusSize = 0, penisSize = 0):
            super(MaleBody, self).__init__(height, bodyparts)
            self.parts['пенис'] = BodyPart('пенис', minSize = 0, maxSize = 30, size = penisSize) #
            self.parts['анус'].size = anusSize

        @classmethod
        def random(cls):
            body = super(MaleBody, cls).random()
            body.parts['пенис'].size = randf(10, 15)
            return body

        def sex(self):
            return 'male'

    # Женское тело
    class FemaleBody(Body):
        def __init__(self, height, bodyparts = None, anusSize = 0, vaginaSize = 0, breastSize = 0):
            super(FemaleBody, self).__init__(height, bodyparts)
            self.parts['вагина'] = BodyPart('вагина', minSize = 0, maxSize = 10, size = vaginaSize)
            self.parts['анус'].size = anusSize
            self.parts['грудь'].size = breastSize

        @classmethod
        def random(cls):
            body = super(FemaleBody, cls).random()
            body.parts['вагина'].size = randf(0, 1)
            body.parts['грудь'].size = randf(0, 3)
            return body

        def sex(self):
            return 'female'

    # Фута
    class FutaBody(Body):
        def __init__(self, height, bodyparts = None, anusSize = 0, vaginaSize = 0, penisSize = 0, breastSize = 0):
            super(FutaBody, self).__init__(height, bodyparts)
            self.parts['вагина'] = BodyPart('вагина', minSize = 0, maxSize = 40, size = vaginaSize)
            self.parts['пенис'] = BodyPart('пенис', minSize = 0, maxSize = 30, size = penisSize)
            self.parts['анус'].size = anusSize
            self.parts['грудь'].size = breastSize

        @classmethod
        def random(cls):
            body = super(FutaBody, cls).random()
            body.parts['пенис'].size = randf(10, 15)
            body.parts['вагина'].size = randf(0, 1)
            body.parts['грудь'].size = randf(0, 3)
            return body

        def sex(self):
            return 'futa'

    # Параметры персонажа
    class Stats:
        def __init__(self, **stats):
            self.str = stats['str'] if 'str' in stats else 0
            self.dex = stats['dex'] if 'dex' in stats else 0
            self.con = stats['con'] if 'con' in stats else 0
            self.int = stats['int'] if 'int' in stats else 0
            self.wis = stats['wis'] if 'wis' in stats else 0
            self.cha = stats['cha'] if 'cha' in stats else 0
            self.hp = stats['hp'] if 'hp' in stats else 0
            self.energy = stats['energy'] if 'energy' in stats else 0
            self.exp = stats['exp'] if 'exp' in stats else 0

        def normalize(self):
            self.str = min(max(self.str,1),18)
            self.dex = min(max(self.dex,1),18)
            self.con = min(max(self.con,1),18)
            self.int = min(max(self.int,1),self.maxlust)
            self.wis = min(max(self.wis,1),18)
            self.cha = min(max(self.cha,1),18)
            self.hp = min(max(self.hp,0),1000)
            self.energy = min(max(self.energy,0),2000)
            self.exp = min(max(self.exp,0),1000000)
            
        @classmethod
        def random(cls):
            stats = cls()
            #TODO нормальная генерация
            self.str = rand(4,20)
            self.dex = rand(4,20)
            self.con = rand(4,20)
            self.int = rand(4,20)
            self.wis = rand(4,20)
            self.cha = rand(4,20)
            self.hp = rand(4,20)
            self.energy = 1000
            self.exp = 0
            return stats

    class Char(object):

        # Мужские имена
        maleNames = ['somemalename1','somemalename2']

        # Женские имена
        femaleNames = ['somefemalename1','somefemalename2']

        # Фамилии
        # maleLastNames = {'Крестьянин':90, 'Охотник':10, 'Лесник':10}
        # femaleLastNames = {'Крестьянка':50, 'Селянка':50, 'Охотница':5}
        maleLastNames = {'Крестьянин':100, 'Селянин':50}
        femaleLastNames = {'Крестьянка':50, 'Селянка':50}
        
        def __init__(self, fname = '', lname = '', color = '#FFFFFF', age = 0, body = None, stats = None, picto = '', location = '', wear = None, inventory = None, money = 0, skills = [], state = [], do = ''):
            if body is None:
                body = Body()
            if stats is None:
                stats = Stats()
            if wear is None:
                wear = []
            if inventory is None:
                inventory = []
            if skills is None:
                skills = []

            self.fname = fname
            self.lname = lname
            self.name = fname + ' ' + lname
            self.sex = body.sex()
            self.age = age
            self.body = body
            self.stats = stats
            self.color = color
            self.inventory = inventory
            self.wear = wear
            self.skills = skills
            self.effects = []
            self.picto = picto
            self.location = location
            self.money = money
            self.do = do
            self.state = state
            self.say = Character (self.fullName(), kind=adv, dynamic = False, color = self.color, show_side_image = Image(self.picto, xalign=0.01, yalign=0.99), window_left_padding = 170)
            self.speak = Character (self.fullName(), kind=adv, dynamic = False, color = self.color)
            config.side_image_tag = self.picto
        
        # Создание случайного персонажа с полом sex ('male', 'female' или 'futa') и картинкой picto
        @classmethod
        def random(cls, sex, picto):
            # выбор пола
            body = Body()
            if sex == 'female':
                body = FemaleBody.random()
            elif sex == 'futa':
                body = FutaBody.random()
            elif sex == 'male':
                body = MaleBody.random()

            stats = Stats.random()
            firstName = choice(cls.maleNames) if body.sex() == 'male' else choice(cls.femaleNames)
            lastName = choice(cls.lastNames)
            if body.sex() != 'male':
                lastName += 'а'

            color = '#FFFFFF'
            if body.sex() == 'female':
                color = '#FF85F1'
            elif body.sex() == 'male':
                color = '#269AFF'
            elif body.sex() == 'futa':
                color = '#FC3A3A'
            
            character = cls(firstName, lastName, color = color, age = rand(20, 60), body = body, stats = stats, picto = picto, inventory = [], wear = [])
            return character

        def normalize(self):
            self.body.normalize()
            self.stats.normalize()

        def fullName(self):
            return self.fname + ' ' + self.lname
########################################################################################
        def getSTR(self):
            return self.stats.str
            
        def getSTRmod(self):
            return int((self.getSTR() - 10)/2)
########################################################################################            
        def getDEX(self):
            return self.stats.dex
            
        def getDEXmod(self):
            return int((self.getDEX() - 10)/2)
########################################################################################
        def getCON(self):
            return self.stats.con
            
        def getCONmod(self):
            return int((self.getCON() - 10)/2)
########################################################################################
        def getINT(self):
            return self.stats.int
            
        def getINTmod(self):
            return int((self.getINT() - 10)/2)
########################################################################################
        def getWIS(self):
            return self.stats.wis
            
        def getWISmod(self):
            return int((self.getWIS() - 10)/2)
########################################################################################
        def getCHA(self):
            return self.stats.cha
            
        def getCHAmod(self):
            return int((self.getCHA() - 10)/2)
########################################################################################
        def getHP(self):
            return self.stats.hp
        
        def setHP(self,amount):
            self.stats.hp = int(amount)
            
        def incHP(self,amount):
            self.stats.hp += int(amount)
########################################################################################
        def getEnergy(self):
            return self.stats.energy
            
        def setEnergy(self,amount):
            self.stats.energy = int(amount)
            
        def incEnergy(self,amount):
            self.stats.energy += int(amount)
########################################################################################
        def getPerception(self):
            if 'alarm' in self.state:
                return dice(self) + self.getWISmod()
            else:
                return 10 + self.getWISmod()
########################################################################################
        def getSneak(self):
            if 'sneak' in self.state:
                return dice(self) + self.getDEXmod()
            else:
                return 0
########################################################################################
        def getUnlock(self):
            return dice(self) + self.getDEXmod()
########################################################################################
        def getDisarmINT(self):
            return dice(self) + self.getINTmod()
            
        def getDisarmDEX(self):
            return dice(self) + self.getDEXmod()
########################################################################################
        def getWeight(self):
            return self.getSTR()*15
            
        def checkRescue(self, item):
            if isinstance(item, Trap):
                if item.rescue == 'str':
                    if item.difficulty <  dice(self) + self.getSTRmod():
                        return True
                elif item.rescue == 'dex':
                    if item.difficulty <  dice(self) + self.getDEXmod():
                        return True
                elif item.rescue == 'con':
                    if item.difficulty <  dice(self) + self.getCONmod():
                        return True
                elif item.rescue == 'int':
                    if item.difficulty <  dice(self) + self.getINTmod():
                        return True
                elif item.rescue == 'wis':
                    if item.difficulty <  dice(self) + self.getWISmod():
                        return True
                elif item.rescue == 'cha':
                    if item.difficulty <  dice(self) + self.getCHAmod():
                        return True
            return False
            
        def toggleSneak(self):
            if 'sneak' in self.state:
                self.state.remove('sneak')
            else:
                self.state.append('sneak')
                
        def togglePerception(self):
            if 'alarm' in self.state:
                self.state.remove('alarm')
            else:
                self.state.append('alarm')
            
            
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
            self.maxHP = stats['maxHP'] if 'maxHP' in stats else 0
            self.level = stats['level'] if 'level' in stats else 0

        def normalize(self):
            self.str = min(max(self.str,8),20)
            self.dex = min(max(self.dex,8),20)
            self.con = min(max(self.con,8),20)
            self.int = min(max(self.int,8),20)
            self.wis = min(max(self.wis,8),20)
            self.cha = min(max(self.cha,8),20)
            self.hp = min(max(self.hp,0),self.maxHP)
            self.energy = min(max(self.energy,0),2000)
            self.exp = min(max(self.exp,0),1000000)
            self.maxHP = min(max(self.maxHP,0), 8 + (self.con-10)/2 + (6 + (self.con-10)/2)*(self.level - 1))
            self.level = min(max(self.maxHP,0),1000)
            
        @classmethod
        def random(cls):
            stats = cls()
            x = 0
            #TODO нормальная генерация
            stats.str = 9
            stats.dex = 9
            stats.con = 9
            stats.int = 9
            stats.wis = 9
            stats.cha = 9
            while x < 20:
                tempChoce = randint(1,6)
                if tempChoce == 1:
                    if stats.str < 14:
                        stats.str += 1
                        x += 1
                    elif stats.str < 16:
                        stats.str += 1
                        x += 2
                elif tempChoce == 2:
                    if stats.dex < 14:
                        stats.dex += 1
                        x += 1
                    elif stats.dex < 16:
                        stats.dex += 1
                        x += 2
                elif tempChoce == 3:
                    if stats.con < 14:
                        stats.con += 1
                        x += 1
                    elif stats.con < 16:
                        stats.con += 1
                        x += 2
                elif tempChoce == 4:
                    if stats.int < 14:
                        stats.int += 1
                        x += 1
                    elif stats.int < 16:
                        stats.int += 1
                        x += 2
                elif tempChoce == 5:
                    if stats.wis < 14:
                        stats.wis += 1
                        x += 1
                    elif stats.wis < 16:
                        stats.wis += 1
                        x += 2
                elif tempChoce == 6:
                    if stats.cha < 14:
                        stats.cha += 1
                        x += 1
                    elif stats.cha < 16:
                        stats.cha += 1
                        x += 2
            stats.energy = 1000
            stats.exp = 0
            stats.maxHP = 8 + (stats.con-10)/2
            stats.hp = stats.maxHP
            stats.level = 1
            return stats

    class Char(object):

        # Мужские имена
        maleNames = ['Аарон', 'Адам', 'Алан', 'Альберт', 'Алекс', 'Александр', 'Альфред', 'Эндрю', 'Энди', 'Энтони', 'Арнольд', 'Артур', 'Барри', 'Бен','Бенджамин', 'Бернард', 'Билл', 'Билли', 'Боб', 'Бобби', 'Брэд', 'Брэндон', 'Брайан', 'Брюс', 'Брайан', 'Бад', 'Кельвин', 'Карл', 'Карлос', 'Чарльз', 'Чарли', 'Крис', 'Кристиан', 'Кристофер', 'Колин', 'Конни', 'Кёртис', 'Дэйл', 'Дэн', 'Дэниел', 'Дэнни','Дэйв', 'Дэвид', 'Дэвис', 'Дин', 'Дэннис', 'Дерек', 'Дик', 'Дон', 'Дональд', 'Дуглас', 'Дюк', 'Дастин', 'Дилан', 'Эрл', 'Эдгар', 'Эдмонд', 'Эдвард', 'Эдвин', 'Элтон', 'Эмметт', 'Эрик', 'Эрнест', 'Этан', 'Феликс', 'Фердинанд', 'Флойд', 'Франсис', 'Фрэнк','Фред', 'Фредерик', 'Фуллер', 'Гарри', 'Джордж', 'Джеральд', 'Гилберт', 'Гловер', 'Гордон', 'Грэм, Грэхам', 'Грег', 'Гарольд','Харрисон', 'Гарри', 'Генри', 'Герберг', 'Говард', 'Джек', 'Джейк', 'Джеймс', 'Джей', 'Джефф', 'Джерри', 'Джим', 'Джоэл','Джон', 'Джонни', 'Джон', 'Джонатан', 'Кейн', 'Кит', 'Кен', 'Кеннет', 'Кевин', 'Курт', 'Ларри', 'Лео', 'Леонард', 'Луис', 'Линн', 'Марк', 'Мартин', 'Марвин', 'Мэттью', 'Морис', 'Макс', 'Мэл', 'Мелвин', 'Майкл', 'Майк', 'Нейтан', 'Нил', 'Нил', 'Ник', 'Норман', 'Оливер', 'Оскар', 'Остин', 'Освальд', 'Оуэн', 'Патрик', 'Пол', 'Пит', 'Питер', 'Фил', 'Филип', 'Ральф', 'Рэнди', 'Рэймонд', 'Ричард', 'Рик', 'Роб', 'Роберт', 'Роджер', 'Роланд','Рональд', 'Ронни', 'Рой', 'Сэм', 'Сэмюэл', 'Сид', 'Симон', 'Смит', 'Стивен', 'Стив', 'Тед', 'Терри', 'Теодор', 'Томас', 'Тим', 'Том', 'Тони', 'Виктор', 'Уэйн', 'Вильгельм', 'Уильям', 'Вилли', 'Уилсон']

        # Женские имена
        femaleNames = ['Амелия', 'Оливия', 'Эмили', 'Ава', 'Айла', 'Джессика', 'Поппи', 'Изабелла', 'Софи', 'Мия', 'Руби', 'Лили', 'Грейс', 'Иви', 'София', 'Элла', 'Скарлетт', 'Хлое', 'Изабель', 'Фрейя', 'Шарлотта', 'Сиенна', 'Дэйзи', 'Фиби', 'Милли', 'Ева', 'Элис', 'Люси', 'Флоренс', 'София', 'Лайла', 'Лола', 'Холли', 'Имоджен', 'Молли', 'Матильда', 'Лилли', 'Рози', 'Элизабет', 'Эрин', 'Мэйси', 'Лекси', 'Элли', 'Ханна', 'Эвелин', 'Эбигейл', 'Элси', 'Саммер', 'Меган', 'Жасмин', 'Майя', 'Амели', 'Лэйси', 'Уиллоу', 'Эмма', 'Белла', 'Элеонора', 'Эсми', 'Элиза', 'Джорджия', 'Харриет', 'Грейси', 'Аннабель', 'Эмилия', 'Эмбер', 'Айви', 'Брук', 'Роуз', 'Анна', 'Зара', 'Леа', 'Молли', 'Марта', 'Фэйт', 'Холли', 'Эми', 'Бетани', 'Вайолет', 'Кэти', 'Марьям', 'Франческа', 'Джулия', 'Мария', 'Дарси', 'Изабель', 'Тилли', 'Мэддисон', 'Виктория', 'Изобель', 'Нив', 'Скай', 'Мэдисон', 'Дарси', 'Айша', 'Беатриче', 'Сара', 'Зои', 'Пейдж', 'Хайди', 'Лидия']

        # Фамилии
        # maleLastNames = {'Крестьянин':90, 'Охотник':10, 'Лесник':10}
        # femaleLastNames = {'Крестьянка':50, 'Селянка':50, 'Охотница':5}
        maleLastNames = ['Торговец','Горожанин','Фермер', 'Алхимик', 'Нищий', 'Шут', 'Ремесленник', 'Кожевенник', 'Кузнец', 'Вор', 'Бард', 'Менестрель', 'Портной']
        femaleLastNames = ['Торговка','Горожанка','Фермер', 'Нищая', 'Ремесленница', 'Менестрель', 'Портниха', 'Шлюха']
        
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
            lastName = choice(cls.maleLastNames) if body.sex() == 'male' else choice(cls.femaleLastNames)

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
        def getMoney(self):
            return self.money
            
        def setMoney(self,amount):
            self.money = int(amount)
            
        def incMoney(self,amount):
            self.money += int(amount)
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
        def getSteal(self):
            # if development == 1:
                # return 100
            return dice(self) + self.getDEXmod()
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
########################################################################################
        def getLevel(self):
            return self.stats.level
            
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
                
        def autoLevel(self, count):
            for temp in range(0, count):
                self.stats.level += 1
                self.stats.maxHP = 8 + (self.stats.con-10)/2 + (5 + (self.stats.con-10)/2)*(self.stats.level - 1)
                self.stats.hp = self.stats.maxHP
                if self.stats.level in [4,8,10,12,16,19]:
                    x = 0
                    while x < 1:
                        tempChoce = rand(1,6)
                        if tempChoce == 1:
                            if self.stats.str >= 20:
                                x -= 1
                                self.stats.str -= 1
                            self.stats.str += 1
                        elif tempChoce == 2:
                            if self.stats.dex >= 20:
                                x -= 1
                                self.stats.dex -= 1
                            self.stats.dex += 1
                        elif tempChoce == 3:
                            if self.stats.con >= 20:
                                x -= 1
                                self.stats.con -= 1
                            self.stats.con += 1
                        elif tempChoce == 4:
                            if self.stats.int >= 20:
                                x -= 1
                                self.stats.int -= 1
                            self.stats.int += 1
                        elif tempChoce == 5:
                            if self.stats.wis >= 20:
                                x -= 1
                                self.stats.wis -= 1
                            self.stats.wis += 1
                        elif tempChoce == 6:
                            if self.stats.cha >= 20:
                                x -= 1
                                self.stats.cha -= 1
                            self.stats.cha += 1
                        x += 1
                        
##########################################################################
#ИНВЕНТАРЬ
##########################################################################
        def addItem(self,item):
            temp = copy.copy(item)
            self.inventory.append(temp)
            
        def stealItem(self, char, item):
            char.removeItem(item)
            player.addItem(item)
            item.steal()

        def removeItem(self,item):
            if type(item) is str:
                for x in self.inventory:
                    if x.name == item:
                        self.inventory.remove(x)
            else:
                if self.inventory.count(item) > 0:
                    self.inventory.remove(item)
                if self.wear.count(item) > 0:
                    self.wear.remove(item)
                for x in self.inventory:
                    if x.name == item.name:
                        self.inventory.remove(x)
            
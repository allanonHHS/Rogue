init 10 python:
    class Location:
        def __init__(self, id, name, description, image, type, doors = None, reputation = 0):
            self.id = id # Для удобства определения, что за локация. Мало ли. пригодится.
            self.name = name # Отображаемое имя
            self.description = description # Массив описаний.
            self.image = image # Картиинка для показа
            self.items = [] # Массив предметов в локации
            if doors == None:
                self.doors = [] # Массив дверей в локации
            self.dos = [] # Массив возможных эвентов в локации
            self.type = type # Тип локации
            self.people = [] # Массив людей в локации
            self.navigation = [] # Массив локаций, в которые можно перейти
            self.reputation = reputation
        
        # Функция добавления возможной локации для перехода.
        def addNav(self, locObj):
            if self != locObj and locObj not in self.navigation:
                self.navigation.append(locObj)
                if self not in locObj.navigation:
                    locObj.navigation.append(self)
                
        def addDoor(self, type, locObj):
            tempArr = []
            doorFound = 0
            for door in self.doors:
                if door.navigation == locObj:
                    return False
                    
            for door in allDoors:
                if door.type == type:
                    tempArr.append(door)
                    
            tempDoor = copy.deepcopy(choice(tempArr))
            tempDoor.location = self
            
            # tempDoor.genLock(self.getLevel())
            
            tempDoor.addNav(locObj)
            self.doors.append(tempDoor)
            
            # Создаём дубликат двери на локации, куда ведёт наша дверь.
            for door in locObj.doors:
                if door.navigation == self:
                    doorFound = 1
                    door = copy.copy(tempDoor)
                    door.addNav(self)
                    door.location = locObj
                    
            # Если двери нет, создаём такую же дверь с той стороны        
            if doorFound == 0:
                anotherDoor = copy.copy(tempDoor)
                anotherDoor.addNav(self)
                anotherDoor.location = locObj
                locObj.doors.append(anotherDoor)
                
        def genDoor(self, type, locObj, investigation):
            tempArr = []
            doorFound = 0
            for door in self.doors:
                if door.navigation == locObj:
                    return False
                    
            for door in allDoors:
                if door.type == type:
                    tempArr.append(door)
                    
            tempDoor = copy.deepcopy(choice(tempArr))
            tempDoor.location = self
            
            if rand(1,2) == 1:
                tempDoor.genLock(self.getLevel())
            
            tempDoor.addNav(locObj)
            self.doors.append(tempDoor)
            
            # Создаём дубликат двери на локации, куда ведёт наша дверь.
            for door in locObj.doors:
                if door.navigation == self:
                    doorFound = 1
                    door = copy.copy(tempDoor)
                    door.addNav(self)
                    door.location = locObj
                    
            # Если двери нет, создаём такую же дверь с той стороны        
            if doorFound == 0:
                anotherDoor = copy.copy(tempDoor)
                anotherDoor.addNav(self)
                anotherDoor.location = locObj
                locObj.doors.append(anotherDoor)
                
        def addItem(self, item):
            self.items.append(item)
            
        def getCharByName(self, name):
            for x in self.people:
                if x.lname == name:
                    return x
            return False
            
        def getDoor(self, id):
            for x in self.doors:
                if x.id == id:
                    return x
            return False
            
        def getLevel(self):
            for x in self.type:
                if 'level' in x:
                    return x
            return 'level1'
            
        def genNavigation(self, where, investigation):
            if rand(1,2) == 0:
                self.addNav(where)
            else:
                self.genDoor(self.getLevel(), where, investigation)

            
    def genLocs():
# Генерация локаций
        allLocs = []
        severPrigorod = Location(
            id = 'severPrigorod',
            name = 'Северный пригород',
            description = ['Северный пригород Ландора.', 'Представляет собой хаотичную застройку из деревянных домов, некоторые из них более напоминают сараи. Богатых домов почти что нет, если не считать редкие лавки небогатых торговцев и мастерские ремесленников.'],
            type = ['public','outside'],
            image = 'images/locations/severPrigorod.png')
        allLocs.append(severPrigorod)
        
        
        zapadPrigorod = Location(
            id = 'zapadPrigorod',
            name = 'Западный пригород',
            description = ['Западный пригород.', 'Наиболее богатый из всех пригородных районов потому как здесь собралось больше всего мастерских ремесленников, у которых не хватает денег на городские налоги. Немало и торговых лавок. Дома выглядят приличней чем в прочих пригородах, но застройка такая же хаотичная.'],
            type = ['public','outside'],
            image = 'images/locations/zapadPrigorod.png')
        allLocs.append(zapadPrigorod)
        
        ugPrigorod = Location(
            id = 'ugPrigorod',
            name = 'Южный пригород',
            description = ['Южный пригород Ландора.', 'Скопление грязных нищих домов, небогатых лавок и бесцельно бродящего люда подозрительной наружности. В сумасшедшем переплетении грязных улочек нередко теряются и местные жители, не говоря уже о редких патрулях стражи.'],
            type = ['public','outside'],
            image = 'images/locations/ugPrigorod.png')
        allLocs.append(ugPrigorod)
        
        severGate = Location(
            id = 'severGate',
            name = 'Северные ворота',
            description = ['Северные ворота Ландора.', 'todo'],
            type = ['public','outside'],
            image = 'images/locations/severGate.png')
        allLocs.append(severGate)
        
        zapadGate = Location(
            id = 'zapadGate',
            name = 'Западные ворота',
            description = ['Западные ворота Ландора.', 'todo'],
            type = ['public','outside'],
            image = 'images/locations/zapadGate.png')
        allLocs.append(zapadGate)
        
        ugGate = Location(
            id = 'ugGate',
            name = 'Южные ворота',
            description = ['Южные ворота Ландора.', 'todo'],
            type = ['public','outside'],
            image = 'images/locations/ugGate.png')
        allLocs.append(ugGate)
        
        severGate.addNav(severPrigorod)
        zapadGate.addNav(zapadPrigorod)
        ugGate.addNav(ugPrigorod)
        severPrigorod.addNav(zapadPrigorod)
        zapadPrigorod.addNav(ugPrigorod)
        
        severArea = Location(
            id = 'severArea',
            name = 'Северный район',
            description = ['Северный район.', 'todo'],
            type = ['public','outside'],
            image = 'images/locations/severGate.png')
        allLocs.append(severArea)
        
        ugArea = Location(
            id = 'ugArea',
            name = 'Южный район',
            description = ['Южный район.', 'todo'],
            type = ['public','outside'],
            image = 'images/locations/ugArea.png')
        allLocs.append(ugArea)
        
        zapadArea = Location(
            id = 'zapadArea',
            name = 'Западный район',
            description = ['Западный район.', 'todo'],
            type = ['public','outside'],
            image = 'images/locations/zapadArea.png')
        allLocs.append(zapadArea)
        
        severArea.addNav(severGate)
        zapadArea.addNav(zapadGate)
        ugArea.addNav(ugGate)
        
        tavern = Location(
            id = 'tavern',
            name = 'Постоялый двор',
            description = ['Постоялый двор «Уют для странника».', 'Это единственное место, где можно снять комнату в пригороде.',''],
            type = ['public','guarded', 'wait', 'safe'],
            image = 'images/locations/tavern.png')
        allLocs.append(tavern)
        
        freeRoom = Location(
            id = 'freeRoom',
            name = 'Свободная комната',
            description = ['Комната в постоялом дворе'],
            type = ['private','sleep', 'safe'],
            image = 'images/locations/room1.png')
        allLocs.append(freeRoom)
        
        elsaRoom = Location(
            id = 'elsaRoom',
            name = 'Комната Эльзы',
            description = ['Комната Эльзы'],
            type = ['private','wait','safe'],
            image = 'images/locations/elsaRoom.png')
        allLocs.append(elsaRoom)
        
        tavern.addDoor('tavernDoor', freeRoom)
        tavern.addDoor('elsaDoor', elsaRoom)
        tavern.addNav(zapadPrigorod)
        
        tailor = Location(
            id = 'tailor',
            name = 'Портной',
            description = ['Портной.', 'todo'],
            type = ['public'],
            image = 'images/locations/tailor.png')
        allLocs.append(tailor)
        
        tailor.addNav(zapadPrigorod)
        
        smallStore = Location(
            id = 'smallStore',
            name = 'Лавка зеленщика Майкла',
            description = ['Небольшая лавка, заставленная горшками, мешками с овощами и пучками с салатом.', ''],
            type = ['public','guarded'],
            image = 'images/locations/small_store.png')
        allLocs.append(smallStore)
        smallStore.addDoor('storeDoor', severPrigorod)

        
###########################################################################################
# Для Генерации домов
###########################################################################################        
        
        gen_cellar = Location(
            id = 'gen_cellar',
            name = 'Подвал',
            description = ['Маленький, узкий, кишащий крысами подвал заставленный невесть чем.', 'Хозяева здесь хранят всякий хлам, но бывает встречается нечто интересное.'],
            type = ['floor0','level1','guarded','store','workshop','generated'],
            image = 'images/locations/generated/gen_cellar_')
        generatedLocs.append(gen_cellar)
        allLocs.append(gen_cellar)
        
        gen_store = Location(
            id = 'gen_store',
            name = 'Лавка торговца',
            description = ['Небольшой магазин с прилавком и полками заставленными нехитрым товаром.', 'Достаточно бедно и убого, но серьёзный навар рассчитывать не стоит.'],
            type = ['level1','guarded','store','exit','single','generated'],
            image = 'images/locations/generated/gen_store_')
        generatedLocs.append(gen_store)
        allLocs.append(gen_store)
        
        gen_store1 = Location(
            id = 'gen_store1',
            name = 'Лавка ремесленника',
            description = ['Небольшой магазин с прилавком и полками заставленными нехитрым товаром.', 'Достаточно бедно и убого, но серьёзный навар рассчитывать не стоит.'],
            type = ['level1','guarded','exit','workshop','generated'],
            image = 'images/locations/generated/gen_store_')
        generatedLocs.append(gen_store1)
        allLocs.append(gen_store1)
        
        gen_storeroom = Location(
            id = 'gen_storeroom',
            name = 'Подсобка',
            description = ['Маленькая комнатушка заваленная дешёвым товаром.'],
            type = ['level1','guarded','store','workshop','single','generated'],
            image = 'images/locations/generated/gen_storeroom_')
        generatedLocs.append(gen_storeroom)
        allLocs.append(gen_storeroom)
        
        gen_backroom = Location(
            id = 'gen_backroom',
            name = 'Прихожая',
            description = ['Прихожая входа со двора.', 'Крохотное грязное помещение для уличной обуви, связок дров и непонятного хлама.'],
            type = ['level1','guarded', 'exit','store','workshop','generated'],
            image = 'images/locations/generated/gen_backroom_')
        generatedLocs.append(gen_backroom)
        allLocs.append(gen_backroom)
        
        gen_refectory = Location(
            id = 'gen_refectory',
            name = 'Трапезная',
            description = ['Зал трапезной с очагом у стены.', 'Унылые закопченные стены, загаженные полы, грубые деревянные столы.', 'Здесь же и топчан помощника хозяина, не выделять же ему отдельную комнату под людскую.'],
            type = ['level1','guarded','store','workshop','generated'],
            image = 'images/locations/generated/gen_refectory_')
        generatedLocs.append(gen_refectory)
        allLocs.append(gen_refectory)
        
        gen_corridor = Location(
            id = 'gen_corridor',
            name = 'Коридор',
            description = ['Короткий, темный и узкий коридор заканчивающийся лестницей.'],
            type = ['level1','guarded', 'floor_change','store','workshop','generated'],
            image = 'images/locations/generated/gen_corridor_')
        generatedLocs.append(gen_corridor)
        allLocs.append(gen_corridor)
        
        gen_kitchen = Location(
            id = 'gen_kitchen',
            name = 'Кухня',
            description = ['Густо покрытая копотью и жиром кухня, большую часть которой занимает печь и разделочные столы.'],
            type = ['level1','guarded','store','workshop','generated'],
            image = 'images/locations/generated/gen_kitchen_')
        generatedLocs.append(gen_kitchen)
        allLocs.append(gen_kitchen)
        
        gen_pantry = Location(
            id = 'gen_pantry',
            name = 'Кладовая',
            description = ['Небольшая темная кладовая, заставленная бочкой и ящиками со снедью и питьём. Весьма сомнительная и чистота, и годность многих продуктов.'],
            type = ['level1','guarded','store','workshop','generated'],
            image = 'images/locations/generated/gen_pantry_')
        generatedLocs.append(gen_pantry)
        allLocs.append(gen_pantry)
        
        gen_bedroom = Location(
            id = 'gen_bedroom',
            name = 'Покои',
            description = ['Большое помещение покоев, разделенное на приватные участки занавесями из тяжелых тканей','Здесь, на грубых деревянных кроватях место отдыха хозяина, хозяйки и всех домочадцы.'],
            type = ['level1','guarded','single','store','workshop','floor2','generated'],
            image = 'images/locations/generated/gen_bedroom_')
        generatedLocs.append(gen_bedroom)
        allLocs.append(gen_bedroom)
        
        gen_workshop = Location(
            id = 'gen_workshop',
            name = 'Мастерская',
            description = ['Помещение мастерской мещанина заставленное всякими страшного вида инструментами, столами для производства работ, бочками с водой и разными ингредиентами.'],
            type = ['level1','guarded','single','workshop','generated'],
            image = 'images/locations/generated/gen_workshop_')
        generatedLocs.append(gen_workshop)
        allLocs.append(gen_workshop)
        return allLocs
                
    def getLocation(id = ''):
        for x in allLocs:
            if x.id == id:
                return x
            
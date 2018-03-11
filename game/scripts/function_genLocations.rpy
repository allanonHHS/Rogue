init 10 python:
    import os
    def genHouse(location, type, addtionalType = type, level = 'level1', investigation = [], special = []):
        houseArr = []
        for genLoc in generatedLocs:
            if level in genLoc.type and type in genLoc.type:
                tempLoc = copy.deepcopy(genLoc)
                tempLoc.image = genImage(tempLoc)
                houseArr.append(tempLoc)
                
######################################################################################################################################
        if addtionalType == 'store':
            gen_store = getRoom('gen_store', houseArr) 
            gen_cellar = getRoom('gen_cellar', houseArr)
            gen_storeroom = getRoom('gen_storeroom', houseArr)
            gen_backroom = getRoom('gen_backroom', houseArr)
            gen_refectory = getRoom('gen_refectory', houseArr)
            gen_corridor = getRoom('gen_corridor', houseArr)
            gen_kitchen = getRoom('gen_kitchen', houseArr)
            gen_pantry = getRoom('gen_pantry', houseArr)
            gen_bedroom = getRoom('gen_bedroom', houseArr)
            
            house = [gen_store,gen_cellar,gen_storeroom,gen_backroom,gen_refectory,gen_corridor,gen_kitchen,gen_pantry,gen_bedroom]
            
            gen_store.genNavigation(location, investigation)
            gen_store.genNavigation(gen_storeroom, investigation)
            gen_backroom.genNavigation(gen_storeroom, investigation)
            gen_store.genNavigation(gen_refectory, investigation)
            gen_refectory.genNavigation(gen_kitchen, investigation)
            gen_kitchen.genNavigation(gen_cellar, investigation)
            gen_refectory.genNavigation(gen_corridor, investigation)
            gen_corridor.genNavigation(gen_bedroom, investigation)
            
            for room in houseArr:
                if room != gen_pantry and rand(1,5) == 1:
                    tempRoom = copy.deepcopy(gen_pantry)
                    room.genNavigation(tempRoom, investigation)
                    house.append(tempRoom)
                    
            for room in house:
                for item in allItems:
                    if 'location' in item.type and rand(1,5) == 1:
                        room.items.append(item)
                        
                if len(special) > 0:
                    if room.id == special[0]:
                        room.items.append(getItem(special[1]))
                        
######################################################################################################################################
        elif addtionalType == 'existStore':
            # gen_store = getRoom('gen_store', houseArr) 
            gen_cellar = getRoom('gen_cellar', houseArr)
            gen_storeroom = getRoom('gen_storeroom', houseArr)
            gen_backroom = getRoom('gen_backroom', houseArr)
            gen_refectory = getRoom('gen_refectory', houseArr)
            gen_corridor = getRoom('gen_corridor', houseArr)
            gen_kitchen = getRoom('gen_kitchen', houseArr)
            gen_pantry = getRoom('gen_pantry', houseArr)
            gen_bedroom = getRoom('gen_bedroom', houseArr)
            
            house = [gen_cellar,gen_storeroom,gen_backroom,gen_refectory,gen_corridor,gen_kitchen,gen_pantry,gen_bedroom]
            
            location.genNavigation(gen_storeroom, investigation)
            gen_backroom.genNavigation(gen_storeroom, investigation)
            location.genNavigation(gen_refectory, investigation)
            gen_refectory.genNavigation(gen_kitchen, investigation)
            gen_kitchen.genNavigation(gen_cellar, investigation)
            gen_refectory.genNavigation(gen_corridor, investigation)
            gen_corridor.genNavigation(gen_bedroom, investigation)
            
            for room in houseArr:
                if room != gen_pantry and rand(1,5) == 1:
                    tempRoom = copy.deepcopy(gen_pantry)
                    room.genNavigation(tempRoom, investigation)
                    house.append(tempRoom)
                    
            for room in house:
                for item in allItems:
                    if 'location' in item.type and rand(1,5) == 1:
                        room.items.append(item)
                        
                if len(special) > 0:
                    if room.id == special[0]:
                        room.items.append(getItem(special[1]))
            
            
    def getRoom(id, rooms):
        for x in rooms:
            if x.id == id:
                return x
        return False
        
    def genImage(location):
        tempArr = []
        for path in config.searchpath:
            try:
                for x in os.listdir(os.path.join(path, 'images/locations/generated/')):
                    if location.image in os.path.join(path, 'images/locations/generated/', x):
                        tempArr.append(os.path.join('images/locations/generated/', x))
            except OSError:
                pass
        if len(tempArr) > 0:
            return choice(tempArr)
        else:
            return 'images/noimage.gif'
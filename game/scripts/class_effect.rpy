init -51 python:
    class Effect:
        def __init__ (self, name, id, type, strength, picto = 'images/noimage.gif', description = '', duration = 60, applied = 0):
            self.name = name
            self.id = id
            self.type = type
            self.strength = strength
            self.duration = duration
            self.applied = applied
            self.picto = picto
            self.description = description
            
            
    def genEffect():
        global allEffects
        allEffects = []
        unlock = Effect(
            name = 'Взлом',
            id = 'unlock',
            type = ['breaking','item'],
            strength = 5,
            description = '+5 ко взлому'
        )
        allEffects.append(unlock)
        
        disarm = Effect(
            name = 'Обезвреживание',
            id = 'disarm',
            type = ['disarm','item'],
            strength = 5,
            description = '+5 к обезвреживанию.'
        )
        allEffects.append(disarm)
        
        dex2plus = Effect(
            name = 'Бонус ловкости',
            id = 'dex2plus',
            type = ['dex','item'],
            strength = 2,
            description = '+2 к ловкости.'
        )
        allEffects.append(dex2plus)
        
        dex2minus = Effect(
            name = 'Штраф к ловкости',
            id = 'dex2minus',
            type = ['dex','item'],
            strength = -2,
            description = '-2 к ловкости.'
        )
        allEffects.append(dex2minus)
            
        cha2plus = Effect(
            name = 'Бонус к обаянию',
            id = 'cha2plus',
            type = ['cha','item'],
            strength = 2,
            description = '+2 к обаянию.'
        )
        allEffects.append(cha2plus)
        
        cha2minus = Effect(
            name = 'Штраф к обаянию',
            id = 'cha2minus',
            type = ['cha','item'],
            strength = -2,
            description = '-2 к обаянию.'
        )
        allEffects.append(cha2minus)
    
    
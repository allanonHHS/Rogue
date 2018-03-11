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
        
        unlock1000 = Effect(
            name = 'Взлом',
            id = 'unlock1000',
            type = ['breaking','item'],
            strength = 1000,
            description = '+1000 ко взлому'
        )
        allEffects.append(unlock1000)
        
        disarm1000 = Effect(
            name = 'Обезвреживание',
            id = 'disarm1000',
            type = ['disarm','item'],
            strength = 1000,
            description = '+1000 к обезвреживанию.'
        )
        allEffects.append(disarm1000)
        
        unlock2 = Effect(
            name = 'Взлом',
            id = 'unlock2',
            type = ['breaking','item'],
            strength = 2,
            description = '+2 ко взлому'
        )
        allEffects.append(unlock2)
        
        disarm2 = Effect(
            name = 'Обезвреживание',
            id = 'disarm2',
            type = ['disarm','item'],
            strength = 2,
            description = '+2 к обезвреживанию.'
        )
        allEffects.append(disarm2)
        
        
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
    
        tiredDEX = Effect(
            name = 'Усталость: штраф к ловкости',
            id = 'tiredDEX',
            type = ['dex'],
            strength = -4,
            description = '-4 к локвости.'
        )
        allEffects.append(tiredDEX)
        
        tiredCHA = Effect(
            name = 'Усталость: штраф к обаянию',
            id = 'tiredCHA',
            type = ['cha'],
            strength = -4,
            description = '-4 к обаянию.'
        )
        allEffects.append(tiredCHA)
        
        deadTiredDEX = Effect(
            name = 'Обессиленность: штраф к ловкости',
            id = 'deadTiredDEX',
            type = ['dex'],
            strength = -8,
            description = '-8 к ловкости.'
        )
        allEffects.append(deadTiredDEX)
        
        deadTiredCHA = Effect(
            name = 'Обессиленность: штраф к обаянию',
            id = 'deadTiredCHA',
            type = ['cha'],
            strength = -8,
            description = '-8 к обаянию.'
        )
        allEffects.append(deadTiredCHA)
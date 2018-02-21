init -50 python:
    class Skill:
        def __init__ (self, name, id, type, ability, picto = 'images/noimage.gif', description = ''):
            self.name = name
            self.id = id
            self.type = type
            self.ability = ability
            self.picto = picto
            self.description = description
            
        def getPower(self, char):
            level = char.getLevel()
            
            if self in char.getAllSkills():
                if level < 5:
                    return 2
                elif level < 9:
                    return 3
                elif level < 13:
                    return 4
                elif level < 17:
                    return 5
                else:
                    return 6
            else:
                return 0
            
    def genSkills():
        strResque = Skill(
            name = 'Спасбросок по силе',
            id = 'str',
            type = ['str'],
            ability = '',
            description = ''
        )
        allSkills.append(strResque)
        
        dexResque = Skill(
            name = 'Спасбросок по ловкости',
            id = 'dex',
            type = ['dex'],
            ability = '',
            description = ''
        )
        allSkills.append(dexResque)
        
        conResque = Skill(
            name = 'Спасбросок по выносливости',
            id = 'con',
            type = ['con'],
            ability = '',
            description = ''
        )
        allSkills.append(conResque)
        
        intResque = Skill(
            name = 'Спасбросок по интеллекту',
            id = 'int',
            type = ['int'],
            ability = '',
            description = ''
        )
        allSkills.append(intResque)
        
        wisResque = Skill(
            name = 'Спасбросок по мудрости',
            id = 'wis',
            type = ['wis'],
            ability = '',
            description = ''
        )
        allSkills.append(wisResque)
        
        chaResque = Skill(
            name = 'Спасбросок по харизме',
            id = 'cha',
            type = ['cha'],
            ability = '',
            description = ''
        )
        allSkills.append(chaResque)
        
##########################################################################################################        

        acrobatics = Skill(
            name = 'Акробатика',
            id = 'acrobatics',
            type = ['dex','player','npc'],
            ability = '',
            description = ''
        )
        allSkills.append(acrobatics)
        
        dexOfHand = Skill(
            name = 'Ловкость рук',
            id = 'dexOfHand',
            type = ['dex','player'],
            ability = '',
            description = ''
        )
        allSkills.append(dexOfHand)
        
        stealth = Skill(
            name = 'Скрытность',
            id = 'stealth',
            type = ['dex','player','npc'],
            ability = '',
            description = ''
        )
        allSkills.append(stealth)
        
        arcana = Skill(
            name = 'Аркана',
            id = 'arcana',
            type = ['int','player'],
            ability = '',
            description = ''
        )
        allSkills.append(arcana)
        
        persuasion = Skill(
            name = 'Убеждение',
            id = 'persuasion',
            type = ['cha','player'],
            ability = '',
            description = ''
        )
        allSkills.append(persuasion)
        
        nature = Skill(
            name = 'Природа',
            id = 'nature',
            type = ['int','player','npc'],
            ability = '',
            description = ''
        )
        allSkills.append(nature)
        
        insight = Skill(
            name = 'Проницательность',
            id = 'insight',
            type = ['wis','player','npc'],
            ability = '',
            description = ''
        )
        allSkills.append(insight)
        
        medicine = Skill(
            name = 'Медицина',
            id = 'medicine',
            type = ['wis','player'],
            ability = '',
            description = ''
        )
        allSkills.append(medicine)
        
        perception = Skill(
            name = 'Восприятие',
            id = 'perception',
            type = ['wis','player','npc'],
            ability = '',
            description = ''
        )
        allSkills.append(perception)
        
        deception = Skill(
            name = 'Обман',
            id = 'deception',
            type = ['cha','player','npc'],
            ability = '',
            description = ''
        )
        allSkills.append(deception)
        
        intimidation = Skill(
            name = 'Устрашение',
            id = 'intimidation',
            type = ['cha','player'],
            ability = '',
            description = ''
        )
        allSkills.append(intimidation)
        
        performance = Skill(
            name = 'Артистизм',
            id = 'performance',
            type = ['wis','player'],
            ability = '',
            description = ''
        )
        allSkills.append(performance)
        
        breaking = Skill(
            name = 'Взломщик',
            id = 'breaking',
            type = ['dex','player'],
            ability = '',
            description = ''
        )
        allSkills.append(breaking)
        
        disarm = Skill(
            name = 'Чувствительные пальцы',
            id = 'disarm',
            type = ['dex','player'],
            ability = '',
            description = ''
        )
        allSkills.append(disarm)
    
    
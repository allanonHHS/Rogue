init -50 python:
    class Skill:
        def __init__ (self, name, id, type, ability, picto = 'images/noimage.gif', description = '', level = 1):
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
            description = 'Позволяет успешно преодолевать различные препятствия, держать баланс и так далее.'
        )
        allSkills.append(acrobatics)
        
        dexOfHand = Skill(
            name = 'Ловкость рук',
            id = 'dexOfHand',
            type = ['dex','player'],
            ability = '',
            description = 'Позволяет незаметно лазить по карманам и воровать различные мелкие вещи.'
        )
        allSkills.append(dexOfHand)
        
        stealth = Skill(
            name = 'Скрытность',
            id = 'stealth',
            type = ['dex','player','npc'],
            ability = '',
            description = 'Умение прятаться от чужого взгляда.'
        )
        allSkills.append(stealth)
        
        arcana = Skill(
            name = 'Аркана',
            id = 'arcana',
            type = ['int','player'],
            ability = '',
            description = 'Знание о магии, иномирных существах, свитках и прочем.'
        )
        allSkills.append(arcana)
        
        persuasion = Skill(
            name = 'Убеждение',
            id = 'persuasion',
            type = ['cha','player'],
            ability = '',
            description = 'Умение убедить собеседника в своей правоте.'
        )
        allSkills.append(persuasion)
        
        nature = Skill(
            name = 'Природа',
            id = 'nature',
            type = ['int','player','npc'],
            ability = '',
            description = 'Знание о природе, животных, умение находить следы в лесу.'
        )
        allSkills.append(nature)
        
        investigation = Skill(
            name = 'Расследование',
            id = 'investigation',
            type = ['int','player','npc'],
            ability = '',
            description = 'Возможность делать аналитические выводы на основе известных фактов.'
        )
        allSkills.append(investigation)
        
        insight = Skill(
            name = 'Проницательность',
            id = 'insight',
            type = ['wis','player','npc'],
            ability = '',
            description = 'Умение понять подноготную человека, распознать обман, выяснить его текущие желания.'
        )
        allSkills.append(insight)
        
        medicine = Skill(
            name = 'Медицина',
            id = 'medicine',
            type = ['wis','player'],
            ability = '',
            description = 'Умение врачевать раны.'
        )
        allSkills.append(medicine)
        
        perception = Skill(
            name = 'Восприятие',
            id = 'perception',
            type = ['wis','player','npc'],
            ability = '',
            description = 'Возможность стать более внимательным, подмечать мелкие детали, искать ловушки и тех, кто хочет своровать у вас.'
        )
        allSkills.append(perception)
        
        deception = Skill(
            name = 'Обман',
            id = 'deception',
            type = ['cha','player','npc'],
            ability = '',
            description = 'Возможность успешно обмануть собеседника.'
        )
        allSkills.append(deception)
        
        intimidation = Skill(
            name = 'Устрашение',
            id = 'intimidation',
            type = ['cha','player'],
            ability = '',
            description = 'Умение запугать собеседника.'
        )
        allSkills.append(intimidation)
        
        performance = Skill(
            name = 'Артистизм',
            id = 'performance',
            type = ['wis','player'],
            ability = '',
            description = 'Перевоплощения, возможность играть в театре, показывать представления.'
        )
        allSkills.append(performance)
        
        breaking = Skill(
            name = 'Взломщик',
            id = 'breaking',
            type = ['dex','player'],
            ability = '',
            description = 'Умение вскрывать замки.'
        )
        allSkills.append(breaking)
        
        disarm = Skill(
            name = 'Чувствительные пальцы',
            id = 'disarm',
            type = ['dex','player'],
            ability = '',
            description = 'Умение обезвреживать ловушки, если вы, конечно, знаете как это надо делать.'
        )
        allSkills.append(disarm)
    
        seduction = Skill(
            name = 'Соблазнение',
            id = 'seduction',
            type = ['cha','player', 'npc'],
            ability = '',
            description = 'Естественное женское очарование. Возможность добиться чего то не общепринятым, но вполне эффективным способом.'
        )
        allSkills.append(seduction)
        
        luck = Skill(
            name = 'Удача',
            id = 'luck',
            type = ['none','player', 'npc'],
            ability = '',
            description = 'Кость кидается два раза с выбором наибольшего результата.'
        )
        allSkills.append(luck)
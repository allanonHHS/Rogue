init -3 python:
    #Start time
    minute = 0
    check_minute = 0
    hour = 6
    ptime = 0
    mtime = 0
    weekday = 1
    month = 5
    number = 1
    year = 1220
    last_sleeped = 0
    
    def gettime(*args):
        #Дни недели
        if weekday == 1: _weekday = 'Понедельник'
        if weekday == 2: _weekday = 'Вторник'
        if weekday == 3: _weekday = 'Среда'
        if weekday == 4: _weekday = 'Четверг'
        if weekday == 5: _weekday = 'Пятница'
        if weekday == 6: _weekday = 'Суббота'
        if weekday == 7: _weekday = 'Воскресенье'

        #Месяца
        if month == 1: _month = 'Января'
        if month == 2: _month = 'Февраля'
        if month == 3: _month = 'Марта'
        if month == 4: _month = 'Апреля'
        if month == 5: _month = 'Мая'
        if month == 6: _month = 'Июня'
        if month == 7: _month = 'Июля'
        if month == 8: _month = 'Августа'
        if month == 9: _month = 'Сентября'
        if month == 10: _month = 'Октября'
        if month == 11: _month = 'Ноября'
        if month == 12: _month = 'Декабря'
        
        if minute < 10:
            output = '%d %s %d, %s. %s:0%s' % (number, _month, year, _weekday, hour, minute)
        else:
            output = '%d %s %d, %s. %s:%s' % (number, _month, year, _weekday, hour, minute)
            
        if 'day' in args:
            output = '%d %s %d, %s.' % (number, _month, year, _weekday)
            
        return output
    
    def advancetime(change):
        global minute, check_minute, hour, ptime, weekday, number, year, month, mtime
        x = 0
        while x < change:
            if hour >= 5 and hour < 9:
                hour = 5
                advance = 4
            elif hour >= 9 and hour < 17:
                hour = 9
                advance = 8
            elif hour >= 17 and hour < 22:
                hour = 17
                advance = 5
            else:
                hour = 22
                advance = 7
            changetime(advance*60)
            x += 1

    def getcurrtime():
        if hour >= 5 and hour < 9:
            return 1
        elif hour >= 9 and hour < 17:
            return 2
        elif hour >= 17 and hour < 22:
            return 3
        else:
            return 4
    
    def changetime(change, *args):
        global minute, check_minute, hour, ptime, weekday, number, year, month, mtime
        
        if change < 30:
            timeMod = 1
            if 'sneak' in player.state:
                timeMod = timeMod*2
                
            if 'alarm' in player.state:
                timeMod = timeMod*2
                
            if 'overweight' in player.state:
                timeMod = timeMod*2
                
            change = change*timeMod
        
        while change != 0:
            tempChange = min(10,change)
            change -= min(10,change)
            minute += tempChange
            mtime += tempChange
            counter = 0
            if minute >= 60:
                # hourlyRecount()
                minute -= 60
                hour += 1
                ptime += 1
                if hour >= 24:
                    hour -= 24
                    weekday += 1
                    if weekday >=8: weekday -=7
                    number += 1
                    if number >= 31:
                        number -= 30
                        month += 1
                        if month == 13:
                            month -=12
                            year += 1
        # return counter
    
    def getWeekday(day):
        if day == 1: return 'Понедельник'
        if day == 2: return 'Вторник'
        if day == 3: return 'Среду'
        if day == 4: return 'Четверг'
        if day == 5: return 'Пятницу'
        if day == 6: return 'Субботу'
        if day == 7: return 'Воскресенье'
    
    def lt():
        if hour in range(5,22):
            return 1
        else:
            return 0
        return result

    def hourlyRecount():
        global hour
        return True
                
                
                
label trap_simpleTrap:
    'Попалась!'
    $ move(curloc)

label sleep:
    show expression curloc.image at center,top as bgPic
    show expression 'images/events/basic/sleep.png' at center,top as tempPic
    'Раздевшись, вы улеглись на грязную, пропахшую сотнями людей до вас кровать, и уснули. Несмотря на обстановку, вы прекрасно выспались!'
    python:
        player.state = []
        changetime(60*7)
        player.setHP(player.stats.maxHP)
        player.setEnergy(player.getMaxEnergy())
        move(curloc)
    
label wait:
    show expression curloc.image at center,top as bgPic
    show expression 'images/events/basic/wait.png' at center,top as tempPic
    'Вы около часа просидели за столом со скучающим видом, ожидая чего-то или кого-то.'
    $ player.state = []
    $ changetime(60)
    $ move(curloc)
    
label rest:
    show expression curloc.image at center,top as bgPic
    show expression 'images/events/basic/rest1.png' at center,top as tempPic
    'Вы решили вздремнуть часок, чтобы восстановить немного сил.'
    $ player.state = []
    $ changetime(60)
    $ player.incEnergy(60)
    $ move(curloc)
    
label breaking_catch:
    show expression curloc.image at center,top as bgPic
    if player.getBodyPart().id == 'nothing':
        show expression 'images/events/basic/breaking_catch_1.png'  at center,top as tempPic
    elif player.getBodyPart().id == 'thiefArmor':
        show expression 'images/events/basic/breaking_catch_2.png'  at center,top as tempPic
    elif player.getBodyPart().id == 'manClothes':
        show expression 'images/events/basic/breaking_catch_4.png'  at center,top as tempPic
    else:
        show expression 'images/events/basic/breaking_catch_3.png'  at center,top as tempPic
    'Сейчас слишком светло, по дому ходит множество людей. Мне надо поскорее убираться отсюда!'
    $ move(outside)
    
label death:
    show expression 'images/events/basic/death.png'  at center,top as tempPic
    if rand(1,2) == 1:
        'Вы умерли. Господь забрал вашу душу в молодом возрасте, защитив её от тяжести будущих грехов. Да будет это уроком тем, кто свернул с пути благочестия и погряз в пучине порока!!!'
    else:
        'Вы умерли. Господь забрал вашу душу в молодом возрасте, защитив её от тяжести будущих грехов. Да будет ваша несчастная судьба уроком для тех девиц, кои свернули с пути благочестия и погрязли в пучине порока!!!'
    $ renpy.quit()
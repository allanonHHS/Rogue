label steal_decline:
    show expression curloc.image at center,top as bgPic
    show expression 'images/events/basic/decline.png' at center,top as tempPic
    player.say '{color=#fff782}Мне не стоит воровать в этом месте.'
    $ move(curloc)
    
label trap_simpleTrap:
    'Попалась!'
    $ move(curloc)
    
label steal_catched:
    'Я попалась и не могу вырваться!'
    $ move(curloc)
    
label steal_escapeSTR:
    'Я попалась, но смогла вырваться!'
    $ move(curloc)
    
label steal_escapeDEX:
    'Меня заметили, пока я лазила по карманам, но я смогла увернуться от рук и убежать!'
    $ move(curloc)
    
label stealth_catched:
    'Меня заметили, пока я пыталась прилюдно взломать дверь!'
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
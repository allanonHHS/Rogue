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
    python:
        player.state = []
        changetime(60*7)
        player.setHP(player.stats.maxHP)
        player.setEnergy(player.getMaxEnergy())
    show expression curloc.image at center,top as bgPic
    show expression 'images/events/basic/sleep.png' at center,top as tempPic
    'Раздевшись, я улеглась на грязную, пропахшую сотнями людей до меня кровать, и уснула. Несмотря на обстановку, я прекрасно выспалась!'
    $ move(curloc)
    
label wait:
    $ player.state = []
    $ changetime(60)
    show expression curloc.image at center,top as bgPic
    show expression 'images/events/basic/wait.png' at center,top as tempPic
    'Я около часа просидела за столом со скучающим видом, ничего не заказывая.'
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
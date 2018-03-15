label steal_decline:
    show expression curloc.image at center,top as bgPic
    show expression 'images/events/basic/decline.png' at center,top as tempPic
    player.say '{color=#fff782}Мне не стоит воровать в этом месте.'
    $ move(curloc)
    
label steal_catched:
    show expression curloc.image at center,top as bgPic
    if currChar.getSex() == 'male':
        if 'woman' in player.getBodyPart().id:
            show expression 'images/events/basic/steal_catched_2.png' at center,top as tempPic
        else:
            show expression 'images/events/basic/steal_catched_1.png' at center,top as tempPic
    else:
        if 'woman' in player.getBodyPart().id:
            show expression 'images/events/basic/steal_catched_3.png' at center,top as tempPic
        else:
            show expression 'images/events/basic/steal_catched_4.png' at center,top as tempPic

    'Для успешной кражи вы были не столь умелой, как хотелось бы. Хозяин кошелька резко  схватил вас за руку с криком : «Поймал вора»!!!'
    menu:
        'Предложить откупиться':  #МЖ
            jump steal_payOff_1
        'Устроить представление (артистизм)':  #МЖ
            jump steal_artistic_1
        'Запугать (Устрашение)':  #МЖ
            jump steal_intimidation_1
        'Взывать к жалости (обман)' if 'woman' in player.getBodyPart().id: #Ж
            jump steal_deception_1
        'Убедить в ошибке (убеждение)':  #МЖ
            jump steal_persuasion_1
        'Соблазнить (соблазнение)' if 'woman' in player.getBodyPart().id and currChar.getSex() == 'male': #Ж (мужской НПС)
            jump steal_seduction_1

    $ move(curloc)
    
label steal_persuasion_1:
    if 'woman' in player.getBodyPart().id:
        show expression 'images/events/basic/steal_persuasion_1.png' at center,top as tempPic
    else:
        show expression 'images/events/basic/steal_persuasion_2.png' at center,top as tempPic
    'Сложно убедить человека в том, что ваша рука случайно оказалась в его кошельке, но почему бы и нет. Прикинувшись рассеянной, вы повели разговор так, словно случайно перепутали кошельки. В этом вам должно было помочь умение мастерски убеждать в самых  невероятных вещах.'
    if isSuccess(player.useSkill('persuasion'), currChar.useSkill('insight'), 'Убеждение: ', exp = 150):
        'Ваш навык убеждения оказался на высоте. Перед вами даже извинились за нелепые подозрения.'
    else:
        if 'woman' in player.getBodyPart().id:
            show expression 'images/events/basic/steal_slap_2.png' at center,top as tempPic
        else:
            show expression 'images/events/basic/steal_slap_1.png' at center,top as tempPic
        'Однако либо окружающие были весьма недоверчивыми, либо ваше искусство убеждения оказалось не на высоте. Вас прервали мощной оплеухой, опустившей вас оземь.'
        jump steal_punish
    $ move(curloc)
    
label steal_seduction_1:
    show expression 'images/events/basic/steal_seduction_1.png' at center,top as tempPic
    'Вы решили, что женские чары позволят вам избежать сурового наказания. Времени на долгий флирт и намеки не было, поэтому вы прямо заявили, что готовы усугубить своё плохое поведение ещё плохими, греховными, но очень приятными поступками.'
    if isSuccess(player.useSkill('seduction'), currChar.useSkill('insight'), 'Соблазнение: ', exp = 150):
        show expression 'images/events/basic/steal_seduction_2.png' at center,top as tempPic
        'Ваше предложение пришлось хозяину кошелька по нраву. Заявив громогласно, что по закону имеет полное право на наказание вора, он потащил вас за руку в ближайший двор и прислонил лицом к телеге. Вы с ужасом поняли что «получать наказание» придется прямо здесь, в двух шагах от улицы, на глазах зевак которые ринулись следом. Мужчина уже собирался стянуть штаны, но сношаться на виду, демонстрировать свои формы всем желающим, это было для вас слишком постыдным. Нужно что-то предпринять.'
        menu:
            'Жалобно просить отвести в укромное место (убеждение)':
                'Жалобно взглянув на мужчину, вы залившись краской стыда, начали горячо упрашивать избавить вас от позора.'
                if isSuccess(player.useSkill('persuasion'), 10, 'Убеждение: ', exp = 50):
                    'Мужик открыл было рот, дабы возразить, но потом кивнул и потащил вас дальше, в глубину переулков.'
                    jump steal_seduction_private
                else:
                    show expression 'images/events/basic/steal_seduction_3.png' at center,top as tempPic
                    'Ваши слова ничуть не тронули грубое сердце мужчины. Ответом была лишь пощечина и напоминание, что уличным девкам не пристало подавать голос.  Вас грубо развернули лицом к телеге и сорвали платье.'
            'Намекнуть об особых удовольствиях доступных в укромном месте (соблазнение)':
                'Прильнув к мужчине, вы страстно зашептали ему на ухо всяки непристойности, обещая подарить ему незабываемые сношения без чужих глаз.'
                if isSuccess(player.useSkill('seduction'), 13, 'Соблазнение: ', exp = 50):
                    'Вы почувствовали, как в живот вам уперся стоячий член. Возбужденный вашими словами и возникающими образами, мужик грубо схватил вас за руку и потащил в переплетение улиц.'
                    jump steal_seduction_special
                else:
                    show expression 'images/events/basic/steal_seduction_3.png' at center,top as tempPic
                    'Вы пытались вложить в слова всю страсть и похоть, но мужчина предпочел получить удовольствие здесь и сейчас. Он грубо развернул вас обратно, лицом к телеге и сорвал платье. '
            'Оставить как есть':
                show expression 'images/events/basic/steal_seduction_3.png' at center,top as tempPic
                'Вы запнулись, думая, стоит ли просить об укромном месте, или не следует испытывать судьбу, выражая недовольство.  Даже малейшего промедления оказалось достаточно, чтобы вопрос был решён сам собой. Грубые руки сорвали с вас платье, и вы оказались голыми пред глазами зевак.'
        jump steal_seduction_wagon

                        
    else:
        if 'woman' in player.getBodyPart().id:
            show expression 'images/events/basic/steal_slap_2.png' at center,top as tempPic
        else:
            show expression 'images/events/basic/steal_slap_1.png' at center,top as tempPic
        'Возможно, хозяин кошелька был изрядно зол, либо ваши женские чары оказались не столь хороши. В любом случае, узнав о себе, что являетесь не только воровкой, но и шлюхой, вы рухнули на землю от сильного удара ладонью по лицу.'
        jump steal_punish
    $ move(curloc)
    
label steal_seduction_wagon:
    show expression 'images/events/basic/steal_seduction_4.png' at center,top as tempPic
    'Вас облокотили о телегу, липкие руки прошлись по телу, облапав грудь, живот, булочки и даже наиболее сокровенные места. Краснея, вы лишь вжали голову, стараясь не смотреть по сторонам от стыда. Вскоре руки наглеца сильно сжали бедра и… Вы лишь всхлипнули, когда внутрь вторгся немалый и горячий стержень, пробивавший дорогу меж узких стеночек.  К счастью, первым движением он вогнал не на наибольшую глубину, не думая вы начали движенье для облегчения следующего проникновения. Второй толчок был ещё больнее, но вы сдержали крик.'
    show expression 'images/events/basic/steal_seduction_5.png' at center,top as tempPic
    'Немного потерпев первые толчки, вы почувствовали, что хождение стержня стало менее болезненным, послышался предательское хлюпанье. Тело само отреагировало, приветливо расширив и смочив щелку пред вторгающимся членом.'
    currChar.speak 'Ты глянь-ка. Мокреет шлюха! - Мужик довольно загоготал, комментируя ваш позор.'
    'Вы ещё больше вжали голову в дурно пахнущие доски телеги, молясь о скорейшем завершении постыдного деяния.'
    show expression 'images/events/basic/steal_seduction_6.png' at center,top as tempPic
    'Однако ваши мольбы не дошли до высших сил. Мужик сношал вас очень долго (или вам так показалось), двигая членом под разными углами и оставив синяки на нежных бедрах. Вы даже начали чувствовать извращенное удовольствие от процесса, низ живота слегка налился теплом. Было уже не больно и даже приятно, если бы не ужасный стыд от осознания собственного грехопадения.'
    show expression 'images/events/basic/steal_seduction_7.png' at center,top as tempPic
    'Но всему приходит конец. Вы с радостью почувствовали как напрягся член, как обжигающая струя бьёт внутрь лона, заливая его семенем. Член постепенно обмяк и вскоре вы, наконец, смогли распрямить уставшее тело. Однако вас ожидало ещё одно испытание.'
    currChar.speak 'Эй, парни. Хорош в штанах хер гонять, - зычно прокричал ваш мучитель. – Можете эту шлюху отыметь!'
    if rand(1,2) == 1:
        'К превеликому счастью смельчаков более не нашлось. Покуда парни в нерешительности переглядывались, не решаясь на публичный блуд, вы подтянули платье и тихими шажочками скрылись с глаз.'
        $ changetime(60)
        $ player.incEnergy(-250)
    else:
        show expression 'images/events/basic/steal_seduction_8.png' at center,top as tempPic
        'Радостно загоготав, вас окружила толпа подвыпивших мужиков. В отчаянии вы попытались вырваться, но получив несколько оплеух обреченно замерли, в ожидании дальнейших истязаний.'
        show expression 'images/events/basic/steal_seduction_9.png' at center,top as tempPic
        'Вас вновь вернули в прежнюю позу и спустя миг новый член начал пробивать дорогу в ваше многострадальное лоно. К счастью, оно было достаточно разогретым и смазанным для безболезненных встреч. Но простого траха было мало.'
        show expression 'images/events/basic/steal_seduction_10.png' at center,top as tempPic
        'Огромный мужик схватил вас за волосы и притянул голову, одновременно сношая сзади. От боли слезы брызнули с глаз, но… неожиданно вы почувствовали прилив возбуждения. Помимо воли вы начали живее двигать бедрами навстречу крепкому члену, низ живота начал наливаться огнем.'
        if rand(1,2) == 1:
            show expression 'images/events/basic/steal_seduction_11.png' at center,top as tempPic
            'Ещё миг и … кульминация. Мощная волна жара затопила ваш разум, тело забилось в судорогах.'
            $ temp = choice(['Джон','Гарри','Майк','Фред'])
            'Смотри как дергается. Шлюхе нравится твой хер [temp], - закричали в толпе, но ваш разум был далеко.'
            'Вы почувствовали сильные шлепки по ягодицам, которые лишь подзадорили ваш пыл. Ваше тело с большей силой изогнулось от нахлынувших  чувств, прежде чем бессильно рухнуть на грязные доски. Ваш насильник тем временем продолжил своё дело, с ещё большим остервенением долбя ваше лоно своим мощным хером. Вскоре новая порция липкой жидкости выстрелила внутрь вашего тела.'
        else:
            show expression 'images/events/basic/steal_seduction_11.png' at center,top as tempPic
            'Но жар быстро стих оставив лишь небольшое приятное вожделение внизу живота. Ваш насильник тем временем продолжал активно долбить ваше лоно,  вгоняя свой мощный хер под разными углами. Вскоре новая порция липкой жидкости выстрелила внутрь вашего тела.'
            show expression 'images/events/basic/steal_seduction_12a.png' at center,top as tempPic
            'Вы обессилено рухнули, лицом на телегу бесстыдно демонстрируя зад толпе, словно приглашая новых насильников. Приглашение не заставило себя ждать. Все, что было в последствии лишь урывками осталось в вашей памяти.'
            $ temp = 0
            $ tempChoiceArr = range(1,8)
            while temp < 3:
                $ tempChoice = choice(tempChoiceArr)
                $ tempChoiceArr.remove(tempChoice)
                if tempChoice == 1:
                    show expression 'images/events/basic/steal_seduction_16.png' at center,top as tempPic
                    'Вас сношают сзади облокотив об, ставшую уже знакомой, телегу.'
                    
                elif tempChoice == 2:
                    show expression 'images/events/basic/steal_seduction_14.png' at center,top as tempPic
                    'Вас положили на спину и ритмично загоняют в лоно хер, кусая груди.'
                    
                elif tempChoice == 3:
                    show expression 'images/events/basic/steal_seduction_15.png' at center,top as tempPic
                    'Один из насильников возжелал вас посадить голым задом на телегу, дабы трахать лицом к лицу, покусывая и облизывая груди. '
                elif tempChoice == 4:
                    show expression 'images/events/basic/steal_seduction_13.png' at center,top as tempPic
                    'Вас скинули с телеги и сношают сзади как четвероногое животное. Вам приходится с трудом стоять на четырёх конечностях под сильными ударами тарана.'
                    
                elif tempChoice == 5:
                    show expression 'images/events/basic/steal_seduction_17.png' at center,top as tempPic
                    'Вас вновь сношают сзади намотав волосы на руку.'
                elif tempChoice == 6:
                    show expression 'images/events/basic/steal_seduction_18.png' at center,top as tempPic
                    'Следующие двое решили удовлетворить свою похоть одновременно.  Вас оттащили от телеги, поместили меж двух насильников и одновременно сношали в лоно и уста, грубо открыв рот и загоняя хер чуть ли не в горло.'
                    
                else:
                    show expression 'images/events/basic/steal_seduction_19.png' at center,top as tempPic
                    'Ужасно уставшая вы лежите на спине дергаясь под толчками очередного насильника и ублажаете рукой  чей-то член.'
                $ temp += 1
        if rand(1,2) == 1:
            show expression 'images/events/basic/steal_seduction_21a.png' at center,top as tempPic
            'Завершением всех этих ужасных испытаний стало ещё большее, и ещё более мерзостное унижение. Сперва вы не поняли, почему вас бросили оземь, и почему вокруг стало несколько недавних насильников, возможно чтоб избить ногами. Но правда оказалась более мерзостной. Спустив штаны, они направили на вас свои херы и начали обильно поливать струями желтой, зловонной мочи. От страха и вы впали в оцепенение. Даже не пытаясь толком защититься, покорно принимая унижение. Когда потоки иссякли, вас наконец оставили в покое. С трудом поднявшись и задыхаясь от исходившей от вас вони, вы натянули потрепанное платье и, пошатываясь, бросились прочь, подальше от этого ужасного места.'
        else:
            show expression 'images/events/basic/steal_seduction_20.png' at center,top as tempPic
            'Очнулись вы лежащей на земле, с бесстыдно раздвинутыми ногами, болью в лоне, покрытая густыми потеками семени. С трудом поднявшись и натянув потрепанное платье, вы пошатываясь бросились прочь, подальше от этого ужасного места.'
        $ player.incEnergy(-1000)
        $ changetime(4*60)
    $move(curloc)

label steal_seduction_private:
    show expression 'images/locations/generated/gen_bedroom_2.png' at center,top as bgPic
    show expression 'images/events/basic/steal_seduction_private_1.png' at center,top as tempPic
    'Вскоре мужчина привел вас  в один из домов, где немедля приступил к исполнению задуманного. Желая как можно скорее избавиться от неприятного действия, вы скинули платье и легли на лежак. Мужик навалился сверху, уперевшись стоячим колом в нижние губы.'
    show expression 'images/events/basic/steal_seduction_private_2.png' at center,top as tempPic
    'Далее всё прошло довольно быстро. Вторжение кола в вашу щелку прошло без боли, вы были слегка разогреты, да и член был средних размеров. Сношали вас активно, но недолго. Вскоре он вытащил член и выпустил семя на живот, а вы (с легким раскаянием) быстро покинули это место, радуясь тому, что всё обошлось достаточно быстро и безболезненно.'
    $ player.incEnergy(-150)
    $ changetime(60)
    $ move(curloc)
    
label steal_seduction_special:
    show expression 'images/locations/generated/gen_bedroom_2.png' at center,top as bgPic
    show expression 'images/events/basic/steal_seduction_special_1.png' at center,top as tempPic
    'Вскоре мужчина привел вас  в один из домов, где немедля приступил к исполнению задуманного. Желая как можно скорее избавиться от неприятного действия, вы скинули платье и хотели было лечь на лежак, для привычной к сношениям позе. Но…'
    currChar.speak 'Нет уж. На колени. Говорила об особом удовольствии, так исполняй. А просто в дырку отыметь и на улице можно было!'
    show expression 'images/events/basic/steal_seduction_special_2.png' at center,top as tempPic
    'Признавая справедливость требований, и опасаясь весьма болезненных последствий за отказ, вы скинули платье и голой покорно встали на колени. Целовать и облизывать устами мужской член было для вас событием неприятным и неприличным, но ради спасения можно и пойти на грех.'
    'Взяв член, вы слегка поласкали его рукой, потом дали легкий поцелуй, перетерпев запах пота и мочи. Далее использовали кончик языка для касания головки. Хер ощутимо напрягся и увеличился в размере. Решившись, вы заглотнули его в рот и начали движенья губами, полируя живой стержень. Далее вы поочередно использовали поцелуи, язык и заглатывания, чувствуя как тверже становится хер.'
    show expression 'images/events/basic/steal_seduction_special_3.png' at center,top as tempPic
    'Неожиданно вам партнер реши вмешаться в процесс, и довольно неприятным для вас образом. Вас схватили за затылок и буквально насадили горлом на кол. Фактически вас сношали в рот и горло, используя их вместо естественного для такого рода дел отверстия. Носом вы бились о кучерявую поросль мужика, дыхания едва хватало, дабы не умереть от удушья.'
    show expression 'images/events/basic/steal_seduction_special_4.png' at center,top as tempPic
    'Но и этого было мало. Сильные руки прижали вашу голову к паху, заставив замереть  членом в горле и мыслью о скором удушьи. Вы уже начали судорожно дергать руками, но ещё какой то миг вас держали между жизнью и смертью, прежде чем вынуть член и дать глотнуть воздуха. Жадно вдыхая драгоценный воздух, вы едва не вывернули на пол содержимое желудка, но сумели сдержаться пред тем, как вновь приняться за член. '
    show expression 'images/events/basic/steal_seduction_special_5.png' at center,top as tempPic
    'Вы потерялись во времени между жестоким сношением горла и несколькими приступами удушья, но всему приходит конец. Сложно было представить, что вы будете рады струе семени заполнившей вам рот, но это куда лучше, чем задохнуться от хера.'
    currChar.speak 'Глотай всё шлюха!'
    show expression 'images/events/basic/steal_seduction_special_6.png' at center,top as tempPic
    'Не задумываясь, вы выполнили приказ, исправно проглотив всю порцию семени и тщательно очистив языком член. Лишь бы скорее покинуть это место.'
    'Будучи удовлетворенным, мужик отпустил вас, сопроводив несколькими похабными замечаниями. Чувствуя себя опозоренной и униженной, вы покинули дом, стараясь поскорее забыть о произошедшем.'
    $ player.incEnergy(-50)
    $ changetime(60)
    $ move(curloc)
    
label steal_deception_1:
    if 'woman' in player.getBodyPart().id:
        show expression 'images/events/basic/steal_deception_2.png' at center,top as tempPic
    else:
        show expression 'images/events/basic/steal_deception_1.png' at center,top as tempPic
    'Вы пошатнулись и взглянули на хозяина (хозяйку) кошелька невинными, широко раскрытыми глазами.'
    player.say 'Прошу вас. Я три дня не ела. Хоть кроху. Избейте, но дайте хоть что-то. Я более не могу…схожу с ума.'
    
    'Опередив гневные вопли, вы немедля залились слезами, всем видом показывая насколько вам стыдно и горько от своего грехопадения. Короткими, но весьма прочувственными фразами вы попытались обрисовать невообразимый ужас ситуации, в которой оказались. В рассказе был и коварный соблазнитель, и разгневанные родители и прочие составляющие типичной слезливой истории. '
    if isSuccess(player.useSkill('deception'), currChar.useSkill('insight'), 'Обман: ', exp = 150):
        if currChar.getSex() == 'male':
            'Сжатые было кулаки постепенно разжались, люди смущенно разошлись. Сам хозяин кошелька сочувственно взглянул на вас и пошёл прочь, чувствуя себя виноватым за то, что не оказал помощи.'
        else:
            'Сжатые было кулаки постепенно разжались, люди смущенно разошлись. Сама хозяйка кошелька сочувственно взглянула на вас и пошла прочь, чувствуя себя виноватой за то, что не оказала помощи.'
        if dice(player) >= 20:
            $ temp = rand(20-57)
            'Из толпы зевак послышались сочувственные возгласы и слова ободрения. Люди переглядывались, у некоторых слезились глаза. Вам протянулись руки для сочувственных похлопываний, в некоторых из них были мелкие монеты. С трудом вы освободились от жалостливой толпы, попутно собрав [temp] крон подаяний.'
    else:
        if 'woman' in player.getBodyPart().id:
            show expression 'images/events/basic/steal_slap_2.png' at center,top as tempPic
        else:
            show expression 'images/events/basic/steal_slap_1.png' at center,top as tempPic
        'То ли вас окружали люди с черствыми душами, то ли ваши умения обмана были не столь велики, но вам явно не поверили. Ваши жалостливые слова прервала мощная пощечина, и вы очутились на земле с гудящей головой и немного помутненным рассудком.'
        jump steal_punish
    $ changetime(20)
    $ move(curloc) 
    
    
label steal_artistic_1:
    $ tempChoice = 1
    if 'woman' in player.getBodyPart().id:
        $ tempChoice = rand(1,2)
    if tempChoice == 1:
        if 'woman' in player.getBodyPart().id:
            show expression 'images/events/basic/steal_artisctic_1.png' at center,top as tempPic
        else:
            show expression 'images/events/basic/steal_artisctic_2.png' at center,top as tempPic
        'Благодаря тому, что никто не видел воочию сам момент кражи, вы получили возможность дать небольшое представление. Забившись в судорогах, вы упали на колени, пытаясь симулировать приступ падучей. Ваши руки беспорядочно двигалась, намекая на то, почему они вдруг оказалась в чужом кармане.'
        if isSuccess(player.useSkill('performance'), currChar.useSkill('insight'), 'Представление: ', exp = 150):
            if currChar.getSex() == 'male':
                '[currChar.fname] немедленно оставил вас в покое, прекратив настаивать на факте кражи. Вокруг собралась сочувствующая толпа, вам подержали руки и голову, когда «приступ» прекратился, дали попить воды. После этого, под жалостливые возгласы, вы пошатываясь покинули место неудавшейся кражи.'
            else:
                '[currChar.fname] немедленно оставила вас в покое, прекратив настаивать на факте кражи. Вокруг собралась сочувствующая толпа, вам подержали руки и голову, когда «приступ» прекратился, дали попить воды. После этого, под жалостливые возгласы, вы пошатываясь покинули место неудавшейся кражи.'
        else:
            'К несчастью, ваших актерских навыков оказалось недостаточно, дабы убедить всех в болезни. Вокруг вас собралась разъяренная толпа, в коей не было слышно ни единого возгласа сочувствия.'
            jump steal_punish
    else:
        show expression 'images/events/basic/steal_artisctic_3.png' at center,top as tempPic
        'Представиться полоумной, лучшее, что пришло вам в голову.'
        player.say 'Освободите карманы. Выбросьте на землю всё скверну что храните там!!! Очиститесь перед Господом!!!'
        'Выпучив глаза, вы кричали всяческий бред, стараясь походить на скорбных разумом, встреченных вами в странствиях.'
        if isSuccess(player.useSkill('performance'), currChar.useSkill('insight'), 'Представление: ', exp = 150):
            'Ваше поведение было настолько натуральным, что никто и не заикнулся о возможности кражи. Более того, некоторые из зевак даже стали выкидывать всякие мелочи из карманов. Проорав несколько безумных призывов, вы покинули это место, бормоча под нос бессвязный поток слов.'
        else:
            show expression 'images/events/basic/steal_slap_2.png' at center,top as tempPic
            'То ли вам попались весьма подозрительные зрители, то ли поведение ваше было слегка наигранным, но вам не поверили. Представление было прервано мощной оплеухой, бросившей вас на землю.'
            jump steal_punish
    $ changetime(20)
    $ move(curloc)
            
label steal_intimidation_1:
    $ tempChoice = rand(1,4)
    if 'woman' in player.getBodyPart().id:
        show expression 'images/events/basic/steal_intimidation_1.png' at center,top as tempPic
    else:
        show expression 'images/events/basic/steal_intimidation_2.png' at center,top as tempPic
    if tempChoice == 1:
        'Вы злобно улыбнулись, сверля неудавшуюся жертву тяжёлым неподвижным взглядом.'
    elif tempChoice == 2:
        player.say 'Ударить хочешь или стражникам сдать? Ну давай, посмотрим, как заклятье на тебя подействует.'
    elif tempChoice == 3:    
        if currChar.getSex() == 'male':
            ' Вы нагло взглянули на державшего вас и вполголоса произнесли.\n
            - Ребята Дикого Гарри рядом. Лучше не ори, а то осерчают. Отрежут чего или подожгут. Жалко ведь тебя.'
        else:
            ' Вы нагло взглянули на хозяйку кошелька  и вполголоса произнесли.\n
            - Ребята Дикого Гарри рядом. Лучше не ори, а то осерчают. Отрежут чего или подожгут. Жалко ведь тебя.'
    else:
        if currChar.getSex() == 'male':
            ' Вы грустно улыбнулись и проговорили безжизненным голосом.
            Отошёл (отошла) бы лучше. Если проказы не боишься.'
        else:
            ' Вы грустно улыбнулись и проговорили безжизненным голосом.
            Отошла бы лучше. Если проказы не боишься.'
    if isSuccess(player.useSkill('intimidation'), currChar.useSkill('insight'), 'Угроза: ', exp = 150):
        'От вас в ужасе отшатнулись окружающие, прочие зеваки срочно нашли иные дела. Не спеша, вы обычным шагом покинули место неудавшейся кражи.'
    else:
        if 'woman' in player.getBodyPart().id:
            show expression 'images/events/basic/steal_slap_2.png' at center,top as tempPic
        else:
            show expression 'images/events/basic/steal_slap_1.png' at center,top as tempPic
        'Мощная оплеуха прервала вашу игру. По-видимому, ваши умение запугивать людей оставляет желать лучшего.'
        jump steal_punish
    $ changetime(10)
    $ move(curloc)

label steal_payOff_1:
    menu:
        'Сколько предложить?'
        'Отказаться платить':
            if 'woman' in player.getBodyPart().id:
                show expression 'images/events/basic/steal_slap_2.png' at center,top as tempPic
            else:
                show expression 'images/events/basic/steal_slap_1.png' at center,top as tempPic

            if currChar.getSex() == 'female':
                'Видя, что вы не собираетесь раскаиваться, [currChar.fname] отвесила мощную пощёчину, бросившую вас оземь.'
            else:
                'Видя, что вы не собираетесь раскаиваться, [currChar.fname] отвесил мощную пощёчину, бросившую вас оземь.'
            jump steal_punish
                
        '10 крон' if player.money >= 10:
            $ player.money -= 10
            'Не дожидаясь побоев, вы предложили немного денег, дабы забыть о недоразумении.'
            if rand(1,100) <= 10:
                if currChar.getSex() == 'male':
                    'Хозяин кошелька удовлетворенно кивнул, радуясь нечаянному заработку. Вы быстро расплатились и бросились прочь.'
                else:
                    'Хозяйка кошелька удовлетворенно кивнула, радуясь нечаянному заработку. Вы быстро расплатились и бросились прочь.'
            else:
                if 'woman' in player.getBodyPart().id:
                    show expression 'images/events/basic/steal_slap_2.png' at center,top as tempPic
                else:
                    show expression 'images/events/basic/steal_slap_1.png' at center,top as tempPic
                'Столь скромная сумма не поразила воображение вашего оппонента. Ответом стала мощная пощечина бросившая вас оземь.'
                jump steal_punish
                
        '30 крон' if player.money >= 30:
            $ player.money -= 30
            'Не дожидаясь побоев, вы предложили немного денег, дабы забыть о недоразумении.'
            if rand(1,100) <= 30:
                if currChar.getSex() == 'male':
                    'Хозяин кошелька удовлетворенно кивнул, радуясь нечаянному заработку. Вы быстро расплатились и бросились прочь.'
                else:
                    'Хозяйка кошелька удовлетворенно кивнула, радуясь нечаянному заработку. Вы быстро расплатились и бросились прочь.'
            else:
                if 'woman' in player.getBodyPart().id:
                    show expression 'images/events/basic/steal_slap_2.png' at center,top as tempPic
                else:
                    show expression 'images/events/basic/steal_slap_1.png' at center,top as tempPic
                'Столь скромная сумма не поразила воображение вашего оппонента. Ответом стала мощная пощечина бросившая вас оземь.'
                jump steal_punish
                
        '50 крон' if player.money >= 50:
            $ player.money -= 50
            'Вы решили, что лучше потерять деньги, чем стать жертвой побоев и предложили хорошую сумму денег, дабы забыть о недоразумении.'
            if rand(1,100) <= 50:
                if currChar.getSex() == 'male':
                    'Хозяин кошелька удовлетворенно кивнул, радуясь нечаянному заработку. Вы быстро расплатились и бросились прочь.'
                else:
                    'Хозяйка кошелька удовлетворенно кивнула, радуясь нечаянному заработку. Вы быстро расплатились и бросились прочь.'
            else:
                if 'woman' in player.getBodyPart().id:
                    show expression 'images/events/basic/steal_slap_2.png' at center,top as tempPic
                else:
                    show expression 'images/events/basic/steal_slap_1.png' at center,top as tempPic
                'Несмотря на величину предложенной суммы, она не поразила воображение вашего оппонента. Ответом стала мощная пощечина бросившая вас оземь.'
                jump steal_punish
                
        '70 крон' if player.money >= 70:
            $ player.money -= 70
            'Вы решили, что лучше потерять деньги, чем стать жертвой побоев и предложили хорошую сумму денег, дабы забыть о недоразумении.'
            if rand(1,100) <= 70:
                if currChar.getSex() == 'male':
                    'Хозяин кошелька удовлетворенно кивнул, радуясь нечаянному заработку. Вы быстро расплатились и бросились прочь.'
                else:
                    'Хозяйка кошелька удовлетворенно кивнула, радуясь нечаянному заработку. Вы быстро расплатились и бросились прочь.'
            else:
                if 'woman' in player.getBodyPart().id:
                    show expression 'images/events/basic/steal_slap_2.png' at center,top as tempPic
                else:
                    show expression 'images/events/basic/steal_slap_1.png' at center,top as tempPic
                'Несмотря на величину предложенной суммы, она не поразила воображение вашего оппонента. Ответом стала мощная пощечина бросившая вас оземь.'
                jump steal_punish
                
        '100 крон' if player.money >= 100:
            $ player.money -= 100
            'Мысль откупиться была первой пришедшей вам в голову. Вы решили не скупиться и предложить большую по меркам бедных людей сумму, дабы забыть о недоразумении.'
            if currChar.getSex() == 'male':
                'Хозяин кошелька радостно кивнул. Ради таких денег можно было забыть о мести вору. Вы быстро расплатились и бросились прочь.'
            else:
                'Хозяйка кошелька радостно кивнула. Ради таких денег можно было забыть о мести вору. Вы быстро расплатились и бросились прочь.'
    $ changetime(10)
    $ move(curloc)

    
label steal_escapeSTR:
    show expression curloc.image at center,top as bgPic
    if currChar.getSex() == 'male':
        if 'woman' in player.getBodyPart().id:
            show expression 'images/events/basic/steal_escapeSTR_1.png' at center,top as tempPic
        else:
            show expression 'images/events/basic/steal_escapeSTR_2.png' at center,top as tempPic
    else:
        if 'woman' in player.getBodyPart().id:
            show expression 'images/events/basic/steal_escapeSTR_4.png' at center,top as tempPic
        else:
            show expression 'images/events/basic/steal_escapeSTR_3.png' at center,top as tempPic
    'Благодаря сильным рукам вы сумели освободиться от захвата и, не мудрствуя, бросились прочь по кратчайшему пути. Все кто на нём стоял, просто отлетал в сторону, столкнувшись с вашим крепким телом,  к тому же несшимся на приличной скорости. Вскоре вы удачно скрылись с глаз разъяренных прохожих.'
    $ changetime(10)
    $ move(curloc)
    
label steal_escapeDEX:
    show expression curloc.image at center,top as bgPic
    if 'woman' in player.getBodyPart().id:
        show expression 'images/events/basic/steal_escapeDEX_1.png' at center,top as tempPic
    else:
        show expression 'images/events/basic/steal_escapeDEX_2.png' at center,top as tempPic
    'Вы с прирожденной ловкостью освободили руку от неумелого захвата и бросились прочь. Несколько зевак сделали было неуклюжие попытки вас перехватить, но вы легко их обошли и исчезли с глаз.'
    $ changetime(10)
    $ move(curloc)
    
label stealth_catched:
    'Меня заметили, пока я пыталась прилюдно взломать дверь!'
    $ move(curloc)
    
label steal_punish:
    $ choicePunish = ['steal_punish_battering', 'steal_punish_batteringHeavy','steal_punish_shame','steal_punish_whip']
    if currChar.lname in ['Вор','Разбойник']:
      $ choicePunish.append('steal_punish_rape')
    $ renpy.jump(choice(choicePunish))
    
label steal_punish_battering:
    show expression curloc.image at center,top as bgPic
    $ player.incEnergy(-200)
    if 'woman' in player.getBodyPart().id:
        show expression 'images/events/basic/steal_punish_battering_1.png' at center,top as tempPic
        $ temp = ''
        $ player.incHP(-5)
    else:
        show expression 'images/events/basic/steal_punish_battering_2.png' at center,top as tempPic
        $ temp = 'Хотя будь вы в женском платье, всё бы обошлось ещё легче. '
        $ player.incHP(-8)
    'Не мешкая, вас начали бить ногами, руками, а также палками и всем прочим, что попало под руку. Скорчившись на земле, вы руками прикрыли голову, стараясь защитить жизненные органы. К счастью, били вас довольно лениво и недолго. [temp]Вскоре вас оставили лежать избитой на земле и вы смогли, хоть и не сразу, со стоном встать на ноги и хромая покинуть это место.'
    $ changetime(60)
    $ move(curloc)
    
label steal_punish_batteringHeavy:
    $ player.incEnergy(-600)
    if 'woman' in player.getBodyPart().id:
        show expression 'images/events/basic/steal_punish_battering_1.png' at center,top as tempPic
        $ temp = ''
        $ player.incHP(-8)
    else:
        show expression 'images/events/basic/steal_punish_battering_2.png' at center,top as tempPic
        $ temp = 'Вы неоднократно пожалели, что не находитесь в  женском платье, возможно тогда к вам были бы немного милосерднее. '
        $ player.incHP(-11)
        
        'Собравшаяся толпа тут же принялась бить вас ногами, кулаками, а также палками и всем прочим, что попало под руку. Скорчившись на земле, вы руками прикрыли голову, стараясь защитить жизненные органы. К несчастью, своими действиями вы раззадорили толпу, били вас довольно долго и серьёзно. [temp]'
        'Однако всё обошлось. Толпе надоело вас пинать, и она разошлась по своим делам. Не веря в то, что остались живы, вы долго лежали избитой на земле, прежде чем смогли с превеликим трудом встать на ноги, и, держась за ограду, покинуть это место.'
    $ changetime(60)
    $ move(curloc)
        
label steal_punish_shame:
    $ player.incEnergy(-200)
    show expression 'images/events/basic/steal_punish_shame_1.png' at center,top as tempPic
    'Вас уже хотели было избить, но одному из зевак пришла в голову иная мысль. С вас сорвали платье и, подстегивая розгами, провели по узким улочкам пригорода, дав многочисленным зевакам поглазеть на ваше голое тело и вдоволь поглумиться. Заливаясь краской, вы шли обнаженной по улице, пытаясь скрыть лицо, но это удавалось лишь в те моменты, когда вас не держали за волосы. Позорная процессия длилась достаточно долго, но всему приходит конец. Удовлетворившись местью и вдоволь натешившись, ваши мучители наконец отпустили вас прочь.'
    $ changetime(60)
    $ move(curloc)
    

label steal_punish_whip:
    if 'woman' in player.getBodyPart().id:
        show expression 'images/events/basic/steal_punish_battering_1.png' at center,top as tempPic
    else:
        show expression 'images/events/basic/steal_punish_battering_2.png' at center,top as tempPic
    $ player.incHP(-5)
    'На земле вам перепало всего несколько ударов. Кому из толпы пришла в голову мысль, что порка розгами будет лучшим наказанием, и его с радостью поддержали. Порка молодой и красивой женщины всегда вызывала у простолюдинов низменный интерес. Само по себе наказание не было для вас необычным, розги являлись обязательным стимулом прилежного обучения для благородных девиц, но голой… на улице… от простолюдинов. Больший позор сложно было представить.'
    show expression 'images/events/basic/steal_punish_whip_1.png' at center,top as tempPic
    'С вас сорвали платье, рядом были найдены козлы для распилки бревен, к которым вас крепко привязали. Быстро нашлись и розги, и желающие вас ими попотчевать. Основная часть ударов досталась вашему многострадальному заду, но также перепало и ляжкам, и спине. Закричав от первого удара, далее вам удавалось проявлять выдержку духа, покуда следы прутьев не покрыли мягкую часть тела. '
    show expression 'images/events/basic/steal_punish_whip_2.png' at center,top as tempPic
    'Далее ожоги от ударов стали нестерпимые, и забыв обо всём, вы огласили округу криками боли, надеясь хоть немного смягчить палачей. Однако пороли вас долго, не считая ударов, ориентируясь лишь по состоянию кожи на ягодицах. Когда ваши булочки стали иссиня-красными вас, наконец, освободили и разрешили идти прочь. Что вы и сделали, плача от боли и стыда, стараясь побыстрее переставлять ноги и страдая от каждого прикосновения ткани платья к поротому месту.'
    $ changetime(60)
    $ move(curloc)
    
label steal_punish_rape:
    if 'woman' in player.getBodyPart().id:
        show expression 'images/events/basic/steal_slap_2.png' at center,top as tempPic
    else:
        show expression 'images/events/basic/steal_slap_1.png' at center,top as tempPic
    'В качестве продолжения вы ожидали град ударов, но вместо того хозяин кошелька остановил возбужденную толпу.'
    currChar.speak 'Стоять. У меня крала, мне и решать как поступить. Жалко девку увечить. Пусть отрабатывает!'
    show expression 'images/events/basic/steal_punish_room.png' at center,top as bgPic
    show expression 'images/events/basic/steal_punish_rape_1.png' at center,top as tempPic
    'Схватив вас за руку, он рывком потащил вас прочь, в какой то узкий переулок. Вскоре вы оказались подле покосившегося дома. Мужик уверенно открыл дверь и затащил вас внутрь. Оказавшись в полутьме, вы заметили ещё несколько человек разбойной наружности.'
    currChar.speak 'Ну что братья. Девку вот привёл, красть у меня вздумала. Можно хер попарить и на шлюх тратиться  не надо.'
    'Мужики довольно загомонили, вставая из-за стола. Видя их разбойные морды и обстановку вы явственно поняли, последствия будут весьма серьёзными.'
    menu:
        'Отчаянно сопротивляться':
            if 'woman' in player.getBodyPart().id:
                show expression 'images/events/basic/steal_punish_rape_2.png' at center,top as tempPic
            else:
                show expression 'images/events/basic/steal_punish_rape_3.png' at center,top as tempPic
            $ player.setHP(1)
            show expression 'images/events/city_entry/run_catch.png' at center,top as tempPic
            'Вы попытались убежать, но вас грубо схватили и доставили в центр комнаты. Проигрывая  в силе и не имея ни малейших шансов на успех, вы начали истошно кричать, биться, пустили в ход ногти, зубы, кулаки и ноги. Сперва вас били умеренно, ладонями по лицу и несильными тычками кулаков в тело. Затем, после нескольких ваших удачных попаданий, окружающие рассвирепели. Начали сыпаться очень сильные и мощные удары, от которых вы не могли должным образом защититься. Вскоре, вы в полубеспамятстве лежали на полу, не в силах пошевелиться.'
            if rand(1,2) == 1:
                if 'woman' in player.getBodyPart().id:
                    show expression 'images/events/basic/steal_punish_rape_5.png' at center,top as tempPic
                else:
                    show expression 'images/events/basic/steal_punish_rape_4.png' at center,top as tempPic
                'Несмотря на страшные последствия вашего сопротивления, оно всё же имело успех. Разбойники не стали насиловать ваше полумёртвое тело и выбросили прочь, подальше от своего дома. Неизвестно сколько вы валялись в кустах, покуда не пришли в себя и не смогли подать голос. Вскоре вас нашли. Добрые люди и помогли добраться до жилья, напоив целебным травами.'
            else:
                show expression 'images/events/basic/steal_punish_rape_7.png' at center,top as tempPic
                'Вас всё же изнасиловали, но вы при этом почти ничего не помнили, пребывая в беспамятстве. Вас грубо трахали, по очереди загоняя свои немытые херы в ваше полумёртвое тело.  При этом вы неподвижно лежали на спине, не зная, в каком мире находитесь.'
                show expression 'images/events/basic/steal_punish_rape_6a.png' at center,top as tempPic
                'Затем разбойники посчитали, что стоит избавиться  от вас покуда вы ещё живы. Вас выбросили прочь, подальше от своего дома. Неизвестно сколько вы валялись в кустах, покуда не пришли в себя и не смогли подать голос, призывая на помощь. Вскоре вас нашли. Добрые люди и помогли добраться до жилья, напоив целебным травами. Вы не знали, стоило ли тогда сопротивляться, ведь всё равно над вашим телом совершили гнусное насилие. Но, во-первых,  вы могли чувствовать гордость за своё поведение, а во-вторых, вы ощущали, что смогли избежать куда более страшной участи.'
                $ changetime(3*24*60)
                $ trigger[9] = ptime + 24
                $ getLocation('tavern').getDoor('tavernDoor1').lock(False)
                $ curloc = getLocation('freeRoom')
                jump sleep
        'Помолчать':
            show expression 'images/events/basic/steal_punish_rape_8.png' at center,top as tempPic
            'С вас тут же сорвали платье и бросили на лежанку. Первый, по-видимому, вожак, сел сверху и сильно сжал груди, выкручивая нежные соски. От боли ваше сознание едва не помутилось. К счастью вожак, немного позабавившись с сосками и дав несколько пощечин, перешёл к удовлетворению своей похоти.'
            show expression 'images/events/basic/steal_punish_rape_9.png' at center,top as tempPic
            'Грубо схватив вас за бёдра, он вогнал на всю длину свой немалый член и начал активно им орудовать, комментируя похабным словами узость вашей щелки.'
            'Выстрелив вам внутрь порцией семени, он уступил место второму, который также удовлетворился прежней позой. На третьем вы едва сдерживались от боли, долгое насилие дало свои плоды – лоно начало сильно болеть от грубых толков. Четвертый разбойник дал покой вашему лону, но вы бы предпочли продолжение предыдущих действий той мерзости, которую он задумал.'
            show expression 'images/events/basic/steal_punish_rape_10.png' at center,top as tempPic
            'Вас поставили на колени и повернули задом, велев нагнуться вперед и уткнуться лицом в лежак. Вы так и не поняли его истинных намерений, даже увидев, как он смазывает чем-то член, пока горячая головка не тыкнула в вашу попу, совсем не туда, куда было принято сношать естественным образом. Насильник велел, подкрепив это несколькими ударами, свести ноги и выпятить задницу. Осознав его намерения, вы надеялись, что его член не пробьёт  себе дорогу, но …'
            show expression 'images/events/basic/steal_punish_rape_11.png' at center,top as tempPic
            player.say 'О Боже!!!'
            'Вы зашлись от крика, чувствуя как раскаленный прут вгоняют внутрь вашего седалища. Боль была ужасающей, сотоварища насильника даже пришлось крепко держать ваше тело. Слезы брызгали с глаз, вы истошно кричали, но насильник неумолимо, раз за разом пытался всё глубже приникнуть членом внутрь. Наконец он зашёл достаточно, по его мнению, глубоко и начал активные движения, вызывающие у вас страшную боль. К счастью, узость отверстия дала вам не только боль, но и ускоренное окончание мерзкого процесса. Вы почувствовали, как внутрь вылилось горячее семя, член обмяк и пытка завершилась.'
            show expression 'images/events/basic/steal_punish_rape_12.png' at center,top as tempPic
            'Однако на спину вас не вернули. Один из разбойников сунул вам член в рот, второй пристроился сзади но, к счастью, воспользовался привычным вратами. Вы покорно работали устами и двигали бедрами, покуда две порции семени не увенчали ваши усилия, одна из них оказалась размазанной по вашему лицу и волосам. Последнего из насильников вы почти не чувствовали, он без изысков уложил вас на спину и вдоволь натешился вашим полумертвым от боли и усталости телом.'
            show expression 'images/events/basic/steal_punish_rape_13.png' at center,top as tempPic
            'Вас бросили в подвал, где вы обессилено свалились на жесткий топчан. Вскоре, оказавшись в полной тьме, ход времени для вас замедлился.'
            $ player.setHP(1)
            'Последующие дни провретились в один нескончаемый кошмар. Вас избивали, трахали без остановки вдвоём, втроём и даже вчетвером. Вы и представить раньше не могли, что сможете удовлетворить такое количество мужчин одновременно. Питались вы исключительно тем, что смогли высосать из неутомимых херов своих пленителей. Но всё рано или поздно кончается...'
            if rand(1,2) == 1:
                show expression 'images/events/basic/steal_punish_rape_6a.png' at center,top as tempPic
                'Разбойники посчитали, что стоит избавиться  от вас покуда вы ещё живы. Вас выбросили прочь, подальше от своего дома. Неизвестно сколько вы валялись в кустах, покуда не пришли в себя и не смогли подать голос, призывая на помощь. Вскоре вас нашли. Добрые люди и помогли добраться до жилья, напоив целебным травами.'
                $ changetime(3*24*60)
                $ trigger[9] = ptime + 24
                $ getLocation('tavern').getDoor('tavernDoor1').lock(False)
                $ curloc = getLocation('freeRoom')
                jump sleep
            else:
                jump badEnd2

label badEnd2:
    show expression 'images/events/basic/steal_punish_room.png' at center,top as bgPic
    show expression 'images/events/basic/badEnd2_1.png' at center,top as tempPic
    'Наступил день когда вас, наконец, достали из подвала. Вы уже было обрадовались, но радость оказалась преждевременной. Никто не собирался вас отпускать. Более того, вас продали торговцу рабами. Ваша мольба, уговоры, обещания денег ни к чему не привели, кроме наказания плеткой. Ваше будущее было предопределено.'
    show expression 'images/events/basic/badEnd2_back_1.png' at center,top as bgPic
    show expression 'images/events/basic/steal_punish_whip_2.png' at center,top as tempPic
    'Конечно, содержание вас в рабстве было незаконным, но кого волновали юридические тонкости. Уже спустя три дня вы были в море, вдали от власти Короля. Спустя же два месяца вы стояли голой на рынке рабов. Два дня позора и вас приобрел по сходной цене наставник школы рабынь, занимающийся обучением товара для богатых домов. За следующие три месяца вас плетью, голодом и изощренными пытками приучили к полному повиновению, обучили всем необходимым для рабыни знаниям и продали во дворец местного бея. Единственным вашим утешением была возможность стать любимой наложницей бея, и занять высокое место в гаремное иерархии.'
    show expression 'images/events/basic/badEnd2_back_1.png' at center,top as bgPic
    show expression 'images/events/basic/badEnd2_2.png' at center,top as tempPic
    'И это вам частично удалось. Господин обратил на вас внимание и несколько раз дозволил усладить в постели, похвалив ваше тело и умение им пользоваться в танцах и любви. К несчастью, вскоре его призвал падишах и вернулся он только через полгода. После этого он и не вспомнил о вас.'
    show expression 'images/events/basic/badEnd2_3.png' at center,top as tempPic
    'Хотя, если бы и вспомнил об одной из сотни рабынь своего дворца, то к тому времени вы уже надежно покоились на дне моря в мешке. По указанию ревнивой старшей жены бея, несколько приближенных рабынь задушили ночью бледную выскочку, а евнухи утопили тело в море.  Обычная участь для смазливой невольницы, возомнившей себя новой жемчужиной гарема.'
    $ renpy.quit()
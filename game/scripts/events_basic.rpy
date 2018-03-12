label steal_decline:
    show expression curloc.image at center,top as bgPic
    show expression 'images/events/basic/decline.png' at center,top as tempPic
    player.say '{color=#fff782}Мне не стоит воровать в этом месте.'
    $ move(curloc)
    
label trap_simpleTrap:
    'Попалась!'
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
    if rand(1,2) == 1:
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

    else:
        'Вы действовали достаточно умело, но совершенно забыли об окружение. Один из зевак схватил вас и огласил округу криками «Вор!».'
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
                else:
                    show expression 'images/events/basic/steal_seduction_3.png' at center,top as tempPic
                    'Ваши слова ничуть не тронули грубое сердце мужчины. Ответом была лишь пощечина и напоминание, что уличным девкам не пристало подавать голос.  Вас грубо развернули лицом к телеге и сорвали платье.'
            'Намекнуть об особых удовольствиях доступных в укромном месте (соблазнение)':
                'Прильнув к мужчине, вы страстно зашептали ему на ухо всяки непристойности, обещая подарить ему незабываемые сношения без чужих глаз.'
                if isSuccess(player.useSkill('seduction'), 13, 'Соблазнение: ', exp = 50):
                    'Вы почувствовали, как в живот вам уперся стоячий член. Возбужденный вашими словами и возникающими образами, мужик грубо схватил вас за руку и потащил в переплетение улиц.'
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
    $move(curloc)
    
    
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
            $ temp = rand(5-17)
            'Из толпы зевак послышались сочувственные возгласы и слова ободрения. Люди переглядывались, у некоторых слезились глаза. Вам протянулись руки для сочувственных похлопываний, в некоторых из них были мелкие монеты. С трудом вы освободились от жалостливой толпы, попутно собрав [temp] крон подаяний.'
    else:
        if 'woman' in player.getBodyPart().id:
            show expression 'images/events/basic/steal_slap_2.png' at center,top as tempPic
        else:
            show expression 'images/events/basic/steal_slap_1.png' at center,top as tempPic
        'То ли вас окружали люди с черствыми душами, то ли ваши умения обмана были не столь велики, но вам явно не поверили. Ваши жалостливые слова прервала мощная пощечина, и вы очутились на земле с гудящей головой и немного помутненным рассудком.'
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
                
        '100 крон' if player.money >= 100:
            $ player.money -= 100
            'Мысль откупиться была первой пришедшей вам в голову. Вы решили не скупиться и предложить большую по меркам бедных людей сумму, дабы забыть о недоразумении.'
            if currChar.getSex() == 'male':
                'Хозяин кошелька радостно кивнул. Ради таких денег можно было забыть о мести вору. Вы быстро расплатились и бросились прочь.'
            else:
                'Хозяйка кошелька радостно кивнула. Ради таких денег можно было забыть о мести вору. Вы быстро расплатились и бросились прочь.'
                
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
    $ move(curloc)
    
label steal_escapeDEX:
    show expression curloc.image at center,top as bgPic
    if 'woman' in player.getBodyPart().id:
        show expression 'images/events/basic/steal_escapeDEX_1.png' at center,top as tempPic
    else:
        show expression 'images/events/basic/steal_escapeDEX_2.png' at center,top as tempPic
    'Вы с прирожденной ловкостью освободили руку от неумелого захвата и бросились прочь. Несколько зевак сделали было неуклюжие попытки вас перехватить, но вы легко их обошли и исчезли с глаз.'
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
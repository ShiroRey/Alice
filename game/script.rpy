﻿# Вы можете расположить сценарий своей игры в этом файле.
# Определение персонажей игры.
define a = Character('Алиса', color="#ffffff")

define me = Character('[name]', color="#ffffff")

define father = Character('Отец', color="#ffffff")

define inc = Character('Инквизитор', color="#ffffff")

define unc = Character('Неизвестный голос', color="#ffffff")

style test_style:
    color "#b3000f"

# Вместо использования оператора image можете просто
# складывать все ваши файлы изображений в папку images.
# Например, сцену bg room можно вызвать файлом "bg room.png",
# а eileen happy — "eileen happy.webp", и тогда они появятся в игре.

# Игра начинается здесь:

# Логотип в начале(Доделать)
label splashscreen:
    scene black with Dissolve(1.0)
    pause 0.5

    scene logo2 with Dissolve(1.5)
    pause 0.5

    scene black with Dissolve(1.0)
    pause 0.5

    return


#label shiza:
#    play sound "horror.mp3" loop 
#    scene eyes with Dissolve(3.5)
#    "{sc}{=test_style}ТЕКСТ{/=test_style}{/sc}"

label start:
    stop music
    scene black with Dissolve(1.5)
    play sound "typewriter.mp3" fadeout 0.0 fadein 2.0
    "XVII век."
    stop sound fadeout 2.0
    
    play music "hor.mp3" fadeout 0.0 fadein 2.0
    scene ink with Dissolve(1.5)
    "Инквизиция была организацией, чьей главной целью являлась борьба с черной магией и ересью, ведущая массовые расследования и проведение судебных процессов во времена Средневековья."
    "Это был темный период в истории, когда люди считали, что ведьмы и колдуны обладают сверхъестественными способностями и могут приносить бедствие в общество."
    
    stop music fadeout 2.0
    scene villagegg with Dissolve(1.5)
    python:
        name = renpy.input("Меня зовут...")
        name = name.strip()
    

    "Я был всего лишь обычным парнем, выросшим среди деревенских дорог, далеко от блеска столицы."
    "С течением лет, как тяжелый туман, депрессия поглотила мою душу. Всё становилось темным, как будто тени одиночества поглотили меня, оставив за собой лишь тусклый свет."
    play sound "horror.mp3" loop fadeout 0.0 fadein 2.0
    scene eyes with Dissolve(3.5)
    "{sc}{=test_style}Почему моя боль и тоска были невидимы для тех, кто меня окружал?{/sc}"
    scene black with Dissolve(.5)
    stop sound fadeout 2.0

    scene villagegg with Dissolve(1.5)
    "Так прошли двадцать лет моей жизни, как серая река времени, но их течение было медленным, тяжелым, будто душа моя была заключена в мраке..."
    scene housegg with Dissolve(.5)
    "После заключительных звонков в воскресной школе, отец, используя свои связи, направил меня в инквизицию."

    show father
    father "Ты завтра вступаешь в должность инквизитора, это не обсуждается."
    "В тот момент мне было всё равно, чем заниматься, и я бездумно согласился."
    me "Да, отец..."
    scene black with Dissolve(.5)
    "Но..."
    "Я ошибался."
    "Среди теней инквизиции, я осознал, что эта 'работа' была явно не тем, чем я хотел заниматься."
    scene reznya
    "Мне приходилось убивать множество людей, и, возможно, многие из них были невиновными в тех обвинениях, которые им назначила церковь."
    "Но мои руки были связаны, ибо отступление было смертельным грехом — мне грозило оказаться в числе еретиков, чьи костры уже были зажжены."
    "Поэтому я смирился."
    scene black with Dissolve(.5)
    "Нет."
    "Мне пришлось смириться."
    play music povozka loop fadeout 0.0 fadein 2.0
    scene povozka with Dissolve(.5)
    "Сегодня поступил 'заказ'."
    inc "[name], мы должны поймать девушку из одной деревни примерно в двух днях пути отсюда, о ней начали разносится странные слухи среди соседей."
    inc "Странный цвет глаз и волос стали поводом для нашего приезда сюда. Мы должны найти ее сегодня, завтра утром ее уже не должно существовать."
    inc "Ты понял?"
    "Как жестоко"
    "И даже при всей нелепости этих слухов, мы вынуждены отправляться в такую дыру."
    me "*Вздох* Надоело..."
    inc "Я бы на твоем месте не говорил таких слов при остальных, на этот раз я закрою глаза."
    inc "Но следующего раза не будет."
    me "Да, я понял, извините."
    stop music fadeout 2.0


    scene black with Dissolve(.5)
    centered "{fi=1-1-1}Два дня спустя...{/fi}"


    scene villagea with Dissolve(.5)
    me "Наконец то мы приехали, ехать в этой повозке невозможно."
    inc "Хватит жаловаться. Найди дом этой девчонки и оповести их семью что завтра утром пройдет сожжение."
    inc "Мы с остальными будем подготавливать площадь."
    me "Ладно ладно. Пойду искать ее дом."

    scene black with Dissolve(.5)
    centered "{fi=1-1-1}Пару часов спустя...{/fi}"

    scene door1 with Dissolve(.5)
    "Так, это вроде бы тот дом..."
    play sound stuk 
    me "Есть кто дома?"
    unc "Секунду!"
    scene door2 with Dissolve(.5)
    scene houseainside with Dissolve(.5)
    show alicen with Dissolve(.5)
    a "Здравствуйте, вы к кому?"
    me "Это вы Алиса Грей?" #Фамилия под вопросом
    a "Да, это я. Вы что то хотели?"
    me "Меня зовут [name]. Я обращаюсь к вам от имени святой инквизиции, вы обвиняетесь в ереси, и должны предстать перед святым судом инквизиции и очистить свои грехи."
    show alices with Dissolve(.5)
    a "Что..."
    a "НО Я НИЧЕГО НЕ ДЕЛАЛА!"
    me "У церкови другое мнение на этот счет."
    me "У вас есть время до завтрашнего утра. Советую попрощаться с родными..."
    me "Утром мы придем за вами. До свидания."
    scene door1 with Dissolve(.5)
    me "*Вздох*"











#$ visited_pier = False
#$ visited_square = False
#label menu_cross:
#menu:
#    "Куда мне идти?"
#    "На пристань":
#        if visited_pier:
#            me "Я здесь уже был..."
#        else:
#            scene
#            me "Никого нет"
#            $ visited_pier = True
#        jump menu_cross
#    "В поле":
#        me "Похоже она где то здесь"
#        jump final_prolg
#    "На площадь":
#        if visited_square:
#            me "Я здесь уже был..."
#        else: 
#            scene
#            me "Не думаю что она придет сюда, ведь завтра здесь ее должны казнить"
#            $ visited_square = True
#        jump menu_cross


#ПОТОМ
#label final_prolg:
#    play music "rain.mp3" fadein 1
#    scene field2 with Dissolve(.5)
#    "Как она собралась убежать в такую погоду?"
#    ""

#label village_prolog:
#    play music "birds.mp3" fadein 1 
#    scene village_prolog with Dissolve(.5)
#       
#    "Алиса была молодой, но решительной девушкой. Она была красивой, с благородными чертами лица, белыми волосами и красными глазами."
#    show alice at center with Dissolve(.5)
#    "Алиса росла в заботливой семье, родители всегда старались создавать для нее уют и радость."
#    "Они придавали большое значение образованию и опыту, и поэтому Алиса была образованной и любознательной."
#    "Она умела читать и писать, она любила исследовать окружающий мир и мечтала о приключениях."
#    "В свои шестнадцать лет она еще не знала больших проблем и не понимала суровости мира."
#    "Пока {cps=15}{color=#8B0000}ИНКВИЗИЦИЯ{/color}{/cps} не явилась в ее деревню."
#    stop music fadeout 1
#
#    scene black with Dissolve(1.5)
#
#    scene bed with Dissolve(1.5)
#    show alice at center with Dissolve(.5)
#    play music "sad.mp3" fadein 1
#    "Вместо того чтобы поддаться страху или позволить инквизиции убить ее без борьбы, Алиса решила сбежать."
#    "Она знала, что это будет опасно, но она была готова рискнуть, чтобы спасти свою жизнь и сохранить надежду на будущее."
#    "Алиса рассказала родителям об обвинениях инквизиции и своем решении бежать из деревни."
#    "Ее родители были отчаянно обеспокоены за свою дочь."
#    "Они знали, что она была невиновна, но знаки и обвинения инквизиции сделали ситуацию очень опасной для них и для Алисы."
#    "Они решили поддержать дочь в ее попытке сбежать, хотя и знали, что это означает их расставание на неопределенное время."
#    scene black with Dissolve(0.5)
#    "Этим же вечером Алиса собрала свои вещи и ушла из деревни..."
#    stop music fadeout 1


#label first_act:
#    scene black
#    "{fi=1-1-1}Воспоминания потеряны...{/fi}"
#    scene winter_forest with Dissolve(.5)
#    
#
#
#    scene black with Dissolve(0.5)
#    "{sc}{=test_style}Забавно{/=test_style}{/sc}"
#    scene winter_forest with Dissolve(0.5)
#
#    scene hunter_house with Dissolve(0.5)








label end:
    python:
        end = renpy.input("restart?")
    scene black
    if end == 'y':
        jump start
    else:
        return

    

transform flip:
    xalign 0.5
    yalign 1.0
    linear 1.0 xalign 0.0
    xzoom -1.0

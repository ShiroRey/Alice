﻿# Вы можете расположить сценарий своей игры в этом файле.

# Определение персонажей игры.
define a = Character('Алиса', color="#bb0028")

define me = Character('[name]', color="#c8f4ff")

# Вместо использования оператора image можете просто
# складывать все ваши файлы изображений в папку images.
# Например, сцену bg room можно вызвать файлом "bg room.png",
# а eileen happy — "eileen happy.webp", и тогда они появятся в игре.

# Игра начинается здесь:
label start:

    scene black with Dissolve(1.5)
    "XVII век." 
    
    scene ink with Dissolve(1.5)
    play music "hor.mp3" fadein 1
    "Инквизиция была организацией, чьей главной целью являлась борьба с черной магией и ересью, ведущая массовые расследования и проведение судебных процессов во времена Средневековья."
    "Это был темный период в истории, когда люди считали, что ведьмы и колдуны обладают сверхъестественными способностями и могут приносить бедствие в общество."
    
    python:
        name = renpy.input("Меня зовут...")
        name = name.strip() 
    "Я был обычным парнем который рос в деревне далеко от столицы."
    "С возрастом пелена депрессии постепенно окутывала мою душу. Я никогда не мог понять, почему мое окружение не видело моей настоящей боли и одиночества. "
    "Я скрывал свои эмоции за маской 'обычного' парня, улыбаясь и веселясь наружу, чтобы удовлетворять общественные нормы."
    "Так и прошли мои 20 лет..."
    scene ink2 with Dissolve(.5)
    "После того как я закончил обучение в воскресной школе, отец по связям устроил меня в инквизицию."
    "К этому моменту моей жизни мне уже было все равно чем заниматься, поэтому я согласился."
    "Со временем я понял что эта работа не по мне, мне приходилось убивать много людей, скорее всего многие из них даже не были виновны в тех обвинениях, которые им присваиивали."
    "Но ослушаться приказа я не мог, иначе я бы оказался на месте еретиков и меня бы сразу же сожгли на костре."
    scene black with Dissolve(.5)
    "Сегодня мы должны поймать одну девушку из небольшой деревни, соседи говорят что у нее странный цвет глаз и волос.
    Даже из за таких пустяковых слухов мы должны ехать куда то в глубинку."
    me "*Вздох* Надоело..."

    scene village_after with Dissolve(.5)
    me "Хмм, вроде они живут где то тут."
    "Я должен оповестить ее семью что сожжение пройдет завтра утром перед площадью."
    "*Тук* *Тук* *Тук*"
    me "Есть кто дома?"
    "*Тишина*"
    scene black with Dissolve(.5)
    me "*Вздох* Неужели сбежала?"
    "Нужно найти ее, иначе останусь без денег..."



    menu:
        me "Куда мне идти?"
        "На пристань":
            me "Никого нет"
            call start

        "В поле":
            me "Похоже она где то здесь"
            jump village_prolog

        "На площадь":
            me "Не думаю что она придет сюда, ведь здесь ее должны казнить"
            call start
            


label village_prolog:
    play music "birds.mp3" fadein 1
    scene village_prolog with Dissolve(.5)

    "Алиса была молодой, но решительной девушкой. Она была красивой, с благородными чертами лица, белыми волосами и красными глазами."
    show al_happy at center with Dissolve(.5)
    "Алиса росла в заботливой семье, родители всегда старались создавать для нее уют и радость."
    "Они придавали большое значение образованию и опыту, и поэтому Алиса была образованной и любознательной."
    "Она умела читать и писать, она любила исследовать окружающий мир и мечтала о приключениях."
    "В свои шестнадцать лет она еще не знала больших проблем и не понимала суровости мира."
    "Пока {cps=10}{color=#8B0000}ИНКВИЗИЦИЯ{/color}{/cps} {cps=20}не явилась в ее деревню.{/cps}"
    stop music fadeout 1

    scene black with Dissolve(1.5)

    scene bed with Dissolve(1.5)
    show al_angry at center with Dissolve(.5)
    play music "sad.mp3" fadein 1
    "Вместо того чтобы поддаться страху или позволить инквизиции убить ее без борьбы, Алиса решила сбежать."
    "Она знала, что это будет опасно, но она была готова рискнуть, чтобы спасти свою жизнь и сохранить надежду на будущее."
    "Алиса рассказала родителям об обвинениях инквизиции и своем решении бежать из деревни."
    "Ее родители были отчаянно обеспокоены за свою дочь."
    "Они знали, что она была невиновна, но знаки и обвинения инквизиции сделали ситуацию очень опасной для них и для Алисы."
    "Они решили поддержать дочь в ее попытке сбежать, хотя и знали, что это означает их расставание на неопределенное время."
    scene black with Dissolve(0.5)
    "Этим же вечером Алиса собрала свои вещи и ушла из деревни..."
    stop music fadeout 1

    scene black with Dissolve(1.5)
    scene field2 with Dissolve(1.5)
    show al_angry at flip with Dissolve(1.5)
    play music "rain.mp3" fadein 1
    "Она стремились оставаться незаметной и шла в удаленные и заброшенные места, где она могла скрыться от инквизиции."
    "Но у нее была надежда на то, что рано или поздно она сможет доказать свою невиновность и вернуться к обычной жизни."
    scene black with Dissolve(0.5)

style test_style:
    color "#77001e"

label village_after:
    scene black with Dissolve(0.5)
    "{sc}{=test_style}Что ты тут забыл?{/=test_style}{/sc}"
    scene winter_forest with Dissolve(0.5)

    scene hunter_house with Dissolve(0.5)



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

## Вы можете расположить сценарий своей игры в этом файле.
#
## Определение персонажей игры.
#define a = Character('Алиса', color="#c8ffc8")
#
#define me = Character('[name]', color="#c8f4ff")
#
## Вместо использования оператора image можете просто
## складывать все ваши файлы изображений в папку images.
## Например, сцену bg room можно вызвать файлом "bg room.png",
## а eileen happy — "eileen happy.webp", и тогда они появятся в игре.
#
## Игра начинается здесь:
#label start:
#
#    play music "room1.mp3"
#
#    scene bg room
#
#    show alisa
#    
#
#    a "Привет, меня зовут Алиса."
#
#    a "А как зовут тебя?"
#    python:
#        name = renpy.input("Введите своё имя")
#
#    a "[name]? хмм, интересное имя"
#
#
#transform left_to_right:
#    xzoom -1.0
#    xalign 0.50
#    linear 1.0 xalign 0.0
#
#label cont:
#    show alisa at left_to_right
#    with Dissolve(.25)
#    a "Может прогуляемся, [name]?"
#    
#    menu :
#        me "Стоит ли мне согласиться?"
#
#        "Да":
#            me "Хорошо, давай прогуляемся."
#            jump yeah
#
#        "Нет":
#            me "Извини, я не хочу сегодня гулять."
#            jump nah
#
#    label yeah:
#        a "Ура! Пошли скорее"
#        scene black
#        "Мы долго гуляли на улице и хорошо провели время."
#        jump prod
#
#    label nah:
#        "Я решил остаться дома."
#        jump prod
#
#label prod:
#    "Наступил вечер. . ."
#
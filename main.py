def on_forever():
    music.play_melody("G C5 A F E F F C5 ", 174)
basic.forever(on_forever)

def on_button_pressed_a():
    global random_num
    random_num = randint(0, 100)
    basic.show_number(random_num)
    if random_num < 50:
        basic.show_string("Oop, sorry!")
    else:
        basic.show_string("Great!")
input.on_button_pressed(Button.A, on_button_pressed_a)

random_num = 0
basic.show_string("LIFE GOALS METER")
basic.show_string("Welcome")
basic.pause(200)
basic.show_string("Press A to see the % chance for achieving your goals")
basic.show_icon(IconNames.HAPPY)


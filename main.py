code = 0
basic.show_string("Welcome.")
def on_button_pressed_a():
    global code
    for index in range(4):
        random_num = randint(1, 5)
    if random_num == 1:
        basic.show_icon(IconNames.MEH)
        code = 12121
    if random_num == 2:
        basic.show_icon(IconNames.SURPRISED)
        code = 2220
    if random_num == 3:
        basic.show_icon(IconNames.TRIANGLE)
        code = 12221
    if random_num == 4:
        basic.show_icon(IconNames.SCISSORS)
        code = 44122
    if random_num == 5:
        basic.show_icon(IconNames.CHESSBOARD)
        code = 23232
input.on_button_pressed(Button.A, on_button_pressed_a)




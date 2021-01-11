let code = 0
basic.showString("Welcome.")
input.onButtonPressed(Button.A, function on_button_pressed_a() {
    let random_num: number;
    
    for (let index = 0; index < 4; index++) {
        random_num = randint(1, 5)
    }
    if (random_num == 1) {
        basic.showIcon(IconNames.Meh)
        code = 12121
    }
    
    if (random_num == 2) {
        basic.showIcon(IconNames.Surprised)
        code = 2220
    }
    
    if (random_num == 3) {
        basic.showIcon(IconNames.Triangle)
        code = 12221
    }
    
    if (random_num == 4) {
        basic.showIcon(IconNames.Scissors)
        code = 44122
    }
    
    if (random_num == 5) {
        basic.showIcon(IconNames.Chessboard)
        code = 23232
    }
    
})

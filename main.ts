input.onButtonPressed(Button.A, function () {
    random_num = randint(0, 100)
    basic.showNumber(random_num)
    if (random_num < 50) {
        basic.showString("Oop, sorry!")
    } else {
        basic.showString("Great!")
    }
})
let random_num = 0
basic.showString("LIFE GOALS METER")
basic.showString("Welcome")
basic.pause(200)
basic.showString("Press A to see the % chance for achieving your goals")
basic.showIcon(IconNames.Happy)

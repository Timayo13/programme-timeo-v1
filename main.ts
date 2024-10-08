input.onSound(DetectedSound.Loud, function () {
    music.stopAllSounds()
})
input.onButtonPressed(Button.A, function () {
    basic.showString("Arrete !")
})
input.onButtonPressed(Button.B, function () {
    basic.showString("Au revoir")
})
input.onGesture(Gesture.Shake, function () {
    music.play(music.stringPlayable("C5 B A G F E D C ", 140), music.PlaybackMode.UntilDone)
})
basic.showLeds(`
    # # # . .
    # . . # .
    # . # . .
    # . . # .
    # # # . .
    `)
basic.showLeds(`
    # # # # #
    # . . . #
    # . . . #
    # . . . #
    # # # # #
    `)
basic.showLeds(`
    # . . . #
    # # . . #
    # . # . #
    # . . # #
    # . . . #
    `)
basic.showLeds(`
    # # # # #
    . . # . .
    . . # . .
    # . # . .
    # # # . .
    `)
basic.showLeds(`
    # # # # #
    # . . . #
    # . . . #
    # . . . #
    # # # # #
    `)
basic.showLeds(`
    # . . . #
    # . . . #
    # . . . #
    # . . . #
    # # # # #
    `)
basic.showLeds(`
    # # # # #
    # . . # .
    # . # . .
    # . . # .
    # . . . #
    `)
basic.showIcon(IconNames.EighthNote)
basic.forever(function () {
	
})

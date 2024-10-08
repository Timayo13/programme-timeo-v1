def on_sound_loud():
    music.stop_all_sounds()
input.on_sound(DetectedSound.LOUD, on_sound_loud)

def on_button_pressed_a():
    basic.show_string("Arrete !")
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_b():
    basic.show_string("Au revoir")
input.on_button_pressed(Button.B, on_button_pressed_b)

def on_gesture_shake():
    music.play(music.string_playable("C5 B A G F E D C ", 140),
        music.PlaybackMode.UNTIL_DONE)
input.on_gesture(Gesture.SHAKE, on_gesture_shake)

basic.show_leds("""
    # # # . .
    # . . # .
    # . # . .
    # . . # .
    # # # . .
    """)
basic.show_leds("""
    # # # # #
    # . . . #
    # . . . #
    # . . . #
    # # # # #
    """)
basic.show_leds("""
    # . . . #
    # # . . #
    # . # . #
    # . . # #
    # . . . #
    """)
basic.show_leds("""
    # # # # #
    . . # . .
    . . # . .
    # . # . .
    # # # . .
    """)
basic.show_leds("""
    # # # # #
    # . . . #
    # . . . #
    # . . . #
    # # # # #
    """)
basic.show_leds("""
    # . . . #
    # . . . #
    # . . . #
    # . . . #
    # # # # #
    """)
basic.show_leds("""
    # # # # #
    # . . # .
    # . # . .
    # . . # .
    # . . . #
    """)
basic.show_icon(IconNames.EIGHTH_NOTE)

def on_forever():
    pass
basic.forever(on_forever)

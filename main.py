def on_received_number(receivedNumber):
    global Bluetooth
    Bluetooth = False
    basic.clear_screen()
    basic.show_string("" + str((receivedNumber)))
    music.play_melody("C5 B A G G F E D ", 120)
radio.on_received_number(on_received_number)

def on_button_pressed_a():
    global Red_Wizard, Play_Game, Blue_Wizard, Bluetooth
    Red_Wizard = 1
    radio.set_group(1)
    radio.send_string("LOL")
    radio.send_number(1)
    Play_Game = 0
    Blue_Wizard = 0
    Bluetooth = True
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_ab():
    global Play_Game, Blue_Wizard, Red_Wizard, Bluetooth
    Play_Game = 1
    Blue_Wizard = 0
    Red_Wizard = 0
    Bluetooth = True
input.on_button_pressed(Button.AB, on_button_pressed_ab)

def on_received_string(receivedString):
    global Bluetooth
    Bluetooth = False
    basic.clear_screen()
    basic.show_string(receivedString)
radio.on_received_string(on_received_string)

def on_button_pressed_b():
    global Blue_Wizard, Red_Wizard, Play_Game, Bluetooth
    Blue_Wizard = 1
    radio.set_group(2)
    radio.send_number(2)
    Red_Wizard = 0
    Play_Game = 0
    Bluetooth = True
input.on_button_pressed(Button.B, on_button_pressed_b)

def Radio():
    while Red_Wizard:
        radio.set_group(1)
    while Blue_Wizard:
        radio.set_group(2)
Blue_Wizard = 0
Play_Game = 0
Red_Wizard = 0
Bluetooth = False
radio.set_group(0)
basic.show_string("HI")
basic.clear_screen()
Bluetooth = True

def on_forever():
    if Red_Wizard:
        while Red_Wizard:
            if Bluetooth:
                basic.show_leds("""
                    . # # . .
                                        . # . # .
                                        . # # . .
                                        . # . # .
                                        . # . . #
                """)
            break
    elif Play_Game:
        while Play_Game:
            if Bluetooth:
                basic.show_icon(IconNames.PITCHFORK)
            break
    elif Blue_Wizard:
        while Blue_Wizard:
            if Bluetooth:
                basic.show_leds("""
                    . # # . .
                                        . # . # .
                                        . # # . .
                                        . # . # .
                                        . # # . .
                """)
            break
    else:
        pass
basic.forever(on_forever)

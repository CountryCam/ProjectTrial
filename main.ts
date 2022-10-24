radio.onReceivedNumber(function on_received_number(receivedNumber: number) {
    
    Bluetooth = false
    basic.clearScreen()
    basic.showString("" + ("" + receivedNumber))
    music.playMelody("C5 B A G G F E D ", 120)
})
input.onButtonPressed(Button.A, function on_button_pressed_a() {
    
    Red_Wizard = 1
    radio.setGroup(1)
    radio.sendString("LOL")
    radio.sendNumber(1)
    Play_Game = 0
    Blue_Wizard = 0
    Bluetooth = true
})
input.onButtonPressed(Button.AB, function on_button_pressed_ab() {
    
    Play_Game = 1
    Blue_Wizard = 0
    Red_Wizard = 0
    Bluetooth = true
})
radio.onReceivedString(function on_received_string(receivedString: string) {
    
    Bluetooth = false
    basic.clearScreen()
    basic.showString(receivedString)
})
input.onButtonPressed(Button.B, function on_button_pressed_b() {
    
    Blue_Wizard = 1
    radio.setGroup(2)
    radio.sendNumber(2)
    Red_Wizard = 0
    Play_Game = 0
    Bluetooth = true
})
function Radio() {
    while (Red_Wizard) {
        radio.setGroup(1)
    }
    while (Blue_Wizard) {
        radio.setGroup(2)
    }
}

let Blue_Wizard = 0
let Play_Game = 0
let Red_Wizard = 0
let Bluetooth = false
radio.setGroup(0)
basic.showString("HI")
basic.clearScreen()
Bluetooth = true
basic.forever(function on_forever() {
    if (Red_Wizard) {
        while (Red_Wizard) {
            if (Bluetooth) {
                basic.showLeds(`
                    . # # . .
                                        . # . # .
                                        . # # . .
                                        . # . # .
                                        . # . . #
                `)
            }
            
            break
        }
    } else if (Play_Game) {
        while (Play_Game) {
            if (Bluetooth) {
                basic.showIcon(IconNames.Pitchfork)
            }
            
            break
        }
    } else if (Blue_Wizard) {
        while (Blue_Wizard) {
            if (Bluetooth) {
                basic.showLeds(`
                    . # # . .
                                        . # . # .
                                        . # # . .
                                        . # . # .
                                        . # # . .
                `)
            }
            
            break
        }
    } else {
        
    }
    
})

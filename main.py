def on_button_pressed_a():
    motor.motor_stop_all()
    music.play(music.builtin_playable_sound_effect(soundExpression.happy),
        music.PlaybackMode.IN_BACKGROUND)
    basic.show_icon(IconNames.YES)
    motor.motor_run(motor.Motors.M1, motor.Dir.CW, 50)
    motor.motor_run(motor.Motors.M2, motor.Dir.CW, 50)
    motor.motor_run(motor.Motors.M3, motor.Dir.CW, 50)
    motor.motor_run(motor.Motors.M4, motor.Dir.CW, 50)
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_gesture_tilt_left():
    motor.motor_stop_all()
    basic.show_icon(IconNames.ASLEEP)
    music.play(music.builtin_playable_sound_effect(soundExpression.giggle),
        music.PlaybackMode.IN_BACKGROUND)
input.on_gesture(Gesture.TILT_LEFT, on_gesture_tilt_left)

def on_uart_data_received():
    global cmd
    cmd = bluetooth.uart_read_until("#")
    if cmd == "F":
        basic.show_string("F")
        motor.motor_run(motor.Motors.M1, motor.Dir.CW, 120)
        motor.motor_run(motor.Motors.M2, motor.Dir.CW, 120)
        motor.motor_run(motor.Motors.M3, motor.Dir.CW, 120)
        motor.motor_run(motor.Motors.M4, motor.Dir.CW, 120)
    elif cmd == "B":
        basic.show_string("B")
        motor.motor_run(motor.Motors.M1, motor.Dir.CCW, 120)
        motor.motor_run(motor.Motors.M2, motor.Dir.CCW, 120)
        motor.motor_run(motor.Motors.M3, motor.Dir.CCW, 120)
        motor.motor_run(motor.Motors.M4, motor.Dir.CCW, 120)
    elif cmd == "S":
        basic.show_string("S")
        motor.motor_stop(motor.Motors.M1)
        motor.motor_stop(motor.Motors.M2)
        motor.motor_stop(motor.Motors.M3)
        motor.motor_stop(motor.Motors.M4)
    elif cmd == "L":
        basic.show_string("L")
        motor.motor_stop_all()
        motor.motor_run(motor.Motors.M1, motor.Dir.CW, 120)
        motor.motor_run(motor.Motors.M2, motor.Dir.CW, 120)
    elif cmd == "R":
        basic.show_string("R")
        motor.motor_stop_all()
        motor.motor_run(motor.Motors.M3, motor.Dir.CW, 120)
        motor.motor_run(motor.Motors.M4, motor.Dir.CW, 120)
bluetooth.on_uart_data_received(serial.delimiters(Delimiters.HASH), on_uart_data_received)

def on_button_pressed_b():
    basic.show_icon(IconNames.NO)
    motor.motor_stop_all()
    music.play(music.builtin_playable_sound_effect(soundExpression.sad),
        music.PlaybackMode.IN_BACKGROUND)
input.on_button_pressed(Button.B, on_button_pressed_b)

def on_logo_touched():
    motor.motor_stop_all()
    music.play(music.builtin_playable_sound_effect(soundExpression.slide),
        music.PlaybackMode.IN_BACKGROUND)
    basic.show_icon(IconNames.HAPPY)
    motor.motor_run(motor.Motors.M1, motor.Dir.CW, 100)
    motor.motor_run(motor.Motors.M2, motor.Dir.CW, 100)
    motor.motor_run(motor.Motors.M3, motor.Dir.CW, 100)
    motor.motor_run(motor.Motors.M4, motor.Dir.CW, 100)
input.on_logo_event(TouchButtonEvent.TOUCHED, on_logo_touched)

cmd = ""
music.set_volume(255)
bluetooth.start_uart_service()
music.play(music.builtin_playable_sound_effect(soundExpression.hello),
    music.PlaybackMode.IN_BACKGROUND)
basic.show_string("Hello")
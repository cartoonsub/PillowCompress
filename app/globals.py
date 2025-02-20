import time

stop_compressing = False
pause_compressing = False

def check_gui_controls() -> bool:
    if stop_compressing:
        print('Compressing stopped...')
        return False

    if pause_compressing:
        while pause_compressing:
            time.sleep(0.5)
            if stop_compressing:
                print('Compressing stopped...')
                return False

    return True

def set_stop_compressing(value: bool) -> None:
    global stop_compressing
    stop_compressing = value

def set_pause_compressing(value: bool) -> None:
    global pause_compressing
    pause_compressing = value

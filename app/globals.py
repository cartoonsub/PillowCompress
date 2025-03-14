import time

stop_compressing = False
pause_compressing = False
is_compressing = False

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

def set_is_compressing(value: bool) -> None:
    global is_compressing
    is_compressing = value

def app_is_running() -> bool:
    flag = False
    if stop_compressing or pause_compressing:
        flag = True
    return flag

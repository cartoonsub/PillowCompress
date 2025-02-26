import time

logs = {
    'processing': [],
    'error': [],
    'done': []
}

stop_compressing = False
pause_compressing = False

def set_logs(log_type: str, value: str) -> None:
    if log_type not in logs:
        print('Error: unknown log type')
        return

    logs[log_type].append(value)

def get_logs(log_type: str = None) -> dict:
    current_logs = {}
    for key, value in logs.items():
        current_logs[key] = value.copy()
        logs[key].clear()
    if not log_type:
        return current_logs

    if log_type not in current_logs:
        print('Error: unknown log type')
        return {}
    return current_logs[log_type]

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

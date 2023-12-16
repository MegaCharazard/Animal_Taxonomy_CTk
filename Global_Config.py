import os

BTN_NORMAL = "normal"
BTN_DISABLED = "disabled"

def fetch_current_directory():
    return os.path.dirname(os.path.realpath(__file__))


def centreScreen(_master,_root,_appwidth, _appheight):
    app_width = _appwidth
    app_height = _appheight

    screen_width = _root.winfo_screenwidth()
    screen_height = _root.winfo_screenheight()

    x = (screen_width/2)-(app_width/2)
    y = (screen_height/2)-(app_height/2)

    _master.geometry(f"{app_width}x{app_height}+{int(x)}+{int(y)}")

def enable_and_disable_btn(_master, _btn_name, _state):
    if _state == "disabled":
        _btn_name.configure(_master, state = "disabled")
import pgzrun
import menu, fruitshooter, coincollector

mode = menu
startup = True
pgzero_objects = {}

def setMode(_module):
    global mode
    mode = _module
    if mode != menu:
        mode.restart()

# code from https://www.reddit.com/r/pygame/comments/savzp5/multiple_files_with_pygame_zero/
def update():
    global startup, pgzero_objects
    if startup:
        pgzero_objects = {
            "images": images,
            "Actor": Actor,
            "keyboard": keyboard,
            "screen": screen,
            "keys": keys
            }
        menu.setup(pgzero_objects, setMode)
        fruitshooter.setup(pgzero_objects, setMode)
        coincollector.setup(pgzero_objects, setMode)
        startup = False

    mode.update()

def draw():
    mode.draw()

def on_mouse_down(pos):
    mode.on_mouse_down(pos)

def on_key_down(key):
    if keys.ESCAPE == key:
        if mode != menu:
            setMode(menu)
        else:
            exit()
    elif mode == menu:
        mode.on_key_down(key)

pgzrun.go()
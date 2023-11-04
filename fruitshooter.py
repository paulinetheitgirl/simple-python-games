import random
from pgzero.builtins import Actor
from pygame import Rect

fruitActors = [Actor("apple"), Actor("orange"), Actor("pineapple")]
currentFruit = random.choice(fruitActors)
textBox = Rect((20, 20), (100, 100))
score = 0
result = ""

# draw is from Pgzero
def draw():
    g = globals()
    centerWidth = g["screen"].surface.get_width()
    centerHeight = g["screen"].surface.get_height()
    g["screen"].fill("black")
    g["screen"].draw.text("Click the fruit to shoot\nScore: " +
                     str(score) +
                     "\nPress Esc to end game", topleft=(0,0), color="white")
    if result == "hit":
        g["screen"].draw.textbox("Good shot!", textBox, center=(centerWidth/2, centerHeight/2), color="green")
    elif result == "miss":
        g["screen"].draw.textbox("Try again", textBox, center=(centerWidth/2, centerHeight/2), color="orange")
    currentFruit.draw()

def place_fruit():
    global currentFruit
    currentFruit = random.choice(fruitActors)
    currentFruit.x = random.randint(20, 780)
    currentFruit.y = random.randint(20, 580)
    
# on_mouse_down is from Pgzero
def on_mouse_down(pos):
    global result, score
    result = "miss"
    if currentFruit.collidepoint(pos):
        result = "hit"
        score += 1
    place_fruit()

def update():
    pass

def unschedule():
    pass

def restart():
    global score, result
    score = 0
    result = ""
    place_fruit()

def setup(pgzero_objects, _modeFunc):
    g = globals()
    g |= pgzero_objects
    global modeFunc
    modeFunc = _modeFunc


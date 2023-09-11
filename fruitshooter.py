import pgzrun
import random
from pgzero.builtins import Actor, keyboard, keys, sounds, clock, music
from pygame import Rect

fruitActors = [Actor("apple"), Actor("orange"), Actor("pineapple")]
currentFruit = random.choice(fruitActors)
textBox = Rect((20, 20), (100, 100))
clicked = False
score = 0

# draw is from Pgzero
def draw():
    screen.fill("black")
    screen.draw.text("Click the fruit to shoot\nScore: " +
                     str(score) +
                     "\nPress Esc to end game", topleft=(0,0), color="white")
    currentFruit.draw()

def place_fruit():
    global currentFruit, clicked
    currentFruit = random.choice(fruitActors)
    currentFruit.x = random.randint(20, 780)
    currentFruit.y = random.randint(20, 580)
    clicked = False
    

# on_mouse_down is from Pgzero
def on_mouse_down(pos):
    global clicked, score
    centerWidth = screen.surface.get_width()
    centerHeight = screen.surface.get_height()
    if currentFruit.collidepoint(pos):
        clicked = True
        score += 1
    screen.clear()
    if clicked:
        screen.draw.textbox("Good shot!", textBox, center=(centerWidth/2, centerHeight/2), color="green")
    else:
        screen.draw.textbox("Try again", textBox, center=(centerWidth/2, centerHeight/2), color="orange")
    clock.schedule_unique(screen.clear, 1)
    place_fruit()

def update():
    pass

def unschedule():
    pass

def restart():
    global score
    score = 0
    place_fruit()

def setup(pgzero_objects, _modeFunc):
    g = globals()
    g |= pgzero_objects
    global modeFunc
    modeFunc = _modeFunc


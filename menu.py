import re, os
from pygame import image, transform, Color, Rect
import fruitshooter, coincollector, starrynight

GAMES = ["Fruit Shooter", "Coin Collector", "Starry Night"]
menuRects = []
backgroundImage = image.load(os.path.abspath("images/background/isis-franca-AuWSzM7kZDA-unsplash.jpg"))

# draw is from Pgzero
def draw():
    g = globals()
    global backgroundImage
    background = transform.scale(backgroundImage, g["screen"].surface.get_size())
    g["screen"].blit(background, (0, 0))
    centerWidth = g["screen"].surface.get_width() / 2
    centerHeight = g["screen"].surface.get_height() / 2
    g["screen"].draw.text("Let's play some Pygame Zero games!",
                     center=(centerWidth,centerHeight - (48 * len(GAMES))),
                     fontsize=48,
                     color="white")
    for i in range(len(GAMES)):
        menuRect = Rect((centerWidth / 2, centerHeight + (48 * i)),
                        (centerWidth, 24 + (i + 1)))
        g["screen"].draw.rect(menuRect, color="black")
        g["screen"].surface.fill(Color("limegreen"), menuRect)
        g["screen"].draw.textbox(f'{i + 1}. {GAMES[i]}', menuRect, color="white")
        menuRects.insert(i, menuRect)
    g["screen"].draw.text("Press Esc to close",
                     center=(centerWidth,centerHeight + (48 * len(GAMES))),
                     color="white")
    g["screen"].draw.text("Background image: Isis França (https://unsplash.com/@isisfra)\n" +
                     "All other images from DK Publishing\n(https://www.dk.com/uk/information/the-python-games-resource-pack/)",
                     center=(centerWidth, g["screen"].surface.get_height() - 100),
                     fontsize=24,
                     color="white")

    
# on_mouse_down is from Pgzero
def on_mouse_down(pos):
    global modeFunc, menuRects
    if menuRects[0].collidepoint(pos):
        modeFunc(fruitshooter)
    if menuRects[1].collidepoint(pos):
        modeFunc(coincollector)
    if menuRects[2].collidepoint(pos):
        modeFunc(starrynight)

def update():
    pass

def on_key_down(key):
    match = re.search(r'K_([0-9])', key.name)
    if match:
        index =int(match.group(1)) - 1
        if index in range(len(GAMES)):
            on_mouse_down((menuRects[index].x, menuRects[index].y))
    

def setup(pgzero_objects, _modeFunc):
    g = globals()
    g |= pgzero_objects
    global modeFunc
    modeFunc = _modeFunc

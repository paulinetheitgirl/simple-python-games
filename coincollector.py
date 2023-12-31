from random import randint
from pgzero.builtins import Actor, keyboard, clock

WIDTH_PX = 400
HEIGHT_PX = 400
score = 0
game_over = False
timer = 15.0

fox = Actor("fox")
fox.pos = 100, 200

coin = Actor("coin")
coin.pos = 200, 300

def draw():
    g = globals()
    g["screen"].fill("green4")
    fox.draw()
    coin.draw()
    g["screen"].draw.text("Collect the coins!\nArrow keys to move\nPress Esc to end game",
                    color="black",
                    topleft=(10, 10),
                    antialias=False)
    g["screen"].draw.text(f'Time left: {timer}\nScore: {score}',
                    color="black",
                    topright=(g["screen"].surface.get_width() - 10, 10),
                    antialias=False)
    if game_over:
        g["screen"].fill("darkorange")
        g["screen"].draw.text(f'Final score: {score}',
                         center=(WIDTH_PX, HEIGHT_PX),
                         fontsize=60)
        g["screen"].draw.text(f'Press Esc to exit',
                         center=(WIDTH_PX, HEIGHT_PX + 60))


def place_coin():
    coin.x = randint(20, (WIDTH_PX - 20))
    coin.y = randint(20, (HEIGHT_PX - 20))

def times_up():
    global game_over
    game_over = True

def update():
    global score
    
    if keyboard.left:
        fox.x -= 2
    elif keyboard.right:
        fox.x += 2
    elif keyboard.up:
        fox.y -= 2
    elif keyboard.down:
        fox.y += 2

    coin_collected = fox.colliderect(coin)

    if coin_collected:
        score += 10
        place_coin()

def unschedule():
    clock.unschedule(decTimer)
    clock.unschedule(times_up)

def decTimer():
    global timer
    timer -= 1

def setup(pgzero_objects, _modeFunc):
    g = globals()
    g |= pgzero_objects
    global modeFunc
    modeFunc = _modeFunc

def restart():
    global game_over, timer, score
    game_over = False
    timer = 15.0
    score = 0
    clock.schedule(times_up, timer)
    clock.schedule_interval(decTimer, 1)
    place_coin()


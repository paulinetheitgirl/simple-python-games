import pgzrun
from random import randint
from pgzero.builtins import Actor, keyboard, keys, sounds, clock, music

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
    screen.fill("green4")
    fox.draw()
    coin.draw()
    screen.draw.text(f'Collect the coins!\nTime left: {timer}\nScore: {score}\nPress Esc to end game',
                     color="black", topleft=(10, 10))
    if game_over:
        screen.fill("darkorange")
        screen.draw.text(f'Final score: {score}',
                         center=(WIDTH_PX, HEIGHT_PX),
                         fontsize=60)
        screen.draw.text(f'Press Esc to exit',
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

def decTimer():
    global timer
    timer -= 1

def setup(pgzero_objects, _modeFunc):
    g = globals()
    g |= pgzero_objects
    global modeFunc
    modeFunc = _modeFunc

def restart():
    global game_over, timer
    game_over = False
    timer = 15.0
    clock.schedule(times_up, timer)
    clock.schedule_interval(decTimer, 1)
    place_coin()


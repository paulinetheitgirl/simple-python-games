import random
from pgzero.builtins import animate, Actor, keys

# Pygame named colors: https://www.pygame.org/docs/ref/color_list.html
FONT_COLOR = (255, 255, 255)
WIDTH = 800
HEIGHT = 600
CENTER_X = WIDTH / 2
CENTER_Y = HEIGHT / 2
CENTER = (CENTER_X, CENTER_Y)
FINAL_LEVEL = WIDTH / 100
START_SPEED = FINAL_LEVEL + 1
# these need to match the image names
COLORS = ["green", "blue", "yellow"]

game_over = True
game_complete = True
current_level = 1
stars = []
animations = []

def draw():
    g = globals()
    global stars, current_level, game_over, game_complete
    g["screen"].clear()
    g["screen"].blit("space", (0,0))
    g["screen"].draw.text(f'Catch the RED star!\nPress Esc to exit',
                         topleft=(10, 10))
    if game_over:
        display_message("GAME OVER", "Try again")
    elif game_complete:
        display_message("YOU WON!", "Well done")
    
    else:
        for star in stars:
            star.draw()

def display_message(heading_text, sub_heading_text):
    g = globals()
    g["screen"].draw.text(heading_text,
                     fontsize=60,
                     center=CENTER,
                     color=FONT_COLOR)
    g["screen"].draw.text(sub_heading_text,
                     fontsize=30,
                     center=(CENTER_X, CENTER_Y + 30),
                     color=FONT_COLOR)

def update():
    global stars
    if len(stars) == 0:
        stars = make_stars(current_level)

def make_stars(star_count):
    colors = get_colors(star_count)
    new_stars = make_star_objects(colors)
    layout_stars(new_stars)
    animate_stars(new_stars)
    return new_stars

def get_colors(star_count):
    colors_to_create = ["red"]
    for i in range(0, star_count):
        random_color = random.choice(COLORS)
        colors_to_create.append(random_color)
    return colors_to_create

def make_star_objects(colors):
    new_stars = []
    for color in colors:
        star = Actor(color + "-star")
        new_stars.append(star)
    return new_stars

def layout_stars(star_objects):
    star_gaps = len(star_objects) + 1
    gap_size = WIDTH / star_gaps
    random.shuffle(star_objects)
    for index, star in enumerate(star_objects):
        new_x_pos = (index + 1) * gap_size
        star.x = new_x_pos

def animate_stars(star_objects):
    for star in star_objects:
        duration = (START_SPEED - current_level) / 2
        star.anchor = ("center", "bottom")
        # animate is from Pygame Zero
        animation = animate(star,
                            tween="linear",
                            duration=duration,
                            on_finished=handle_game_over,
                            y=HEIGHT)
        animations.append(animation)

def handle_game_over():
    global game_over
    game_over = True

def on_key_down(key):
    if keys.ESCAPE == key:
        exit()

def on_mouse_down(pos):
    global stars, current_level
    for star in stars:
        if star.collidepoint(pos):
            if "red" in star.image:
                red_star_click()
            else:
                handle_game_over()

def red_star_click():
    global current_level, stars, animations, game_complete
    stop_animations(animations)
    if current_level == FINAL_LEVEL:
        game_complete = True
    else:
        current_level = current_level + 1
        stars = []
        animations = []

def stop_animations(animations):
    for a in animations:
        if a.running:
            a.stop()

def setup(pgzero_objects, _modeFunc):
    g = globals()
    g |= pgzero_objects
    global modeFunc
    modeFunc = _modeFunc

def restart():
    global game_over, game_complete, current_level, stars, animations
    game_over = False
    game_complete = False
    current_level = 1
    stars = []
    animations = []

def unschedule():
    global animations
    stop_animations(animations)
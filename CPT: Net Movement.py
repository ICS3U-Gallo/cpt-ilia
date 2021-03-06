import arcade
import os


WIDTH = 640
HEIGHT = 480

#net
net_x = 0
net_y = 445

net_right = True
net_left = False
net_up = False
net_down = False

def setup():
    arcade.open_window(WIDTH, HEIGHT, "My Arcade Game")
    arcade.set_background_color(arcade.color.WHITE)
    arcade.schedule(update, 1/60)

    # Override arcade window methods
    window = arcade.get_window()
    window.on_draw = on_draw
    window.on_key_press = on_key_press
    window.on_key_release = on_key_release
    window.on_mouse_press = on_mouse_press


    arcade.run()


def update(delta_time):
    global WIDTH
    global HEIGHT
    global net_right
    global net_left
    global net_x
    global net_y
    global net_up, net_down

    # net_x
    if net_x <= 50 and net_y == 445:
            net_right = True
            net_left = False
            net_down = False
            net_up = False
    elif net_x >= WIDTH-50 and net_y >= 445:
            net_right = False
            net_left = False
            net_down = True
            net_up = False
    elif net_x == WIDTH-50 and net_y <= 300:
            net_right = False
            net_left = True
            net_down = False
            net_up = False

    elif net_x <= 50 and net_y <= 300:
            net_right = False
            net_left = False
            net_down = False
            net_up = True


    if net_right == True:
        net_x += 10

    elif net_left ==  True:
        net_x -= 10


    if net_down == True:
        net_y -= 10

    if net_up == True:
        net_y += 10


def on_draw():
    global net_x
    global net_y
    arcade.start_render()
    # Draw in here...

    arcade.draw_circle_filled(net_x, net_y, 25, arcade.color.BLUE)


def on_key_press(key, modifiers):
    pass


def on_key_release(key, modifiers):
    pass


def on_mouse_press(x, y, button, modifiers):
    pass


if __name__ == '__main__':
    setup()


def on_mouse_press(x, y, button, modifiers):
    pass


if __name__ == '__main__':
    setup()

import arcade
import math


WIDTH = 640
HEIGHT = 480

# Buttons
#        x ,  y ,  w , h
play = [175, 210, 125, 50]

highscores = [325, 210, 125, 50]

instructions = [237.5, 140, 150, 50]

# net
#        x    ,  y , r
net = [WIDTH/2, 410, 30]
net_speed = 0

net_reset = False

net_right = True
net_left = False
net_up = False
net_down = False

# Ball
#        x    y   r
ball = [320, 150, 25]
ball_speed = 10
ball_reset = False

# Aim
aim_x = 320
aim_y = 250
aim_right = False
aim_left = False
show_aim = True

# Shoot
shoot_ball = False
ball_move = False

# Score
score = 0
final_score = 0
collision = "No"
score_list = [0, 0, 0, 0, 0]

# Health
health = 5

# Screen

current_screen = "Menu"

def setup():
    arcade.open_window(WIDTH, HEIGHT, "Hoops")
    arcade.set_background_color(arcade.color.WHITE)
    arcade.schedule(update, 1 / 60)

    # Override arcade window methods
    window = arcade.get_window()
    window.on_draw = on_draw
    window.on_key_press = on_key_press
    window.on_key_release = on_key_release
    window.on_mouse_press = on_mouse_press

    arcade.run()


def update(delta_time):
    global WIDTH, HEIGHT
    global net, net_right, net_left, net_up, net_down, net_speed, net_reset
    global ball, shoot_ball, ball_speed, ball_reset
    global aim_x, aim_y, aim_right, aim_left, show_aim
    global health, score, final_score
    global current_screen

    # net movement
    if net[0] <= 50 and net[1] >= 410:
            net_right = True
            net_left = False
            net_down = False
            net_up = False
    elif net[0] >= WIDTH-50 and net[1] >= 410:
            net_right = False
            net_left = False
            net_down = True
            net_up = False
    elif net[0] >= WIDTH-50 and net[1] <= 300:
            net_right = False
            net_left = True
            net_down = False
            net_up = False

    elif net[0] <= 50 and net[1] <= 300:
            net_right = False
            net_left = False
            net_down = False
            net_up = True


    if net_right == True:
        net[0] += net_speed
    elif net_left == True:
        net[0] -= net_speed

    if net_down == True:
        net[1] -= net_speed
    elif net_up == True:
        net[1] += net_speed

    if net[1] > HEIGHT - 50:
        net[1] == 410
    if net[1] < 300:
        net[1] == 300

    # Ball Shoot
    if shoot_ball == True:
        x_diff = aim_x - ball[0]
        y_diff = aim_y - ball[1]
        angle = math.atan2(y_diff, x_diff)

        ball_change_x = math.cos(angle) * ball_speed
        ball_change_y = math.sin(angle) * ball_speed

        ball[1] += ball_change_y
        ball[0] += ball_change_x

        aim_y += ball_change_y
        aim_x += ball_change_x

        show_aim = False

    # Aim
    if aim_left == True:
        aim_x -= 5
    elif aim_right == True:
        aim_x += 5

    if aim_x in range(WIDTH-60, WIDTH + 1):
        aim_x = WIDTH - 60
    if aim_x in range(0, 60):
        aim_x = 60

    # Boundaries and Health
    if ball[1] >= HEIGHT or ball[0] <= 0 or ball[0] >= WIDTH:
        health -= 1
        ball_reset = True


    if health == 0:
        print('YOU DIED !!!')
        current_screen = "Death"
        final_score = score
        get_highscore(final_score)
        print(score_list)
        score = 0
        net_reset = True
        ball_reset = True
        health = 5


    if ball_reset == True:
        ball[0] = 320
        ball[1] = 150
        aim_x = 320
        aim_y = 250
        shoot_ball = False
        show_aim = True
        ball_reset = False

    if net_reset == True:
        net = [WIDTH/2, 410, 30]
        net_speed = 0
        net_reset = False

    if current_screen != "Play":
        ball_reset = True
        net_reset = True
        health = 5
        score = 0

    # Score Keeping

    dist_x = ball[0] - net[0]
    dist_y = ball[1] - net[1]
    dist = math.sqrt(dist_x ** 2 + dist_y ** 2)

    if dist < (ball[2] + net[2] - 10):
        ball_reset = True
        score += 1
        net_speed += 0.5




def on_draw():
    global net
    global ball
    global aim_x, aim_y, show_aim
    global current_screen
    global play, instructions, highscores
    global final_score


    arcade.start_render()
    # Draw in here...

    if current_screen == "Death":

        arcade.draw_text("You Died!!! (Press M to go to menu)", 85, HEIGHT/2, arcade.color.BLACK, 20)
        arcade.set_background_color(arcade.color.RED_DEVIL)

        arcade.draw_text(f"Final Score: {final_score}", WIDTH/2 - 80, HEIGHT/2 - 50, arcade.color.BLACK)


    if current_screen == "Menu":

        arcade.set_background_color(arcade.color.WHITE)

        arcade.draw_text("Hoops", 256, HEIGHT * 2/3, arcade.color.BLACK, 30, italic=True)

        # Play Button
        arcade.draw_xywh_rectangle_filled(play[0], play[1], play[2], play[3], arcade.color.ORANGE)
        arcade.draw_text("Play", 215, 228, arcade.color.BLACK, 15)

        # Highscore Button
        arcade.draw_xywh_rectangle_filled(instructions[0], instructions[1], instructions[2], instructions[3], arcade.color.ORANGE)
        arcade.draw_text("Instructions", 256, 157, arcade.color.BLACK, 15)

        # Instructions Button
        arcade.draw_xywh_rectangle_filled(highscores[0], highscores[1], highscores[2], highscores[3], arcade.color.ORANGE)
        arcade.draw_text("Highscores", 332, 228, arcade.color.BLACK, 15)


    if current_screen == "Play":

        # background
        arcade.set_background_color(arcade.color.WHITE)

        # net
        arcade.draw_circle_filled(net[0], net[1], net[2], arcade.color.BLUE)

        # aim
        if show_aim == True:
            arcade.draw_line(320, 150, aim_x, aim_y, arcade.color.BLACK)

        # ball
        arcade.draw_circle_filled(ball[0], ball[1], ball[2], arcade.color.ORANGE)

        # Health
        for num in range(health):
            for x in range(health * 25, 24, -25):
                arcade.draw_xywh_rectangle_filled(x, 35, 20, 20, arcade.color.RADICAL_RED)

        arcade.draw_text("Health:", 25, 60, arcade.color.BLACK)

        # Score
        arcade.draw_text(f"Score: {score}", WIDTH - 80, 60, arcade.color.BLACK)


    if current_screen == "Highscores":

        arcade.draw_text("Highscores", 200, HEIGHT * 4/5, arcade.color.BLACK, 30, italic=True)

        # Top 5 Highscores
        for num, value in enumerate(score_list):
            arcade.draw_text(f"{num+1}. {value}", 270, HEIGHT * 2/3 - num*50, arcade.color.BLACK, 15, italic=True)

    if current_screen == "Instructions":
        arcade.draw_text("Instructions", 190, HEIGHT * 4 / 5, arcade.color.BLACK, 30, italic=True)

def on_key_press(key, modifiers):
    global aim_left, aim_right
    global shoot_ball
    global current_screen

    # In-game Controls
    if key == arcade.key.LEFT and current_screen == "Play":
        aim_left = True
    elif key == arcade.key.RIGHT and current_screen == "Play":
        aim_right = True

    if key == arcade.key.SPACE and current_screen == "Play":
        shoot_ball = True

    # Shortcuts
    if key == arcade.key.M:
        current_screen = "Menu"

    if key == arcade.key.P and current_screen == "Menu":
        current_screen = "Play"

    if key == arcade.key.H:
        current_screen = "Highscores"

    if key == arcade.key.I:
        current_screen = "Instructions"

def on_key_release(key, modifiers):
    global aim_left, aim_right

    if key == arcade.key.LEFT:
        aim_left = False

    if key == arcade.key.RIGHT:
        aim_right = False


def on_mouse_press(x, y, button, modifiers):
    global play, instructions, highscores
    global current_screen

    print(x, y)

    if x > play[0] and x < play[0]+play[2] and y > play[1] and y < play[1]+play[3] and current_screen == "Menu":
        current_screen = "Play"

    if x > highscores[0] and x < highscores[0]+highscores[2] and y > highscores[1] and y < highscores[1]+highscores[3] and current_screen == "Menu":
        current_screen = "Highscores"

    if x > instructions[0] and x < instructions[0]+instructions[2] and y > instructions[1] and y < instructions[1]+instructions[3] and current_screen == "Menu":
        current_screen = "Instructions"


def get_highscore(num):
    global final_score, score_list, current_screen

    if num > score_list[4]:
            score_list.append(num)
            score_list.remove(min(score_list))
            score_list.sort(reverse = True)

if __name__ == '__main__':
    setup()

import turtle as ball
import random

######Main Functional frontend bit intialises main ballon game components######
# Set up the screen
display = ball.Screen()
display.title("Balloon Shooting Game")
display.bgcolor("white")
display.setup(width=600, height=600)

# Set up the cannon
shooter = ball.Turtle()
shooter.shape("square")
shooter.color("black")
shooter.shapesize(stretch_wid=2, stretch_len=1)
shooter.penup()
shooter.goto(-250, 0)
cannon_speed = 20  # Cannon speed

# Set up the balloon
balloon = ball.Turtle()
balloon.shape("circle")
balloon.color("red")
balloon.penup()
balloon.goto(250, random.randint(-200, 200))  # Random starting y position
balloon_speed = 5  # Balloon speed

# Set up the bullet
bullet_tri = ball.Turtle()
bullet_tri.shape("triangle")
bullet_tri.color("blue")
bullet_tri.shapesize(stretch_wid=0.5, stretch_len=1)
bullet_tri.penup()
bullet_tri.goto(-250, 0)
bullet_speed = 10 * balloon_speed  # Bullet speed has to be 10 x that of the balloon 
bullet_postion = "ready"  # Bullet state (ready or fire)

# Set up the missed shots count
missed_shots = 0 #initialise to add incrementing count 

######Specific functions that will trasnlate to specific actions on the keyboard######
# Define functions for moving the cannon and firing the bullet
def move_up():
    vert = shooter.ycor()
    if vert < 250:
        vert += cannon_speed
    shooter.sety(vert)

def move_down():
    vert = shooter.ycor()
    if vert > -250:
        vert -= cannon_speed
    shooter.sety(vert)

def fire_bullet():
    global bullet_postion
    if bullet_postion == "ready":
        bullet_postion = "fire"
        x = shooter.xcor() + 10  # Shift bullet to the right of the cannon
        y = shooter.ycor()
        bullet_tri.goto(x, y)

def is_collision(t1, t2):
    dist_col = ((t1.xcor() - t2.xcor()) ** 2 + (t1.ycor() - t2.ycor()) ** 2) ** 0.5
    if dist_col < 20:
        return True
    else:
        return False

# Set up the keyboard bindings
display.listen()
display.onkeypress(move_up, "Up")
display.onkeypress(move_down, "Down")
display.onkeypress(fire_bullet, "space")

######Main Backend game looping, which sets the game instriuctions######
while True:
    # Move the balloon
    balloon.sety(balloon.ycor() + balloon_speed)
    if balloon.ycor() > 250 or balloon.ycor() < -250:
        balloon_speed *= -1  # Reverse the direction when the balloon hits the top or bottom

    # Move the bullet
    if bullet_postion == "fire":
        bullet_tri.setx(bullet_tri.xcor() + bullet_speed)
        # Check if the bullet hits the balloon
        if is_collision(bullet_tri, balloon):
            balloon.hideturtle()  # Hide the balloon
            print("Game over! You shot the ballon down!")
            break
        # Check if the bullet goes out of bounds
        if bullet_tri.xcor() > 300:
            bullet_postion = "ready"
            bullet_tri.goto(-250, 0)
            missed_shots += 1
            print("Missed shot: ", missed_shots)

######Final program displayed on app window######
display.mainloop()

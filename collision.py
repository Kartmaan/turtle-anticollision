"""Random generation of circles on the screen bounded by an 
anti-collision system. The circles appearing at the edge 
of the window are colored in red, those located on an axis 0 
in blue, the others without color."""

import random
import time, datetime
import turtle as tu

__author__ = "Kartmaan"

circles = 1600 # Number of circles generated
# For the following parameters : screen(1024,720) and r = 5
# 1700 circles seems to be the most reasonable maximum number

width = 1024 # Window width
height = 720 # Window height
screen = tu.setup(width, height, 300, 200) #(x_res, y_res, x_pos, y_pos)
r = 5 # Circle radius
b = r*2 # Space coefficient between two circles

i = 0 # Loops cursor
collision = False # Collision detector
total_collisions = 0 # Total collisions detected
empty = 0 # Circles with no color
red = 0 # Number of red circles
blue = 0 # Number of blue circles
xy_list = [] # Coordinates of all circles placed (tuple x,y)

tu.bgcolor("white")
tu.title("Anti-collision system")
tu.color("black")
tu.speed(0)

def percent(partial, total):
    # Percentage function
    percentage = (partial/total) * 100
    percentage = round(percentage, 1)
    return percentage

start = time.time() # Chrono start

while i < circles: # Main loop
    tu.up()

    if len(xy_list) == 0:
        # The first circle is randomly placed on the screen, unconditionally
        x = random.randint(-(width/2), (width/2)) # (-500, 500)
        y = random.randint(-(height/2), (height/2))
        xy_list.append((x,y)) # Put coordinates in tuple and add it to xy_list

# Anti-collision --------------------------
        """Before adding the generated x, y coordinates, we check if 
        each of them is present in xy_list within a margin of 
        -1 circle diameter to +2 circle diameter. If no coordinate 
        pair is present in this range, the new coordinate is added, 
        otherwise the loop resumes and another coordinate pair is 
        generated."""

    else:
        while True:
            x = random.randint(-(width/2), (width/2))
            y = random.randint(-(height/2), (height/2))
            for coor in xy_list : # coor is tuple
                x_list,y_list = coor
                if ((x_list-b)<=x<=(x_list+(b*2))) and ((y_list-b)<=y<=(y_list+(b*2))):
                    collision = True
                    break # Exit from for loop

            if collision == True : # Collision detected
                collision = False
                total_collisions += 1
                continue # Return to while True

            if collision == False : # No collision detected
                xy_list.append((x,y))
                #collision = 0
                break # Exit from while True

# Draw --------------------------
    tu.goto(x, y) # Coordinates in px
    tu.down()
    cond = ((x < -400) or (x > 400)) or ((y < -250) or (y > 250)) and (x != 0 or y != 0)
    if cond:
        tu.fillcolor("red")
        tu.begin_fill()
        tu.circle(r, 360)
        tu.end_fill()
        i += 1
        red += 1
    elif x == 0 or y == 0:
        tu.fillcolor("blue")
        tu.begin_fill()
        tu.circle(r, 360)
        tu.end_fill()
        blue += 1
        i += 1
    else:
        tu.circle(r, 360)
        empty += 1
        i += 1
    
    if i % 100 == 0: # Display every 100 circles
        print("Drawn circles : {}({}%) - Collisions avoided = {}({}%)".format(i, percent(i, circles), 
        total_collisions, percent(total_collisions, (i+total_collisions))))

# Stats --------------------------
end = time.time() # Chrono end
laps = round(end - start)

total_try = i + total_collisions
per_empty = percent(empty,i)
per_red = percent(red,i)
per_blue = percent(blue,i)
per_col = percent(total_collisions, total_try)

print("\nTotal = {}, Empty = {}({}%), Red = {}({}%), Blue = {}({}%)".format(i, empty, per_empty, 
red, per_red, blue, per_blue))
print("{} collisions avoided ({}%)".format(total_collisions, per_col))

if laps > 60 :
    laps = str(datetime.timedelta(seconds=laps))
    print("Generated in {}m".format(laps))

else :
    print("Generated in {}s".format(round(laps,1)))

tu.exitonclick()
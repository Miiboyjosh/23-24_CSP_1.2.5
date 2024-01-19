import turtle as trtl

# SIV Turtles
ring1 = trtl.Turtle()
ring2 = trtl.Turtle()
ring3 = trtl.Turtle()
ring4 = trtl.Turtle()
drawer = trtl.Turtle()

# Screen Setup
ringoffire_image = "ringoffire.gif"
wn = trtl.Screen()
wn.addshape(ringoffire_image)
wn.setup(width=1.0, height=1.0)
wn.tracer(False)
wn.bgpic("background.gif")

# Standard Setup
letter_list = ['a', 's', 'k', 'l']
ring_letter_x_offset = 25
ring_letter_y_offset = 50

# Functions
def drawRing(active_ring):
    active_ring.penup()
    active_ring.goto(-315, 100)
    drawLetter(active_ring)
    active_ring.shape(ringoffire_image)
    wn.update()

def drawLetter(active_ring):
    global letter
    letter = letter_list[0]
    active_ring.xcor = -315
    active_ring.ycor = 100
    drawer.penup()
    drawer.goto(active_ring.xcor - ring_letter_x_offset, active_ring.ycor - ring_letter_y_offset)
    drawer.color("Red")
    drawer.write(letter, font=("Arial", 55, "bold"))

def resetRing(active_ring):
    active_ring.goto(active_ring.xcor(), 100)
    drawRing(active_ring)

def dropRing(active_ring):
    active_ring.ycor -= 10
    active_ring.goto(active_ring.xcor(), active_ring.ycor)

# Function Calls
drawRing(ring1)
drawRing(ring2)
drawRing(ring3)
drawRing(ring4)

# On Key Presses
def check_answer(letter, key):
    if letter == key:
        return True
    else:
        return False

def on_key_press_a():
    if check_answer(letter_list[0], "a"):
        resetRing(ring1)
        dropRing(ring1)

def on_key_press_s():
    if check_answer(letter_list[1], "s"):
        resetRing(ring2)
        dropRing(ring2)

def on_key_press_k():
    if check_answer(letter_list[2], "k"):
        resetRing(ring3)
        dropRing(ring3)

def on_key_press_l():
    if check_answer(letter_list[3], "l"):
        resetRing(ring4)
        dropRing(ring4)

wn.onkeypress(on_key_press_a, "a")
wn.onkeypress(on_key_press_s, "s")
wn.onkeypress(on_key_press_k, "k")
wn.onkeypress(on_key_press_l, "l")

drawer.goto(0,0)
drawer.circle(50)
drawer.penup()
drawer.goto(-17,50)
drawer.pendown()
drawer.write("You Win")

# Listen for key presses
wn.listen()
wn.mainloop()

# --Import Turtle--
import turtle as trtl
# --SIV Turtles--
track_1 = trtl.Turtle()
track_2 = trtl.Turtle()
track_3 = trtl.Turtle()
track_4 = trtl.Turtle()
# -- Screen Setup --
ringoffire_image = "ringoffire.gif"
wn = trtl.Screen()
wn.addshape(ringoffire_image)
wn.setup(width=1.0, height=1.0)
wn.tracer(False)
wn.bgpic("background.gif")
# --Standard Setup--
letter_list = ['a', 's', 'k', 'l']
ring_letter_x_offset = 25
ring_letter_y_offset = 50

ring1.penup()
# -- Functions --
def drawRing(active_ring):
    active_ring.penup()
    active_ring.goto(-315, 100)
    drawLetter(ring1)
    active_ring.shape(ringoffire_image)
    dropRing()
    wn.update()


def drawRing_2(active_ring):
    active_ring.penup()
    active_ring.goto(-115, 100)
    drawLetter2(ring2)
    active_ring.shape(ringoffire_image)
    dropRing2()
    wn.update()


def drawRing_3(active_ring):
    active_ring.penup()
    active_ring.goto(65, 100)
    drawLetter3(ring3)
    active_ring.shape(ringoffire_image)
    dropRing3()
    wn.update()


def drawRing_4(active_ring):
    active_ring.penup()
    active_ring.goto(265, 100)
    drawLetter4(ring4)
    active_ring.shape(ringoffire_image)
    dropRing4()
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

def drawLetter2(active_ring):
    global letter
    letter = letter_list[1]
    active_ring.xcor = -115
    active_ring.ycor = 100
    drawer.penup()
    drawer.goto(active_ring.xcor - ring_letter_x_offset, active_ring.ycor - ring_letter_y_offset)
    drawer.color("Red")

    drawer.write(letter, font=("Arial", 55, "bold"))

def drawLetter3(active_ring):
    global letter
    letter = letter_list[2]
    active_ring.xcor = 65
    active_ring.ycor = 100
    drawer.penup()
    drawer.goto(active_ring.xcor - ring_letter_x_offset, active_ring.ycor - ring_letter_y_offset)
    drawer.color("Red")
    drawer.write(letter, font=("Arial", 55, "bold"))

def drawLetter4(active_ring):
    global letter
    letter = letter_list[3]
    active_ring.xcor = 265
    active_ring.ycor = 100
    drawer.penup()
    drawer.goto(active_ring.xcor - ring_letter_x_offset, active_ring.ycor - ring_letter_y_offset)
    drawer.color("Red")
    drawer.write(letter, font=("Arial", 55, "bold"))

def resetRing():
    ring1.goto(-315, 100)
    drawRing(ring1)

def resetRing_2():
    ring2.goto(-115, 100)
    drawRing_2(ring2)


def resetRing_3():
    ring3.goto(65, 100)
    drawRing_3(ring3)

def resetRing_4():
    ring4.goto(265, 100)
    drawRing_4(ring4)

def dropRing():
    wn.tracer(True)
    ring1.xcor = -315
    ring1.ycor = 100
    ring1.goto(ring1.xcor, ring1.ycor - 400)
    ring1.hideturtle()
    wn.tracer(False)

def dropRing2():
    wn.tracer(True)
    ring2.xcor = -115
    ring2.ycor = 100
    ring2.goto(ring2.xcor, ring2.ycor - 400)
    ring2.hideturtle()
    wn.tracer(False)


def dropRing3():
    wn.tracer(True)
    ring3.xcor = 65
    ring3.ycor = 100
    ring3.goto(ring3.xcor, ring3.ycor - 400)
    ring3.hideturtle()
    wn.tracer(False)


def dropRing4():
    wn.tracer(True)
    ring4.xcor = 265
    ring4.ycor = 100
    ring4.goto(ring4.xcor, ring4.ycor - 400)
    ring4.hideturtle()
    wn.tracer(False)




# --Function Call--
drawRing(ring1)
drawRing_2(ring2)
drawRing_3(ring3)
drawRing_4(ring4)
#--On Key Presses--
wn.onkeypress(resetRing, "a")
wn.onkeypress(resetRing_2, "s")
wn.onkeypress(resetRing_3, "k")
wn.onkeypress(resetRing_4, "l")
wn.mainloop()

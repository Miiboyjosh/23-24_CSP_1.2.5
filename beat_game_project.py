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
# --Standard Setup--
letter_list = ['a', 's', 'k', 'l']
letter = "a"
ring_letter_x_offset = 25
ring_letter_y_offset = 50


# -- Functions --
def drawLetter(active_ring, letter):
    drawer.penup()
    drawer.goto(active_ring.xcor() - ring_letter_x_offset, active_ring.ycor() - ring_letter_y_offset)



def drawRing(active_ring, letter):
    active_ring.showturtle()
    active_ring.shape(ringoffire_image)
    drawLetter(active_ring, letter)
    wn.update()





# pt 1 - Get the game functioning and playable

# pt 2 - Store and display scores using list

# pt 3 - display highscores by using parameters


# --Function Call--
drawRing(ring1, A)

wn.bgpic("background.gif")
wn.mainloop()

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

ring1.penup()
# -- Functions --
def drawRing(active_ring, letter):
    active_ring.goto(-300, 0)
    active_ring.shape(ringoffire_image)
    wn.update()


# pt 1 - Get the game functioning and playable

# pt 2 - Store and display scores using list

# pt 3 - display highscores by using parameters


# --Function Call--
drawRing(ring1)

wn.bgpic("background.gif")
wn.mainloop()

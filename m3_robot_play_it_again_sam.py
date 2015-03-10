"""
This module lets you integrate:
  -- SEQUENCES, and
  -- ROBOT METHODS.

Additionally, it lets you practice:
  -- PROCEDURAL DECOMPOSITION: breaking a problem into sub-problems.
  -- ITERATIVE ENHANCEMENT:
       -- Implement a bit and test that bit, getting it to work.
       -- Implement a bit more and test it, getting it to work.
       -- Etc until the entire program works corectly.

Authors: David Mutchler, Amanda Stouder, Chandan Rupakheti, Katie Dion,
         Claude Anderson, Delvin Defoe, Curt Clifton, their colleagues,
         and Joshua Spalding and Thomas Bonatti.  January 2014.
"""  # TODOne: 1. PUT YOUR NAME IN THE ABOVE LINE.

#-----------------------------------------------------------------------
# TODO: 2. Implement a program that accomplishes the specification
#   that is sketched in the attached    PlayItAgainSam_picture.pdf.
#
#   IMPORTANT:
#     1. Implement using ITERATIVE ENHANCEMENT:
#          -- Implement a bit and test that bit, getting it to work.
#          -- Implement a bit more and test it, getting it to work.
#          -- Etc until the entire program works corectly.
#
#     2. Put meaningful chunks of work into FUNCTIONS.
#        Do NOT put the entire program (i.e., all the code) in main!
#
#     3. Write and use TEST FUNCTIONS as needed (but only as needed).
#
#     4. Include BRIEF but MEANINGFUL comments AS YOU WRITE THE CODE.
#-----------------------------------------------------------------------

import new_create
import time
import zellegraphics as zg


def main():
    """ Calls the other functions in this module, as needed. """
    music_bob = robotStart()
    window = windowStart()
    clicking(window, music_bob)


def windowStart():
    # window (xmin=31, xmax=127.... 960 wide. height = 500)
    # rectangles 96(x) by 25(y)... filled different colors
    #   (0,0) (960,250) (black)... (0,250) (960,500) (yellow)
    # starts up the robot (mode: safe)

    width = 960
    height = 500
    title = 'play it again sam'
    window = zg.GraphWin(title, width, height)


    top1 = zg.Point(0, 0)
    top2 = zg.Point(960, 250)

    top_rectangle = zg.Rectangle(top1, top2)

    top_rectangle.setFill('black')

    bottom1 = zg.Point(0, 250)
    bottom2 = zg.Point(960, 500)

    bottom_rectangle = zg.Rectangle(bottom1, bottom2)

    bottom_rectangle.setFill('white')

    top_rectangle.draw(window)
    bottom_rectangle.draw(window)

    return window

def robotStart():

    port = 'sim'  # Note the quotes.
    music_bob = new_create.Create(port)

    return music_bob

def clicking(window, music_bob):
    # get mouse/circle coordinates
    # draw circle (filled, small radius)
    # while loops that breaks with click in lower rectangle
    # (goes to different function: "replay")

    notes_list = []
    while True:
        music_point = window.getMouse()
        if music_point.y > 250:
            break
        draw_circle(music_point, window)
        music_value = round((music_point.x) / 10) + 31
        notes_list.append(music_value)
        musicnotes(music_value, music_bob)

    replay(notes_list, window, music_bob)

def musicnotes(music_value, music_bob):
    # obtains mouse coordinate in clicking() and plays the music notes
    # as per the x coordinate (127-31=96)
    # the duration of the music note should be a half second

    music_bob.playNote(music_value, 32)

def replay(notes_list, window, music_bob):
    # once engaged, replays all the notes that the user generates
    # these notes should be stored in a list
    # once played, shuts robot down and closes window... ends program

    for k in range(len(notes_list)):
        music_bob.playNote(notes_list[k], 32)
        time.sleep(.55)

    time.sleep(.05)
    music_bob.shutdown
    window.close()

def draw_circle(music_point, window):
    radius = 5
    circle = zg.Circle(music_point, radius)
    circle.setFill("yellow")
    circle.draw(window)

#-----------------------------------------------------------------------
# If this module is running at the top level (as opposed to being
# imported by another module), then call the 'main' function.
#-----------------------------------------------------------------------
if __name__ == '__main__':
    main()

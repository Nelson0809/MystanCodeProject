"""
File: Steeplechase.py
Name: Nelson Chen
---------------------------------
Nelson
"""

from karel.stanfordkarel import *

def main():
    """
    Karel crosses hurdles in a 12x12 world
    with a for loop
    """
    for i in range(11):
        if front_is_clear():
            move()
        else:
            jump()
            turn_left()



def jump():
    """
    Pre-condition:Karel is on the left of the side of the wall,facing East
    Post-condition:Karel is on the right side of wall
    """
    up()
    cross()
    down()


def up():
    """
    Pre-condition:Karel is on the left of the side of the wall,facing East
    Post-condition:Karel is at the upper left of the wall,facing North
    """
    turn_left()
    while not right_is_clear():
        move()
    # alternative
    # while not front_is_clear():
    #     turn_left()
    #     move()
    #     turn_right()


def turn_right():
    turn_left()
    turn_left()
    turn_left()


def cross():
    """
    pre-condition:Karel is at the upper left of the wall,facing North
    post-condition:Karel is at the upper right,facing south
    """
    turn_right()
    move()
    turn_right()


def down():
    """
    pre-condition:Karel is at the upper right,facing south
    post-condition:Karel is on the right of the side of the wall,facing South
    """
    while front_is_clear():
        move()



# ----- DO NOT MODIFY CODE BELOW THIS LINE ----- #
if __name__ == '__main__':
    execute_karel_task(main)

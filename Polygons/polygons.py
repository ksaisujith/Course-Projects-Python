__author__ = "Sai Sujith Kammari"

'''
CSCI-603: LAB 3
Author1: SAI SUJITH KAMMARI
Author2: KEERTHI NAGAPPA PRADHANI

This program draws some polygons of decreasing sides, revursively
'''

import turtle
import sys

# global constants for window dimensions
WINDOW_WIDTH    = 1000
WINDOW_HEIGHT   = 1000
# global constants for turtle settings
COLORS = ['orange','red', 'violet', 'yellow','green','blue','#00FA9A','#A9A9A9','#8B0000']
LENGTH = 200
PEN_SIZE = 3

def init(myWindowname):
    """
    Initialize for drawing.  (-500, -500) is in the lower left and
    (500, 500) is in the upper right.

    :pre: pos (0,0), heading (east), up
    :post: pos (-(WINDOW_WIDTH/2)-250,-(WINDOW_WIDTH / 2)-250), heading (east), up
    :return: None
    """
    turtle.setworldcoordinates(-WINDOW_WIDTH/2, -WINDOW_WIDTH/2,
        WINDOW_WIDTH/2, WINDOW_HEIGHT/2)
    turtle.up()
    turtle.backward((WINDOW_WIDTH/2)-50)
    turtle.right(90)
    turtle.forward((WINDOW_WIDTH/2)-50)
    turtle.left(90)
    turtle.write(arg='Sai Sujith K\nKeerthi Pradhani', align='left', move=False, font =("Arial", 10, "normal"))
    turtle.left(90)
    turtle.forward((WINDOW_WIDTH/2)-250)
    turtle.right(90)
    turtle.forward((WINDOW_WIDTH / 2)-250)
    turtle.title(myWindowname)


def drawPolygons(sides,isFill,length):
    """
    Draws polygons inside of another polygon with decresing sides

    :pre: pos (0,0), heading (east), up
    :post: pos (0,0), heading (east), down
    :return: totalLength
    """
    turtle.down()
    totalLength = 0
    #Draws polygon without filling
    if isFill == 'nofill':
        if sides ==2:
            return totalLength
        else:
            turtle.pensize(PEN_SIZE)
            for i in range(sides):
                turtle.pencolor(COLORS[sides])
                turtle.forward(length)
                totalLength += length
                turtle.left(360/sides)
                totalLength += drawPolygons(sides - 1,'nofill',length/2)
    else:
        # Draws polygon with filling
        if sides == 2:
            return totalLength
        else:
            turtle.fillcolor(COLORS[len(COLORS) - sides])
            turtle.begin_fill()
            turtle.pencolor(COLORS[len(COLORS) - sides])
            for side in range(sides):
                totalLength += length
                turtle.forward(length)
                turtle.left(360 / sides)
            turtle.end_fill()
            for side in range(sides):
                turtle.forward(length)
                turtle.left(360 / sides)
                totalLength += drawPolygons(sides - 1, isFill, length / 2)
    return totalLength

def drawFlower(number,fill):
    """
        Draws flower starting with number of sides

        :pre: pos (0,0), heading (east), up
        :post: pos (0,0), heading (east), up
        :return: totalLength
        """
    turtle.down()
    totalLength = 0
    if number >2:
        for petal in range(16):
            turtle.color(COLORS[len(COLORS)-number])
            turtle.pensize(number)
            turtle.right(360/16)
            if fill == 'fill':
                turtle.fillcolor(COLORS[len(COLORS) - number])
                turtle.begin_fill()
            turtle.pencolor(COLORS[len(COLORS) - number])
            for side in range(number):
                turtle.forward(LENGTH)
                turtle.left(360 / number)
                totalLength += LENGTH
            turtle.forward(10)
            if fill == 'fill':
                turtle.end_fill()
        totalLength += drawFlower(number-1,fill)
    else:
        return totalLength
    turtle.up()
    return totalLength


def main():
    """
        The main function.
        :pre: pos (0,0), heading (east), up
        :post: pos (0,-0), heading (east), up
        :return: None
        """
    #Running the program by taking sides and fill as command line arguemnts
    if len(sys.argv) != 3:
        #Parameters are not passed
        print("Please provide correct command line arguments \n"
              ,"Usage of this program is polygons.py #_sides [fill\\nofill]")
        sys.exit()

    sides = int(sys.argv[1])
    isFill =sys.argv[2]

    if isFill not in ['fill','nofill','NOFILL','FILL','NoFill','Fill']:
        #Wrong parameter has been passed for fill or no fill
        print("Please provide correct command line arguments for fill or nofill\n"
              , "Usage of this program is polygo22ns.py #_sides [fill\\nofill]")
        sys.exit()

    turtle.speed(5)
    #turtle.tracer(0,0)

    ########################################################
    ## Drawing an art with the recursive sides of polygons##
    ########################################################
    init('Polygons - inside')
    print("The total length of all the sides in the diagram is:",drawPolygons(sides,isFill,LENGTH))
    turtle.up()
    input("Please press enter to draw a flower")

    turtle.reset()

    ########################################################
    ## Drawing Flower with the recursive sides of polygons##
    ########################################################
    init('Polygons - flower')
    turtle.left(90)
    turtle.forward(250)
    turtle.right(90)
    turtle.forward(100)
    print("The total length of all the sides in the diagram is:", drawFlower(sides, isFill))
    turtle.update()
    turtle.mainloop()

if __name__ == '__main__':
    main()
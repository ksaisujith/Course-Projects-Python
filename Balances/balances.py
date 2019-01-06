__author__ = "Sai Sujith Kammari"

'''
CSCI-603: LAB 8
Author1: SAI SUJITH KAMMARI
Author2: KEERTHI NAGAPPA PRADHANI

Draws the balance with the weights provided. If the torque on the right doesn't match then exits
'''

import sys
import turtle

# global constants for turtle window dimensions
WINDOW_WIDTH    = 2000
WINDOW_HEIGHT   = 2000

class Beam:
    """
    This class creates the beams with hangers and the distance of each hanger
    """
    __slots__ = 'dist', 'hanger', 'beam_hang_index', 'scaling_factor'

    def __init__(self,beam_details):
        """
        Creates the beam object

        :param beam_details: the list of hangers and their positions on the beam
        """
        self.dist = []
        self.hanger = []
        for index in range(len(beam_details)):
            # Splitting the values to the distances and hangers
            if index%2 == 0:
                self.dist.append(int(beam_details[index]))
            else:
                if isinstance(beam_details[index], Beam):
                    # Creating a beam
                    self.hanger.append(beam_details[index])
                else:
                    # Creating the weight
                    self.hanger.append(Weight(beam_details[index]))

        if len(self.hanger) != len(self.dist):
            # Validating the input provided
            print('Wrong input provided')
        else:
            # Validating if the input provided is balanced
            self.beam_hang_index = self.get_midindex()

            #Setting the scaling factor for the beam which is used while drawing
            self.scaling_factor = self.weight() * 10

            # Adjusting the scaling factor so that the balance doesn't go out of screen
            if self.scaling_factor > WINDOW_WIDTH / 2:
                self.scaling_factor = WINDOW_WIDTH / 4

            # Checking if a weight is missing
            if len([missing_weights for missing_weights in self.hanger if missing_weights.weight() == -1 ]) > 0:
                # Finding the missing weight
                self.find_missing_weight()

            if not self.isbalanced():
                # Weights are not balanced
                print("It is not a balanced weights. Please provide a balance with equal torques")
                sys.exit(0)

    def get_total_torque(self):
        """
        Returns the total torque on the beam

        :return: torque value
        """
        return sum([abs(hang.weight() * dist) for hang, dist in zip(self.hanger[:], self.dist[:])])

    def get_midindex(self):
        """
        Returns the index on the hanger which where the hanger is hanging

        :return: middle index
        """
        return len([left_numbers for left_numbers in self.dist if int(left_numbers) < 0])

    def find_missing_weight(self):
        """
        Finding and replacing the value of the empty weight in the balance to balance the weight

        :return: None
        """
        # Finding the indexof the missing value
        missing_value_index = 0
        for hang in self.hanger:
            if hang.weight() == -1:
                break
            else:
                missing_value_index += 1

        # Finding the missing value
        total_torque = 0
        for index in range(len(self.dist)):
            total_torque += self.dist[index] * self.hanger[index].weight()
        total_torque -= self.dist[missing_value_index] * self.hanger[missing_value_index].weight()
        missing_value = abs(total_torque // self.dist[missing_value_index])

        # Replacing the missing value in the balance
        self.hanger[missing_value_index].set_weight(missing_value)
        print("Missing weight found and replaced with " + str(missing_value))


    def weight(self):
        """
        returns the total weight of the beam

        :return: total Weight
        """
        return sum([weight.weight() for weight in self.hanger if not isinstance(weight, Beam)]) + \
               sum([beam.weight() for beam in self.hanger if isinstance(beam, Beam)])

    def isbalanced(self):
        """
        Checks if the beam is balanced or not

        :return: True if balanced else False
        """
        left_torque = abs(sum([hang.weight() * dist  for hang,dist in zip(self.hanger[:self.beam_hang_index],self.dist[:self.beam_hang_index])]))
        right_torque = abs(sum([hang.weight() * dist  for hang,dist in zip(self.hanger[self.beam_hang_index:],self.dist[self.beam_hang_index:])]))
        if left_torque != right_torque:
             # Not Balanced
             return False
        else:
            # Balanced
            return True

    def turtle_window_init (self,myWindowname):
        """
        Initialize for drawing.
        :pre: pos (0,0), heading (east), up
        :post: pos (0,WINDOW_HEIGHT/3), heading (east), up
        :return: None
        """
        turtle.setworldcoordinates(-WINDOW_WIDTH / 2, -WINDOW_WIDTH / 2,
                                   WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2)
        turtle.up()
        turtle.left(90)
        turtle.forward(WINDOW_HEIGHT/3)
        turtle.right(90)
        turtle.title(myWindowname)

    def drawBalance(self, beam, factor, vert_height = WINDOW_HEIGHT/10):
        """
        Draws the Beam

        :pre: pos (0,0), heading (east), down
        :post: pos (0,0), heading (east), down
        :param beam: beam that has to be drawn
        :param vert_height: length that has to be suspended
        :return: None
        """
        turtle.right(90)
        turtle.forward(vert_height)
        turtle.left(90)
        for d in range(len(beam.dist)):
            turtle.forward(factor * int(beam.dist[d]))
            if isinstance(beam.hanger[d],Beam):
                self.drawBalance(beam.hanger[d], factor/3)
            else:
                self.drawWeight(beam.hanger[d].weight())
            for x in range(abs(int(beam.dist[d]))):
                # Drawing the beam factor indicators
                turtle.backward(factor * (int(beam.dist[d]) / abs(int(beam.dist[d] ))))
                turtle.right(90)
                turtle.forward(10)
                turtle.backward(10)
                turtle.left(90)

        # Returning back
        turtle.left(90)
        turtle.forward(vert_height)
        turtle.right(90)

    def drawWeight(self,weight, hanger_length = WINDOW_HEIGHT // 100  ):
        """
        Draws the weights

        :pre: pos (0,0), heading (east), down
        :post: pos (0,0), heading (east), down
        :param weight: Weight that has to be written
        :return: None
        """
        turtle.left(180)
        turtle.right(90)
        turtle.backward(hanger_length * 1.5)
        turtle.up()
        turtle.backward(hanger_length * 2.5)
        turtle.write(weight)
        turtle.forward(hanger_length * 4 )
        turtle.right(90)
        turtle.down()


    def draw(self):
        """
        Draws the Balance
        :pre: pos (0,0), heading (east), up
        :post: pos (0,0), heading (east), up
        :return: None
        """
        self.turtle_window_init("Balance")
        turtle.down()
        self.drawBalance(self, self.scaling_factor )
        turtle.up()
        turtle.mainloop()

class Weight:
    """
    Holds the values of the weight

    """
    __slots__ =  'value'
    def __init__(self,weight):
        """
        Creates the weight object

        :param weight: value of the weight that is being hanged
        """
        self.value = int(weight)


    def weight(self):
        """
        Returns the weight of the object

        :return value: The value of the weight
        """
        return self.value

    def set_weight(self, weight):
        """
        Sets the value

        :param weight: weight that has to be set
        :return: None
        """
        self.value = weight

def main():
    """
    Main Method

    :return: None
    """
    beams = {}
    # Reading the file
    try:
        with open(input("Please provide the file location which have balance details"), mode='r') as input_file:
            for line in input_file:
                command = line.strip().split(' ')
                beams[command[0]] =  command[1:]
    except:
        # Handling the wrong file name
        print("Bad file. Please check the file")
        sys.exit(1)

    # Replacing the beam values
    balance_arguments = ' '.join(beams['B'])
    while 'B' in balance_arguments:
        for key in beams.keys():
            if key != 'B':
                balance_arguments = balance_arguments.replace(key, "ss*" +','.join(beams[key])+"*")
    balance_arguments = balance_arguments.replace('ss*','Beam([')
    balance_arguments = balance_arguments.replace('*', '])').split(' ')

    # Building the arguments for the main Balance
    arguments = []
    count = 0
    for index in range(len(balance_arguments)):
        if (balance_arguments[index] != ''):
            if count % 2 == 0:
                # adding the distances
                arguments.append(balance_arguments[index])
            else:
                # creating the objects
                if 'Beam' in balance_arguments[index]:
                    arguments.append(eval(balance_arguments[index]))
                else:
                    arguments.append(int(balance_arguments[index]))
            count += 1

    # Creating the main Balance
    balance  = Beam(arguments)

    # Drawing the main balance
    balance.draw()

if __name__ == '__main__':
    main()
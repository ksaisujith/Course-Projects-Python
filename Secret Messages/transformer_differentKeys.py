__author__ = "Sai Sujith Kammari"

'''
CSCI-603: LAB 4
Author1: SAI SUJITH KAMMARI
Author2: KEERTHI NAGAPPA PRADHANI

This program will read in input file, file with instructions for encrypt/decrypt and output the encrypted/decrypted results to a third  file.
The keys used for encryption should be reversed and values to be negated in the instruction file that is used to decrypt the message. 
 
'''

import sys
from math import ceil


def sigmaShift(message,msgIndex,shiftPlace=1):
    """
    Shifts the string forward at the index by "shiftPlace" positions

    :param message: The message that has to be transformed
    :param msgIndex: The index of the character that has to be shifted
    :param shiftPlace: Integer value specifying the number of places to be shifted. If nothing specified, shifting only by one place
    :return: message
    """
    #If the index is greater than the length of the message
    if msgIndex >= len(message):
        return 'IndexOutofBound Exception. Max index allowed:'+str(len(message) - 1 )

    #If the letters are Capital
    if ord('A') <= ord(message[msgIndex]) <= ord('Z'):
        message =  (message[:msgIndex]
                + chr(((ord(message[msgIndex]) - 65 + shiftPlace) % 26)  + 65)
                + message[msgIndex + 1:])

    # If the letters are small.
    elif ord('a') <= ord(message[msgIndex]) <= ord('z'):
        message = (message[:msgIndex]
                + chr(((ord(message[msgIndex]) - 97 + shiftPlace) % 26) + 97)
                + message[msgIndex + 1:])
    return message

def rotateTransform(message,rotationCount=1):
    """
    Rotates the String by one position right for "rotationCount" times

    :param message: The message that has to be transformed
    :param rotationCount: Number of time the string has to rotate
    :return: message
    """
    #to Encrypt the message
    if rotationCount > 0:
        rotationCount = rotationCount % len(message)
    #to Decrypt the message
    else:
        rotationCount = -1*(abs(rotationCount) % len(message))

    message = message[-rotationCount:] + message[:-rotationCount]
    return  message


def deltaShift(message,msgIndex,isEncryption,deltaShiftCount=1):
    """
    Duplicates (in place) the letter at index for "deltaShiftCount" times

    :param message: The message that has to be transformed
    :param msgIndex: Index of the character that has to be duplicated
    :param deltaShiftCount: Num of duplications required
    :return: message
    """
    # If the index is greater than the length of the message
    if msgIndex >= len(message):
        return 'IndexOutofBound Exception. Max index allowed:' + str(len(message) - 1)

    if isEncryption:
        #Adding duplicates in the message
        for _ in range(deltaShiftCount):
            message=message[:msgIndex]+message[msgIndex]+message[msgIndex:]
    else:
        #Removing duplicates in the string
        for _ in range (abs(deltaShiftCount)):
            message = message[:msgIndex]+message[msgIndex+1:]
    return message



def touShift(message,srcIndex,dstIndex,splitCount = 1):
    """
    TouShift swaps the characters at srcIndex and dstIndex if the splitcount is 1.
    If splitcount is great than 1, the message is split into splitCount messages and the substring at srcIndex and dstIndex are swapped

    :param message: The message that has to be transformed
    :param srcIndex: Index in the string to be swapped
    :param dstIndex: Index in the string to be swapped
    :param splitCount: Number of splits required in the string
    :return: mutatedMessage
    """

    messageList = []
    if splitCount == 1:
        #splitting the message by character
        messageList = [c for c in message]
    else:
        #calculating the length of each group
        groupCharLength = int(ceil(len(message)/splitCount))

        # splitting characters in the groups of splitCount size
        for groupStartIndex in range(0,len(message),groupCharLength):
            messageList.append(message[groupStartIndex:groupStartIndex+groupCharLength])
    # Error Handling
    if srcIndex >= len(messageList) or dstIndex >= len(messageList):
        return 'IndexOutofBound Exception. Max index allowed:' + str(len(messageList) - 1)
    #Swapping the srcIndex and dstIndex in the list
    messageList[srcIndex], messageList[dstIndex] = messageList[dstIndex], messageList[srcIndex]
    #Converting list to String
    mutatedMessage = ''.join(messageList)
    return  mutatedMessage

def omegaShift(message,index,isEncryption,length=1):
    """
    OmegaShift takes the message and index position and the length. It shifts the characters of length "length" from the index position
    to the first. Length & Index parameter will never take negative values. The code should be passed as O<index>,length
    example: python will be transformed to tpyhon for O2 or O2,1
    and python will be tranformed to thpyon for O2,2

    :param message: The message that has to be transformed
    :param index: The index of character that has to be moved to the front
    :param isEncryption: if the string has to be encrypted or decrypted
    :param length: Number of characters that has to be pushed to front
    :return: message
    """
    # If the index is greater than the length of the message
    if index >= len(message):
        return 'IndexOutofBound Exception. Max index allowed:' + str(len(message) - 1)

    if isEncryption:
        # Moving the characters at index position to front
        message = message[index:index+length]+message[:index]+message[index+length:]
    else:
        # Moving the characters from front to the correct index position
        message = message[length:length + index] + message[:length] + message[index + length:]
    return message

def writeOutput(message,outputFilePath):
    """
    Writes the transformed message to the output file

    :param message: The message that is transformed and to be written in the output
    :param outputFilePath: path of the outputfile it has write the results
    :return: None
    """
    with open(outputFilePath,"a+") as output:
        #opening the file to write the results
        output.write(message+"\n")

def processMessage(message,passcode,ouputFilePath,mode):
    """
    Driver function
    Takes the passcode and parse to generate the commands and call the appropriate functions required

    :param message: Input message that has to be encrypted or decrypted
    :param passcode: The code that is used for transformation
    :param ouputFilePath: Complete path of the file where we write the output
    :param mode: Encryption/Decryption
    :return: None
    """
    #splitting the commands to read each command seperately
    commands = passcode.split(";")
    for command in commands:
        #checking the command and calling the appropriate function
        if command[0].lower() == 's':
            if command.find(',') != -1:
                #Slicing the command to read the parameters
               message =  sigmaShift(message,
                                     int(command.split(',')[0][1:].strip()),
                                     int(command.split(',')[1].strip()))
            else:
                # Slicing the command to read the parameters
                message = sigmaShift(message,
                                     int(command[1:].strip()))
        if command[0].lower() == 'r':
            if len(command) >1:
                # Slicing the command to read the parameters
                message = rotateTransform(message,int(command[1:]))
            else:
                message = rotateTransform(message)
        if command[0].lower() == 'd':
            if command.find(',') == -1:
                # Slicing the command to read the parameters
                message = deltaShift(message,int(command[1:]),mode)
            else:
                # Slicing the command to read the parameters
                message = deltaShift(message
                                     ,int(command.split(',')[0][1:].strip())
                                     ,mode
                                     ,int(command.split(',')[1].strip()))
        if command[0].lower() == 't':
            if command.find('(') == -1:
                # Slicing the command to read the parameters
                message = touShift(message
                                   ,int(command.split(',')[0][1:].strip())
                                   ,int(command.split(',')[1].strip()))
            else:
                # Slicing the command to read the parameters
                bracesOpenIndex = int(command.split(',')[0].strip().find('('))
                bracesCloseIndex = int(command.split(',')[0].strip().find(')'))
                message = touShift(message
                                   ,int(command.split(',')[0][bracesCloseIndex+1:].strip())
                                   ,int(command.split(',')[1].strip())
                                   ,int(command.split(',')[0][bracesOpenIndex+1:bracesCloseIndex].strip())
                                   )
        if command[0].lower() == 'o':
            if command.find(',') == -1:
                # Slicing the command to read the parameters
                message = omegaShift(message,int(command[1:]),mode)
            else:
                # Slicing the command to read the parameters
                message = omegaShift(message
                           ,int(command.split(',')[0][1:].strip())
                           ,mode
                           ,int(command.split(',')[1].strip()))
    #Writing results
    writeOutput(message,ouputFilePath)
    #Printing result to console
    print(message)

def main():
    """
    The main function
    :return: None
    """
    if len(sys.argv ) == 5 :
        messageFileLoc = sys.argv[1]
        instructionFileLoc = sys.argv[2]
        outputFileLoc = sys.argv[3]
        if sys.argv[4].lower() in ('e','d'):
            isEncryption =  True if sys.argv[4].lower() == 'e' else False
        else:
            print('Unknown command '+sys.argv[4] + '.Please provide e for encryption and d for decryption')
            sys.exit(1)
    else:
        messageFileLoc = input("Please provide complete path of the file with the messages")
        instructionFileLoc = input("Please provide complete path of the file with the instructions")
        outputFileLoc = input("Please provide complete path of the file to write results")
        encryptionDecryption = input("Please choose the function (e/d):")
        if encryptionDecryption.lower() in ('e','d'):
            isEncryption = True if encryptionDecryption.lower() == 'e' else False
        else:
            print('Unknown command ' + encryptionDecryption + '.Please provide e for encryption and d for decryption')
            sys.exit(1)

    #Opening the input and passcode file to process. Closing the file will be handled by 'with' automatically
    with open(messageFileLoc) as messageFile:
        with open(instructionFileLoc) as instructionFile:
            for message in messageFile:
                print(message.strip() , "transformed to:", end="")
                processMessage(message.strip() , instructionFile.readline().strip() , outputFileLoc , isEncryption)

if __name__ == '__main__':
    main()
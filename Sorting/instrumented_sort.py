__author__ = "Keerthi Pradhani"

'''
CSCI-603: LAB 5
Author1: SAI SUJITH KAMMARI
Author2: KEERTHI NAGAPPA PRADHANI

This program has different algorithms implemented to sort the list of unsorted elemetns 
'''

############ Selection Sort ############
def ssort(mylist):
    """
    Sorts mylist using selection sort algorithm

    :param mylist: unsorted list
    :return (mylist,comparisionCount):  Returns a tuple sorted list and number of comparisions it took to sort
    """
    comparisionCount = 0
    for position in range(len(mylist)):
        # Assume the current position is the minimum element
        minPosition = position
        for nextPos in range(position+1,len(mylist)):
            comparisionCount = comparisionCount + 1 # Comparing the values in the positions
            if (mylist[minPosition]>mylist[nextPos]):
                # Remembering the position of the minimum value
                minPosition = nextPos

        comparisionCount = comparisionCount + 1 #Comparing the positions
        if position != minPosition:
            # Swap the numbers
            mylist[minPosition],mylist[position] = mylist[position],mylist[minPosition]
    return (mylist,comparisionCount)

############ Merge Sort ############
def msort(mylist):
    """
    Sorts mylist using merge sort algorithm

    :param mylist: unsorted list
    :return (mylist,comparision_count):  Returns a tuple sorted list and number of comparisions it took to sort
    """
    comparision_count = 0
    if len(mylist)>1:
        # Dividing the list
        mid_point = len(mylist)//2
        leftlist = msort(mylist[: mid_point])
        rightlist = msort(mylist[mid_point:])

        # Merging the results
        merged_results = merge(leftlist[0],rightlist[0])
        comparision_count = comparision_count + merged_results[1]
        return (merged_results[0], comparision_count )
    else:
        return (mylist,comparision_count)

def merge(left,right):
    """
    Helper function for Merge sort

    :param left: left part of the unsorted list
    :param right: right part of the unsorted list
    :return (result,comparision_count): sorted list and comparisions made to sort
    """
    result = []
    comparision_count = 0
    left_index , right_index = 0 , 0
    # Compare elements of one list with another until we run out of atleast one list
    while left_index < len(left) and right_index < len(right):
        comparision_count = comparision_count + 1
        if left[left_index] < right[right_index]:
            result.append(left[left_index])
            left_index = left_index + 1
        else:
            result.append(right[right_index])
            right_index = right_index + 1
    # Appending the rest of the elements to the result
    for element in left[left_index:]:
        result.append(element)
    for element in right[right_index:]:
        result.append(element)
    return (result,comparision_count)

############ Insertion Sort ############
def isort(my_list):
    """
    Sorts my_list using Insertion sort algorithm

    :param mylist: unsorted list
    :return (my_list , comparision_count):  Returns a tuple sorted list and number of comparisions it took to sort
    """
    comparision_count = 0
    for index in range(len(my_list)-1):
        # Picking for each Number
        comparision_count = comparision_count + 1
        if my_list[index+1] < my_list[index]:
            # moving the element
            my_list[index + 1], my_list[index] = my_list[index], my_list[index + 1]
            newposition = index

            # Comparing the changed element with the already sorted list
            for i in range(index,0,-1):
                comparision_count = comparision_count + 1
                if my_list[newposition-1] > my_list[i]:
                    # moving the element
                    my_list[i] , my_list[newposition-1] = my_list[newposition-1] , my_list[i]
                    newposition = i-1 # remembering the new position
                else:
                    # Since it is a sorted list, breaking loop if condition fails atleast once
                    break
    return (my_list , comparision_count)

############ Quick Sort ############
def qsort(my_list):
    """
    sorts the elements using Quick Sort algorithm

    :param my_list: unsorted list
    :return (my_list, comparisions): sorted list and comparisions made
    """

    comparisions = quickSortHelper(my_list,0,len(my_list)-1)
    return  (my_list, comparisions)

def quickSortHelper(givenList,first=0,last = 0):
    """
    Helper function to sort the numbers using quick sort

    :param givenList: unsorted list
    :param first: index number
    :param last: index number
    :return splitpoint[1]:
    """

    splitpoint =([],0)
    if first<last:
        splitpoint = partition(givenList,first,last)
        quickSortHelper(givenList,first,splitpoint[0]-1)
        quickSortHelper(givenList,splitpoint[0]+1,last)
    return splitpoint[1]


def partition(givenList,first,last):
    """
    Creates the partition

    :param givenList: unsorted list
    :param first: index number
    :param last: index number
    :return (rightmark , comparisonInQuick): sorted list and comparisions made
    """
    comparisonInQuick = 0
    pivotvalue = givenList[first]

    leftmark = first+1
    rightmark = last

    done = False
    while not done:

        while leftmark <= rightmark and givenList[leftmark] <= pivotvalue:
            comparisonInQuick = comparisonInQuick + 1
            leftmark = leftmark + 1


        while givenList[rightmark] >= pivotvalue and rightmark >= leftmark:
            comparisonInQuick = comparisonInQuick + 1
            rightmark = rightmark -1

        comparisonInQuick = comparisonInQuick + 1
        if rightmark < leftmark:
            done = True
        else:
           temp = givenList[leftmark]
           givenList[leftmark] = givenList[rightmark]
           givenList[rightmark] = temp

    temp = givenList[first]
    givenList[first] = givenList[rightmark]
    givenList[rightmark] = temp
    return (rightmark , comparisonInQuick)
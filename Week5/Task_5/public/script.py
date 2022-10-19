#!/usr/bin/env python3


# Complete the following to implement the described hamming distance function.
# This signature is required for the automated grading to work.
# Do not rename the function or change its list of parameters!

def hamming_dist(signal_1, signal_2):

    signal_1 = signal_1["data"]
    signal_2 = list(signal_2) #technically unnecessary but will cause AttributeError because of empty check

    if len(signal_1) != len(signal_2) or (signal_1 == [] and signal_2 == []):
        return "Empty signal on at least one of the sensors"
    #Check length equality

    if any (len(first) != len(second) for first, second in zip(signal_1, signal_2)):
        return "Sensor defect detected"
    #Check string length equality

    ham = [hamming(pear[0], pear[1]) for pear in zip(signal_1, signal_2)]
    #create list of hamming distances of tuples where you compare first element with second in tuple

    return [(first, second, dist) for first, second, dist in (zip(signal_1, signal_2, ham)) if dist]
    #return triplet tuple of signal 1, 2 and hamming distance whenever hamming distance is not equal to 0

def hamming(a, b):
    #Function that computes hamming distance between two strings
    distance = 0
    for i in range(len(a)):
        if a[i] != b[i]:
            distance += 1
    return distance

# The following lines print your function's output for an exemplary input to the console.
# Note that this does not include any of the mentioned edge cases for defective sensors or signals of different lenghts.
# Try to write your own tests for this.

signal_sensor_1 = {"times": [0, 1, 2, 3, 4, 5],
                   "data": ["00101110", "11001011", "11110000", "01000011", "11001101", "00011011"]}
signal_sensor_2 = ("00101110", "11001001", "11110011", "01111011", "11001101", "00011011")
print(hamming_dist(signal_sensor_1, signal_sensor_2))

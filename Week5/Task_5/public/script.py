#!/usr/bin/env python3


# Complete the following to implement the described hamming distance function.
# This signature is required for the automated grading to work.
# Do not rename the function or change its list of parameters!

def hamming_dist(signal_1, signal_2):
    if signal_1 == {} and signal_2 == ():
        return "Empty signal on at least one of the sensors"

    signal_1 = signal_1["data"]
    signal_2 = list(signal_2)

    if len(signal_1) != len(signal_2) or (signal_1 == [] and signal_2 == []):
        return "Empty signal on at least one of the sensors"

    first = [len(item) for item in signal_1]
    second = [len(item) for item in signal_2]
    lengths = [pair[0] - pair[1] for pair in zip(first, second)]

    if sum(lengths) != 0:
        return "Sensor defect detected"

    ham = [hamming(pear[0], pear[1]) for pear in zip(signal_1, signal_2)]

    for i in range(len(ham)-1, -1, -1):
        if ham[i] == 0:
            signal_1.pop(i)
            signal_2.pop(i)
            ham.pop(i)

    return list(zip(signal_1, signal_2, ham))

def hamming(a, b):
    dist = 0
    for i in range(len(a)):
        if a[i] != b[i]:
            dist += 1
    return dist

# The following lines print your function's output for an exemplary input to the console.
# Note that this does not include any of the mentioned edge cases for defective sensors or signals of different lenghts.
# Try to write your own tests for this.

signal_sensor_1 = {}
signal_sensor_2 = ()
print(hamming_dist(signal_sensor_1, signal_sensor_2))

#You are completely free to change this variables to check your algorithm.
num1 = 0
num2 = 1

#Function to check whether two numbers are friendly pairs or not.
def isFriendlyPair():
    #You need to complete this function.
    #You need to return a boolean variable . If num1 and num2 are friendly pairs return True. 
    # If they are not return False. 
    # The numbers must be valid according to description before determining friendly parity situations. 
    # Return "Invalid" if they are not valid.
    if num1 == 0 or num2 == 0:
        return False

    def sumdiv(num):
        sum = 0
        for i in range(1, num + 1):
            if num % i == 0:
                sum += i
        return sum


    print(sumdiv(num1), " ", num1)
    print(sumdiv(num2), " ", num2)

    if (sumdiv(num1)/num1) == (sumdiv(num2)/num2) and num1 != num2:
        return True

    return False

#This line prints your method's return so that you can check your output.
print(isFriendlyPair())
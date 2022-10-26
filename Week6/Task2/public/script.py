#You are completely free to change this variables to check your algorithm.
num1 = 30
num2 = 30

#Function to check whether two numbers are friendly pairs or not.
def isFriendlyPair():
    #You need to complete this function.
    #You need to return a boolean variable . If num1 and num2 are friendly pairs return True. 
    # If they are not return False. 
    # The numbers must be valid according to description before determining friendly parity situations. 
    # Return "Invalid" if they are not valid.
    if (num1 <= 0) or (num2 <= 0) or (type(num1) is float) or (type(num2) is float) or num1 == num2:
        return "Invalid"

    def sumdiv(num):
        sum = 0
        for i in range(1, int(num**0.5)+1):
            if num % i == 0 and i != num/i:
                sum += i + num/i
            elif num % i == 0 and i == num/i:
                sum += i
        return int(sum)


    #print(sumdiv(num1), " ", num1)
    #print(sumdiv(num2), " ", num2)
    #print(sumdiv(num1)/num1, " ", sumdiv(num2)/num2)

    if (sumdiv(num1)/num1) == (sumdiv(num2)/num2):
        return True

    return False

#This line prints your method's return so that you can check your output.
print(isFriendlyPair())
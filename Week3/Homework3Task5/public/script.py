#!/usr/bin/env python3
import sys

# Height in M
height = 10
# Weight in KG
weight = 10


# Determine the BMI. Change the function
# below to calculate the BMI return which category the result is in.
# Your implementation should work with any specific value.
# You must use the variables defined above.


def get_bmi_category():
    # You need to change the following part of the function
    # to determine the BMI and return the correct category.
    #bmi function = weight/height^2
    #[0, 18.5]	Underweight
    #(18.5, 25]	Normal weight
    #(25, 30]	Pre-obesity
    #(30, 35]	Obesity class I
    #(35, 40]	Obesity class II
    #(40, ♾️)	Obesity class III

    if height < 0 or weight < 0:
        return 'N/A'

    bmi =  weight/ (height **2)
    bmi = "{:.2f}".format(bmi)
    cat = ""
    if float(bmi) <= 18.5:
        cat = "Underweight"
    elif float(bmi) <= 25:
        cat = "Normal weight"
    elif float(bmi) <= 30:
        cat = "Pre-obesity"
    elif float(bmi) <= 35:
        cat = "Obesity class I"
    elif float(bmi) <= 40:
        cat = "Obesity class II"
    else:
        cat = "Obesity class III"

    BMI = "BMI: " + bmi + ", Category: " + cat
    return BMI

# The following line calls the function and prints the return
# value to the Console. This way you can check what it does.
print(get_bmi_category())

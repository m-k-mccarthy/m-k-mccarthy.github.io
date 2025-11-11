#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
name: Madeline McCarthy

student number: 125106449
"""
"""
steps left to do:
    change inputs to in-code values??
    change classif to add invalidated values
    make sure comments are right
"""

# defining a function to determine the BMI value
def BMI (height,weight):
    
    # BMI value = weight divided by height squared
    while weight >0 and height >0:
        return weight/(height**2)


# defining a function to convert imperial height to metric height
def con_h (a,b):
   
    # converts feet and inches to meters
    while a >0 and b >0:
        foot = a / 3.281
        inch = b / 39.37
        
        # returns total height
        return foot + inch
   
 
# defining a function to convert imperial weight to metric weight
def con_w (x, y):
    
    # converts stones and pounds to kilograms
    while x >0 and y >0:
        stone = x * 6.35
        pound = y / 2.205
        
        # returns total weight
        return stone + pound
   
 
# defining a function to find the BMI classification based on 
# earlier BMI value
def classif (m):
    if m <0:
        level = 'N/A' 
        outcome = 'N/A'
    elif m <18.5:
        level = 1
        outcome = 'underweight'
    elif m <25.0:
        level = 2 
        outcome = 'healthy weight'
    elif m <30.0:
        level = 3 
        outcome = 'overweight'
    elif m <35.0:
        level = 4 
        outcome = 'obesity I'
    elif m <40.0:
        level = 5 
        outcome  = 'obesity II'
    elif m >= 40.0:
        level = 5 
        outcome = 'obesity III'
    
    return level, outcome
    

# defining a function to find all the information above and return it at once
def patient_full_classif (feet, inches, stones, pounds):
    
    # calling the functions to convert the values to metric
    height = con_h(feet,inches)
    weight = con_w(stones,pounds)
    
    # calling the function to find the BMI value
    bmi = BMI(height,weight)
    
    # calling the function to determine the BMI classification
    level, outcome = classif(bmi)
   
    # returning the classification
    return level, outcome


    
# MAIN PROGRAM

# QUESTION 1

# setting values for their height and weight
height = 1.66
weight = 55

# calling the function to calculate BMI based on inputted values and printing it
print('Your BMI value is', BMI(height,weight))



# QUESTION 2

# setting values for imperial height
imperial_feet = 5
imperial_inches = 11


# calling function to convert inputs to metric and printing
print('Your height in meters is',con_h(imperial_feet,imperial_inches))
 

# setting values for imperial weight
imperial_stones = 10
imperial_pounds = 10 
 

# calling function to convert inputs to metric and printing
print('Your weight in kgs is', con_w(imperial_stones, imperial_pounds))    
 


# QUESTION 3

# setting for BMI value
value = 23.5

# calling functions to determine full BMI classification and setting two outputs
level, outcome = classif(value)

# setting output message
msg = 'Your BMI level is {} and weight classification is {}'

# printing message
print(msg.format(level,outcome))  
 


# QUESTION 4

# calling functions to convert all values and determine full BMI classification
level, outcome = patient_full_classif(imperial_feet,imperial_inches,imperial_stones,imperial_pounds)

# printing output message
print(msg.format(level, outcome))    
 









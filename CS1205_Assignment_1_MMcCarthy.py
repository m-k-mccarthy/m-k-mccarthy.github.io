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
    if weight >0 and height >0:
        return weight/(height**2)
    
    # setting a fault control
    else:
        return 'invalid'


# defining a function to convert imperial height to metric height
def con_h (a,b):
   
    # converts feet and inches to meters
    if a >=0 and b >=0:
        foot = a / 3.281
        inch = b / 39.37
        
        # returns total height
        return foot + inch
    
    # setting a fault control
    else:
        return 'invalid'
   
 
# defining a function to convert imperial weight to metric weight
def con_w (x, y):
    
    # converts stones and pounds to kilograms
    if x >=0 and y >=0:
        stone = x * 6.35
        pound = y / 2.205
        
        # returns total weight
        return stone + pound
    
    # setting a fault control
    else:
        return 'invalid'
   
 
# defining a function to find the BMI classification based on 
# earlier BMI value
def classif (m):
    if m <0:
        outcome = 'N/A'
    elif m <18.5:
        outcome = 'underweight'
    elif m <25.0:
        outcome = 'healthy weight'
    elif m <30.0:
        outcome = 'overweight'
    elif m <35.0:
        outcome = 'obesity I'
    elif m <40.0:
        outcome  = 'obesity II'
    elif m >= 40.0:
        outcome = 'obesity III'
    
    return outcome
    

# defining a function to find all the information above and return it at once
def patient_full_classif (feet, inches, stones, pounds):
    
    # calling the functions to convert the values to metric
    height = con_h(feet,inches)
    weight = con_w(stones,pounds)
    
    # calling the function to find the BMI value
    bmi = BMI(height,weight)
    
    # calling the function to determine the BMI classification
    outcome = classif(bmi)
   
    # returning the classification
    return outcome


    
# MAIN PROGRAM

# QUESTION 1

# calling the function to calculate BMI based on inputted values and printing it
print('Your BMI value is', BMI(1.66,55))



# QUESTION 2

# calling function to convert inputs to metric and printing
print('Your height in meters is',con_h(5,11))
 
 

# calling function to convert inputs to metric and printing
print('Your weight in kgs is', con_w(10, 10))    
 


# QUESTION 3

# calling functions to determine full BMI classification and setting output
outcome = classif(23.5)

# setting output message for this question and the next
msg = 'Your BMI weight classification is {}'

# printing message
print(msg.format(outcome))  
 


# QUESTION 4

# calling functions to convert all values and determine full BMI classification
outcome = patient_full_classif(imperial_feet,imperial_inches,imperial_stones,imperial_pounds)

# printing output message
print(msg.format(outcome))    
 









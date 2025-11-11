#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
name: Madeline McCarthy

student number: 125106449
"""
"""
steps left to do:
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
def con_h (foot,inch):
   
    # converts feet and inches to meters
    if foot >=0 and inch >=0:
        converted_foot = foot / 3.281
        converted_inch = inch / 39.37
        
        # returns total height
        return converted_foot + converted_inch
    
    # setting a fault control
    else:
        return 'invalid'
   
 
# defining a function to convert imperial weight to metric weight
def con_w (stone, pound):
    
    # converts stones and pounds to kilograms
    if stone >=0 and pound >=0:
        converted_stone = stone * 6.35
        converted_pound = pound / 2.205
        
        # returns total weight
        return converted_stone + converted_pound
    
    # setting a fault control
    else:
        return 'invalid'
   
 
# defining a function to find the BMI classification based on 
# earlier BMI value
def classif (bmi):
    if bmi <=0:
        outcome = 'N/A'
    elif bmi <18.50:
        outcome = 'underweight'
    elif bmi <25.00:
        outcome = 'healthy weight'
    elif bmi <30.00:
        outcome = 'overweight'
    elif bmi <35.00:
        outcome = 'obesity I'
    elif bmi <40.00:
        outcome  = 'obesity II'
    elif bmi >= 40.00:
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
outcome = classif(25)

# setting output message for this question and the next
msg = 'Your BMI weight classification is {}'

# printing message
print(msg.format(outcome))  
 


# QUESTION 4

# calling functions to convert all values and determine full BMI classification
outcome = patient_full_classif(5,11,10,10)

# printing output message
print(msg.format(outcome))    
 









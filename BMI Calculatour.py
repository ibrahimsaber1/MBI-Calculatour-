#!/usr/bin/env python
# coding: utf-8

# # MBI Calculatour 
# 
# Metric Units:
# BMI = mass (kg) / height * height (m)
# 

# In[3]:





# In[ ]:





# In[22]:


name = input("write your name :")
mass =int (input("write your wight im Kg :"))
height =float (input("write your height in M"))
BMI = (mass/(height*height))
print(BMI)

if BMI>0:
    if(BMI < 16):
        print(name +" ,Your Wight is Severe Thinness" + " ,For your Information Healthy BMI range: 18.5 kg/m2 - 25 kg/m2")
    elif(BMI < 17):
        print(name +" ,Your Wight is Moderate Thinness"+ " ,For your Information Healthy BMI range: 18.5 kg/m2 - 25 kg/m2")
    elif(BMI < 18):
        print(name +" ,Your Wight is Mild Thinness"+ " ,For your Information Healthy BMI range: 18.5 kg/m2 - 25 kg/m2")
    elif(BMI < 25):
        print(name +" ,Your Wight is Normal" + " you need to start going to the Gym"+ 
              " ,For your Information Healthy BMI range: 18.5 kg/m2 - 25 kg/m2")
    elif(BMI < 30):
        print(name +" ,Your Wight is Overweight"+ " ,For your Information Healthy BMI range: 18.5 kg/m2 - 25 kg/m2")
    elif(BMI < 35):
        print(name +" ,Your Wight is Obese severely "+ " ,For your Information Healthy BMI range: 18.5 kg/m2 - 25 kg/m2")
    else:
        print(name +" ,Your Wight is Morbidly obese"+ " ,For your Information Healthy BMI range: 18.5 kg/m2 - 25 kg/m2")
else:
    print(name +" ,Write a valid Information")


# In[ ]:





# In[ ]:


## the information below from this link
# https://www.calculator.net/bmi-calculator.html?cage=23&csex=m&cheightfeet=5&cheightinch=10&cpound=160&cheightmeter=181&ckg=76&printit=0&ctype=metric&x=Calculate

#Severe Thinness	< 16	< 0.64
#Moderate Thinness	16 - 17	0.64 - 0.68
#Mild Thinness	17 - 18.5	0.68 - 0.74
#Normal	18.5 - 25	0.74 - 1
#Overweight	25 - 30	1 - 1.2
#Obese severely 	30 - 35	1.2- 1.4
#Obese morbidly 	35 - 40	1.4 - 1.6


# In[20]:


if BMI>0:
    if(BMI < 16):
        print(name +" ,Your Wight is Severe Thinness" + " ,For your Information Healthy BMI range: 18.5 kg/m2 - 25 kg/m2")
    elif(BMI < 17):
        print(name +" ,Your Wight is Moderate Thinness"+ " ,For your Information Healthy BMI range: 18.5 kg/m2 - 25 kg/m2")
    elif(BMI < 18):
        print(name +" ,Your Wight is Mild Thinness"+ " ,For your Information Healthy BMI range: 18.5 kg/m2 - 25 kg/m2")
    elif(BMI < 25):
        print(name +" ,Your Wight is Normal" + " you need to start going to the Gym"+ 
              " ,For your Information Healthy BMI range: 18.5 kg/m2 - 25 kg/m2")
    elif(BMI < 30):
        print(name +" ,Your Wight is Overweight"+ " ,For your Information Healthy BMI range: 18.5 kg/m2 - 25 kg/m2")
    elif(BMI < 35):
        print(name +" ,Your Wight is Obese severely "+ " ,For your Information Healthy BMI range: 18.5 kg/m2 - 25 kg/m2")
    else:
        print(name +" ,Your Wight is Morbidly obese"+ " ,For your Information Healthy BMI range: 18.5 kg/m2 - 25 kg/m2")
else:
    print(name +" ,Write a valid Information")


# In[ ]:





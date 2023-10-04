#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#Elijah Devadas # 100826898
answer = ""
num1 = ""
num2 = ""
z = ""
while True:
    
    print("Hey there! Welcome to my calculator!")
    exp = 1
    y = 1
    operation = input("Please select operations to perform: add (+), subtract (-), multiply (*), divide (/), exponential (**),\nor exit/stop: ")
    if operation == "exit" or operation == "stop":
        break
    num1 = input("Please enter your first number: ")
    if num1 == "exit" or num1 == "stop":
        break
    num2 = input("Please enter your second number: ") 
    if num2 == "exit" or num2 == "stop":
        break
 
    if operation == "add" or operation == "+":
        if num1 == "" and num2 != "":
            answer = z + float(num2)
            print(answer)
        elif num2 == "" and num1 != "":
            answer = z + float(num1)
            print(answer)
        else:
            answer = float(num1) + float(num2) 
            print(answer)
            z = float(answer) 
            
    if operation == "subtract" or operation == "-":
        if num1 == "" and num2 != "":
            answer = z - float(num2)
            print(answer)
        elif num2 == "" and num1 != "":
            answer = z - float(num1)
            print(answer)
        else:
            answer = float(num1) - float(num2) 
            print(answer)
            z = float(answer) 
    
    if operation == "multiply" or operation == "*":
        if num1 == "" and num2 != "":
            answer = z * float(num2)
            print(answer)
        elif num2 == "" and num1 != "":
            answer = z * float(num1)
            print(answer)
        else:
            answer = float(num1) * float(num2) 
            print(answer)
            z = float(answer) 
       
    if operation == "divide" or operation == "/":
        if num1 == "" and num2 != "":
            answer = z / float(num2)
            print(answer)
        elif num2 == "" and num1 != "":
            answer = z / float(num1)
            print(answer)
        else:
            answer = float(num1) / float(num2) 
            print(answer)
            z = float(answer) 
            
    if operation == "exponential" or operation == "**":
        if num1 == "" and num2 != "":
            for y in range(int(num2)):
                exp = exp * int(z)
            print(exp)
        elif num2 == "" and num1 != "":
            for y in range(int(num1)):
                exp = exp * int(z)
            print(exp)
            
        else:
            for y in range(int(num2)):
                exp = exp * int(num1)
            print(exp)
        z = exp

            
     
    
    

    
        
    
        
        
    
    
    


# In[ ]:





# In[ ]:





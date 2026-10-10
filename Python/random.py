import random as rnd 
import math  
num = rnd.random()  
num1 = num * 100
print(math.floor(num1))  

num2 = rnd.randint(0,9);
print(num2)


num1 = rnd.randint(0,1000)
num2 = rnd.randint(0,1000)
newrand = num1/num2
print(newrand)


colour = rnd.choice(["red", "black", "green"])
print(colour)


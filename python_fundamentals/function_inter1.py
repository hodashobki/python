import random
def randInt(min=0, max=100):
    num = random.random()*max
    return num
print(randInt()) 		   
#print(randInt(max=50))
import random
def randInt(min=0, max=100):
    num = random.random()*max
    return num
print(randInt(max=50))	   
#print(randInt(min=50))
import random
def randInt(min=0, max=100):
    num = random.random()*(max-min)+min
    return num 
print(randInt(min=50))	  
#print(randInt(min=50, max=500))
import random
def randInt(min=0, max=100):
    num = random.random()*(max-min)+min
    return num 
print(randInt(min=50, max=500))
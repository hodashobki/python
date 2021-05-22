listt=[]
def countd(a):
    
    for m in range(a,0,-1):
     listt.append(m)
    return listt
b=countd(5)    
print(b)   

#2 print and return
def printre(lis):
    for i in range(0,2):
        print(lis[0])
        return lis[1]

print(printre([2,5])) 


  #3 First plus length
sum=0
def first_len(lis):
    sum =lis[0]+len(lis)
    return sum
print(first_len([4,5,6,8,1,2,3]))

#Values Greater than Second 
lisNew=[]
def greater_than(lis):
    
    for i in range(len(lis)):
        if lis[i]>lis[1]:
            lisNew.append(lis[i])
    print(len(lisNew))        
    return lisNew       
print(greater_than([3,2,5,6,7,9,1,0]))

#This Length, That Value
lis=[]
def this_that(a,b):
    for i in range(a):
        lis.append(b)
    return lis
print(this_that(4, 5))                
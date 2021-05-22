for v in range(0,151):
    print(v)

#q2
for x in range(1,201):
     print(x * 5)

for x in range(1,1001):
    if x%5==0:
         print(x)


#Q3
for m in range(1,100):
    if m%10 ==0:
        print("Coding Dojo")
    elif m%5 ==0:
        print("Coding")
    else:
        print(m)
       
# Q4 
sum=0
for y in range(0,500000):
     if y%2!=0:
        sum+=y
print(sum)        
# 
# Q5
for m in range(2018,0,-1):
     if m%4==0:
        print(m) 

#6
lowNum=8
highNum=20
mult=2
for x in range(lowNum,highNum+1):
     if x%mult==0:
         print(x) 
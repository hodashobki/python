#Biggie Size
def biggi(lis):
    for i in range(len(lis)):
        if lis[i]<0:
            lis[i]="big"
    return lis
print(biggi([1,2,-4,7,-6]))  

#Count Positives

def countpos(lis):
    count=0
    for x in range(len(lis)):
        if lis[x]>0 & lis[i]!=0:
            count+=1
    lis[-1]=count
    return lis
print(countpos([2,5,-7,-1,-1,5,-8]))

#Sum Total
def sum_lis(lis):
    sum=0
    for i in range(len(lis)):
        sum+=lis[i]
    return sum
print(sum_lis([1,3,5,7])) 

#Average 
def sum_lis(lis):
    sum=0
    average=0
    for i in range(len(lis)):
        sum+=lis[i]
    average=sum/len(lis)
    return average

print(sum_lis([1,3,5,7])) 


#Length 
def lis_length(lis):
    return len(lis)
print(lis_length([5,8,6,7,1,0,5,4,2,0]))   


#Minimum
def minimum(lis):
    min=lis[0]
    for i in range(1,len(lis)):
        if len(lis)==0:
            return False
        elif lis[i]<min:
            min=lis[i]
    return min
print(minimum([2,8,-1,4,7])) 

#maximum
def Maximum(lis):
    max=lis[0]
    for i in range(1,len(lis)):
        if lis[i]>max:
            max=lis[i]
        elif len(lis)<2:
            return False
    return max        
print(Maximum([2,5,8,78,1]))

#Ultimate Analysis
def ultimate(lis):
    max=lis[0]
    min=lis[0]
    sum=0
    average=0
    for i in range(len(lis)):
        sum+=lis[i]
        if lis[i]>max:
            max=lis[i]
        elif lis[i]<min:
            min=lis[i]
    average=sum/len(lis)
    return {"sum Total":sum,"average":average,"maximum":max,"minimum":min}

print(ultimate([1,3,5,7])) 

#Reverse list
def reversel(lis):
    i=0
    while i<len(lis)/2:
       lis[i],lis[len(lis)-1-i]=lis[len(lis)-1-i],lis[i]
       i+=1
    return lis
print(reversel([1,2,3,4,5,6])) 
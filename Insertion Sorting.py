listA=[]

#listA = [6, 3, 7, 2, 8, 9, 0, 5, 4, 1]
t=0
while t==0:
    y = input("would you like to input values into the list")
    if y in "Yy" :
        input_user = int(input("What value would you like to insert into the list"))
        listA.append(input_user)
    elif y in "Nn":
        t=1
    else: print("Please insert the proper answer")
print(listA)


num= len(listA)

for i in range (0,num-1):
    
    minIndex = i+1 
    minValue = listA[minIndex]
    
    for j in range(i+1, num):
        if listA[j] < minValue: 
            minValue = listA[j]
            minIndex = j
    
    if minValue < listA[i]: 
        temp = listA[i] #first value of list replaces the min value of remainder list
        listA[i] = minValue #replaces 
        listA[minIndex] = temp
            
print(listA)
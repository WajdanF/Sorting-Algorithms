listA = []
##listA = [6, 3, 7, 2, 8, 9, 0, 5=, 4, 1]
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
for j in range(1,num): # j is the pass number
    for i in range(1, num-j+1):  # i is the step number for the current pass
        if (listA[i-1] > listA[i]):
            listA[i-1], listA[i] = listA[i], listA[i-1]
        print("")           
print(listA)
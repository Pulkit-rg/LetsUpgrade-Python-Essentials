#Using for loop please print all the prime numbers between 1- 200 using FOR LOOP AND RANGE
#function.


for i in range(2,201):
    if(i%2==0):
        continue
    else:
        for j in range(2,i):
            if ((i%j)==0):
                break
        else:
            print(i, "is a prime number")
        

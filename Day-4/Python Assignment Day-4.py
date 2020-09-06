#Print the first ArmStrong number in the range of 1042000 to 702648265 and exit the loop as soon
#as you encounter the first armstrong number.
#Use while loop



for i in range(1042000,702648266):
        summ=0
        count = 0
        van=i
        nav=i
        
        while(i>0):
                count = count+1
                i=i//10
        
        while (van>0):
                aaa=van%10
                summ=summ+ (aaa**count)
                van=van//10
        if summ==nav:
                print(nav, "is an armstrong number")
                break
        else:
                continue




def armstrong():
    for i in range(1, 1001):
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
                yield  nav
                
        else:
                continue


aaa=armstrong()
print(list(aaa))






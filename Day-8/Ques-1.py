def returnfibonacci(funct):
    def fibbo():
        n=funct()
        a=0
        b=1
        for i in range(0,n):
            if i<=1:
                print(i)
            else:
                c=a+b
                print(c)
                a=b
                b=c
    return fibbo

@returnfibonacci
def takeInput():
    s=int(input("Enter a number"))
    return s

takeInput()


















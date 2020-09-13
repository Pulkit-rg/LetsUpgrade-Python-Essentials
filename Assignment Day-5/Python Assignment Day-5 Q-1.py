#Write a program to identify sub list [1,1,5] is there in the given list in the same order, if yes print
#“it’s a Match” if no then print “it’s Gone” in function.
#Example -
 #Listy =[1,5,6,4,1,2,3,5] - it’s a Match
#Listy = [1,5,6,5,1,2,3.6] - it’s Gone



def sublist(b):
    lis=[1,1,5]
    a=0
    for i in lis:
        if i in b[a:]:
            a=b.index(i, a)+1
        else:
            return False
    return True

listy=[1,6,5,4,1,2,3,5]
ch=sublist(listy)
if(ch==True):
    print(" it’s a Match")
else:
    print(" it’s gone")
            

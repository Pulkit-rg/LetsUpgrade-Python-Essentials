#You all are Pilots, you want to land a plane safely, so altitude required for landing a plane is
#1000ft, it it is less than tell pilot to land the plane, or it is more than that but less than 5000ft ask
#the pilot to “come down to 1000ft”, else if it more than 5000ft ask the pilot to “go around and try
#later”


alt=1000                                          #required altitude in feets
cur=int(input("Enter the current altitude"))      #current altitude in feets    

if (cur<=alt):
    print("Land the plane now")
elif(cur>alt and cur<5000):
    print("Come down to 1000ft")
else:
    print("Go around and try")

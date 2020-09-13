# Question-2

#Make a Function for prime numbers and use Filter to filter out all the prime numbers from 1-2500

def prime_numm(sh):
                for i in range (2, sh):
                    if(sh%i ==0):
                        return False
                        break
                    
                else:
                    return True
                
        



dav=list(filter(prime_numm, range(1,2501)))
print(dav)










num = int(input("Enter your numbe:\n"))
lst =[2,3,4,5,6,7]
for i in lst:
    if (num%i)==0:
        
     print( num,"is not prime ")
     break
    else :
        print("Number is prime ")
from os import major


n1=float(input("Dime el primer numero: "))
n2=float(input("Dime el segon numero: "))
n3=float(input("Dime el tercer numero: "))

#major = 0

if n1 > n2 and n1 > n3:
    print ("Es el numero mes gran es: " , n1)
    #major = n1
else:
    if n2 > n3:
        print ("Es el numero mes gran es: " , n2)
        #major = n2
    else:
        print ("Es el numero mes gran es: " , n3)
        #major = n3

#print ("El numero major es: " , major)
#greter 

a=input("enter first number:")
b=input("enter second number:")
c=input("enter third number:")

if(a>b and a>c):
    print("a is greater ",a)

elif(b>c):
    print("b is greater",b)

else:
    print("c is greater",c)


    #odd or even

 a=int(input("enter any number:"))
rem=a%2
if(rem==0):
    print("Given number is EVEN")
else:
    print("Given number is ODD")  
     
#uppercase or lowercase
char=input("enter any charecter:")
if char.isupper():
   print("char is UPPER CASE")

elif char.islower():
   print("char is LOWER CASE")
else:
   print("char is not alpha")




#number or charecter
a=input("enter any value:")
if a.isalpha():
    print("given value is CHARECTER")
else:
    print("given value is NUMBER")
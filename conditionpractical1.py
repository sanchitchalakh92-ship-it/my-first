
a=input("enter first number:")
b=input("enter second number:")
c=input("enter third number:")
d=input("enter fourth number:")

if(a>b and a>c and a>d):
    print("a is gretest number ",a)
    
elif(b>c and b>d):
    print("b is gretest",b)
    
elif(c>d and c>a and c>b):
    print("c is greter",c)
    
else:
    print("d is greter",d)
